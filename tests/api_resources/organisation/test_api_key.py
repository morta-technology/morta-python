# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from morta import Morta, AsyncMorta
from tests.utils import assert_matches_type
from morta.types.user import APIKey
from morta.types.organisation import APIKeyRetrieveAPIKeyResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAPIKey:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Morta) -> None:
        api_key = client.organisation.api_key.update(
            api_key_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            access_level=0,
        )
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Morta) -> None:
        api_key = client.organisation.api_key.update(
            api_key_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            access_level=0,
            document_restrictions=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            name="name",
            project_restrictions=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            site_restrictions=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            table_restrictions=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Morta) -> None:
        response = client.organisation.api_key.with_raw_response.update(
            api_key_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            access_level=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Morta) -> None:
        with client.organisation.api_key.with_streaming_response.update(
            api_key_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            access_level=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Morta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            client.organisation.api_key.with_raw_response.update(
                api_key_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                organisation_public_id="",
                access_level=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_public_id` but received ''"):
            client.organisation.api_key.with_raw_response.update(
                api_key_public_id="",
                organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                access_level=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Morta) -> None:
        api_key = client.organisation.api_key.delete(
            api_key_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert api_key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Morta) -> None:
        response = client.organisation.api_key.with_raw_response.delete(
            api_key_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert api_key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Morta) -> None:
        with client.organisation.api_key.with_streaming_response.delete(
            api_key_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert api_key is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Morta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            client.organisation.api_key.with_raw_response.delete(
                api_key_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                organisation_public_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_public_id` but received ''"):
            client.organisation.api_key.with_raw_response.delete(
                api_key_public_id="",
                organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_api_key(self, client: Morta) -> None:
        api_key = client.organisation.api_key.api_key(
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            access_level=0,
        )
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_api_key_with_all_params(self, client: Morta) -> None:
        api_key = client.organisation.api_key.api_key(
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            access_level=0,
            document_restrictions=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            name="name",
            project_restrictions=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            site_restrictions=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            table_restrictions=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_api_key(self, client: Morta) -> None:
        response = client.organisation.api_key.with_raw_response.api_key(
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            access_level=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_api_key(self, client: Morta) -> None:
        with client.organisation.api_key.with_streaming_response.api_key(
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            access_level=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_api_key(self, client: Morta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            client.organisation.api_key.with_raw_response.api_key(
                organisation_public_id="",
                access_level=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_api_key(self, client: Morta) -> None:
        api_key = client.organisation.api_key.retrieve_api_key(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIKeyRetrieveAPIKeyResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_api_key(self, client: Morta) -> None:
        response = client.organisation.api_key.with_raw_response.retrieve_api_key(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = response.parse()
        assert_matches_type(APIKeyRetrieveAPIKeyResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_api_key(self, client: Morta) -> None:
        with client.organisation.api_key.with_streaming_response.retrieve_api_key(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = response.parse()
            assert_matches_type(APIKeyRetrieveAPIKeyResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_api_key(self, client: Morta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            client.organisation.api_key.with_raw_response.retrieve_api_key(
                "",
            )


class TestAsyncAPIKey:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMorta) -> None:
        api_key = await async_client.organisation.api_key.update(
            api_key_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            access_level=0,
        )
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMorta) -> None:
        api_key = await async_client.organisation.api_key.update(
            api_key_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            access_level=0,
            document_restrictions=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            name="name",
            project_restrictions=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            site_restrictions=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            table_restrictions=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMorta) -> None:
        response = await async_client.organisation.api_key.with_raw_response.update(
            api_key_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            access_level=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMorta) -> None:
        async with async_client.organisation.api_key.with_streaming_response.update(
            api_key_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            access_level=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMorta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            await async_client.organisation.api_key.with_raw_response.update(
                api_key_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                organisation_public_id="",
                access_level=0,
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_public_id` but received ''"):
            await async_client.organisation.api_key.with_raw_response.update(
                api_key_public_id="",
                organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                access_level=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMorta) -> None:
        api_key = await async_client.organisation.api_key.delete(
            api_key_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert api_key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMorta) -> None:
        response = await async_client.organisation.api_key.with_raw_response.delete(
            api_key_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert api_key is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMorta) -> None:
        async with async_client.organisation.api_key.with_streaming_response.delete(
            api_key_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert api_key is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMorta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            await async_client.organisation.api_key.with_raw_response.delete(
                api_key_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                organisation_public_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `api_key_public_id` but received ''"):
            await async_client.organisation.api_key.with_raw_response.delete(
                api_key_public_id="",
                organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_api_key(self, async_client: AsyncMorta) -> None:
        api_key = await async_client.organisation.api_key.api_key(
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            access_level=0,
        )
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_api_key_with_all_params(self, async_client: AsyncMorta) -> None:
        api_key = await async_client.organisation.api_key.api_key(
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            access_level=0,
            document_restrictions=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            name="name",
            project_restrictions=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            site_restrictions=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            table_restrictions=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
        )
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_api_key(self, async_client: AsyncMorta) -> None:
        response = await async_client.organisation.api_key.with_raw_response.api_key(
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            access_level=0,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKey, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_api_key(self, async_client: AsyncMorta) -> None:
        async with async_client.organisation.api_key.with_streaming_response.api_key(
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            access_level=0,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKey, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_api_key(self, async_client: AsyncMorta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            await async_client.organisation.api_key.with_raw_response.api_key(
                organisation_public_id="",
                access_level=0,
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_api_key(self, async_client: AsyncMorta) -> None:
        api_key = await async_client.organisation.api_key.retrieve_api_key(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(APIKeyRetrieveAPIKeyResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_api_key(self, async_client: AsyncMorta) -> None:
        response = await async_client.organisation.api_key.with_raw_response.retrieve_api_key(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        api_key = await response.parse()
        assert_matches_type(APIKeyRetrieveAPIKeyResponse, api_key, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_api_key(self, async_client: AsyncMorta) -> None:
        async with async_client.organisation.api_key.with_streaming_response.retrieve_api_key(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            api_key = await response.parse()
            assert_matches_type(APIKeyRetrieveAPIKeyResponse, api_key, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_api_key(self, async_client: AsyncMorta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            await async_client.organisation.api_key.with_raw_response.retrieve_api_key(
                "",
            )
