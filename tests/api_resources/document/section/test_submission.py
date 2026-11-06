# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from morta import Morta, AsyncMorta
from tests.utils import assert_matches_type
from morta.types.document.section import (
    SubmissionResetResponse,
    SubmissionCreateResponse,
    SubmissionDeleteResponse,
    SubmissionSubmitResponse,
    SubmissionUpdateResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSubmission:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: Morta) -> None:
        submission = client.document.section.submission.create(
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SubmissionCreateResponse, submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: Morta) -> None:
        submission = client.document.section.submission.create(
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            context={
                "process_public_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "process_section_public_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            enable_submission=True,
            reset_after_submission=True,
        )
        assert_matches_type(SubmissionCreateResponse, submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: Morta) -> None:
        response = client.document.section.submission.with_raw_response.create(
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        submission = response.parse()
        assert_matches_type(SubmissionCreateResponse, submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: Morta) -> None:
        with client.document.section.submission.with_streaming_response.create(
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            submission = response.parse()
            assert_matches_type(SubmissionCreateResponse, submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_create(self, client: Morta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.document.section.submission.with_raw_response.create(
                document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_section_id` but received ''"):
            client.document.section.submission.with_raw_response.create(
                document_section_id="",
                document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: Morta) -> None:
        submission = client.document.section.submission.update(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SubmissionUpdateResponse, submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: Morta) -> None:
        submission = client.document.section.submission.update(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            context={
                "process_public_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "process_section_public_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            enable_submission=True,
            reset_after_submission=True,
        )
        assert_matches_type(SubmissionUpdateResponse, submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: Morta) -> None:
        response = client.document.section.submission.with_raw_response.update(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        submission = response.parse()
        assert_matches_type(SubmissionUpdateResponse, submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: Morta) -> None:
        with client.document.section.submission.with_streaming_response.update(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            submission = response.parse()
            assert_matches_type(SubmissionUpdateResponse, submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: Morta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.document.section.submission.with_raw_response.update(
                submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_id="",
                document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_section_id` but received ''"):
            client.document.section.submission.with_raw_response.update(
                submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_section_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `submission_id` but received ''"):
            client.document.section.submission.with_raw_response.update(
                submission_id="",
                document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: Morta) -> None:
        submission = client.document.section.submission.delete(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SubmissionDeleteResponse, submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: Morta) -> None:
        response = client.document.section.submission.with_raw_response.delete(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        submission = response.parse()
        assert_matches_type(SubmissionDeleteResponse, submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: Morta) -> None:
        with client.document.section.submission.with_streaming_response.delete(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            submission = response.parse()
            assert_matches_type(SubmissionDeleteResponse, submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: Morta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.document.section.submission.with_raw_response.delete(
                submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_id="",
                document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_section_id` but received ''"):
            client.document.section.submission.with_raw_response.delete(
                submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_section_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `submission_id` but received ''"):
            client.document.section.submission.with_raw_response.delete(
                submission_id="",
                document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_reset(self, client: Morta) -> None:
        submission = client.document.section.submission.reset(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SubmissionResetResponse, submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_reset(self, client: Morta) -> None:
        response = client.document.section.submission.with_raw_response.reset(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        submission = response.parse()
        assert_matches_type(SubmissionResetResponse, submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_reset(self, client: Morta) -> None:
        with client.document.section.submission.with_streaming_response.reset(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            submission = response.parse()
            assert_matches_type(SubmissionResetResponse, submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_reset(self, client: Morta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.document.section.submission.with_raw_response.reset(
                submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_id="",
                document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_section_id` but received ''"):
            client.document.section.submission.with_raw_response.reset(
                submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_section_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `submission_id` but received ''"):
            client.document.section.submission.with_raw_response.reset(
                submission_id="",
                document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit(self, client: Morta) -> None:
        submission = client.document.section.submission.submit(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SubmissionSubmitResponse, submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit(self, client: Morta) -> None:
        response = client.document.section.submission.with_raw_response.submit(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        submission = response.parse()
        assert_matches_type(SubmissionSubmitResponse, submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit(self, client: Morta) -> None:
        with client.document.section.submission.with_streaming_response.submit(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            submission = response.parse()
            assert_matches_type(SubmissionSubmitResponse, submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_submit(self, client: Morta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            client.document.section.submission.with_raw_response.submit(
                submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_id="",
                document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_section_id` but received ''"):
            client.document.section.submission.with_raw_response.submit(
                submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_section_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `submission_id` but received ''"):
            client.document.section.submission.with_raw_response.submit(
                submission_id="",
                document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )


class TestAsyncSubmission:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncMorta) -> None:
        submission = await async_client.document.section.submission.create(
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SubmissionCreateResponse, submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncMorta) -> None:
        submission = await async_client.document.section.submission.create(
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            context={
                "process_public_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "process_section_public_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            enable_submission=True,
            reset_after_submission=True,
        )
        assert_matches_type(SubmissionCreateResponse, submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncMorta) -> None:
        response = await async_client.document.section.submission.with_raw_response.create(
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        submission = await response.parse()
        assert_matches_type(SubmissionCreateResponse, submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncMorta) -> None:
        async with async_client.document.section.submission.with_streaming_response.create(
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            submission = await response.parse()
            assert_matches_type(SubmissionCreateResponse, submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_create(self, async_client: AsyncMorta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.document.section.submission.with_raw_response.create(
                document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_section_id` but received ''"):
            await async_client.document.section.submission.with_raw_response.create(
                document_section_id="",
                document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncMorta) -> None:
        submission = await async_client.document.section.submission.update(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SubmissionUpdateResponse, submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncMorta) -> None:
        submission = await async_client.document.section.submission.update(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            context={
                "process_public_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "process_section_public_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                "project_id": "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            },
            enable_submission=True,
            reset_after_submission=True,
        )
        assert_matches_type(SubmissionUpdateResponse, submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncMorta) -> None:
        response = await async_client.document.section.submission.with_raw_response.update(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        submission = await response.parse()
        assert_matches_type(SubmissionUpdateResponse, submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncMorta) -> None:
        async with async_client.document.section.submission.with_streaming_response.update(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            submission = await response.parse()
            assert_matches_type(SubmissionUpdateResponse, submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncMorta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.document.section.submission.with_raw_response.update(
                submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_id="",
                document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_section_id` but received ''"):
            await async_client.document.section.submission.with_raw_response.update(
                submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_section_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `submission_id` but received ''"):
            await async_client.document.section.submission.with_raw_response.update(
                submission_id="",
                document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncMorta) -> None:
        submission = await async_client.document.section.submission.delete(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SubmissionDeleteResponse, submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncMorta) -> None:
        response = await async_client.document.section.submission.with_raw_response.delete(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        submission = await response.parse()
        assert_matches_type(SubmissionDeleteResponse, submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncMorta) -> None:
        async with async_client.document.section.submission.with_streaming_response.delete(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            submission = await response.parse()
            assert_matches_type(SubmissionDeleteResponse, submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncMorta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.document.section.submission.with_raw_response.delete(
                submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_id="",
                document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_section_id` but received ''"):
            await async_client.document.section.submission.with_raw_response.delete(
                submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_section_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `submission_id` but received ''"):
            await async_client.document.section.submission.with_raw_response.delete(
                submission_id="",
                document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_reset(self, async_client: AsyncMorta) -> None:
        submission = await async_client.document.section.submission.reset(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SubmissionResetResponse, submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_reset(self, async_client: AsyncMorta) -> None:
        response = await async_client.document.section.submission.with_raw_response.reset(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        submission = await response.parse()
        assert_matches_type(SubmissionResetResponse, submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_reset(self, async_client: AsyncMorta) -> None:
        async with async_client.document.section.submission.with_streaming_response.reset(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            submission = await response.parse()
            assert_matches_type(SubmissionResetResponse, submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_reset(self, async_client: AsyncMorta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.document.section.submission.with_raw_response.reset(
                submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_id="",
                document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_section_id` but received ''"):
            await async_client.document.section.submission.with_raw_response.reset(
                submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_section_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `submission_id` but received ''"):
            await async_client.document.section.submission.with_raw_response.reset(
                submission_id="",
                document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit(self, async_client: AsyncMorta) -> None:
        submission = await async_client.document.section.submission.submit(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(SubmissionSubmitResponse, submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncMorta) -> None:
        response = await async_client.document.section.submission.with_raw_response.submit(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        submission = await response.parse()
        assert_matches_type(SubmissionSubmitResponse, submission, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncMorta) -> None:
        async with async_client.document.section.submission.with_streaming_response.submit(
            submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            submission = await response.parse()
            assert_matches_type(SubmissionSubmitResponse, submission, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_submit(self, async_client: AsyncMorta) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_id` but received ''"):
            await async_client.document.section.submission.with_raw_response.submit(
                submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_id="",
                document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `document_section_id` but received ''"):
            await async_client.document.section.submission.with_raw_response.submit(
                submission_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_section_id="",
            )

        with pytest.raises(ValueError, match=r"Expected a non-empty value for `submission_id` but received ''"):
            await async_client.document.section.submission.with_raw_response.submit(
                submission_id="",
                document_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
                document_section_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            )
