"""Official lightweight Python client for the CheapAIModel API.

CheapAIModel is OpenAI-compatible, so this package is a thin layer over the
official ``openai`` SDK that fills in the right base URL and API key.
"""
from __future__ import annotations

import os
from typing import Any

from openai import AsyncOpenAI, OpenAI

__all__ = ["CheapAIModel", "AsyncCheapAIModel", "DEFAULT_BASE_URL", "__version__"]
__version__ = "0.1.0"

DEFAULT_BASE_URL = "https://api.cheapaimodel.com/v1"


def _resolve(api_key: str | None, base_url: str | None) -> tuple[str, str]:
    key = api_key or os.getenv("CHEAPAIMODEL_API_KEY")
    if not key:
        raise ValueError(
            "No API key found. Pass api_key=... or set the CHEAPAIMODEL_API_KEY environment variable."
        )
    url = base_url or os.getenv("CHEAPAIMODEL_BASE_URL") or DEFAULT_BASE_URL
    return key, url


class CheapAIModel(OpenAI):
    """Synchronous client. Use it exactly like ``openai.OpenAI``.

    >>> client = CheapAIModel()  # reads CHEAPAIMODEL_API_KEY
    >>> client.chat.completions.create(model="gpt-4o-mini", messages=[...])
    """

    def __init__(self, *, api_key: str | None = None, base_url: str | None = None, **kwargs: Any) -> None:
        key, url = _resolve(api_key, base_url)
        super().__init__(api_key=key, base_url=url, **kwargs)

    def chat_text(self, prompt: str, *, model: str = "gpt-4o-mini", **kwargs: Any) -> str:
        """Shortcut: send one user message and return the reply text."""
        res = self.chat.completions.create(
            model=model, messages=[{"role": "user", "content": prompt}], **kwargs
        )
        return res.choices[0].message.content or ""


class AsyncCheapAIModel(AsyncOpenAI):
    """Async client. Use it exactly like ``openai.AsyncOpenAI``."""

    def __init__(self, *, api_key: str | None = None, base_url: str | None = None, **kwargs: Any) -> None:
        key, url = _resolve(api_key, base_url)
        super().__init__(api_key=key, base_url=url, **kwargs)

    async def chat_text(self, prompt: str, *, model: str = "gpt-4o-mini", **kwargs: Any) -> str:
        """Shortcut: send one user message and return the reply text."""
        res = await self.chat.completions.create(
            model=model, messages=[{"role": "user", "content": prompt}], **kwargs
        )
        return res.choices[0].message.content or ""
