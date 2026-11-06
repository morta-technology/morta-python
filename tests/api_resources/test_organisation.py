# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from morta import Morta, AsyncMorta
from morta.types import OrganisationRetrieveHubsResponse, OrganisationRetrieveSitesResponse
from tests.utils import assert_matches_type
from morta.types.organisation import Organisation

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrganisation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Morta) -> None:
        organisation = client.organisation.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Organisation, organisation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Morta) -> None:
        response = client.organisation.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organisation = response.parse()
        assert_matches_type(Organisation, organisation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Morta) -> None:
        with client.organisation.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organisation = response.parse()
            assert_matches_type(Organisation, organisation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Morta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            client.organisation.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Morta) -> None:
        organisation = client.organisation.update(
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Organisation, organisation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Morta) -> None:
        organisation = client.organisation.update(
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            disable_personal_view_saving=True,
            enable_user_api_keys=True,
            enforce_login="enforceLogin",
            idp_certificate="idpCertificate",
            idp_issuer="idpIssuer",
            idp_sso_url="idpSsoUrl",
            name="x",
            restrict_hub_creation=True,
            restrict_sync_configuration=True,
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
        assert_matches_type(Organisation, organisation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Morta) -> None:
        response = client.organisation.with_raw_response.update(
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organisation = response.parse()
        assert_matches_type(Organisation, organisation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Morta) -> None:
        with client.organisation.with_streaming_response.update(
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organisation = response.parse()
            assert_matches_type(Organisation, organisation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Morta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            client.organisation.with_raw_response.update(
                organisation_public_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_hubs(self, client: Morta) -> None:
        organisation = client.organisation.retrieve_hubs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OrganisationRetrieveHubsResponse, organisation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_hubs(self, client: Morta) -> None:
        response = client.organisation.with_raw_response.retrieve_hubs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organisation = response.parse()
        assert_matches_type(OrganisationRetrieveHubsResponse, organisation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_hubs(self, client: Morta) -> None:
        with client.organisation.with_streaming_response.retrieve_hubs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organisation = response.parse()
            assert_matches_type(OrganisationRetrieveHubsResponse, organisation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_hubs(self, client: Morta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            client.organisation.with_raw_response.retrieve_hubs(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_sites(self, client: Morta) -> None:
        organisation = client.organisation.retrieve_sites(
            "organisation_public_id",
        )
        assert_matches_type(OrganisationRetrieveSitesResponse, organisation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_sites(self, client: Morta) -> None:
        response = client.organisation.with_raw_response.retrieve_sites(
            "organisation_public_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organisation = response.parse()
        assert_matches_type(OrganisationRetrieveSitesResponse, organisation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_sites(self, client: Morta) -> None:
        with client.organisation.with_streaming_response.retrieve_sites(
            "organisation_public_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organisation = response.parse()
            assert_matches_type(OrganisationRetrieveSitesResponse, organisation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve_sites(self, client: Morta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            client.organisation.with_raw_response.retrieve_sites(
                "",
            )


class TestAsyncOrganisation:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMorta) -> None:
        organisation = await async_client.organisation.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Organisation, organisation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMorta) -> None:
        response = await async_client.organisation.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organisation = await response.parse()
        assert_matches_type(Organisation, organisation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMorta) -> None:
        async with async_client.organisation.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organisation = await response.parse()
            assert_matches_type(Organisation, organisation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMorta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            await async_client.organisation.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMorta) -> None:
        organisation = await async_client.organisation.update(
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Organisation, organisation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMorta) -> None:
        organisation = await async_client.organisation.update(
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            disable_personal_view_saving=True,
            enable_user_api_keys=True,
            enforce_login="enforceLogin",
            idp_certificate="idpCertificate",
            idp_issuer="idpIssuer",
            idp_sso_url="idpSsoUrl",
            name="x",
            restrict_hub_creation=True,
            restrict_sync_configuration=True,
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
        assert_matches_type(Organisation, organisation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMorta) -> None:
        response = await async_client.organisation.with_raw_response.update(
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organisation = await response.parse()
        assert_matches_type(Organisation, organisation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMorta) -> None:
        async with async_client.organisation.with_streaming_response.update(
            organisation_public_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organisation = await response.parse()
            assert_matches_type(Organisation, organisation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMorta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            await async_client.organisation.with_raw_response.update(
                organisation_public_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_hubs(self, async_client: AsyncMorta) -> None:
        organisation = await async_client.organisation.retrieve_hubs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(OrganisationRetrieveHubsResponse, organisation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_hubs(self, async_client: AsyncMorta) -> None:
        response = await async_client.organisation.with_raw_response.retrieve_hubs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organisation = await response.parse()
        assert_matches_type(OrganisationRetrieveHubsResponse, organisation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_hubs(self, async_client: AsyncMorta) -> None:
        async with async_client.organisation.with_streaming_response.retrieve_hubs(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organisation = await response.parse()
            assert_matches_type(OrganisationRetrieveHubsResponse, organisation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_hubs(self, async_client: AsyncMorta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            await async_client.organisation.with_raw_response.retrieve_hubs(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_sites(self, async_client: AsyncMorta) -> None:
        organisation = await async_client.organisation.retrieve_sites(
            "organisation_public_id",
        )
        assert_matches_type(OrganisationRetrieveSitesResponse, organisation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_sites(self, async_client: AsyncMorta) -> None:
        response = await async_client.organisation.with_raw_response.retrieve_sites(
            "organisation_public_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        organisation = await response.parse()
        assert_matches_type(OrganisationRetrieveSitesResponse, organisation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_sites(self, async_client: AsyncMorta) -> None:
        async with async_client.organisation.with_streaming_response.retrieve_sites(
            "organisation_public_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            organisation = await response.parse()
            assert_matches_type(OrganisationRetrieveSitesResponse, organisation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve_sites(self, async_client: AsyncMorta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            await async_client.organisation.with_raw_response.retrieve_sites(
                "",
            )
