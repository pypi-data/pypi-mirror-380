# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["ResearchCreateParams"]


class ResearchCreateParams(TypedDict, total=False):
    query: Required[str]
    """Primary research question or instruction."""

    compute_units: int
    """Optional compute budget for the job. Defaults to 1."""

    files: SequenceNotStr[str]
    """IDs of previously uploaded files to include."""

    system_prompt: str
    """Optional system prompt to steer the assistant."""
