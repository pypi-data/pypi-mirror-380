"""
Multi-provider support for PromptFit.

Supports multiple LLM providers with a unified interface.
"""

from .base import LLMProvider, EmbeddingProvider, GenerationConfig, EmbeddingConfig
from .cohere_provider import CohereProvider
from .gemini_provider import GeminiProvider
from .provider_manager import ProviderManager, create_provider_manager

__all__ = [
    "LLMProvider",
    "EmbeddingProvider",
    "GenerationConfig", 
    "EmbeddingConfig",
    "CohereProvider",
    "GeminiProvider",
    "ProviderManager",
    "create_provider_manager"
]
