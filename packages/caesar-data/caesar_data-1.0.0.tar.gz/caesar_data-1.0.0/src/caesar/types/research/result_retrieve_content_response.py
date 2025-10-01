# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from ..._models import BaseModel

__all__ = ["ResultRetrieveContentResponse"]


class ResultRetrieveContentResponse(BaseModel):
    content: str
    """
    Raw extracted content for this result (may include HTML, markdown, or plain
    text).
    """
