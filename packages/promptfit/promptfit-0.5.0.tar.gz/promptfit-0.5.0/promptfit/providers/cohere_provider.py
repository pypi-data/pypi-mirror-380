"""
Cohere provider implementation.
"""

import logging
from typing import List, Dict, Any, Optional

try:
    import cohere
except ImportError:
    cohere = None

from .base import UnifiedProvider, GenerationConfig, EmbeddingConfig

logger = logging.getLogger(__name__)

class CohereProvider(UnifiedProvider):
    """Cohere provider for both generation and embeddings."""
    
    def __init__(self, api_key: str, **kwargs):
        super().__init__(api_key, **kwargs)
        
        if cohere is None:
            raise ImportError("cohere package is required. Install with: pip install cohere")
        
        self.client = cohere.Client(api_key)
        self.generation_model = kwargs.get("generation_model", "command-r-08-2024")
        self.embedding_model = kwargs.get("embedding_model", "embed-english-v3.0")
    
    @property
    def provider_name(self) -> str:
        return "cohere"
    
    @property
    def supported_models(self) -> List[str]:
        return [
            "command-r-08-2024",
            "command-r-plus-08-2024",
            "command-light",
            "embed-english-v3.0",
            "embed-multilingual-v3.0"
        ]
    
    def generate(
        self, 
        prompt: str, 
        config: Optional[GenerationConfig] = None
    ) -> str:
        """Generate text using Cohere Chat API."""
        if config is None:
            config = GenerationConfig()
        
        try:
            response = self.client.chat(
                model=self.generation_model,
                message=prompt,
                temperature=config.temperature,
                max_tokens=config.max_tokens,
                p=config.top_p,
                k=config.top_k,
                stop_sequences=config.stop_sequences or []
            )
            
            # Handle different response formats
            if hasattr(response, 'text') and response.text:
                return response.text.strip()
            elif hasattr(response, 'message') and hasattr(response.message, 'content'):
                # Handle structured response
                if isinstance(response.message.content, list):
                    text_parts = []
                    for content in response.message.content:
                        if hasattr(content, 'text'):
                            text_parts.append(content.text)
                        elif isinstance(content, dict) and content.get('type') == 'text':
                            text_parts.append(content.get('text', ''))
                    return ''.join(text_parts).strip()
                else:
                    return str(response.message.content).strip()
            else:
                return str(response).strip()
                
        except Exception as e:
            if "rate limit" in str(e).lower():
                logger.error(f"Cohere rate limit exceeded: {e}")
                raise
            elif "api" in str(e).lower() or "cohere" in str(e).lower():
                logger.error(f"Cohere API error: {e}")
                raise
            else:
                logger.error(f"Unexpected Cohere error: {e}")
                raise
    
    def embed(
        self, 
        texts: List[str], 
        config: Optional[EmbeddingConfig] = None
    ) -> List[List[float]]:
        """Generate embeddings using Cohere."""
        if config is None:
            config = EmbeddingConfig()
        
        if not texts:
            return []
        
        try:
            # Batch processing for large requests
            all_embeddings = []
            batch_size = config.batch_size
            
            for i in range(0, len(texts), batch_size):
                batch = texts[i:i + batch_size]
                
                response = self.client.embed(
                    texts=batch,
                    model=config.model or self.embedding_model,
                    input_type=config.input_type
                )
                
                all_embeddings.extend(response.embeddings)
            
            return all_embeddings
            
        except Exception as e:
            if "rate limit" in str(e).lower():
                logger.error(f"Cohere embedding rate limit exceeded: {e}")
                raise
            elif "api" in str(e).lower() or "cohere" in str(e).lower():
                logger.error(f"Cohere embedding API error: {e}")
                raise
            else:
                logger.error(f"Unexpected Cohere embedding error: {e}")
                raise
    
    def get_embedding_dimension(self) -> int:
        """Get embedding dimension for Cohere models."""
        model_dimensions = {
            "embed-english-v3.0": 1024,
            "embed-multilingual-v3.0": 1024,
            "embed-english-light-v3.0": 384,
            "embed-multilingual-light-v3.0": 384
        }
        return model_dimensions.get(self.embedding_model, 1024)
    
    def get_model_info(self) -> Dict[str, Any]:
        """Get model information."""
        return {
            "provider": self.provider_name,
            "generation_model": self.generation_model,
            "embedding_model": self.embedding_model,
            "embedding_dimension": self.get_embedding_dimension(),
            "supported_models": self.supported_models
        }
    
    def tokenize(self, text: str) -> List[str]:
        """Tokenize text using Cohere tokenizer."""
        try:
            response = self.client.tokenize(text)
            return response.tokens
        except Exception as e:
            logger.error(f"Cohere tokenization error: {e}")
            # Fallback to simple word splitting
            return text.split()
    
    def estimate_tokens(self, text: str) -> int:
        """Estimate token count."""
        try:
            tokens = self.tokenize(text)
            return len(tokens)
        except Exception:
            # Fallback estimation: ~4 chars per token
            return max(1, len(text) // 4)
