# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["FileCreateResponse"]


class FileCreateResponse(BaseModel):
    id: str
    """Unique identifier for the file."""

    content_type: str
    """MIME type of the file as detected/stored."""

    file_name: str
    """Original uploaded filename."""
