"""
Provider manager for handling multiple LLM providers with failover.
"""

import logging
from typing import List, Dict, Any, Optional, Union
from enum import Enum

from .base import LLMProvider, EmbeddingProvider, GenerationConfig, EmbeddingConfig
from .cohere_provider import CohereProvider
from .gemini_provider import GeminiProvider

logger = logging.getLogger(__name__)

class ProviderType(Enum):
    """Supported provider types."""
    COHERE = "cohere"
    GEMINI = "gemini"

class ProviderManager:
    """Manages multiple LLM providers with failover support."""
    
    def __init__(self, 
                 primary_provider: LLMProvider,
                 fallback_providers: Optional[List[LLMProvider]] = None,
                 embedding_provider: Optional[EmbeddingProvider] = None):
        """
        Initialize provider manager.
        
        Args:
            primary_provider: Primary LLM provider
            fallback_providers: List of fallback providers
            embedding_provider: Provider for embeddings (can be same as primary)
        """
        self.primary_provider = primary_provider
        self.fallback_providers = fallback_providers or []
        self.embedding_provider = embedding_provider or primary_provider
        
        # Validate embedding provider
        if not isinstance(self.embedding_provider, EmbeddingProvider):
            logger.warning("Embedding provider doesn't support embeddings, using Cohere as fallback")
            # This would need to be handled based on available API keys
    
    @classmethod
    def create_from_config(cls, config: Dict[str, Any]) -> 'ProviderManager':
        """Create provider manager from configuration."""
        providers = []
        embedding_provider = None
        
        # Create providers based on config
        if config.get("cohere_api_key"):
            cohere_provider = CohereProvider(
                api_key=config["cohere_api_key"],
                generation_model=config.get("cohere_model", "command-r-08-2024"),
                embedding_model=config.get("cohere_embedding_model", "embed-english-v3.0")
            )
            providers.append(cohere_provider)
            if embedding_provider is None:
                embedding_provider = cohere_provider
        
        if config.get("gemini_api_key"):
            gemini_provider = GeminiProvider(
                api_key=config["gemini_api_key"],
                generation_model=config.get("gemini_model", "gemini-1.5-flash")
            )
            providers.append(gemini_provider)
        
        if not providers:
            raise ValueError("At least one provider API key must be provided")
        
        # Set primary and fallback providers
        primary = providers[0]
        fallbacks = providers[1:] if len(providers) > 1 else []
        
        return cls(
            primary_provider=primary,
            fallback_providers=fallbacks,
            embedding_provider=embedding_provider
        )
    
    def generate(self, 
                prompt: str, 
                config: Optional[GenerationConfig] = None,
                use_fallback: bool = True) -> str:
        """
        Generate text with automatic failover.
        
        Args:
            prompt: Input prompt
            config: Generation configuration
            use_fallback: Whether to use fallback providers on failure
        
        Returns:
            Generated text
        """
        providers_to_try = [self.primary_provider]
        if use_fallback:
            providers_to_try.extend(self.fallback_providers)
        
        last_error = None
        
        for i, provider in enumerate(providers_to_try):
            try:
                logger.info(f"Attempting generation with {provider.provider_name} (attempt {i+1})")
                result = provider.generate(prompt, config)
                
                if i > 0:  # Used fallback
                    logger.warning(f"Primary provider failed, used fallback: {provider.provider_name}")
                
                return result
                
            except Exception as e:
                last_error = e
                logger.error(f"Provider {provider.provider_name} failed: {e}")
                
                if i == len(providers_to_try) - 1:  # Last provider
                    logger.error("All providers failed")
                    raise last_error
                else:
                    logger.info(f"Trying next provider...")
        
        raise last_error or Exception("No providers available")
    
    def embed(self, 
              texts: List[str], 
              config: Optional[EmbeddingConfig] = None) -> List[List[float]]:
        """
        Generate embeddings using the embedding provider.
        
        Args:
            texts: List of texts to embed
            config: Embedding configuration
        
        Returns:
            List of embedding vectors
        """
        if not isinstance(self.embedding_provider, EmbeddingProvider):
            raise ValueError("No embedding provider available")
        
        try:
            return self.embedding_provider.embed(texts, config)
        except Exception as e:
            logger.error(f"Embedding generation failed: {e}")
            raise
    
    def get_provider_info(self) -> Dict[str, Any]:
        """Get information about all configured providers."""
        info = {
            "primary_provider": self.primary_provider.get_model_info(),
            "fallback_providers": [p.get_model_info() for p in self.fallback_providers],
            "embedding_provider": None
        }
        
        if isinstance(self.embedding_provider, EmbeddingProvider):
            if hasattr(self.embedding_provider, 'get_model_info'):
                info["embedding_provider"] = self.embedding_provider.get_model_info()
            else:
                info["embedding_provider"] = {"provider": self.embedding_provider.provider_name}
        
        return info
    
    def estimate_tokens(self, text: str, provider: Optional[str] = None) -> int:
        """
        Estimate token count using specified or primary provider.
        
        Args:
            text: Text to estimate tokens for
            provider: Specific provider to use (optional)
        
        Returns:
            Estimated token count
        """
        target_provider = self.primary_provider
        
        if provider:
            # Find specific provider
            all_providers = [self.primary_provider] + self.fallback_providers
            for p in all_providers:
                if p.provider_name == provider:
                    target_provider = p
                    break
        
        if hasattr(target_provider, 'estimate_tokens'):
            return target_provider.estimate_tokens(text)
        else:
            # Fallback estimation
            return max(1, len(text) // 4)
    
    def health_check(self) -> Dict[str, bool]:
        """Check health of all providers."""
        health = {}
        
        test_prompt = "Hello"
        test_config = GenerationConfig(max_tokens=10, temperature=0.1)
        
        # Check generation providers
        for provider in [self.primary_provider] + self.fallback_providers:
            try:
                result = provider.generate(test_prompt, test_config)
                health[f"{provider.provider_name}_generation"] = bool(result)
            except Exception as e:
                logger.error(f"Health check failed for {provider.provider_name}: {e}")
                health[f"{provider.provider_name}_generation"] = False
        
        # Check embedding provider
        if isinstance(self.embedding_provider, EmbeddingProvider):
            try:
                embeddings = self.embedding_provider.embed(["test"])
                health[f"{self.embedding_provider.provider_name}_embeddings"] = bool(embeddings)
            except Exception as e:
                logger.error(f"Embedding health check failed: {e}")
                health[f"{self.embedding_provider.provider_name}_embeddings"] = False
        
        return health

def create_provider_manager(
    cohere_api_key: Optional[str] = None,
    gemini_api_key: Optional[str] = None,
    primary_provider: str = "cohere",
    **kwargs
) -> ProviderManager:
    """
    Convenience function to create a provider manager.
    
    Args:
        cohere_api_key: Cohere API key
        gemini_api_key: Gemini API key  
        primary_provider: Which provider to use as primary
        **kwargs: Additional configuration
    
    Returns:
        Configured ProviderManager
    """
    config = {
        "cohere_api_key": cohere_api_key,
        "gemini_api_key": gemini_api_key,
        **kwargs
    }
    
    manager = ProviderManager.create_from_config(config)
    
    # Reorder providers if different primary requested
    if primary_provider == "gemini" and gemini_api_key:
        # Find gemini provider and make it primary
        all_providers = [manager.primary_provider] + manager.fallback_providers
        gemini_provider = None
        other_providers = []
        
        for provider in all_providers:
            if provider.provider_name == "gemini":
                gemini_provider = provider
            else:
                other_providers.append(provider)
        
        if gemini_provider:
            manager.primary_provider = gemini_provider
            manager.fallback_providers = other_providers
    
    return manager
