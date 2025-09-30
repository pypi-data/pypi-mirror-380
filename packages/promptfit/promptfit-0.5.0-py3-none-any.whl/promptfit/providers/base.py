"""
Base classes for LLM providers.
"""

from abc import ABC, abstractmethod
from typing import List, Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class GenerationConfig:
    """Configuration for text generation."""
    max_tokens: int = 2048
    temperature: float = 0.3
    top_p: float = 0.9
    top_k: Optional[int] = None
    stop_sequences: Optional[List[str]] = None

@dataclass
class EmbeddingConfig:
    """Configuration for embeddings."""
    model: Optional[str] = None
    input_type: str = "search_document"
    batch_size: int = 96

class LLMProvider(ABC):
    """Abstract base class for LLM providers."""
    
    def __init__(self, api_key: str, **kwargs):
        self.api_key = api_key
        self.config = kwargs
    
    @abstractmethod
    def generate(
        self, 
        prompt: str, 
        config: Optional[GenerationConfig] = None
    ) -> str:
        """Generate text from prompt."""
        pass
    
    @abstractmethod
    def get_model_info(self) -> Dict[str, Any]:
        """Get information about the model."""
        pass
    
    @property
    @abstractmethod
    def provider_name(self) -> str:
        """Name of the provider."""
        pass
    
    @property
    @abstractmethod
    def supported_models(self) -> List[str]:
        """List of supported models."""
        pass

class EmbeddingProvider(ABC):
    """Abstract base class for embedding providers."""
    
    def __init__(self, api_key: str, **kwargs):
        self.api_key = api_key
        self.config = kwargs
    
    @abstractmethod
    def embed(
        self, 
        texts: List[str], 
        config: Optional[EmbeddingConfig] = None
    ) -> List[List[float]]:
        """Generate embeddings for texts."""
        pass
    
    @abstractmethod
    def get_embedding_dimension(self) -> int:
        """Get the dimension of embeddings."""
        pass
    
    @property
    @abstractmethod
    def provider_name(self) -> str:
        """Name of the provider."""
        pass

class UnifiedProvider(LLMProvider, EmbeddingProvider):
    """Base class for providers that support both generation and embeddings."""
    pass
