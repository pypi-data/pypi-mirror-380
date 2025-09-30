# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["RepoCloneResponse", "File"]


class File(BaseModel):
    content: str

    filename: str


class RepoCloneResponse(BaseModel):
    files: Optional[List[File]] = None
