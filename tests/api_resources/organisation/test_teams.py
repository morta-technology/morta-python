# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from morta import Morta, AsyncMorta

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTeams:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Morta) -> None:
        team = client.organisation.teams.create(
            "organisation_public_id",
        )
        assert team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Morta) -> None:
        response = client.organisation.teams.with_raw_response.create(
            "organisation_public_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Morta) -> None:
        with client.organisation.teams.with_streaming_response.create(
            "organisation_public_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert team is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Morta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            client.organisation.teams.with_raw_response.create(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: Morta) -> None:
        team = client.organisation.teams.retrieve(
            team_public_id="team_public_id",
            organisation_public_id="organisation_public_id",
        )
        assert team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: Morta) -> None:
        response = client.organisation.teams.with_raw_response.retrieve(
            team_public_id="team_public_id",
            organisation_public_id="organisation_public_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: Morta) -> None:
        with client.organisation.teams.with_streaming_response.retrieve(
            team_public_id="team_public_id",
            organisation_public_id="organisation_public_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert team is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: Morta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            client.organisation.teams.with_raw_response.retrieve(
                team_public_id="team_public_id",
                organisation_public_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_public_id` but received ''"):
            client.organisation.teams.with_raw_response.retrieve(
                team_public_id="",
                organisation_public_id="organisation_public_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Morta) -> None:
        team = client.organisation.teams.update(
            team_public_id="team_public_id",
            organisation_public_id="organisation_public_id",
        )
        assert team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Morta) -> None:
        response = client.organisation.teams.with_raw_response.update(
            team_public_id="team_public_id",
            organisation_public_id="organisation_public_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Morta) -> None:
        with client.organisation.teams.with_streaming_response.update(
            team_public_id="team_public_id",
            organisation_public_id="organisation_public_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert team is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Morta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            client.organisation.teams.with_raw_response.update(
                team_public_id="team_public_id",
                organisation_public_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_public_id` but received ''"):
            client.organisation.teams.with_raw_response.update(
                team_public_id="",
                organisation_public_id="organisation_public_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: Morta) -> None:
        team = client.organisation.teams.list(
            "organisation_public_id",
        )
        assert team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: Morta) -> None:
        response = client.organisation.teams.with_raw_response.list(
            "organisation_public_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: Morta) -> None:
        with client.organisation.teams.with_streaming_response.list(
            "organisation_public_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert team is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list(self, client: Morta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            client.organisation.teams.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Morta) -> None:
        team = client.organisation.teams.delete(
            team_public_id="team_public_id",
            organisation_public_id="organisation_public_id",
        )
        assert team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Morta) -> None:
        response = client.organisation.teams.with_raw_response.delete(
            team_public_id="team_public_id",
            organisation_public_id="organisation_public_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = response.parse()
        assert team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Morta) -> None:
        with client.organisation.teams.with_streaming_response.delete(
            team_public_id="team_public_id",
            organisation_public_id="organisation_public_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = response.parse()
            assert team is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Morta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            client.organisation.teams.with_raw_response.delete(
                team_public_id="team_public_id",
                organisation_public_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_public_id` but received ''"):
            client.organisation.teams.with_raw_response.delete(
                team_public_id="",
                organisation_public_id="organisation_public_id",
            )


class TestAsyncTeams:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMorta) -> None:
        team = await async_client.organisation.teams.create(
            "organisation_public_id",
        )
        assert team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMorta) -> None:
        response = await async_client.organisation.teams.with_raw_response.create(
            "organisation_public_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMorta) -> None:
        async with async_client.organisation.teams.with_streaming_response.create(
            "organisation_public_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert team is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncMorta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            await async_client.organisation.teams.with_raw_response.create(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncMorta) -> None:
        team = await async_client.organisation.teams.retrieve(
            team_public_id="team_public_id",
            organisation_public_id="organisation_public_id",
        )
        assert team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncMorta) -> None:
        response = await async_client.organisation.teams.with_raw_response.retrieve(
            team_public_id="team_public_id",
            organisation_public_id="organisation_public_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncMorta) -> None:
        async with async_client.organisation.teams.with_streaming_response.retrieve(
            team_public_id="team_public_id",
            organisation_public_id="organisation_public_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert team is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncMorta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            await async_client.organisation.teams.with_raw_response.retrieve(
                team_public_id="team_public_id",
                organisation_public_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_public_id` but received ''"):
            await async_client.organisation.teams.with_raw_response.retrieve(
                team_public_id="",
                organisation_public_id="organisation_public_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMorta) -> None:
        team = await async_client.organisation.teams.update(
            team_public_id="team_public_id",
            organisation_public_id="organisation_public_id",
        )
        assert team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMorta) -> None:
        response = await async_client.organisation.teams.with_raw_response.update(
            team_public_id="team_public_id",
            organisation_public_id="organisation_public_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMorta) -> None:
        async with async_client.organisation.teams.with_streaming_response.update(
            team_public_id="team_public_id",
            organisation_public_id="organisation_public_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert team is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMorta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            await async_client.organisation.teams.with_raw_response.update(
                team_public_id="team_public_id",
                organisation_public_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_public_id` but received ''"):
            await async_client.organisation.teams.with_raw_response.update(
                team_public_id="",
                organisation_public_id="organisation_public_id",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncMorta) -> None:
        team = await async_client.organisation.teams.list(
            "organisation_public_id",
        )
        assert team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncMorta) -> None:
        response = await async_client.organisation.teams.with_raw_response.list(
            "organisation_public_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncMorta) -> None:
        async with async_client.organisation.teams.with_streaming_response.list(
            "organisation_public_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert team is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list(self, async_client: AsyncMorta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            await async_client.organisation.teams.with_raw_response.list(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMorta) -> None:
        team = await async_client.organisation.teams.delete(
            team_public_id="team_public_id",
            organisation_public_id="organisation_public_id",
        )
        assert team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMorta) -> None:
        response = await async_client.organisation.teams.with_raw_response.delete(
            team_public_id="team_public_id",
            organisation_public_id="organisation_public_id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        team = await response.parse()
        assert team is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMorta) -> None:
        async with async_client.organisation.teams.with_streaming_response.delete(
            team_public_id="team_public_id",
            organisation_public_id="organisation_public_id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            team = await response.parse()
            assert team is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMorta) -> None:
        with pytest.raises(
            ValueError, match=r"Expected a non-empty value for `organisation_public_id` but received ''"
        ):
            await async_client.organisation.teams.with_raw_response.delete(
                team_public_id="team_public_id",
                organisation_public_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `team_public_id` but received ''"):
            await async_client.organisation.teams.with_raw_response.delete(
                team_public_id="",
                organisation_public_id="organisation_public_id",
            )
