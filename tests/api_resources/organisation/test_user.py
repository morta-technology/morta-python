# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from morta import Morta, AsyncMorta

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUser:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Morta) -> None:
        user = client.organisation.user.delete(
            user_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Morta) -> None:
        response = client.organisation.user.with_raw_response.delete(
            user_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Morta) -> None:
        with client.organisation.user.with_streaming_response.delete(
            user_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Morta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            client.organisation.user.with_raw_response.delete(
                user_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                organisation_public_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_public_id` but received ''"):
            client.organisation.user.with_raw_response.delete(
                user_public_id="",
                organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_allocate_license(self, client: Morta) -> None:
        user = client.organisation.user.allocate_license(
            user_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_allocate_license(self, client: Morta) -> None:
        response = client.organisation.user.with_raw_response.allocate_license(
            user_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_allocate_license(self, client: Morta) -> None:
        with client.organisation.user.with_streaming_response.allocate_license(
            user_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_allocate_license(self, client: Morta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            client.organisation.user.with_raw_response.allocate_license(
                user_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                organisation_public_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_public_id` but received ''"):
            client.organisation.user.with_raw_response.allocate_license(
                user_public_id="",
                organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_remove_license(self, client: Morta) -> None:
        user = client.organisation.user.remove_license(
            user_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_remove_license(self, client: Morta) -> None:
        response = client.organisation.user.with_raw_response.remove_license(
            user_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_remove_license(self, client: Morta) -> None:
        with client.organisation.user.with_streaming_response.remove_license(
            user_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_remove_license(self, client: Morta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            client.organisation.user.with_raw_response.remove_license(
                user_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                organisation_public_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_public_id` but received ''"):
            client.organisation.user.with_raw_response.remove_license(
                user_public_id="",
                organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncUser:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMorta) -> None:
        user = await async_client.organisation.user.delete(
            user_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMorta) -> None:
        response = await async_client.organisation.user.with_raw_response.delete(
            user_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMorta) -> None:
        async with async_client.organisation.user.with_streaming_response.delete(
            user_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMorta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            await async_client.organisation.user.with_raw_response.delete(
                user_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                organisation_public_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_public_id` but received ''"):
            await async_client.organisation.user.with_raw_response.delete(
                user_public_id="",
                organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_allocate_license(self, async_client: AsyncMorta) -> None:
        user = await async_client.organisation.user.allocate_license(
            user_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_allocate_license(self, async_client: AsyncMorta) -> None:
        response = await async_client.organisation.user.with_raw_response.allocate_license(
            user_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_allocate_license(self, async_client: AsyncMorta) -> None:
        async with async_client.organisation.user.with_streaming_response.allocate_license(
            user_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_allocate_license(self, async_client: AsyncMorta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            await async_client.organisation.user.with_raw_response.allocate_license(
                user_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                organisation_public_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_public_id` but received ''"):
            await async_client.organisation.user.with_raw_response.allocate_license(
                user_public_id="",
                organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_remove_license(self, async_client: AsyncMorta) -> None:
        user = await async_client.organisation.user.remove_license(
            user_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_remove_license(self, async_client: AsyncMorta) -> None:
        response = await async_client.organisation.user.with_raw_response.remove_license(
            user_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert user is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_remove_license(self, async_client: AsyncMorta) -> None:
        async with async_client.organisation.user.with_streaming_response.remove_license(
            user_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert user is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_remove_license(self, async_client: AsyncMorta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            await async_client.organisation.user.with_raw_response.remove_license(
                user_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                organisation_public_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `user_public_id` but received ''"):
            await async_client.organisation.user.with_raw_response.remove_license(
                user_public_id="",
                organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
