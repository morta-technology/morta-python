# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NoneType, NotGiven, not_given
from ..._utils import path_template
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options

__all__ = ["UserResource", "AsyncUserResource"]


class UserResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return UserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return UserResourceWithStreamingResponse(self)

    def delete(
        self,
        user_public_id: str,
        *,
        organisation_public_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Soft delete a user and remove them from all hubs.

        Only organisation admins can
        perform this action.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organisation_public_id:
            raise ValueError(
                f"Expected a non-empty value for `organisation_public_id` but received {organisation_public_id!r}"
            )
        if not user_public_id:
            raise ValueError(f"Expected a non-empty value for `user_public_id` but received {user_public_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/v1/organisation/{organisation_public_id}/user/{user_public_id}",
                organisation_public_id=organisation_public_id,
                user_public_id=user_public_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def allocate_license(
        self,
        user_public_id: str,
        *,
        organisation_public_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Allocate a paid license to a specific user.

        When the team plan flag is enabled
        the user is assigned a seat on the organisation's default team.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organisation_public_id:
            raise ValueError(
                f"Expected a non-empty value for `organisation_public_id` but received {organisation_public_id!r}"
            )
        if not user_public_id:
            raise ValueError(f"Expected a non-empty value for `user_public_id` but received {user_public_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template(
                "/v1/organisation/{organisation_public_id}/user/{user_public_id}/allocate-license",
                organisation_public_id=organisation_public_id,
                user_public_id=user_public_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def remove_license(
        self,
        user_public_id: str,
        *,
        organisation_public_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a paid license from a specific user within the specified organisation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organisation_public_id:
            raise ValueError(
                f"Expected a non-empty value for `organisation_public_id` but received {organisation_public_id!r}"
            )
        if not user_public_id:
            raise ValueError(f"Expected a non-empty value for `user_public_id` but received {user_public_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template(
                "/v1/organisation/{organisation_public_id}/user/{user_public_id}/remove-license",
                organisation_public_id=organisation_public_id,
                user_public_id=user_public_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncUserResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUserResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUserResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUserResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return AsyncUserResourceWithStreamingResponse(self)

    async def delete(
        self,
        user_public_id: str,
        *,
        organisation_public_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Soft delete a user and remove them from all hubs.

        Only organisation admins can
        perform this action.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organisation_public_id:
            raise ValueError(
                f"Expected a non-empty value for `organisation_public_id` but received {organisation_public_id!r}"
            )
        if not user_public_id:
            raise ValueError(f"Expected a non-empty value for `user_public_id` but received {user_public_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/v1/organisation/{organisation_public_id}/user/{user_public_id}",
                organisation_public_id=organisation_public_id,
                user_public_id=user_public_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def allocate_license(
        self,
        user_public_id: str,
        *,
        organisation_public_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Allocate a paid license to a specific user.

        When the team plan flag is enabled
        the user is assigned a seat on the organisation's default team.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organisation_public_id:
            raise ValueError(
                f"Expected a non-empty value for `organisation_public_id` but received {organisation_public_id!r}"
            )
        if not user_public_id:
            raise ValueError(f"Expected a non-empty value for `user_public_id` but received {user_public_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template(
                "/v1/organisation/{organisation_public_id}/user/{user_public_id}/allocate-license",
                organisation_public_id=organisation_public_id,
                user_public_id=user_public_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def remove_license(
        self,
        user_public_id: str,
        *,
        organisation_public_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Remove a paid license from a specific user within the specified organisation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organisation_public_id:
            raise ValueError(
                f"Expected a non-empty value for `organisation_public_id` but received {organisation_public_id!r}"
            )
        if not user_public_id:
            raise ValueError(f"Expected a non-empty value for `user_public_id` but received {user_public_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template(
                "/v1/organisation/{organisation_public_id}/user/{user_public_id}/remove-license",
                organisation_public_id=organisation_public_id,
                user_public_id=user_public_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class UserResourceWithRawResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.delete = to_raw_response_wrapper(
            user.delete,
        )
        self.allocate_license = to_raw_response_wrapper(
            user.allocate_license,
        )
        self.remove_license = to_raw_response_wrapper(
            user.remove_license,
        )


class AsyncUserResourceWithRawResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.delete = async_to_raw_response_wrapper(
            user.delete,
        )
        self.allocate_license = async_to_raw_response_wrapper(
            user.allocate_license,
        )
        self.remove_license = async_to_raw_response_wrapper(
            user.remove_license,
        )


class UserResourceWithStreamingResponse:
    def __init__(self, user: UserResource) -> None:
        self._user = user

        self.delete = to_streamed_response_wrapper(
            user.delete,
        )
        self.allocate_license = to_streamed_response_wrapper(
            user.allocate_license,
        )
        self.remove_license = to_streamed_response_wrapper(
            user.remove_license,
        )


class AsyncUserResourceWithStreamingResponse:
    def __init__(self, user: AsyncUserResource) -> None:
        self._user = user

        self.delete = async_to_streamed_response_wrapper(
            user.delete,
        )
        self.allocate_license = async_to_streamed_response_wrapper(
            user.allocate_license,
        )
        self.remove_license = async_to_streamed_response_wrapper(
            user.remove_license,
        )
