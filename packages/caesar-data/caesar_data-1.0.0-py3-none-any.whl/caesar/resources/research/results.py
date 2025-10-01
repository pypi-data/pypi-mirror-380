# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.research.result_retrieve_content_response import ResultRetrieveContentResponse

__all__ = ["ResultsResource", "AsyncResultsResource"]


class ResultsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ResultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/caesar-data/python-sdk#accessing-raw-response-data-eg-headers
        """
        return ResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/caesar-data/python-sdk#with_streaming_response
        """
        return ResultsResourceWithStreamingResponse(self)

    def retrieve_content(
        self,
        result_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResultRetrieveContentResponse:
        """
        Returns the raw content for a specific result within a research object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not result_id:
            raise ValueError(f"Expected a non-empty value for `result_id` but received {result_id!r}")
        return self._get(
            f"/research/{id}/results/{result_id}/content",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResultRetrieveContentResponse,
        )


class AsyncResultsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncResultsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/caesar-data/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncResultsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResultsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/caesar-data/python-sdk#with_streaming_response
        """
        return AsyncResultsResourceWithStreamingResponse(self)

    async def retrieve_content(
        self,
        result_id: str,
        *,
        id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResultRetrieveContentResponse:
        """
        Returns the raw content for a specific result within a research object.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        if not result_id:
            raise ValueError(f"Expected a non-empty value for `result_id` but received {result_id!r}")
        return await self._get(
            f"/research/{id}/results/{result_id}/content",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResultRetrieveContentResponse,
        )


class ResultsResourceWithRawResponse:
    def __init__(self, results: ResultsResource) -> None:
        self._results = results

        self.retrieve_content = to_raw_response_wrapper(
            results.retrieve_content,
        )


class AsyncResultsResourceWithRawResponse:
    def __init__(self, results: AsyncResultsResource) -> None:
        self._results = results

        self.retrieve_content = async_to_raw_response_wrapper(
            results.retrieve_content,
        )


class ResultsResourceWithStreamingResponse:
    def __init__(self, results: ResultsResource) -> None:
        self._results = results

        self.retrieve_content = to_streamed_response_wrapper(
            results.retrieve_content,
        )


class AsyncResultsResourceWithStreamingResponse:
    def __init__(self, results: AsyncResultsResource) -> None:
        self._results = results

        self.retrieve_content = async_to_streamed_response_wrapper(
            results.retrieve_content,
        )
