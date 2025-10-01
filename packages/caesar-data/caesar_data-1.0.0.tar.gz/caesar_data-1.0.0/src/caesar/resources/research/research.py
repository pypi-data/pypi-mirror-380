# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .files import (
    FilesResource,
    AsyncFilesResource,
    FilesResourceWithRawResponse,
    AsyncFilesResourceWithRawResponse,
    FilesResourceWithStreamingResponse,
    AsyncFilesResourceWithStreamingResponse,
)
from ...types import research_list_params, research_create_params
from .results import (
    ResultsResource,
    AsyncResultsResource,
    ResultsResourceWithRawResponse,
    AsyncResultsResourceWithRawResponse,
    ResultsResourceWithStreamingResponse,
    AsyncResultsResourceWithStreamingResponse,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...pagination import SyncPagination, AsyncPagination
from ..._base_client import AsyncPaginator, make_request_options
from ...types.research_list_response import ResearchListResponse
from ...types.research_create_response import ResearchCreateResponse
from ...types.research_retrieve_response import ResearchRetrieveResponse

__all__ = ["ResearchResource", "AsyncResearchResource"]


class ResearchResource(SyncAPIResource):
    @cached_property
    def files(self) -> FilesResource:
        return FilesResource(self._client)

    @cached_property
    def results(self) -> ResultsResource:
        return ResultsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ResearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/caesar-data/python-sdk#accessing-raw-response-data-eg-headers
        """
        return ResearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ResearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/caesar-data/python-sdk#with_streaming_response
        """
        return ResearchResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        query: str,
        compute_units: int | Omit = omit,
        files: SequenceNotStr[str] | Omit = omit,
        system_prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResearchCreateResponse:
        """
        Start a new research job using a query and optional file IDs.

        Args:
          query: Primary research question or instruction.

          compute_units: Optional compute budget for the job. Defaults to 1.

          files: IDs of previously uploaded files to include.

          system_prompt: Optional system prompt to steer the assistant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/research",
            body=maybe_transform(
                {
                    "query": query,
                    "compute_units": compute_units,
                    "files": files,
                    "system_prompt": system_prompt,
                },
                research_create_params.ResearchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResearchCreateResponse,
        )

    def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResearchRetrieveResponse:
        """
        Retrieve a single research object by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/research/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResearchRetrieveResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncPagination[ResearchListResponse]:
        """
        Returns a paginated list of research objects.

        Args:
          limit: Page size (items per page).

          page: 1-based page index.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/research",
            page=SyncPagination[ResearchListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    research_list_params.ResearchListParams,
                ),
            ),
            model=ResearchListResponse,
        )


class AsyncResearchResource(AsyncAPIResource):
    @cached_property
    def files(self) -> AsyncFilesResource:
        return AsyncFilesResource(self._client)

    @cached_property
    def results(self) -> AsyncResultsResource:
        return AsyncResultsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncResearchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/caesar-data/python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncResearchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncResearchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/caesar-data/python-sdk#with_streaming_response
        """
        return AsyncResearchResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        query: str,
        compute_units: int | Omit = omit,
        files: SequenceNotStr[str] | Omit = omit,
        system_prompt: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResearchCreateResponse:
        """
        Start a new research job using a query and optional file IDs.

        Args:
          query: Primary research question or instruction.

          compute_units: Optional compute budget for the job. Defaults to 1.

          files: IDs of previously uploaded files to include.

          system_prompt: Optional system prompt to steer the assistant.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/research",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "compute_units": compute_units,
                    "files": files,
                    "system_prompt": system_prompt,
                },
                research_create_params.ResearchCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResearchCreateResponse,
        )

    async def retrieve(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ResearchRetrieveResponse:
        """
        Retrieve a single research object by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/research/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ResearchRetrieveResponse,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[ResearchListResponse, AsyncPagination[ResearchListResponse]]:
        """
        Returns a paginated list of research objects.

        Args:
          limit: Page size (items per page).

          page: 1-based page index.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/research",
            page=AsyncPagination[ResearchListResponse],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "page": page,
                    },
                    research_list_params.ResearchListParams,
                ),
            ),
            model=ResearchListResponse,
        )


class ResearchResourceWithRawResponse:
    def __init__(self, research: ResearchResource) -> None:
        self._research = research

        self.create = to_raw_response_wrapper(
            research.create,
        )
        self.retrieve = to_raw_response_wrapper(
            research.retrieve,
        )
        self.list = to_raw_response_wrapper(
            research.list,
        )

    @cached_property
    def files(self) -> FilesResourceWithRawResponse:
        return FilesResourceWithRawResponse(self._research.files)

    @cached_property
    def results(self) -> ResultsResourceWithRawResponse:
        return ResultsResourceWithRawResponse(self._research.results)


class AsyncResearchResourceWithRawResponse:
    def __init__(self, research: AsyncResearchResource) -> None:
        self._research = research

        self.create = async_to_raw_response_wrapper(
            research.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            research.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            research.list,
        )

    @cached_property
    def files(self) -> AsyncFilesResourceWithRawResponse:
        return AsyncFilesResourceWithRawResponse(self._research.files)

    @cached_property
    def results(self) -> AsyncResultsResourceWithRawResponse:
        return AsyncResultsResourceWithRawResponse(self._research.results)


class ResearchResourceWithStreamingResponse:
    def __init__(self, research: ResearchResource) -> None:
        self._research = research

        self.create = to_streamed_response_wrapper(
            research.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            research.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            research.list,
        )

    @cached_property
    def files(self) -> FilesResourceWithStreamingResponse:
        return FilesResourceWithStreamingResponse(self._research.files)

    @cached_property
    def results(self) -> ResultsResourceWithStreamingResponse:
        return ResultsResourceWithStreamingResponse(self._research.results)


class AsyncResearchResourceWithStreamingResponse:
    def __init__(self, research: AsyncResearchResource) -> None:
        self._research = research

        self.create = async_to_streamed_response_wrapper(
            research.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            research.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            research.list,
        )

    @cached_property
    def files(self) -> AsyncFilesResourceWithStreamingResponse:
        return AsyncFilesResourceWithStreamingResponse(self._research.files)

    @cached_property
    def results(self) -> AsyncResultsResourceWithStreamingResponse:
        return AsyncResultsResourceWithStreamingResponse(self._research.results)
