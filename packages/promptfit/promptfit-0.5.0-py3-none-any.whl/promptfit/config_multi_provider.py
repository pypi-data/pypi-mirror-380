"""
Multi-provider configuration for PromptFit.
"""

import os
from typing import Optional, Dict, Any
from dataclasses import dataclass
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

@dataclass
class MultiProviderConfig:
    """Configuration for multiple LLM providers."""
    
    # API Keys
    cohere_api_key: Optional[str] = None
    gemini_api_key: Optional[str] = None
    
    # Primary provider selection
    primary_provider: str = "cohere"
    
    # Model configurations
    cohere_generation_model: str = "command-r-08-2024"
    cohere_embedding_model: str = "embed-english-v3.0"
    gemini_generation_model: str = "gemini-1.5-pro"
    
    # Performance settings
    max_concurrent_requests: int = 10
    request_timeout: int = 30
    enable_fallback: bool = True
    
    # Cache settings
    cache_size: int = 1000
    cache_ttl: int = 3600
    
    @classmethod
    def from_env(cls) -> 'MultiProviderConfig':
        """Create configuration from environment variables."""
        return cls(
            cohere_api_key=os.getenv("COHERE_API_KEY"),
            gemini_api_key=os.getenv("GEMINI_API_KEY"),
            primary_provider=os.getenv("PROMPTFIT_PRIMARY_PROVIDER", "cohere"),
            cohere_generation_model=os.getenv("COHERE_GENERATION_MODEL", "command-r-08-2024"),
            cohere_embedding_model=os.getenv("COHERE_EMBEDDING_MODEL", "embed-english-v3.0"),
            gemini_generation_model=os.getenv("GEMINI_GENERATION_MODEL", "gemini-1.5-flash"),
            max_concurrent_requests=int(os.getenv("PROMPTFIT_MAX_CONCURRENT", "10")),
            request_timeout=int(os.getenv("PROMPTFIT_REQUEST_TIMEOUT", "30")),
            enable_fallback=os.getenv("PROMPTFIT_ENABLE_FALLBACK", "true").lower() == "true",
            cache_size=int(os.getenv("PROMPTFIT_CACHE_SIZE", "1000")),
            cache_ttl=int(os.getenv("PROMPTFIT_CACHE_TTL", "3600"))
        )
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for provider manager."""
        return {
            "cohere_api_key": self.cohere_api_key,
            "gemini_api_key": self.gemini_api_key,
            "cohere_model": self.cohere_generation_model,
            "cohere_embedding_model": self.cohere_embedding_model,
            "gemini_model": self.gemini_generation_model,
            "primary_provider": self.primary_provider,
            "enable_fallback": self.enable_fallback
        }
    
    def validate(self) -> bool:
        """Validate configuration."""
        if not self.cohere_api_key and not self.gemini_api_key:
            raise ValueError("At least one API key (Cohere or Gemini) must be provided")
        
        if self.primary_provider not in ["cohere", "gemini"]:
            raise ValueError("Primary provider must be 'cohere' or 'gemini'")
        
        if self.primary_provider == "cohere" and not self.cohere_api_key:
            raise ValueError("Cohere API key required when Cohere is primary provider")
        
        if self.primary_provider == "gemini" and not self.gemini_api_key:
            raise ValueError("Gemini API key required when Gemini is primary provider")
        
        return True

# Supported models by provider
SUPPORTED_MODELS = {
    "cohere": {
        "generation": [
            "command-r-08-2024",
            "command-r-plus-08-2024", 
            "command-light"
        ],
        "embedding": [
            "embed-english-v3.0",
            "embed-multilingual-v3.0",
            "embed-english-light-v3.0",
            "embed-multilingual-light-v3.0"
        ]
    },
    "gemini": {
        "generation": [
            "gemini-1.5-pro",
            "gemini-1.5-flash",
            "gemini-1.0-pro",
            "gemini-pro-vision"
        ],
        "embedding": []  # Gemini doesn't provide embeddings
    }
}

def validate_model(provider: str, model: str, model_type: str = "generation") -> bool:
    """Validate that a model is supported by the provider."""
    if provider not in SUPPORTED_MODELS:
        return False
    
    if model_type not in SUPPORTED_MODELS[provider]:
        return False
    
    return model in SUPPORTED_MODELS[provider][model_type]

# Default token limits
DEFAULT_TOKEN_LIMITS = {
    "cohere": {
        "command-r-08-2024": 128_000,
        "command-r-plus-08-2024": 128_000,
        "command-light": 4_096
    },
    "gemini": {
        "gemini-1.5-pro": 2_000_000,
        "gemini-1.5-flash": 1_000_000,
        "gemini-1.0-pro": 32_768,
        "gemini-pro-vision": 16_384
    }
}

def get_token_limit(provider: str, model: str) -> int:
    """Get token limit for a specific model."""
    return DEFAULT_TOKEN_LIMITS.get(provider, {}).get(model, 4_096)
