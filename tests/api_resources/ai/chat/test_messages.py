# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from morta import Morta, AsyncMorta

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMessages:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: Morta) -> None:
        message = client.ai.chat.messages.cancel(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: Morta) -> None:
        response = client.ai.chat.messages.with_raw_response.cancel(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = response.parse()
        assert message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: Morta) -> None:
        with client.ai.chat.messages.with_streaming_response.cancel(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = response.parse()
            assert message is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: Morta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            client.ai.chat.messages.with_raw_response.cancel(
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                conversation_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            client.ai.chat.messages.with_raw_response.cancel(
                message_id="",
                conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncMessages:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncMorta) -> None:
        message = await async_client.ai.chat.messages.cancel(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncMorta) -> None:
        response = await async_client.ai.chat.messages.with_raw_response.cancel(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        message = await response.parse()
        assert message is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncMorta) -> None:
        async with async_client.ai.chat.messages.with_streaming_response.cancel(
            message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            message = await response.parse()
            assert message is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncMorta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `conversation_id` but received ''"):
            await async_client.ai.chat.messages.with_raw_response.cancel(
                message_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                conversation_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `message_id` but received ''"):
            await async_client.ai.chat.messages.with_raw_response.cancel(
                message_id="",
                conversation_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
