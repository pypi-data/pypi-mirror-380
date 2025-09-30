# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime

from .._models import BaseModel

__all__ = ["RepoMetadata"]


class RepoMetadata(BaseModel):
    created_at: datetime

    repo_id: str

    metadata: Optional[Dict[str, str]] = None

    updated_at: Optional[datetime] = None
