# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["RepoRetrieveContentResponse", "Result"]


class Result(BaseModel):
    filename: str

    score: float

    content: Optional[str] = None


class RepoRetrieveContentResponse(BaseModel):
    pending_embeddings: int

    results: List[Result]
