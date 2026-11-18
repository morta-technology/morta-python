# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from morta import Morta, AsyncMorta
from tests.utils import assert_matches_type
from morta.types.table.views.columns import (
    SelectOptionRetrieveCheckResponse,
    SelectOptionRetrieveSelectOptionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSelectOptions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_check(self, client: Morta) -> None:
        select_option = client.table.views.columns.select_options.retrieve_check(
            column_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            values="values",
        )
        assert_matches_type(SelectOptionRetrieveCheckResponse, select_option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_check(self, client: Morta) -> None:
        response = client.table.views.columns.select_options.with_raw_response.retrieve_check(
            column_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            values="values",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        select_option = response.parse()
        assert_matches_type(SelectOptionRetrieveCheckResponse, select_option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_check(self, client: Morta) -> None:
        with client.table.views.columns.select_options.with_streaming_response.retrieve_check(
            column_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            values="values",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            select_option = response.parse()
            assert_matches_type(SelectOptionRetrieveCheckResponse, select_option, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_check(self, client: Morta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.table.views.columns.select_options.with_raw_response.retrieve_check(
                column_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                view_id="",
                values="values",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `column_id` but received ''"):
            client.table.views.columns.select_options.with_raw_response.retrieve_check(
                column_id="",
                view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                values="values",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_select_options(self, client: Morta) -> None:
        select_option = client.table.views.columns.select_options.retrieve_select_options(
            column_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SelectOptionRetrieveSelectOptionsResponse, select_option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_select_options_with_all_params(self, client: Morta) -> None:
        select_option = client.table.views.columns.select_options.retrieve_select_options(
            column_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after="after",
            dependency_values="dependencyValues",
            search="search",
            size=1,
        )
        assert_matches_type(SelectOptionRetrieveSelectOptionsResponse, select_option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_select_options(self, client: Morta) -> None:
        response = client.table.views.columns.select_options.with_raw_response.retrieve_select_options(
            column_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        select_option = response.parse()
        assert_matches_type(SelectOptionRetrieveSelectOptionsResponse, select_option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_select_options(self, client: Morta) -> None:
        with client.table.views.columns.select_options.with_streaming_response.retrieve_select_options(
            column_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            select_option = response.parse()
            assert_matches_type(SelectOptionRetrieveSelectOptionsResponse, select_option, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_select_options(self, client: Morta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.table.views.columns.select_options.with_raw_response.retrieve_select_options(
                column_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                view_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `column_id` but received ''"):
            client.table.views.columns.select_options.with_raw_response.retrieve_select_options(
                column_id="",
                view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncSelectOptions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_check(self, async_client: AsyncMorta) -> None:
        select_option = await async_client.table.views.columns.select_options.retrieve_check(
            column_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            values="values",
        )
        assert_matches_type(SelectOptionRetrieveCheckResponse, select_option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_check(self, async_client: AsyncMorta) -> None:
        response = await async_client.table.views.columns.select_options.with_raw_response.retrieve_check(
            column_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            values="values",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        select_option = await response.parse()
        assert_matches_type(SelectOptionRetrieveCheckResponse, select_option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_check(self, async_client: AsyncMorta) -> None:
        async with async_client.table.views.columns.select_options.with_streaming_response.retrieve_check(
            column_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            values="values",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            select_option = await response.parse()
            assert_matches_type(SelectOptionRetrieveCheckResponse, select_option, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_check(self, async_client: AsyncMorta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.table.views.columns.select_options.with_raw_response.retrieve_check(
                column_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                view_id="",
                values="values",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `column_id` but received ''"):
            await async_client.table.views.columns.select_options.with_raw_response.retrieve_check(
                column_id="",
                view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                values="values",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_select_options(self, async_client: AsyncMorta) -> None:
        select_option = await async_client.table.views.columns.select_options.retrieve_select_options(
            column_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SelectOptionRetrieveSelectOptionsResponse, select_option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_select_options_with_all_params(self, async_client: AsyncMorta) -> None:
        select_option = await async_client.table.views.columns.select_options.retrieve_select_options(
            column_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            after="after",
            dependency_values="dependencyValues",
            search="search",
            size=1,
        )
        assert_matches_type(SelectOptionRetrieveSelectOptionsResponse, select_option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_select_options(self, async_client: AsyncMorta) -> None:
        response = await async_client.table.views.columns.select_options.with_raw_response.retrieve_select_options(
            column_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        select_option = await response.parse()
        assert_matches_type(SelectOptionRetrieveSelectOptionsResponse, select_option, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_select_options(self, async_client: AsyncMorta) -> None:
        async with async_client.table.views.columns.select_options.with_streaming_response.retrieve_select_options(
            column_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            select_option = await response.parse()
            assert_matches_type(SelectOptionRetrieveSelectOptionsResponse, select_option, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_select_options(self, async_client: AsyncMorta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.table.views.columns.select_options.with_raw_response.retrieve_select_options(
                column_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                view_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `column_id` but received ''"):
            await async_client.table.views.columns.select_options.with_raw_response.retrieve_select_options(
                column_id="",
                view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
