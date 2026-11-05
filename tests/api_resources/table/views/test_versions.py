# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from morta import Morta, AsyncMorta
from tests.utils import assert_matches_type
from morta._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)
from morta.types.table.views import (
    VersionListResponse,
    VersionCreateResponse,
    VersionUpdateResponse,
    VersionRestoreResponse,
    VersionRetrieveResponse,
    VersionDeleteUnpublishedResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestVersions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Morta) -> None:
        version = client.table.views.versions.create(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            html="html",
        )
        assert_matches_type(VersionCreateResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Morta) -> None:
        version = client.table.views.versions.create(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            html="html",
            publish=True,
        )
        assert_matches_type(VersionCreateResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Morta) -> None:
        response = client.table.views.versions.with_raw_response.create(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            html="html",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionCreateResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Morta) -> None:
        with client.table.views.versions.with_streaming_response.create(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            html="html",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionCreateResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Morta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.table.views.versions.with_raw_response.create(
                view_id="",
                html="html",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Morta) -> None:
        version = client.table.views.versions.retrieve(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VersionRetrieveResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Morta) -> None:
        response = client.table.views.versions.with_raw_response.retrieve(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionRetrieveResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Morta) -> None:
        with client.table.views.versions.with_streaming_response.retrieve(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionRetrieveResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Morta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.table.views.versions.with_raw_response.retrieve(
                version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                view_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.table.views.versions.with_raw_response.retrieve(
                version_id="",
                view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Morta) -> None:
        version = client.table.views.versions.update(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VersionUpdateResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Morta) -> None:
        version = client.table.views.versions.update(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            summary="summary",
            thumbnail="thumbnail",
            title="title",
        )
        assert_matches_type(VersionUpdateResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Morta) -> None:
        response = client.table.views.versions.with_raw_response.update(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionUpdateResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Morta) -> None:
        with client.table.views.versions.with_streaming_response.update(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionUpdateResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Morta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.table.views.versions.with_raw_response.update(
                version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                view_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.table.views.versions.with_raw_response.update(
                version_id="",
                view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Morta) -> None:
        version = client.table.views.versions.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VersionListResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Morta) -> None:
        response = client.table.views.versions.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionListResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Morta) -> None:
        with client.table.views.versions.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionListResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Morta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.table.views.versions.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Morta) -> None:
        version = client.table.views.versions.delete(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert version is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Morta) -> None:
        response = client.table.views.versions.with_raw_response.delete(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert version is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Morta) -> None:
        with client.table.views.versions.with_streaming_response.delete(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert version is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Morta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.table.views.versions.with_raw_response.delete(
                version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                view_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.table.views.versions.with_raw_response.delete(
                version_id="",
                view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete_unpublished(self, client: Morta) -> None:
        version = client.table.views.versions.delete_unpublished(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VersionDeleteUnpublishedResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete_unpublished(self, client: Morta) -> None:
        response = client.table.views.versions.with_raw_response.delete_unpublished(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionDeleteUnpublishedResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete_unpublished(self, client: Morta) -> None:
        with client.table.views.versions.with_streaming_response.delete_unpublished(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionDeleteUnpublishedResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete_unpublished(self, client: Morta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.table.views.versions.with_raw_response.delete_unpublished(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restore(self, client: Morta) -> None:
        version = client.table.views.versions.restore(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VersionRestoreResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_restore_with_all_params(self, client: Morta) -> None:
        version = client.table.views.versions.restore(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            delete_newer=True,
        )
        assert_matches_type(VersionRestoreResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_restore(self, client: Morta) -> None:
        response = client.table.views.versions.with_raw_response.restore(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = response.parse()
        assert_matches_type(VersionRestoreResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_restore(self, client: Morta) -> None:
        with client.table.views.versions.with_streaming_response.restore(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = response.parse()
            assert_matches_type(VersionRestoreResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_restore(self, client: Morta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.table.views.versions.with_raw_response.restore(
                version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                view_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.table.views.versions.with_raw_response.restore(
                version_id="",
                view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve_thumbnail(self, client: Morta, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/v1/table/views/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/versions/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/thumbnail"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        version = client.table.views.versions.retrieve_thumbnail(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert version.is_closed
        assert version.json() == {"foo": "bar"}
        assert cast(Any, version.is_closed) is True
        assert isinstance(version, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve_thumbnail(self, client: Morta, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/v1/table/views/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/versions/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/thumbnail"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        version = client.table.views.versions.with_raw_response.retrieve_thumbnail(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert version.is_closed is True
        assert version.http_request.headers.get("X-Stainless-Lang") == "python"
        assert version.json() == {"foo": "bar"}
        assert isinstance(version, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve_thumbnail(self, client: Morta, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/v1/table/views/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/versions/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/thumbnail"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        with client.table.views.versions.with_streaming_response.retrieve_thumbnail(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as version:
            assert not version.is_closed
            assert version.http_request.headers.get("X-Stainless-Lang") == "python"

            assert version.json() == {"foo": "bar"}
            assert cast(Any, version.is_closed) is True
            assert isinstance(version, StreamedBinaryAPIResponse)

        assert cast(Any, version.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve_thumbnail(self, client: Morta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            client.table.views.versions.with_raw_response.retrieve_thumbnail(
                version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                view_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            client.table.views.versions.with_raw_response.retrieve_thumbnail(
                version_id="",
                view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncVersions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMorta) -> None:
        version = await async_client.table.views.versions.create(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            html="html",
        )
        assert_matches_type(VersionCreateResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMorta) -> None:
        version = await async_client.table.views.versions.create(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            html="html",
            publish=True,
        )
        assert_matches_type(VersionCreateResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMorta) -> None:
        response = await async_client.table.views.versions.with_raw_response.create(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            html="html",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(VersionCreateResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMorta) -> None:
        async with async_client.table.views.versions.with_streaming_response.create(
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            html="html",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionCreateResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncMorta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.table.views.versions.with_raw_response.create(
                view_id="",
                html="html",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMorta) -> None:
        version = await async_client.table.views.versions.retrieve(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VersionRetrieveResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMorta) -> None:
        response = await async_client.table.views.versions.with_raw_response.retrieve(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(VersionRetrieveResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMorta) -> None:
        async with async_client.table.views.versions.with_streaming_response.retrieve(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionRetrieveResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMorta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.table.views.versions.with_raw_response.retrieve(
                version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                view_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.table.views.versions.with_raw_response.retrieve(
                version_id="",
                view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMorta) -> None:
        version = await async_client.table.views.versions.update(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VersionUpdateResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMorta) -> None:
        version = await async_client.table.views.versions.update(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            summary="summary",
            thumbnail="thumbnail",
            title="title",
        )
        assert_matches_type(VersionUpdateResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMorta) -> None:
        response = await async_client.table.views.versions.with_raw_response.update(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(VersionUpdateResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMorta) -> None:
        async with async_client.table.views.versions.with_streaming_response.update(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionUpdateResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMorta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.table.views.versions.with_raw_response.update(
                version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                view_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.table.views.versions.with_raw_response.update(
                version_id="",
                view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMorta) -> None:
        version = await async_client.table.views.versions.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VersionListResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMorta) -> None:
        response = await async_client.table.views.versions.with_raw_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(VersionListResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMorta) -> None:
        async with async_client.table.views.versions.with_streaming_response.list(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionListResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncMorta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.table.views.versions.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMorta) -> None:
        version = await async_client.table.views.versions.delete(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert version is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMorta) -> None:
        response = await async_client.table.views.versions.with_raw_response.delete(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert version is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMorta) -> None:
        async with async_client.table.views.versions.with_streaming_response.delete(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert version is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMorta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.table.views.versions.with_raw_response.delete(
                version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                view_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.table.views.versions.with_raw_response.delete(
                version_id="",
                view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete_unpublished(self, async_client: AsyncMorta) -> None:
        version = await async_client.table.views.versions.delete_unpublished(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VersionDeleteUnpublishedResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete_unpublished(self, async_client: AsyncMorta) -> None:
        response = await async_client.table.views.versions.with_raw_response.delete_unpublished(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(VersionDeleteUnpublishedResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete_unpublished(self, async_client: AsyncMorta) -> None:
        async with async_client.table.views.versions.with_streaming_response.delete_unpublished(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionDeleteUnpublishedResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete_unpublished(self, async_client: AsyncMorta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.table.views.versions.with_raw_response.delete_unpublished(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restore(self, async_client: AsyncMorta) -> None:
        version = await async_client.table.views.versions.restore(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(VersionRestoreResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_restore_with_all_params(self, async_client: AsyncMorta) -> None:
        version = await async_client.table.views.versions.restore(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            delete_newer=True,
        )
        assert_matches_type(VersionRestoreResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_restore(self, async_client: AsyncMorta) -> None:
        response = await async_client.table.views.versions.with_raw_response.restore(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        version = await response.parse()
        assert_matches_type(VersionRestoreResponse, version, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_restore(self, async_client: AsyncMorta) -> None:
        async with async_client.table.views.versions.with_streaming_response.restore(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            version = await response.parse()
            assert_matches_type(VersionRestoreResponse, version, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_restore(self, async_client: AsyncMorta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.table.views.versions.with_raw_response.restore(
                version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                view_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.table.views.versions.with_raw_response.restore(
                version_id="",
                view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve_thumbnail(self, async_client: AsyncMorta, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/v1/table/views/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/versions/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/thumbnail"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        version = await async_client.table.views.versions.retrieve_thumbnail(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert version.is_closed
        assert await version.json() == {"foo": "bar"}
        assert cast(Any, version.is_closed) is True
        assert isinstance(version, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve_thumbnail(self, async_client: AsyncMorta, respx_mock: MockRouter) -> None:
        respx_mock.get(
            "/v1/table/views/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/versions/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/thumbnail"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))

        version = await async_client.table.views.versions.with_raw_response.retrieve_thumbnail(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert version.is_closed is True
        assert version.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await version.json() == {"foo": "bar"}
        assert isinstance(version, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve_thumbnail(
        self, async_client: AsyncMorta, respx_mock: MockRouter
    ) -> None:
        respx_mock.get(
            "/v1/table/views/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/versions/182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e/thumbnail"
        ).mock(return_value=httpx.Response(200, json={"foo": "bar"}))
        async with async_client.table.views.versions.with_streaming_response.retrieve_thumbnail(
            version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as version:
            assert not version.is_closed
            assert version.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await version.json() == {"foo": "bar"}
            assert cast(Any, version.is_closed) is True
            assert isinstance(version, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, version.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve_thumbnail(self, async_client: AsyncMorta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `view_id` but received ''"):
            await async_client.table.views.versions.with_raw_response.retrieve_thumbnail(
                version_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                view_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `version_id` but received ''"):
            await async_client.table.views.versions.with_raw_response.retrieve_thumbnail(
                version_id="",
                view_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
