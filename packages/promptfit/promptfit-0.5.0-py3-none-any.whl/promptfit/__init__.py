"""
PromptFit: Modular toolkit for optimizing LLM prompts.

Estimate token usage, rank by semantic relevance, and compress with LLMs 
to fit any token budget. Perfect for RAG, few-shot, and instruction-heavy GenAI workflows.

Now supports multiple LLM providers (Cohere, Gemini) with automatic failover!
"""

# Core single-provider functions (backward compatibility)
from .optimizer import optimize_prompt, optimize_prompt_auto
from .token_budget import estimate_tokens, estimate_tokens_per_section, estimate_total_tokens
from .relevance import rank_segments_by_relevance, compute_cosine_similarities
from .paraphraser import paraphrase_prompt
from .quality import self_consistency_check, detect_hallucination_risk
from .summarizer import summarize_long_chunks, enforce_prompt_structure, detect_and_merge_duplicates

# Multi-provider functionality
from .multi_provider_optimizer import (
    MultiProviderOptimizer, 
    optimize_prompt_multi, 
    optimize_prompt_auto_multi
)
from .config_multi_provider import MultiProviderConfig
from .providers import (
    ProviderManager, 
    CohereProvider, 
    GeminiProvider, 
    create_provider_manager
)

__version__ = "0.5.0"  # Updated for multi-provider support

__all__ = [
    # Core functions (backward compatibility)
    "optimize_prompt",
    "optimize_prompt_auto", 
    "estimate_tokens",
    "estimate_tokens_per_section",
    "estimate_total_tokens",
    "rank_segments_by_relevance",
    "compute_cosine_similarities",
    "paraphrase_prompt",
    "self_consistency_check",
    "detect_hallucination_risk",
    "summarize_long_chunks",
    "enforce_prompt_structure",
    "detect_and_merge_duplicates",
    
    # Multi-provider functionality
    "MultiProviderOptimizer",
    "optimize_prompt_multi",
    "optimize_prompt_auto_multi",
    "MultiProviderConfig",
    "ProviderManager",
    "CohereProvider", 
    "GeminiProvider",
    "create_provider_manager"
]