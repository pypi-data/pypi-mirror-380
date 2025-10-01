# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ResearchListParams"]


class ResearchListParams(TypedDict, total=False):
    limit: int
    """Page size (items per page)."""

    page: int
    """1-based page index."""
