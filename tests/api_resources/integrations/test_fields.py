# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from morta import Morta, AsyncMorta

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFields:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_options(self, client: Morta) -> None:
        field = client.integrations.fields.retrieve_options(
            field_key="field_key",
            provider="provider",
        )
        assert field is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_options(self, client: Morta) -> None:
        response = client.integrations.fields.with_raw_response.retrieve_options(
            field_key="field_key",
            provider="provider",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = response.parse()
        assert field is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_options(self, client: Morta) -> None:
        with client.integrations.fields.with_streaming_response.retrieve_options(
            field_key="field_key",
            provider="provider",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = response.parse()
            assert field is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_options(self, client: Morta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            client.integrations.fields.with_raw_response.retrieve_options(
                field_key="field_key",
                provider="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `field_key` but received ''"):
            client.integrations.fields.with_raw_response.retrieve_options(
                field_key="",
                provider="provider",
            )


class TestAsyncFields:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_options(self, async_client: AsyncMorta) -> None:
        field = await async_client.integrations.fields.retrieve_options(
            field_key="field_key",
            provider="provider",
        )
        assert field is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_options(self, async_client: AsyncMorta) -> None:
        response = await async_client.integrations.fields.with_raw_response.retrieve_options(
            field_key="field_key",
            provider="provider",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        field = await response.parse()
        assert field is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_options(self, async_client: AsyncMorta) -> None:
        async with async_client.integrations.fields.with_streaming_response.retrieve_options(
            field_key="field_key",
            provider="provider",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            field = await response.parse()
            assert field is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_options(self, async_client: AsyncMorta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `provider` but received ''"):
            await async_client.integrations.fields.with_raw_response.retrieve_options(
                field_key="field_key",
                provider="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `field_key` but received ''"):
            await async_client.integrations.fields.with_raw_response.retrieve_options(
                field_key="",
                provider="provider",
            )
