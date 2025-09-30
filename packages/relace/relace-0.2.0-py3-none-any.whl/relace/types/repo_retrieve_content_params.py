# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["RepoRetrieveContentParams"]


class RepoRetrieveContentParams(TypedDict, total=False):
    query: Required[str]

    include_content: bool

    rerank: bool

    score_threshold: float

    token_limit: int
