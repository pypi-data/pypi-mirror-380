# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ResearchRetrieveResponse", "Result"]


class Result(BaseModel):
    id: str
    """Result object identifier."""

    score: float
    """Relevance score (0–1)."""

    title: str
    """Result title."""

    url: str
    """Canonical URL of the result."""

    citation_index: Optional[int] = None
    """Index used for inline citations (if present)."""


class ResearchRetrieveResponse(BaseModel):
    id: str
    """Research job identifier."""

    created_at: datetime
    """ISO 8601 timestamp when the job was created."""

    query: str
    """Original query."""

    results: List[Result]
    """Ranked retrieval results and citations."""

    status: Literal["queued", "searching", "summarizing", "analyzing", "completed", "failed", "researching"]
    """Current status of the research job."""

    content: Optional[str] = None
    """Final content/synthesis (null until available)."""

    transformed_content: Optional[str] = None
    """Post-processed content (e.g., formatted/converted)."""
