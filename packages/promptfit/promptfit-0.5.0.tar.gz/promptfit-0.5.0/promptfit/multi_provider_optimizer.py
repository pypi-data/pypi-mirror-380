"""
Multi-provider optimizer that works with both Cohere and Gemini.
"""

import logging
from typing import Optional, Dict, Any, List
from .providers import ProviderManager, GenerationConfig, EmbeddingConfig
from .config_multi_provider import MultiProviderConfig
from .token_budget import estimate_tokens
from .relevance import rank_segments_by_relevance
from .utils import split_sentences

logger = logging.getLogger(__name__)

class MultiProviderOptimizer:
    """PromptFit optimizer with multi-provider support."""
    
    def __init__(self, config: Optional[MultiProviderConfig] = None):
        """Initialize with configuration."""
        self.config = config or MultiProviderConfig.from_env()
        self.config.validate()
        
        # Create provider manager
        self.provider_manager = ProviderManager.create_from_config(self.config.to_dict())
        
        logger.info(f"Initialized multi-provider optimizer with primary: {self.config.primary_provider}")
    
    def optimize_prompt(
        self,
        prompt: str,
        query: str,
        max_tokens: int = 2048,
        *,
        top_k: int = 8,
        min_keep_ratio: float = 0.7,
        use_paraphrasing: bool = True,
        quality_check: bool = False,
        fallback_on_low_relevance: bool = True,
        pre_summarize_chunks: bool = False,
        provider_preference: Optional[str] = None
    ) -> str:
        """
        Optimize prompt using multi-provider approach.
        
        Args:
            prompt: Original prompt text
            query: Reference query for relevance
            max_tokens: Target token budget
            top_k: Number of top segments to keep
            min_keep_ratio: Minimum ratio of content to preserve
            use_paraphrasing: Whether to use LLM for paraphrasing
            quality_check: Whether to perform quality checks
            fallback_on_low_relevance: Whether to fallback on low relevance
            pre_summarize_chunks: Whether to pre-summarize long chunks
            provider_preference: Preferred provider for this operation
        
        Returns:
            Optimized prompt
        """
        logger.info(
            "Starting multi-provider optimization",
            extra={
                "prompt_length": len(prompt),
                "query_length": len(query),
                "max_tokens": max_tokens,
                "provider_preference": provider_preference
            }
        )
        
        try:
            # 1. Split into sentences
            sections = split_sentences(prompt)
            logger.debug(f"Split prompt into {len(sections)} sections")
            
            # 2. Estimate tokens
            original_tokens = self.provider_manager.estimate_tokens(prompt)
            
            # If already within budget, return as-is
            if original_tokens <= max_tokens:
                logger.info("Prompt already within budget", extra={"tokens": original_tokens})
                return prompt
            
            # 3. Rank by relevance using embeddings
            try:
                embeddings_config = EmbeddingConfig(input_type="search_document")
                
                # Get embeddings for query and sections
                all_texts = [query] + sections
                embeddings = self.provider_manager.embed(all_texts, embeddings_config)
                
                query_embedding = embeddings[0]
                section_embeddings = embeddings[1:]
                
                # Compute similarities and rank
                from .relevance import compute_cosine_similarities
                similarities = compute_cosine_similarities(query_embedding, section_embeddings)
                
                # Create ranked list
                ranked_sections = list(zip(sections, similarities))
                ranked_sections.sort(key=lambda x: x[1], reverse=True)
                
                logger.debug(f"Ranked sections by relevance, top score: {ranked_sections[0][1]:.3f}")
                
            except Exception as e:
                logger.error(f"Relevance ranking failed: {e}")
                # Fallback: keep original order
                ranked_sections = [(section, 1.0) for section in sections]
            
            # 4. Select top-k sections within budget
            selected_sections = []
            running_tokens = 0
            min_keep_tokens = int(max_tokens * min_keep_ratio)
            
            # First, add top-k sections
            for section, score in ranked_sections[:top_k]:
                section_tokens = self.provider_manager.estimate_tokens(section)
                if running_tokens + section_tokens <= max_tokens:
                    selected_sections.append(section)
                    running_tokens += section_tokens
            
            # Then, add more sections until min_keep_ratio is met
            for section, score in ranked_sections[len(selected_sections):]:
                if running_tokens >= min_keep_tokens:
                    break
                section_tokens = self.provider_manager.estimate_tokens(section)
                if running_tokens + section_tokens <= max_tokens:
                    selected_sections.append(section)
                    running_tokens += section_tokens
            
            # 5. Combine selected sections
            pruned_prompt = "\n\n".join(selected_sections)
            current_tokens = self.provider_manager.estimate_tokens(pruned_prompt)
            
            logger.info(
                "Selected sections",
                extra={
                    "sections_selected": len(selected_sections),
                    "tokens_after_selection": current_tokens
                }
            )
            
            # 6. Paraphrase if still over budget and paraphrasing enabled
            if current_tokens > max_tokens and use_paraphrasing:
                logger.info("Paraphrasing to meet token budget")
                
                paraphrase_prompt = (
                    f"Rewrite the following text to be more concise while preserving all key information, "
                    f"facts, and instructions. Target approximately {max_tokens} tokens:\n\n{pruned_prompt}"
                )
                
                generation_config = GenerationConfig(
                    max_tokens=max_tokens,
                    temperature=0.2
                )
                
                try:
                    paraphrased = self.provider_manager.generate(
                        paraphrase_prompt,
                        generation_config,
                        use_fallback=True
                    )
                    
                    paraphrased_tokens = self.provider_manager.estimate_tokens(paraphrased)
                    
                    if paraphrased_tokens <= max_tokens:
                        pruned_prompt = paraphrased
                        current_tokens = paraphrased_tokens
                        logger.info(f"Paraphrasing successful, tokens: {current_tokens}")
                    else:
                        logger.warning(f"Paraphrasing exceeded budget: {paraphrased_tokens} tokens")
                
                except Exception as e:
                    logger.error(f"Paraphrasing failed: {e}")
                    # Continue with non-paraphrased version
            
            # 7. Final validation
            final_tokens = self.provider_manager.estimate_tokens(pruned_prompt)
            reduction_pct = ((original_tokens - final_tokens) / original_tokens) * 100
            
            logger.info(
                "Optimization completed",
                extra={
                    "original_tokens": original_tokens,
                    "final_tokens": final_tokens,
                    "reduction_percentage": reduction_pct,
                    "within_budget": final_tokens <= max_tokens
                }
            )
            
            return pruned_prompt
            
        except Exception as e:
            logger.error(f"Optimization failed: {e}")
            raise
    
    def optimize_prompt_auto(
        self,
        prompt: str,
        query: str,
        *,
        target_ratio: Optional[float] = None,
        desired_max_tokens: Optional[int] = None,
        min_tokens: int = 400,
        max_tokens_cap: Optional[int] = None,
        **kwargs
    ) -> str:
        """
        Auto-optimize prompt with intelligent token budget selection.
        
        Args:
            prompt: Original prompt text
            query: Reference query
            target_ratio: Desired compression ratio (e.g., 0.6 for 60% of original)
            desired_max_tokens: Explicit token target
            min_tokens: Minimum token budget
            max_tokens_cap: Maximum token budget cap
            **kwargs: Additional optimization parameters
        
        Returns:
            Optimized prompt
        """
        # Estimate original size
        original_tokens = self.provider_manager.estimate_tokens(prompt)
        
        # Determine target budget
        if desired_max_tokens is not None and desired_max_tokens > 0:
            budget = int(desired_max_tokens)
        else:
            # Auto-sizing based on original size
            if target_ratio is None:
                if original_tokens < 1000:
                    ratio = 0.8
                elif original_tokens < 3000:
                    ratio = 0.6
                elif original_tokens < 8000:
                    ratio = 0.5
                else:
                    ratio = 0.4
            else:
                ratio = max(0.05, min(1.0, target_ratio))
            
            budget = int(original_tokens * ratio)
        
        # Apply constraints
        budget = max(min_tokens, budget)
        if max_tokens_cap:
            budget = min(budget, max_tokens_cap)
        
        logger.info(
            "Auto-optimization parameters",
            extra={
                "original_tokens": original_tokens,
                "target_budget": budget,
                "ratio": budget / original_tokens if original_tokens > 0 else 0
            }
        )
        
        return self.optimize_prompt(prompt, query, max_tokens=budget, **kwargs)
    
    def get_provider_info(self) -> Dict[str, Any]:
        """Get information about configured providers."""
        return self.provider_manager.get_provider_info()
    
    def health_check(self) -> Dict[str, bool]:
        """Check health of all providers."""
        return self.provider_manager.health_check()
    
    def estimate_tokens(self, text: str, provider: Optional[str] = None) -> int:
        """Estimate tokens using specified or primary provider."""
        return self.provider_manager.estimate_tokens(text, provider)

# Convenience functions for backward compatibility
def optimize_prompt_multi(
    prompt: str,
    query: str,
    max_tokens: int = 2048,
    cohere_api_key: Optional[str] = None,
    gemini_api_key: Optional[str] = None,
    primary_provider: str = "cohere",
    **kwargs
) -> str:
    """
    Convenience function for multi-provider optimization.
    
    Args:
        prompt: Original prompt
        query: Reference query
        max_tokens: Token budget
        cohere_api_key: Cohere API key
        gemini_api_key: Gemini API key
        primary_provider: Primary provider to use
        **kwargs: Additional optimization parameters
    
    Returns:
        Optimized prompt
    """
    config = MultiProviderConfig(
        cohere_api_key=cohere_api_key,
        gemini_api_key=gemini_api_key,
        primary_provider=primary_provider
    )
    
    optimizer = MultiProviderOptimizer(config)
    return optimizer.optimize_prompt(prompt, query, max_tokens, **kwargs)

def optimize_prompt_auto_multi(
    prompt: str,
    query: str,
    cohere_api_key: Optional[str] = None,
    gemini_api_key: Optional[str] = None,
    primary_provider: str = "cohere",
    **kwargs
) -> str:
    """
    Convenience function for auto multi-provider optimization.
    
    Args:
        prompt: Original prompt
        query: Reference query
        cohere_api_key: Cohere API key
        gemini_api_key: Gemini API key
        primary_provider: Primary provider to use
        **kwargs: Additional optimization parameters
    
    Returns:
        Optimized prompt
    """
    config = MultiProviderConfig(
        cohere_api_key=cohere_api_key,
        gemini_api_key=gemini_api_key,
        primary_provider=primary_provider
    )
    
    optimizer = MultiProviderOptimizer(config)
    return optimizer.optimize_prompt_auto(prompt, query, **kwargs)
