import time
from typing import Optional

try:
    import cohere # type: ignore
except ImportError:
    cohere = None

from .utils import get_cohere_api_key
from .config import COHERE_LLM_MODEL
from .token_budget import estimate_tokens


def paraphrase_prompt(prompt: str, instructions: Optional[str] = None, max_tokens: int = 2048) -> str:
    if cohere is None:
        raise ImportError("cohere package is required for paraphrasing.")

    api_key = get_cohere_api_key()
    co = cohere.Client(api_key)

    def cohere_generate(prompt_text: str) -> str:
        """Call Cohere Chat API and robustly extract the response text."""
        # Using Chat API since Generate API was deprecated (Sept 2025)
        chat_resp = co.chat(
            model=COHERE_LLM_MODEL,
            message=prompt_text,
            temperature=0.2,
            max_tokens=max_tokens,
        )

        # Cohere SDKs can expose either `.text` or `.message.content` depending on version
        if hasattr(chat_resp, "text") and isinstance(chat_resp.text, str) and chat_resp.text.strip():
            return chat_resp.text.strip()

        # Fallback: try to read message content blocks
        try:
            msg = getattr(chat_resp, "message", None)
            if msg and hasattr(msg, "content") and isinstance(msg.content, list):
                parts = []
                for c in msg.content:
                    # text block
                    if isinstance(c, dict) and c.get("type") == "text" and isinstance(c.get("text"), str):
                        parts.append(c["text"]) 
                    else:
                        # Some SDKs expose objects with `.text`
                        t = getattr(c, "text", None)
                        if isinstance(t, str):
                            parts.append(t)
                if parts:
                    return "".join(parts).strip()
        except Exception:
            pass

        # As a last resort, try str() and strip
        return str(chat_resp).strip()

    # HyDE phase — create semantically complete version
    hyde_prompt = (
        "Rewrite the following prompt into a clear, complete, and unambiguous version, "
        "adding any implied but important details so that it fully represents the intended meaning:\n\n"
        f"{prompt}"
    )
    expanded_prompt = cohere_generate(hyde_prompt)

    # Compression phase
    base_system_prompt = (
        "Rewrite the following prompt to fit within the token budget, preserving all key instructions and meaning. "
        "Be as concise as possible."
    )
    if instructions:
        base_system_prompt += f"\nAdditional instructions: {instructions}"

    retries = 0
    max_retries = 5
    backoff_base = 1
    current_prompt = expanded_prompt

    best_attempt = expanded_prompt
    best_attempt_tokens = estimate_tokens(expanded_prompt)

    while retries <= max_retries:
        try:
            text = cohere_generate(f"{base_system_prompt}\n\nPROMPT:\n{current_prompt}")
            token_count = estimate_tokens(text)

            if token_count < best_attempt_tokens:
                best_attempt = text
                best_attempt_tokens = token_count

            if token_count <= max_tokens:
                return text

            retries += 1
            wait_time = backoff_base * (2 ** (retries - 1))
            print(f"[WARN] Output exceeded {max_tokens} tokens. Retrying in {wait_time}s...")
            time.sleep(wait_time)

            current_prompt = text
            base_system_prompt += f"\nEnsure output under {max_tokens} tokens. Further compress."

        except Exception as e:
            retries += 1
            wait_time = backoff_base * (2 ** (retries - 1))
            print(f"[ERROR] Cohere API error: {e}. Retrying in {wait_time}s...")
            time.sleep(wait_time)

    print("[INFO] Returning best attempt despite exceeding token limit.")
    return best_attempt
