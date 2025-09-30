from typing import List, Dict

try:
    import cohere # type: ignore
except ImportError:
    cohere = None

from .utils import get_cohere_api_key
from .config import COHERE_EMBED_MODEL

# Simple in-memory cache for embeddings; key includes input_type for correctness
_embedding_cache: Dict[str, List[float]] = {}

def _cache_key(text: str, input_type: str) -> str:
    return f"{input_type}::" + text

def get_embeddings_typed(texts: List[str], *, input_type: str) -> List[List[float]]:
    """Get embeddings with a specified input_type (e.g., 'search_document' or 'search_query')."""
    if cohere is None:
        raise ImportError("cohere package is required for embedding generation.")
    api_key = get_cohere_api_key()
    co = cohere.Client(api_key)
    # Compute which are missing from cache (with input_type in the key)
    uncached = [t for t in texts if _cache_key(t, input_type) not in _embedding_cache]
    if uncached:
        def _batch(iterable, size=96):
            for i in range(0, len(iterable), size):
                yield iterable[i:i + size]
        for batch_texts in _batch(uncached):
            response = co.embed(
                texts=batch_texts,
                model=COHERE_EMBED_MODEL,
                input_type=input_type,
            )
            for text, emb in zip(batch_texts, response.embeddings):
                _embedding_cache[_cache_key(text, input_type)] = emb
    return [_embedding_cache[_cache_key(t, input_type)] for t in texts]

def get_embeddings(texts: List[str]) -> List[List[float]]:
    """Get embeddings for a list of texts using Cohere. Uses in-memory cache."""
    if cohere is None:
        raise ImportError("cohere package is required for embedding generation.")
    api_key = get_cohere_api_key()
    co = cohere.Client(api_key)
    # Backward-compat default to documents mode
    input_type = "search_document"
    uncached = [t for t in texts if _cache_key(t, input_type) not in _embedding_cache]
    if uncached:
        # ===== CHANGED: Batch calls to avoid model limits =====
        def _batch(iterable, size=96):
            for i in range(0, len(iterable), size):
                yield iterable[i:i + size]

        for batch_texts in _batch(uncached):
            response = co.embed(
                texts=batch_texts,
                model=COHERE_EMBED_MODEL,
                input_type=input_type  # Required for embed-english-v3.0
            )
            for text, emb in zip(batch_texts, response.embeddings):
                _embedding_cache[_cache_key(text, input_type)] = emb
    return [_embedding_cache[_cache_key(t, input_type)] for t in texts]


