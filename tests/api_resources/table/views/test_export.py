# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from morta import Morta, AsyncMorta
from morta._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestExport:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create(self, client: Morta, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/table/views/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        export = client.table.views.export.create(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert export.is_closed
        assert export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_create_with_all_params(self, client: Morta, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/table/views/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        export = client.table.views.export.create(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            colour=[{}],
            display_comment_rows=0,
            filter=[{}],
            format="csv",
            hidden=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sort=["string"],
            timezone="timezone",
        )
        assert export.is_closed
        assert export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_create(self, client: Morta, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/table/views/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        export = client.table.views.export.with_raw_response.create(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert export.is_closed is True
        assert export.http_request.headers.get("X-Stainless-Lang") == "python"
        assert export.json() == {"foo": "bar"}
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_create(self, client: Morta, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/table/views/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.table.views.export.with_streaming_response.create(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as export:
            assert not export.is_closed
            assert export.http_request.headers.get("X-Stainless-Lang") == "python"

            assert export.json() == {"foo": "bar"}
            assert cast(Any, export.is_closed) is True
            assert isinstance(export, StreamedBinaryAPIResponse)

        assert cast(Any, export.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_create(self, client: Morta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.table.views.export.with_raw_response.create(
                view_id="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list(self, client: Morta, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/table/views/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        export = client.table.views.export.list(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert export.is_closed
        assert export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_list_with_all_params(self, client: Morta, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/table/views/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        export = client.table.views.export.list(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            colour="colour",
            filter="filter",
            format="csv",
            hidden="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sort="sort",
            timezone="timezone",
        )
        assert export.is_closed
        assert export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_list(self, client: Morta, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/table/views/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        export = client.table.views.export.with_raw_response.list(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert export.is_closed is True
        assert export.http_request.headers.get("X-Stainless-Lang") == "python"
        assert export.json() == {"foo": "bar"}
        assert isinstance(export, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_list(self, client: Morta, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/table/views/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.table.views.export.with_streaming_response.list(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as export:
            assert not export.is_closed
            assert export.http_request.headers.get("X-Stainless-Lang") == "python"

            assert export.json() == {"foo": "bar"}
            assert cast(Any, export.is_closed) is True
            assert isinstance(export, StreamedBinaryAPIResponse)

        assert cast(Any, export.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_list(self, client: Morta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.table.views.export.with_raw_response.list(
                view_id="",
            )


class TestAsyncExport:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create(self, async_client: AsyncMorta, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/table/views/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        export = await async_client.table.views.export.create(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert export.is_closed
        assert await export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_create_with_all_params(self, async_client: AsyncMorta, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/table/views/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        export = await async_client.table.views.export.create(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            colour=[{}],
            display_comment_rows=0,
            filter=[{}],
            format="csv",
            hidden=["182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e"],
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sort=["string"],
            timezone="timezone",
        )
        assert export.is_closed
        assert await export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_create(self, async_client: AsyncMorta, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/table/views/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        export = await async_client.table.views.export.with_raw_response.create(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert export.is_closed is True
        assert export.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await export.json() == {"foo": "bar"}
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_create(self, async_client: AsyncMorta, respx_mock: MockRouter) -> None:
        respx_mock.post("/v1/table/views/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.table.views.export.with_streaming_response.create(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as export:
            assert not export.is_closed
            assert export.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await export.json() == {"foo": "bar"}
            assert cast(Any, export.is_closed) is True
            assert isinstance(export, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, export.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_create(self, async_client: AsyncMorta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.table.views.export.with_raw_response.create(
                view_id="",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list(self, async_client: AsyncMorta, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/table/views/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        export = await async_client.table.views.export.list(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert export.is_closed
        assert await export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_list_with_all_params(self, async_client: AsyncMorta, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/table/views/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        export = await async_client.table.views.export.list(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            colour="colour",
            filter="filter",
            format="csv",
            hidden="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            process_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            sort="sort",
            timezone="timezone",
        )
        assert export.is_closed
        assert await export.json() == {"foo": "bar"}
        assert cast(Any, export.is_closed) is True
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_list(self, async_client: AsyncMorta, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/table/views/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        export = await async_client.table.views.export.with_raw_response.list(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert export.is_closed is True
        assert export.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await export.json() == {"foo": "bar"}
        assert isinstance(export, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_list(self, async_client: AsyncMorta, respx_mock: MockRouter) -> None:
        respx_mock.get("/v1/table/views/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/export").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.table.views.export.with_streaming_response.list(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as export:
            assert not export.is_closed
            assert export.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await export.json() == {"foo": "bar"}
            assert cast(Any, export.is_closed) is True
            assert isinstance(export, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, export.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_list(self, async_client: AsyncMorta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.table.views.export.with_raw_response.list(
                view_id="",
            )
