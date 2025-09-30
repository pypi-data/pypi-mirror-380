import typer # type: ignore
from rich import print # type: ignore
from . import optimize_prompt, optimize_prompt_auto

def main(
    prompt: str = typer.Argument(..., help="Prompt to optimize."),
    query: str = typer.Argument(..., help="Reference query for relevance scoring."),
    max_tokens: int = typer.Option(2048, help="Token budget for the optimized prompt."),
    mode: str = typer.Option("hybrid", help="Optimization mode: structured | narrative | hybrid"),
    top_k: int = typer.Option(-1, help="Override number of top relevant sections to preserve before paraphrasing."),
    min_keep_ratio: float = typer.Option(-1.0, help="Override minimum fraction of budget to fill with preserved content before paraphrasing."),
    auto_budget: bool = typer.Option(False, help="If set, compute budget adaptively from size using ratio and/or desired max tokens."),
    target_ratio: float = typer.Option(0.6, help="Target ratio of original tokens for auto budget (e.g., 0.5 means 50%)."),
    desired_max_tokens: int = typer.Option(-1, help="If >0, directly target this max token size (overrides ratio)."),
    min_tokens: int = typer.Option(400, help="Minimum token budget when using auto budget."),
    max_tokens_cap: int = typer.Option(-1, help="Optional hard cap on token budget when using auto budget."),
    quality_check: bool = typer.Option(False, help="Enable quality checks and self-consistency validation."),
    fallback_on_low_relevance: bool = typer.Option(True, help="Use fallback optimization when relevance is very low."),
):
    """Optimize a prompt to fit within a token budget with adjustable retention behavior."""

    # Map mode to sensible defaults; allow explicit overrides via flags
    mode = (mode or "hybrid").lower()
    if mode not in {"structured", "narrative", "hybrid"}:
        raise typer.BadParameter("mode must be one of: structured, narrative, hybrid")

    if mode == "structured":
        default_top_k = 5
        default_min_keep_ratio = 0.7
    elif mode == "narrative":
        default_top_k = 8
        default_min_keep_ratio = 0.45
    else:  # hybrid
        default_top_k = 8
        default_min_keep_ratio = 0.7

    eff_top_k = default_top_k if top_k is None or top_k < 0 else top_k
    eff_min_keep_ratio = default_min_keep_ratio if min_keep_ratio is None or min_keep_ratio < 0 else min_keep_ratio

    if auto_budget:
        cap = None if max_tokens_cap is None or max_tokens_cap < 0 else max_tokens_cap
        desired = None if desired_max_tokens is None or desired_max_tokens < 0 else desired_max_tokens
        optimized = optimize_prompt_auto(
            prompt,
            query,
            target_ratio=target_ratio,
            desired_max_tokens=desired,
            min_tokens=min_tokens,
            max_tokens_cap=cap,
            top_k=eff_top_k,
            min_keep_ratio=eff_min_keep_ratio,
            quality_check=quality_check,
            fallback_on_low_relevance=fallback_on_low_relevance,
        )
    else:
        optimized = optimize_prompt(
            prompt,
            query,
            max_tokens=max_tokens,
            top_k=eff_top_k,
            min_keep_ratio=eff_min_keep_ratio,
            quality_check=quality_check,
            fallback_on_low_relevance=fallback_on_low_relevance,
        )
    print("[bold green]Optimized Prompt:[/bold green]")
    print(optimized)

if __name__ == "__main__":
    typer.run(main)