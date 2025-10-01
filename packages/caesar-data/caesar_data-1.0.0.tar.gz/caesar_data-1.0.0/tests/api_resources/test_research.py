# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from caesar import Caesar, AsyncCaesar
from tests.utils import assert_matches_type
from caesar.types import (
    ResearchListResponse,
    ResearchCreateResponse,
    ResearchRetrieveResponse,
)
from caesar.pagination import SyncPagination, AsyncPagination

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestResearch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: Caesar) -> None:
        research = client.research.create(
            query="Is lithium supply a bottleneck for EV adoption?",
        )
        assert_matches_type(ResearchCreateResponse, research, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Caesar) -> None:
        research = client.research.create(
            query="Is lithium supply a bottleneck for EV adoption?",
            compute_units=1,
            files=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            system_prompt="system_prompt",
        )
        assert_matches_type(ResearchCreateResponse, research, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Caesar) -> None:
        response = client.research.with_raw_response.create(
            query="Is lithium supply a bottleneck for EV adoption?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        research = response.parse()
        assert_matches_type(ResearchCreateResponse, research, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Caesar) -> None:
        with client.research.with_streaming_response.create(
            query="Is lithium supply a bottleneck for EV adoption?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            research = response.parse()
            assert_matches_type(ResearchCreateResponse, research, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Caesar) -> None:
        research = client.research.retrieve(
            "id",
        )
        assert_matches_type(ResearchRetrieveResponse, research, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Caesar) -> None:
        response = client.research.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        research = response.parse()
        assert_matches_type(ResearchRetrieveResponse, research, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Caesar) -> None:
        with client.research.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            research = response.parse()
            assert_matches_type(ResearchRetrieveResponse, research, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Caesar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.research.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: Caesar) -> None:
        research = client.research.list()
        assert_matches_type(SyncPagination[ResearchListResponse], research, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: Caesar) -> None:
        research = client.research.list(
            limit=1,
            page=1,
        )
        assert_matches_type(SyncPagination[ResearchListResponse], research, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Caesar) -> None:
        response = client.research.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        research = response.parse()
        assert_matches_type(SyncPagination[ResearchListResponse], research, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Caesar) -> None:
        with client.research.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            research = response.parse()
            assert_matches_type(SyncPagination[ResearchListResponse], research, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncResearch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncCaesar) -> None:
        research = await async_client.research.create(
            query="Is lithium supply a bottleneck for EV adoption?",
        )
        assert_matches_type(ResearchCreateResponse, research, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncCaesar) -> None:
        research = await async_client.research.create(
            query="Is lithium supply a bottleneck for EV adoption?",
            compute_units=1,
            files=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            system_prompt="system_prompt",
        )
        assert_matches_type(ResearchCreateResponse, research, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncCaesar) -> None:
        response = await async_client.research.with_raw_response.create(
            query="Is lithium supply a bottleneck for EV adoption?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        research = await response.parse()
        assert_matches_type(ResearchCreateResponse, research, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncCaesar) -> None:
        async with async_client.research.with_streaming_response.create(
            query="Is lithium supply a bottleneck for EV adoption?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            research = await response.parse()
            assert_matches_type(ResearchCreateResponse, research, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncCaesar) -> None:
        research = await async_client.research.retrieve(
            "id",
        )
        assert_matches_type(ResearchRetrieveResponse, research, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncCaesar) -> None:
        response = await async_client.research.with_raw_response.retrieve(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        research = await response.parse()
        assert_matches_type(ResearchRetrieveResponse, research, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncCaesar) -> None:
        async with async_client.research.with_streaming_response.retrieve(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            research = await response.parse()
            assert_matches_type(ResearchRetrieveResponse, research, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncCaesar) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.research.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncCaesar) -> None:
        research = await async_client.research.list()
        assert_matches_type(AsyncPagination[ResearchListResponse], research, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncCaesar) -> None:
        research = await async_client.research.list(
            limit=1,
            page=1,
        )
        assert_matches_type(AsyncPagination[ResearchListResponse], research, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncCaesar) -> None:
        response = await async_client.research.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        research = await response.parse()
        assert_matches_type(AsyncPagination[ResearchListResponse], research, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncCaesar) -> None:
        async with async_client.research.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            research = await response.parse()
            assert_matches_type(AsyncPagination[ResearchListResponse], research, path=["response"])

        assert cast(Any, response.is_closed) is True
