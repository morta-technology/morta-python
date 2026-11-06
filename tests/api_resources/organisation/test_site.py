# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from morta import Morta, AsyncMorta
from tests.utils import assert_matches_type
from morta.types.organisation import Site

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSite:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Morta) -> None:
        site = client.organisation.site.create(
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Site, site, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Morta) -> None:
        site = client.organisation.site.create(
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
            users=[
                {
                    "email": "dev@stainless.com",
                    "role": "admin",
                    "context": {
                        "process_public_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "process_section_public_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                }
            ],
        )
        assert_matches_type(Site, site, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Morta) -> None:
        response = client.organisation.site.with_raw_response.create(
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site = response.parse()
        assert_matches_type(Site, site, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Morta) -> None:
        with client.organisation.site.with_streaming_response.create(
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site = response.parse()
            assert_matches_type(Site, site, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Morta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            client.organisation.site.with_raw_response.create(
                organisation_public_id="",
                team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Morta) -> None:
        site = client.organisation.site.retrieve(
            site_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Site, site, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Morta) -> None:
        response = client.organisation.site.with_raw_response.retrieve(
            site_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site = response.parse()
        assert_matches_type(Site, site, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Morta) -> None:
        with client.organisation.site.with_streaming_response.retrieve(
            site_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site = response.parse()
            assert_matches_type(Site, site, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Morta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            client.organisation.site.with_raw_response.retrieve(
                site_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                organisation_public_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_public_id` but received ''"):
            client.organisation.site.with_raw_response.retrieve(
                site_public_id="",
                organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Morta) -> None:
        site = client.organisation.site.update(
            site_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Site, site, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Morta) -> None:
        site = client.organisation.site.update(
            site_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            users=[
                {
                    "email": "dev@stainless.com",
                    "role": "admin",
                    "context": {
                        "process_public_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "process_section_public_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                }
            ],
        )
        assert_matches_type(Site, site, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Morta) -> None:
        response = client.organisation.site.with_raw_response.update(
            site_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site = response.parse()
        assert_matches_type(Site, site, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Morta) -> None:
        with client.organisation.site.with_streaming_response.update(
            site_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site = response.parse()
            assert_matches_type(Site, site, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Morta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            client.organisation.site.with_raw_response.update(
                site_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                organisation_public_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_public_id` but received ''"):
            client.organisation.site.with_raw_response.update(
                site_public_id="",
                organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Morta) -> None:
        site = client.organisation.site.delete(
            site_public_id="site_public_id",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert site is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Morta) -> None:
        response = client.organisation.site.with_raw_response.delete(
            site_public_id="site_public_id",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site = response.parse()
        assert site is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Morta) -> None:
        with client.organisation.site.with_streaming_response.delete(
            site_public_id="site_public_id",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site = response.parse()
            assert site is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Morta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            client.organisation.site.with_raw_response.delete(
                site_public_id="site_public_id",
                organisation_public_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_public_id` but received ''"):
            client.organisation.site.with_raw_response.delete(
                site_public_id="",
                organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncSite:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMorta) -> None:
        site = await async_client.organisation.site.create(
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Site, site, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMorta) -> None:
        site = await async_client.organisation.site.create(
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
            users=[
                {
                    "email": "dev@stainless.com",
                    "role": "admin",
                    "context": {
                        "process_public_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "process_section_public_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                }
            ],
        )
        assert_matches_type(Site, site, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMorta) -> None:
        response = await async_client.organisation.site.with_raw_response.create(
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site = await response.parse()
        assert_matches_type(Site, site, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMorta) -> None:
        async with async_client.organisation.site.with_streaming_response.create(
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site = await response.parse()
            assert_matches_type(Site, site, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncMorta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            await async_client.organisation.site.with_raw_response.create(
                organisation_public_id="",
                team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMorta) -> None:
        site = await async_client.organisation.site.retrieve(
            site_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Site, site, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMorta) -> None:
        response = await async_client.organisation.site.with_raw_response.retrieve(
            site_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site = await response.parse()
        assert_matches_type(Site, site, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMorta) -> None:
        async with async_client.organisation.site.with_streaming_response.retrieve(
            site_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site = await response.parse()
            assert_matches_type(Site, site, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMorta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            await async_client.organisation.site.with_raw_response.retrieve(
                site_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                organisation_public_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_public_id` but received ''"):
            await async_client.organisation.site.with_raw_response.retrieve(
                site_public_id="",
                organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMorta) -> None:
        site = await async_client.organisation.site.update(
            site_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Site, site, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMorta) -> None:
        site = await async_client.organisation.site.update(
            site_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            name="x",
            team_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            users=[
                {
                    "email": "dev@stainless.com",
                    "role": "admin",
                    "context": {
                        "process_public_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "process_section_public_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                        "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                    },
                }
            ],
        )
        assert_matches_type(Site, site, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMorta) -> None:
        response = await async_client.organisation.site.with_raw_response.update(
            site_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site = await response.parse()
        assert_matches_type(Site, site, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMorta) -> None:
        async with async_client.organisation.site.with_streaming_response.update(
            site_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site = await response.parse()
            assert_matches_type(Site, site, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMorta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            await async_client.organisation.site.with_raw_response.update(
                site_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                organisation_public_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_public_id` but received ''"):
            await async_client.organisation.site.with_raw_response.update(
                site_public_id="",
                organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMorta) -> None:
        site = await async_client.organisation.site.delete(
            site_public_id="site_public_id",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert site is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMorta) -> None:
        response = await async_client.organisation.site.with_raw_response.delete(
            site_public_id="site_public_id",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        site = await response.parse()
        assert site is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMorta) -> None:
        async with async_client.organisation.site.with_streaming_response.delete(
            site_public_id="site_public_id",
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            site = await response.parse()
            assert site is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMorta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            await async_client.organisation.site.with_raw_response.delete(
                site_public_id="site_public_id",
                organisation_public_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `site_public_id` but received ''"):
            await async_client.organisation.site.with_raw_response.delete(
                site_public_id="",
                organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
