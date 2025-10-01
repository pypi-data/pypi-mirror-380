# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ResearchCreateResponse"]


class ResearchCreateResponse(BaseModel):
    id: str
    """Research job identifier."""

    status: Literal["queued", "searching", "summarizing", "analyzing", "completed", "failed", "researching"]
    """Current status of the research job."""
