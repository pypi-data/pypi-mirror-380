import re
from typing import List
from functools import lru_cache

try:
    import cohere # type: ignore
    _has_cohere = True
except ImportError:
    _has_cohere = False

_S_NON_WS_RE = re.compile(r'\S+')

@lru_cache(maxsize=4096)
def _estimate_tokens_uncached(text: str) -> int:
    if _has_cohere:
        try:
            from .utils import get_cohere_api_key
            api_key = get_cohere_api_key()
            co = cohere.Client(api_key)
            resp = co.tokenize(text)
            return len(resp.tokens)
        except Exception:
            pass
    tokens = _S_NON_WS_RE.findall(text)
    return max(1, int(len(tokens) / 0.75))

def estimate_tokens(text: str, role: str = "user", include_separators: bool = True) -> int:
    """
    Enhanced token estimation for text with role-based and separator considerations.
    
    Args:
        text: Input text to estimate
        role: Role context ("system", "user", "assistant") - affects token overhead
        include_separators: Whether to include separator tokens between sections
    
    Uses a heuristic: ~4 characters per token + role overhead + separators.
    For production accuracy, integrate with tiktoken or similar.
    """
    if not text:
        return 0
    
    # Base token count from text length
    base_tokens = max(1, len(text) // 4)
    
    # Role-based overhead (system messages, role indicators, etc.)
    role_overhead = {
        "system": 10,  # System message wrapper tokens
        "user": 5,     # User message wrapper tokens  
        "assistant": 5 # Assistant message wrapper tokens
    }
    
    tokens_with_role = base_tokens + role_overhead.get(role, 5)
    
    # Add separator tokens if requested (for multi-section prompts)
    if include_separators:
        # Estimate ~2-3 separator tokens per section boundary
        section_count = text.count('\n\n') + 1
        separator_tokens = max(0, (section_count - 1) * 3)
        tokens_with_role += separator_tokens
    
    return tokens_with_role

def estimate_tokens_per_section(sections: List[str]) -> List[int]:
    return [estimate_tokens(section) for section in sections]

def estimate_total_tokens(sections: List[str]) -> int:
    return sum(estimate_tokens_per_section(sections))

def clear_token_cache() -> None:
    _estimate_tokens_uncached.cache_clear()
