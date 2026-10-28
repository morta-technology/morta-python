# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from morta import Morta, AsyncMorta
from tests.utils import assert_matches_type
from morta.types.hub import SidebarContainersResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSidebar:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_containers(self, client: Morta) -> None:
        sidebar = client.hub.sidebar.containers(
            hub_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            containers=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(SidebarContainersResponse, sidebar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_containers(self, client: Morta) -> None:
        response = client.hub.sidebar.with_raw_response.containers(
            hub_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            containers=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sidebar = response.parse()
        assert_matches_type(SidebarContainersResponse, sidebar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_containers(self, client: Morta) -> None:
        with client.hub.sidebar.with_streaming_response.containers(
            hub_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            containers=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sidebar = response.parse()
            assert_matches_type(SidebarContainersResponse, sidebar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_containers(self, client: Morta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hub_id` but received ''"):
            client.hub.sidebar.with_raw_response.containers(
                hub_id="",
                containers=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )


class TestAsyncSidebar:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_containers(self, async_client: AsyncMorta) -> None:
        sidebar = await async_client.hub.sidebar.containers(
            hub_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            containers=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(SidebarContainersResponse, sidebar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_containers(self, async_client: AsyncMorta) -> None:
        response = await async_client.hub.sidebar.with_raw_response.containers(
            hub_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            containers=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        sidebar = await response.parse()
        assert_matches_type(SidebarContainersResponse, sidebar, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_containers(self, async_client: AsyncMorta) -> None:
        async with async_client.hub.sidebar.with_streaming_response.containers(
            hub_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            containers=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            sidebar = await response.parse()
            assert_matches_type(SidebarContainersResponse, sidebar, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_containers(self, async_client: AsyncMorta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `hub_id` but received ''"):
            await async_client.hub.sidebar.with_raw_response.containers(
                hub_id="",
                containers=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            )
