from __future__ import annotations

from typing import Any

try:
    from langchain_core.documents import Document as LCDocument
except Exception:  # pragma: no cover - optional dependency
    LCDocument = Any  # type: ignore

from ..config import Settings
from ..rerank import Reranker
from ..types import Document as NC_Document


class NeuralCacheLangChainReranker:
    def __init__(self, settings: Settings | None = None) -> None:
        self.settings = settings or Settings()
        self.reranker = Reranker(self.settings)

    def __call__(self, query: str, documents: list[LCDocument]) -> list[LCDocument]:
        # Convert to NeuralCache docs
        nc_docs = [
            NC_Document(
                id=str(index),
                text=doc.page_content,
                metadata=doc.metadata,
            )
            for index, doc in enumerate(documents)
        ]
        if len(nc_docs) > self.settings.max_documents:
            raise ValueError(
                f"NeuralCache received {len(nc_docs)} documents, exceeding max_documents={self.settings.max_documents}"
            )
        for doc in nc_docs:
            if len(doc.text) > self.settings.max_text_length:
                raise ValueError(
                    f"Document {doc.id} text length exceeds max_text_length={self.settings.max_text_length}"
                )
        # Hash-based query embedding for demo
        q = self.reranker.encode_query(query)

        scored = self.reranker.score(q, nc_docs)
        # Map back to LC docs preserving metadata
        return [documents[int(sd.id)] for sd in scored]
