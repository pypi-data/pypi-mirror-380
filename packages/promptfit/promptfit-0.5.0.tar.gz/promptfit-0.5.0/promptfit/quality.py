"""
Quality assurance and self-consistency checks for PromptFit optimization.
"""
from typing import List, Dict, Optional, Callable, Tuple
import numpy as np
from .token_budget import estimate_tokens
from .relevance import rank_segments_by_relevance
from .utils import split_sentences

def self_consistency_check(
    original_prompt: str,
    optimized_prompt: str,
    query: str,
    get_embeddings_fn: Callable[[List[str]], List[List[float]]],
    *,
    similarity_threshold: float = 0.85
) -> Dict[str, float]:
    """
    Perform self-consistency check between original and optimized prompts.
    
    Returns metrics indicating how well the optimized prompt preserves
    the semantic content and intent of the original.
    """
    # Split both prompts into sentences for granular comparison
    orig_sentences = split_sentences(original_prompt)
    opt_sentences = split_sentences(optimized_prompt)
    
    if not orig_sentences or not opt_sentences:
        return {"semantic_preservation": 0.0, "content_coverage": 0.0, "compression_ratio": 0.0}
    
    # Get embeddings for all sentences
    all_sentences = orig_sentences + opt_sentences
    embeddings = get_embeddings_fn(all_sentences)
    
    orig_embs = embeddings[:len(orig_sentences)]
    opt_embs = embeddings[len(orig_sentences):]
    
    # Compute semantic preservation: how well optimized sentences match original intent
    preservation_scores = []
    for opt_emb in opt_embs:
        # Find best match in original sentences
        similarities = []
        for orig_emb in orig_embs:
            # Cosine similarity
            opt_norm = np.array(opt_emb) / (np.linalg.norm(opt_emb) + 1e-8)
            orig_norm = np.array(orig_emb) / (np.linalg.norm(orig_emb) + 1e-8)
            sim = np.dot(opt_norm, orig_norm)
            similarities.append(sim)
        
        if similarities:
            preservation_scores.append(max(similarities))
    
    semantic_preservation = np.mean(preservation_scores) if preservation_scores else 0.0
    
    # Compute content coverage: what fraction of original content is represented
    coverage_scores = []
    for orig_emb in orig_embs:
        similarities = []
        for opt_emb in opt_embs:
            orig_norm = np.array(orig_emb) / (np.linalg.norm(orig_emb) + 1e-8)
            opt_norm = np.array(opt_emb) / (np.linalg.norm(opt_emb) + 1e-8)
            sim = np.dot(orig_norm, opt_norm)
            similarities.append(sim)
        
        if similarities:
            coverage_scores.append(max(similarities))
    
    content_coverage = np.mean(coverage_scores) if coverage_scores else 0.0
    
    # Compression ratio
    orig_tokens = estimate_tokens(original_prompt)
    opt_tokens = estimate_tokens(optimized_prompt)
    compression_ratio = opt_tokens / orig_tokens if orig_tokens > 0 else 0.0
    
    return {
        "semantic_preservation": float(semantic_preservation),
        "content_coverage": float(content_coverage), 
        "compression_ratio": float(compression_ratio)
    }

def evaluate_relevance_quality(
    segments: List[str],
    query: str,
    get_embeddings_fn: Callable[[List[str]], List[List[float]]],
    *,
    min_relevance_threshold: float = 0.3
) -> Dict[str, float]:
    """
    Evaluate the quality of relevance ranking and filtering.
    
    Returns metrics about relevance distribution and quality.
    """
    if not segments:
        return {"avg_relevance": 0.0, "relevance_std": 0.0, "low_relevance_ratio": 1.0}
    
    # Get relevance scores
    ranked = rank_segments_by_relevance(
        segments, 
        query, 
        get_embeddings_fn,
        adaptive_threshold=False  # Get all scores for analysis
    )
    
    if not ranked:
        return {"avg_relevance": 0.0, "relevance_std": 0.0, "low_relevance_ratio": 1.0}
    
    scores = [score for _, score in ranked]
    
    avg_relevance = np.mean(scores)
    relevance_std = np.std(scores)
    low_relevance_count = sum(1 for score in scores if score < min_relevance_threshold)
    low_relevance_ratio = low_relevance_count / len(scores)
    
    return {
        "avg_relevance": float(avg_relevance),
        "relevance_std": float(relevance_std),
        "low_relevance_ratio": float(low_relevance_ratio)
    }

def detect_hallucination_risk(
    optimized_prompt: str,
    original_segments: List[str],
    get_embeddings_fn: Callable[[List[str]], List[List[float]]],
    *,
    risk_threshold: float = 0.4
) -> Dict[str, float]:
    """
    Detect potential hallucination risk in optimized prompt.
    
    Checks if optimized content deviates significantly from original segments.
    """
    if not original_segments:
        return {"hallucination_risk": 0.0, "novel_content_ratio": 0.0}
    
    opt_sentences = split_sentences(optimized_prompt)
    if not opt_sentences:
        return {"hallucination_risk": 0.0, "novel_content_ratio": 0.0}
    
    # Get embeddings
    all_text = original_segments + opt_sentences
    embeddings = get_embeddings_fn(all_text)
    
    orig_embs = embeddings[:len(original_segments)]
    opt_embs = embeddings[len(original_segments):]
    
    # For each optimized sentence, find best match in original segments
    novel_content_count = 0
    min_similarities = []
    
    for opt_emb in opt_embs:
        similarities = []
        for orig_emb in orig_embs:
            opt_norm = np.array(opt_emb) / (np.linalg.norm(opt_emb) + 1e-8)
            orig_norm = np.array(orig_emb) / (np.linalg.norm(orig_emb) + 1e-8)
            sim = np.dot(opt_norm, orig_norm)
            similarities.append(sim)
        
        if similarities:
            max_sim = max(similarities)
            min_similarities.append(max_sim)
            
            if max_sim < risk_threshold:
                novel_content_count += 1
    
    novel_content_ratio = novel_content_count / len(opt_sentences) if opt_sentences else 0.0
    avg_min_similarity = np.mean(min_similarities) if min_similarities else 0.0
    hallucination_risk = 1.0 - avg_min_similarity  # Higher when similarity is low
    
    return {
        "hallucination_risk": float(hallucination_risk),
        "novel_content_ratio": float(novel_content_ratio)
    }
