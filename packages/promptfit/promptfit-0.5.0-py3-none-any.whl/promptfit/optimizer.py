from .token_budget import estimate_tokens, estimate_tokens_per_section, estimate_total_tokens
from .relevance import rank_segments_by_relevance
from .utils import split_sentences
from .paraphraser import paraphrase_prompt
from .embedder import get_embeddings
from .config import DEFAULT_MAX_TOKENS
from .quality import self_consistency_check, evaluate_relevance_quality, detect_hallucination_risk
from .summarizer import summarize_long_chunks, enforce_prompt_structure, detect_and_merge_duplicates

def optimize_prompt(
    prompt: str,
    query: str,
    max_tokens: int = DEFAULT_MAX_TOKENS,
    *,
    top_k: int = 5,
    min_keep_ratio: float = 0.6,
    paraphrase: bool = True,
    redundancy_threshold_jaccard: float = 0.85,
    quality_check: bool = False,
    fallback_on_low_relevance: bool = True,
    pre_summarize_chunks: bool = False,
    enforce_structure: bool = False,
) -> str:
    """
    Optimize a prompt to fit within a token budget:
    1. Split into sentences/sections
    2. Estimate tokens per section
    3. Rank by relevance to query
    4. Preserve top-K and ensure at least a minimum keep ratio of the budget before paraphrasing
    5. Paraphrase trimmed content (or full prompt) to enforce budget
    """
    # 1. Split and optionally pre-process
    sections = split_sentences(prompt)
    
    # Pre-summarize long chunks if requested
    if pre_summarize_chunks:
        sections = summarize_long_chunks(sections, max_chunk_tokens=400, summary_ratio=0.7)
    
    # Detect and merge duplicates
    sections = detect_and_merge_duplicates(sections, similarity_threshold=0.9)

    # 2. Estimate tokens
    tokens_per_section = estimate_tokens_per_section(sections)
    total_tokens= sum(tokens_per_section)
    # If already within budget
    if total_tokens <= max_tokens:
        return prompt

    # 3. Rank by relevance with adaptive thresholding
    ranked_sections = rank_segments_by_relevance(
        sections, 
        query, 
        get_embeddings,
        adaptive_threshold=True,
        top_k=None  # Get all for quality assessment
    )
    
    # Quality check: evaluate relevance distribution
    if quality_check:
        relevance_quality = evaluate_relevance_quality(sections, query, get_embeddings)
        # If average relevance is very low, consider fallback
        if fallback_on_low_relevance and relevance_quality["avg_relevance"] < 0.2:
            # Return minimally processed prompt to avoid irrelevant optimization
            if estimate_tokens(prompt) <= max_tokens:
                return prompt
            # Simple truncation fallback
            words = prompt.split()
            target_words = int(len(words) * (max_tokens / estimate_tokens(prompt)))
            return " ".join(words[:target_words])
    
    sorted_sections = [s for s, _ in ranked_sections]

    # 3b. Remove highly similar/near-duplicate sections (simple Jaccard on words)
    def _norm_words(s: str) -> set[str]:
        return set(w.strip(".,:;!?()[]{}'\"-").lower() for w in s.split())

    deduped_sections: list[str] = []
    seen_wordsets: list[set[str]] = []
    for s in sorted_sections:
        ws = _norm_words(s)
        is_dup = False
        for prev_ws in seen_wordsets:
            inter = len(ws & prev_ws)
            union = len(ws | prev_ws) or 1
            jacc = inter / union
            if jacc >= redundancy_threshold_jaccard:
                is_dup = True
                break
        if not is_dup:
            deduped_sections.append(s)
            seen_wordsets.append(ws)
    sorted_sections = deduped_sections

    # 4. Preserve top-K and enforce minimum keep ratio before paraphrasing
    min_keep_tokens = max(0, int(max_tokens * max(0.0, min(min_keep_ratio, 1.0))))
    pruned_sections = []
    running_total = 0

    # Always start with top-K most relevant sections (or fewer if fewer sections)
    seed = sorted_sections[: max(0, top_k)]
    for section in seed:
        sec_tokens = estimate_tokens(section)
        if running_total + sec_tokens <= max_tokens:
            pruned_sections.append(section)
            running_total += sec_tokens

    # Try to add more sections (still in relevance order) until we reach min_keep_tokens
    for section in sorted_sections[len(pruned_sections):]:
        if running_total >= min_keep_tokens:
            break
        sec_tokens = estimate_tokens(section)
        if running_total + sec_tokens <= max_tokens:
            pruned_sections.append(section)
            running_total += sec_tokens

    # If nothing fit (all sections larger than budget), fall back to the single most relevant section
    if not pruned_sections and sorted_sections:
        pruned_sections = [sorted_sections[0]]
        running_total = estimate_tokens(pruned_sections[0])

    pruned_prompt = " \n".join(pruned_sections)

    # 5. Paraphrase ONLY if needed (and enabled)
    if not pruned_sections:
        # No section fits: paraphrase original prompt
        if not paraphrase:
            return pruned_prompt
        try:
            pruned_prompt = paraphrase_prompt(
                prompt,
                instructions=(
                    "Compress as much as possible while preserving critical facts and instructions."
                ),
                max_tokens=max_tokens
            )
        except Exception:
            # Fallback: paraphrase top section
            pruned_prompt = paraphrase_prompt(
                sorted_sections[0],
                instructions=(
                    "Compress as much as possible while preserving critical facts and instructions."
                ),
                max_tokens=max_tokens
            )
    else:
        current_tokens = estimate_tokens(pruned_prompt)
        if current_tokens <= max_tokens:
            # Already fits — avoid paraphrasing to prevent over-compression
            return pruned_prompt
        if not paraphrase:
            # If paraphrasing disabled and content is still over budget, return the pruned content as-is
            return pruned_prompt
        # First try section-wise paraphrasing to distribute length more evenly
        kept = pruned_sections
        target_total = int(max_tokens * 0.9)  # leave some slack for joiners
        per_quota = max(120, target_total // max(1, len(kept)))
        section_instr = (
            "Rewrite concisely while preserving concrete facts (IDs, error codes, numbers, temperatures) "
            f"and key instructions. Aim near {per_quota} tokens for this section (±20%). "
            "Do not repeat points already covered in earlier sections; focus on unique details."
        )
        compressed_sections = []
        for sec in kept:
            compressed = paraphrase_prompt(
                sec,
                instructions=section_instr,
                max_tokens=per_quota,
            )
            compressed_sections.append(compressed)

        # De-duplicate compressed sections as well
        dedup_compressed: list[str] = []
        seen_wordsets2: list[set[str]] = []
        for sec in compressed_sections:
            ws2 = _norm_words(sec)
            is_dup2 = any((len(ws2 & prev) / (len(ws2 | prev) or 1)) >= redundancy_threshold_jaccard for prev in seen_wordsets2)
            if not is_dup2:
                dedup_compressed.append(sec)
                seen_wordsets2.append(ws2)

        paraphrased = " \n".join(dedup_compressed)

        cur = estimate_tokens(paraphrased)
        # If still over budget, compress globally
        retries = 0
        while cur > max_tokens and retries < 2:
            paraphrased = paraphrase_prompt(
                paraphrased,
                instructions=(
                    "Further compress while keeping meaning and preserving key facts/IDs; keep bullets concise."
                ),
                max_tokens=max_tokens,
            )
            retries += 1
            cur = estimate_tokens(paraphrased)

        # If we undershot too much, iteratively add next-most-relevant sections not yet included
        if cur < int(0.8 * max_tokens):
            remaining = [s for s in sorted_sections if s not in kept]
            i = 0
            while cur < int(0.9 * max_tokens) and i < len(remaining):
                sec = remaining[i]
                i += 1
                # Paraphrase this section to about per_quota/2 to avoid overshoot spikes
                add_quota = max(80, per_quota // 2)
                added = paraphrase_prompt(
                    sec,
                    instructions=(
                        "Condense this section preserving concrete facts and instructions; "
                        f"aim near {add_quota} tokens (±20%). Do not repeat already covered points."
                    ),
                    max_tokens=add_quota,
                )
                # Skip if added is near-duplicate of existing content
                ws_added = _norm_words(added)
                is_dup_added = any((len(ws_added & prev) / (len(ws_added | prev) or 1)) >= redundancy_threshold_jaccard for prev in seen_wordsets2)
                if is_dup_added:
                    continue
                tentative = paraphrased + " \n" + added
                new_tokens = estimate_tokens(tentative)
                if new_tokens <= max_tokens:
                    paraphrased = tentative
                    cur = new_tokens
                    seen_wordsets2.append(ws_added)
                else:
                    # If this addition overshoots, try compressing the addition further
                    added2 = paraphrase_prompt(
                        added,
                        instructions="Compress slightly while keeping key facts; keep bullets concise.",
                        max_tokens=max_tokens - estimate_tokens(paraphrased)
                    )
                    tentative2 = paraphrased + " \n" + added2
                    ws_added2 = _norm_words(added2)
                    if estimate_tokens(tentative2) <= max_tokens and not any((len(ws_added2 & prev) / (len(ws_added2 | prev) or 1)) >= redundancy_threshold_jaccard for prev in seen_wordsets2):
                        paraphrased = tentative2
                        cur = estimate_tokens(paraphrased)
                        seen_wordsets2.append(ws_added2)
                    else:
                        break
        pruned_prompt = paraphrased
    
    # Final quality check if enabled
    if quality_check:
        consistency = self_consistency_check(prompt, pruned_prompt, query, get_embeddings)
        hallucination = detect_hallucination_risk(pruned_prompt, sections, get_embeddings)
        
        # If quality is very poor, fall back to simpler optimization
        if (consistency["semantic_preservation"] < 0.3 or 
            consistency["content_coverage"] < 0.3 or
            hallucination["hallucination_risk"] > 0.7):
            
            # Simple fallback: keep top sections without heavy paraphrasing
            top_sections = sorted_sections[:min(top_k, len(sorted_sections))]
            fallback_prompt = "\n\n".join(top_sections)
            
            if estimate_tokens(fallback_prompt) <= max_tokens:
                return fallback_prompt
            else:
                # Last resort: truncate
                words = fallback_prompt.split()
                target_words = int(len(words) * (max_tokens / estimate_tokens(fallback_prompt)))
                return " ".join(words[:target_words])
    
    # Apply structure enforcement if requested
    if enforce_structure:
        pruned_prompt = enforce_prompt_structure(
            pruned_prompt,
            user_instructions=query,
            add_hallucination_guard=True
        )

    return pruned_prompt


def optimize_prompt_auto(
    prompt: str,
    query: str,
    *,
    target_ratio: float | None = 0.6,
    desired_max_tokens: int | None = None,
    min_tokens: int = 400,
    max_tokens_cap: int | None = None,
    top_k: int = 8,
    min_keep_ratio: float = 0.7,
    paraphrase: bool = True,
    quality_check: bool = False,
    fallback_on_low_relevance: bool = True,
    pre_summarize_chunks: bool = False,
    enforce_structure: bool = False,
) -> str:
    """
    Optimize a prompt using a ratio-based target budget derived from the original size.

    Args:
        prompt: Original prompt text.
        query: Reference text for relevance.
        target_ratio: Desired compressed size as a fraction of original tokens (e.g., 0.5-0.6).
        min_tokens: Lower bound on the token budget to avoid over-compression.
        max_tokens_cap: Optional hard upper cap on the token budget.
        top_k: See optimize_prompt.
        min_keep_ratio: See optimize_prompt.

    Returns:
        Optimized prompt string.
    """
    # Estimate original size
    orig_tokens = estimate_tokens(prompt)
    # Compute target budget from desired_max_tokens (if given) else ratio
    if desired_max_tokens is not None and desired_max_tokens > 0:
        budget = int(desired_max_tokens)
    else:
        # Fallback to ratio logic
        if target_ratio is None:
            # Auto policy: adapt ratio to original size bands
            # <1k: keep ~80%; 1k-3k: keep ~60%; 3k-8k: keep ~50%; >8k: keep ~40%
            if orig_tokens < 1000:
                ratio = 0.8
            elif orig_tokens < 3000:
                ratio = 0.6
            elif orig_tokens < 8000:
                ratio = 0.5
            else:
                ratio = 0.4
        else:
            ratio = float(target_ratio)
        ratio = max(0.05, min(1.0, ratio))
        budget = int(orig_tokens * ratio)
    # Enforce floors/caps
    budget = max(min_tokens, budget)
    if max_tokens_cap is not None:
        budget = min(budget, int(max_tokens_cap))

    return optimize_prompt(
        prompt,
        query,
        max_tokens=budget,
        top_k=top_k,
        min_keep_ratio=min_keep_ratio,
        paraphrase=paraphrase,
        quality_check=quality_check,
        fallback_on_low_relevance=fallback_on_low_relevance,
        pre_summarize_chunks=pre_summarize_chunks,
        enforce_structure=enforce_structure,
    )