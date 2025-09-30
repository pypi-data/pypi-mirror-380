"""
Document summarization for long chunks before optimization.
"""
from typing import List, Optional
from .paraphraser import paraphrase_prompt
from .token_budget import estimate_tokens

def summarize_long_chunks(
    chunks: List[str], 
    *,
    max_chunk_tokens: int = 300,
    summary_ratio: float = 0.6
) -> List[str]:
    """
    Summarize chunks that exceed max_chunk_tokens to reduce noise.
    
    Args:
        chunks: List of text chunks to potentially summarize
        max_chunk_tokens: Threshold above which chunks get summarized
        summary_ratio: Target ratio for summarization (0.6 = 60% of original)
    
    Returns:
        List of chunks with long ones summarized
    """
    summarized_chunks = []
    
    for chunk in chunks:
        chunk_tokens = estimate_tokens(chunk)
        
        if chunk_tokens > max_chunk_tokens:
            # Summarize this chunk
            target_tokens = max(50, int(chunk_tokens * summary_ratio))
            
            summary_instructions = (
                f"Summarize this content concisely while preserving key facts, "
                f"numbers, dates, and actionable information. Target ~{target_tokens} tokens. "
                f"Maintain technical accuracy and specific details."
            )
            
            try:
                summarized = paraphrase_prompt(
                    chunk,
                    instructions=summary_instructions,
                    max_tokens=target_tokens
                )
                summarized_chunks.append(summarized)
            except Exception:
                # Fallback: simple truncation if summarization fails
                words = chunk.split()
                target_words = int(len(words) * summary_ratio)
                summarized_chunks.append(" ".join(words[:target_words]))
        else:
            # Keep chunk as-is
            summarized_chunks.append(chunk)
    
    return summarized_chunks

def enforce_prompt_structure(
    content: str,
    *,
    system_message: Optional[str] = None,
    user_instructions: Optional[str] = None,
    add_hallucination_guard: bool = True
) -> str:
    """
    Enforce consistent prompt template structure.
    
    Args:
        content: Main content to structure
        system_message: Optional system message to prepend
        user_instructions: Optional user instructions to append
        add_hallucination_guard: Whether to add anti-hallucination instructions
    
    Returns:
        Structured prompt following system → context → user → instructions format
    """
    parts = []
    
    # System message
    if system_message:
        parts.append(f"System: {system_message}")
    elif add_hallucination_guard:
        default_system = (
            "You are a helpful assistant. Base your responses strictly on the provided context. "
            "If information is not available in the context, clearly state that you don't have "
            "that information rather than making assumptions."
        )
        parts.append(f"System: {default_system}")
    
    # Main content
    if content.strip():
        parts.append(f"Context:\n{content}")
    
    # User instructions
    if user_instructions:
        parts.append(f"Instructions: {user_instructions}")
    
    return "\n\n".join(parts)

def detect_and_merge_duplicates(
    chunks: List[str],
    *,
    similarity_threshold: float = 0.85
) -> List[str]:
    """
    Detect and merge highly similar chunks to reduce redundancy.
    
    Uses simple text-based similarity (Jaccard) for efficiency.
    For semantic similarity, use the embedding-based dedup in optimizer.py.
    """
    if len(chunks) <= 1:
        return chunks
    
    def _normalize_text(text: str) -> set[str]:
        """Normalize text to word set for Jaccard similarity."""
        words = text.lower().split()
        return set(word.strip(".,!?;:()[]{}\"'") for word in words if len(word) > 2)
    
    merged_chunks = []
    processed_indices = set()
    
    for i, chunk in enumerate(chunks):
        if i in processed_indices:
            continue
            
        chunk_words = _normalize_text(chunk)
        merged_content = [chunk]
        processed_indices.add(i)
        
        # Find similar chunks to merge
        for j, other_chunk in enumerate(chunks[i+1:], start=i+1):
            if j in processed_indices:
                continue
                
            other_words = _normalize_text(other_chunk)
            
            # Jaccard similarity
            intersection = len(chunk_words & other_words)
            union = len(chunk_words | other_words)
            
            if union > 0 and (intersection / union) >= similarity_threshold:
                merged_content.append(other_chunk)
                processed_indices.add(j)
        
        # If we found duplicates, merge them intelligently
        if len(merged_content) > 1:
            # Take the longest version as base, add unique info from others
            base_chunk = max(merged_content, key=len)
            merged_chunks.append(base_chunk)  # For now, just use the longest
        else:
            merged_chunks.append(chunk)
    
    return merged_chunks
