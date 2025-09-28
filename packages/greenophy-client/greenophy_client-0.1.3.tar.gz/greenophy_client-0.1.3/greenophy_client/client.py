"""Client library for the Greenophy substantiveness classification API."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List, Optional, Sequence

import os
import requests


@dataclass(frozen=True)
class SubstantivenessResult:
    """Represents a single sentence classification result."""

    index: int
    sentence: str
    label: int
    label_name: str


class SubstantivenessClient:
    """Thin wrapper around the `/api/substantiveness` endpoint."""

    def __init__(
        self,
        base_url: Optional[str] = None,
        *,
        api_key: Optional[str] = None,
        timeout: float = 10.0,
        session: Optional[requests.Session] = None,
    ) -> None:
        if base_url is None:
            base_url = os.getenv("GREENOPHY_API_BASE_URL")
        if not base_url:
            raise ValueError("base_url is required (set explicitly or via GREENOPHY_API_BASE_URL)")
        self.base_url = base_url.rstrip('/')
        if api_key is None:
            api_key = os.getenv("GREENOPHY_API_KEY")
        self.api_key = api_key
        self.timeout = timeout
        self._session = session or requests.Session()

    # ------------------------------------------------------------------
    def classify_esg_text(self, text: str) -> List[SubstantivenessResult]:
        """Split and classify free-form text on the server."""
        if not isinstance(text, str) or not text.strip():
            raise ValueError("text must be a non-empty string")
        payload = {"text": text}
        return self._classify(payload, endpoint="/api/substantiveness")

    def classify_esg_sentences(self, sentences: Sequence[str]) -> List[SubstantivenessResult]:
        """Classify a pre-tokenised list of sentences."""
        if not isinstance(sentences, Iterable):
            raise ValueError("sentences must be an iterable of strings")
        sentence_list = [s.strip() if isinstance(s, str) else str(s).strip() for s in sentences]
        sentence_list = [s for s in sentence_list if s]
        if not sentence_list:
            raise ValueError("sentences iterable contained no non-empty strings")
        payload = {"sentences": sentence_list}
        return self._classify(payload, endpoint="/api/substantiveness")

    def classify_generic_text(self, text: str) -> List[SubstantivenessResult]:
        if not isinstance(text, str) or not text.strip():
            raise ValueError("text must be a non-empty string")
        payload = {"text": text}
        return self._classify(payload, endpoint="/api/generic_classification")

    def classify_generic_sentences(self, sentences: Sequence[str]) -> List[SubstantivenessResult]:
        if not isinstance(sentences, Iterable):
            raise ValueError("sentences must be an iterable of strings")
        sentence_list = [s.strip() if isinstance(s, str) else str(s).strip() for s in sentences]
        sentence_list = [s for s in sentence_list if s]
        if not sentence_list:
            raise ValueError("sentences iterable contained no non-empty strings")
        payload = {"sentences": sentence_list}
        return self._classify(payload, endpoint="/api/generic_classification")

    # ------------------------------------------------------------------
    def _classify(self, payload: dict, *, endpoint: str) -> List[SubstantivenessResult]:
        url = f"{self.base_url}{endpoint}"
        headers = {"Content-Type": "application/json"}
        if self.api_key:
            headers["X-API-Key"] = self.api_key

        response = self._session.post(url, json=payload, headers=headers, timeout=self.timeout)
        try:
            response.raise_for_status()
        except requests.HTTPError as exc:
            message = self._extract_error(response) or str(exc)
            raise requests.HTTPError(message, response=response) from exc

        data = response.json()
        results = data.get("results", [])
        return [
            SubstantivenessResult(
                index=item.get("index", i),
                sentence=item.get("sentence", ""),
                label=item.get("label", 0),
                label_name=item.get("label_name", "") or "",
            )
            for i, item in enumerate(results)
        ]

    @staticmethod
    def _extract_error(response: requests.Response) -> Optional[str]:
        try:
            payload = response.json()
        except ValueError:
            return response.text
        return payload.get("error") or payload.get("message")

    # ------------------------------------------------------------------
    def close(self) -> None:
        """Close the underlying session."""
        self._session.close()

    def __enter__(self) -> "SubstantivenessClient":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.close()
