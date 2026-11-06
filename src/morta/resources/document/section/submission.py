# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.document.section import submission_create_params, submission_update_params
from ....types.base_request_context_param import BaseRequestContextParam
from ....types.document.section.submission_reset_response import SubmissionResetResponse
from ....types.document.section.submission_create_response import SubmissionCreateResponse
from ....types.document.section.submission_delete_response import SubmissionDeleteResponse
from ....types.document.section.submission_submit_response import SubmissionSubmitResponse
from ....types.document.section.submission_update_response import SubmissionUpdateResponse

__all__ = ["SubmissionResource", "AsyncSubmissionResource"]


class SubmissionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SubmissionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return SubmissionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SubmissionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return SubmissionResourceWithStreamingResponse(self)

    def create(
        self,
        document_section_id: str,
        *,
        document_id: str,
        context: BaseRequestContextParam | Omit = omit,
        enable_submission: bool | Omit = omit,
        reset_after_submission: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubmissionCreateResponse:
        """
        Create the submission settings an embedded table in a document section points at
        with its submissionId. Requires the owner role.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        if not document_section_id:
            raise ValueError(
                f"Expected a non-empty value for `document_section_id` but received {document_section_id!r}"
            )
        return self._post(
            path_template(
                "/v1/document/{document_id}/section/{document_section_id}/submission",
                document_id=document_id,
                document_section_id=document_section_id,
            ),
            body=maybe_transform(
                {
                    "context": context,
                    "enable_submission": enable_submission,
                    "reset_after_submission": reset_after_submission,
                },
                submission_create_params.SubmissionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubmissionCreateResponse,
        )

    def update(
        self,
        submission_id: str,
        *,
        document_id: str,
        document_section_id: str,
        context: BaseRequestContextParam | Omit = omit,
        enable_submission: Optional[bool] | Omit = omit,
        reset_after_submission: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubmissionUpdateResponse:
        """
        Change whether an embedded table requires submission and whether it resets after
        each submission. Requires the owner role. Emits process.response_updated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        if not document_section_id:
            raise ValueError(
                f"Expected a non-empty value for `document_section_id` but received {document_section_id!r}"
            )
        if not submission_id:
            raise ValueError(f"Expected a non-empty value for `submission_id` but received {submission_id!r}")
        return self._put(
            path_template(
                "/v1/document/{document_id}/section/{document_section_id}/submission/{submission_id}",
                document_id=document_id,
                document_section_id=document_section_id,
                submission_id=submission_id,
            ),
            body=maybe_transform(
                {
                    "context": context,
                    "enable_submission": enable_submission,
                    "reset_after_submission": reset_after_submission,
                },
                submission_update_params.SubmissionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubmissionUpdateResponse,
        )

    def delete(
        self,
        submission_id: str,
        *,
        document_id: str,
        document_section_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubmissionDeleteResponse:
        """
        Stop requiring submission for an embedded table by removing the submission id
        from the embed and deleting the submission. Requires the owner role. Emits
        process.response_deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        if not document_section_id:
            raise ValueError(
                f"Expected a non-empty value for `document_section_id` but received {document_section_id!r}"
            )
        if not submission_id:
            raise ValueError(f"Expected a non-empty value for `submission_id` but received {submission_id!r}")
        return self._delete(
            path_template(
                "/v1/document/{document_id}/section/{document_section_id}/submission/{submission_id}",
                document_id=document_id,
                document_section_id=document_section_id,
                submission_id=submission_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubmissionDeleteResponse,
        )

    def reset(
        self,
        submission_id: str,
        *,
        document_id: str,
        document_section_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubmissionResetResponse:
        """Reopen a submitted embedded table.

        Only the user who submitted it or a document
        owner can reset it. Emits process.response_reset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        if not document_section_id:
            raise ValueError(
                f"Expected a non-empty value for `document_section_id` but received {document_section_id!r}"
            )
        if not submission_id:
            raise ValueError(f"Expected a non-empty value for `submission_id` but received {submission_id!r}")
        return self._put(
            path_template(
                "/v1/document/{document_id}/section/{document_section_id}/submission/{submission_id}/reset",
                document_id=document_id,
                document_section_id=document_section_id,
                submission_id=submission_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubmissionResetResponse,
        )

    def submit(
        self,
        submission_id: str,
        *,
        document_id: str,
        document_section_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubmissionSubmitResponse:
        """Submit an embedded table, locking it until it is reset.

        Requires the contributor
        role. Emits process.response_submitted, then resets the submission straight away
        if it resets after each submission.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        if not document_section_id:
            raise ValueError(
                f"Expected a non-empty value for `document_section_id` but received {document_section_id!r}"
            )
        if not submission_id:
            raise ValueError(f"Expected a non-empty value for `submission_id` but received {submission_id!r}")
        return self._put(
            path_template(
                "/v1/document/{document_id}/section/{document_section_id}/submission/{submission_id}/submit",
                document_id=document_id,
                document_section_id=document_section_id,
                submission_id=submission_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubmissionSubmitResponse,
        )


class AsyncSubmissionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSubmissionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSubmissionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSubmissionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return AsyncSubmissionResourceWithStreamingResponse(self)

    async def create(
        self,
        document_section_id: str,
        *,
        document_id: str,
        context: BaseRequestContextParam | Omit = omit,
        enable_submission: bool | Omit = omit,
        reset_after_submission: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubmissionCreateResponse:
        """
        Create the submission settings an embedded table in a document section points at
        with its submissionId. Requires the owner role.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        if not document_section_id:
            raise ValueError(
                f"Expected a non-empty value for `document_section_id` but received {document_section_id!r}"
            )
        return await self._post(
            path_template(
                "/v1/document/{document_id}/section/{document_section_id}/submission",
                document_id=document_id,
                document_section_id=document_section_id,
            ),
            body=await async_maybe_transform(
                {
                    "context": context,
                    "enable_submission": enable_submission,
                    "reset_after_submission": reset_after_submission,
                },
                submission_create_params.SubmissionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubmissionCreateResponse,
        )

    async def update(
        self,
        submission_id: str,
        *,
        document_id: str,
        document_section_id: str,
        context: BaseRequestContextParam | Omit = omit,
        enable_submission: Optional[bool] | Omit = omit,
        reset_after_submission: Optional[bool] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubmissionUpdateResponse:
        """
        Change whether an embedded table requires submission and whether it resets after
        each submission. Requires the owner role. Emits process.response_updated.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        if not document_section_id:
            raise ValueError(
                f"Expected a non-empty value for `document_section_id` but received {document_section_id!r}"
            )
        if not submission_id:
            raise ValueError(f"Expected a non-empty value for `submission_id` but received {submission_id!r}")
        return await self._put(
            path_template(
                "/v1/document/{document_id}/section/{document_section_id}/submission/{submission_id}",
                document_id=document_id,
                document_section_id=document_section_id,
                submission_id=submission_id,
            ),
            body=await async_maybe_transform(
                {
                    "context": context,
                    "enable_submission": enable_submission,
                    "reset_after_submission": reset_after_submission,
                },
                submission_update_params.SubmissionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubmissionUpdateResponse,
        )

    async def delete(
        self,
        submission_id: str,
        *,
        document_id: str,
        document_section_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubmissionDeleteResponse:
        """
        Stop requiring submission for an embedded table by removing the submission id
        from the embed and deleting the submission. Requires the owner role. Emits
        process.response_deleted.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        if not document_section_id:
            raise ValueError(
                f"Expected a non-empty value for `document_section_id` but received {document_section_id!r}"
            )
        if not submission_id:
            raise ValueError(f"Expected a non-empty value for `submission_id` but received {submission_id!r}")
        return await self._delete(
            path_template(
                "/v1/document/{document_id}/section/{document_section_id}/submission/{submission_id}",
                document_id=document_id,
                document_section_id=document_section_id,
                submission_id=submission_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubmissionDeleteResponse,
        )

    async def reset(
        self,
        submission_id: str,
        *,
        document_id: str,
        document_section_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubmissionResetResponse:
        """Reopen a submitted embedded table.

        Only the user who submitted it or a document
        owner can reset it. Emits process.response_reset.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        if not document_section_id:
            raise ValueError(
                f"Expected a non-empty value for `document_section_id` but received {document_section_id!r}"
            )
        if not submission_id:
            raise ValueError(f"Expected a non-empty value for `submission_id` but received {submission_id!r}")
        return await self._put(
            path_template(
                "/v1/document/{document_id}/section/{document_section_id}/submission/{submission_id}/reset",
                document_id=document_id,
                document_section_id=document_section_id,
                submission_id=submission_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubmissionResetResponse,
        )

    async def submit(
        self,
        submission_id: str,
        *,
        document_id: str,
        document_section_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SubmissionSubmitResponse:
        """Submit an embedded table, locking it until it is reset.

        Requires the contributor
        role. Emits process.response_submitted, then resets the submission straight away
        if it resets after each submission.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        if not document_section_id:
            raise ValueError(
                f"Expected a non-empty value for `document_section_id` but received {document_section_id!r}"
            )
        if not submission_id:
            raise ValueError(f"Expected a non-empty value for `submission_id` but received {submission_id!r}")
        return await self._put(
            path_template(
                "/v1/document/{document_id}/section/{document_section_id}/submission/{submission_id}/submit",
                document_id=document_id,
                document_section_id=document_section_id,
                submission_id=submission_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SubmissionSubmitResponse,
        )


class SubmissionResourceWithRawResponse:
    def __init__(self, submission: SubmissionResource) -> None:
        self._submission = submission

        self.create = to_raw_response_wrapper(
            submission.create,
        )
        self.update = to_raw_response_wrapper(
            submission.update,
        )
        self.delete = to_raw_response_wrapper(
            submission.delete,
        )
        self.reset = to_raw_response_wrapper(
            submission.reset,
        )
        self.submit = to_raw_response_wrapper(
            submission.submit,
        )


class AsyncSubmissionResourceWithRawResponse:
    def __init__(self, submission: AsyncSubmissionResource) -> None:
        self._submission = submission

        self.create = async_to_raw_response_wrapper(
            submission.create,
        )
        self.update = async_to_raw_response_wrapper(
            submission.update,
        )
        self.delete = async_to_raw_response_wrapper(
            submission.delete,
        )
        self.reset = async_to_raw_response_wrapper(
            submission.reset,
        )
        self.submit = async_to_raw_response_wrapper(
            submission.submit,
        )


class SubmissionResourceWithStreamingResponse:
    def __init__(self, submission: SubmissionResource) -> None:
        self._submission = submission

        self.create = to_streamed_response_wrapper(
            submission.create,
        )
        self.update = to_streamed_response_wrapper(
            submission.update,
        )
        self.delete = to_streamed_response_wrapper(
            submission.delete,
        )
        self.reset = to_streamed_response_wrapper(
            submission.reset,
        )
        self.submit = to_streamed_response_wrapper(
            submission.submit,
        )


class AsyncSubmissionResourceWithStreamingResponse:
    def __init__(self, submission: AsyncSubmissionResource) -> None:
        self._submission = submission

        self.create = async_to_streamed_response_wrapper(
            submission.create,
        )
        self.update = async_to_streamed_response_wrapper(
            submission.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            submission.delete,
        )
        self.reset = async_to_streamed_response_wrapper(
            submission.reset,
        )
        self.submit = async_to_streamed_response_wrapper(
            submission.submit,
        )
