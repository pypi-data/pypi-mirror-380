"""
Google Gemini provider implementation.
"""

import logging
from typing import List, Dict, Any, Optional

try:
    import google.generativeai as genai
except ImportError:
    genai = None

from .base import LLMProvider, GenerationConfig

logger = logging.getLogger(__name__)

class GeminiProvider(LLMProvider):
    """Google Gemini provider for text generation."""
    
    def __init__(self, api_key: str, **kwargs):
        super().__init__(api_key, **kwargs)
        
        if genai is None:
            raise ImportError("google-generativeai package is required. Install with: pip install google-generativeai")
        
        # Configure Gemini
        genai.configure(api_key=api_key)
        
        self.generation_model_name = kwargs.get("generation_model", "gemini-1.5-pro")
        self.model = genai.GenerativeModel(self.generation_model_name)
        
        # Configure generation settings
        self.generation_config = genai.types.GenerationConfig(
            temperature=kwargs.get("temperature", 0.3),
            top_p=kwargs.get("top_p", 0.9),
            top_k=kwargs.get("top_k", 40),
            max_output_tokens=kwargs.get("max_tokens", 2048),
        )
    
    @property
    def provider_name(self) -> str:
        return "gemini"
    
    @property
    def supported_models(self) -> List[str]:
        return [
            "gemini-1.5-pro",
            "gemini-1.5-flash", 
            "gemini-1.0-pro",
            "gemini-pro-vision"
        ]
    
    def generate(
        self, 
        prompt: str, 
        config: Optional[GenerationConfig] = None
    ) -> str:
        """Generate text using Gemini."""
        try:
            # Update generation config if provided
            generation_config = self.generation_config
            if config:
                generation_config = genai.types.GenerationConfig(
                    temperature=config.temperature,
                    top_p=config.top_p,
                    top_k=config.top_k,
                    max_output_tokens=config.max_tokens,
                    stop_sequences=config.stop_sequences or []
                )
            
            # Generate response
            response = self.model.generate_content(
                prompt,
                generation_config=generation_config
            )
            
            # Handle response
            if response.text:
                return response.text.strip()
            else:
                # Check if response was blocked
                if hasattr(response, 'prompt_feedback'):
                    logger.warning(f"Gemini response blocked: {response.prompt_feedback}")
                return ""
                
        except Exception as e:
            logger.error(f"Gemini generation error: {e}")
            raise
    
    def get_model_info(self) -> Dict[str, Any]:
        """Get model information."""
        return {
            "provider": self.provider_name,
            "generation_model": self.generation_model_name,
            "supported_models": self.supported_models,
            "has_embeddings": False,
            "context_window": self._get_context_window()
        }
    
    def _get_context_window(self) -> int:
        """Get context window size for the model."""
        context_windows = {
            "gemini-1.5-pro": 2_000_000,
            "gemini-1.5-flash": 1_000_000,
            "gemini-1.0-pro": 32_768,
            "gemini-pro-vision": 16_384
        }
        return context_windows.get(self.generation_model_name, 32_768)
    
    def estimate_tokens(self, text: str) -> int:
        """Estimate token count for Gemini."""
        try:
            # Use Gemini's token counting if available
            response = self.model.count_tokens(text)
            return response.total_tokens
        except Exception as e:
            logger.debug(f"Token counting failed, using fallback: {e}")
            # Fallback: Gemini uses similar tokenization to GPT
            # Approximately 4 characters per token for English
            return max(1, len(text) // 4)
    
    def list_available_models(self) -> List[str]:
        """List available Gemini models."""
        try:
            models = []
            for model in genai.list_models():
                if 'generateContent' in model.supported_generation_methods:
                    models.append(model.name.replace('models/', ''))
            return models
        except Exception as e:
            logger.error(f"Failed to list Gemini models: {e}")
            return self.supported_models
