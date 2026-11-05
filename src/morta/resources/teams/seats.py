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

__all__ = ["SeatsResource", "AsyncSeatsResource"]


class SeatsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SeatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return SeatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SeatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return SeatsResourceWithStreamingResponse(self)

    def list(
        self,
        team_public_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Returns team details with all members and seat stats.

        Requires Team Manager,
        Organisation Admin, or Super Admin role.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not team_public_id:
            raise ValueError(f"Expected a non-empty value for `team_public_id` but received {team_public_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/v1/teams/{team_public_id}/seats", team_public_id=team_public_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def assign(
        self,
        team_public_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Assigns a paid seat to a user by email within this team.

        Requires Team Manager,
        Organisation Admin, or Super Admin role.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not team_public_id:
            raise ValueError(f"Expected a non-empty value for `team_public_id` but received {team_public_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/v1/teams/{team_public_id}/seats/assign", team_public_id=team_public_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def revoke(
        self,
        team_public_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Revokes a paid seat from a user within this team.

        Manager cannot revoke own
        seat. Requires Team Manager, Organisation Admin, or Super Admin role.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not team_public_id:
            raise ValueError(f"Expected a non-empty value for `team_public_id` but received {team_public_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            path_template("/v1/teams/{team_public_id}/seats/revoke", team_public_id=team_public_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncSeatsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSeatsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSeatsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSeatsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return AsyncSeatsResourceWithStreamingResponse(self)

    async def list(
        self,
        team_public_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Returns team details with all members and seat stats.

        Requires Team Manager,
        Organisation Admin, or Super Admin role.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not team_public_id:
            raise ValueError(f"Expected a non-empty value for `team_public_id` but received {team_public_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/v1/teams/{team_public_id}/seats", team_public_id=team_public_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def assign(
        self,
        team_public_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Assigns a paid seat to a user by email within this team.

        Requires Team Manager,
        Organisation Admin, or Super Admin role.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not team_public_id:
            raise ValueError(f"Expected a non-empty value for `team_public_id` but received {team_public_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/v1/teams/{team_public_id}/seats/assign", team_public_id=team_public_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def revoke(
        self,
        team_public_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Revokes a paid seat from a user within this team.

        Manager cannot revoke own
        seat. Requires Team Manager, Organisation Admin, or Super Admin role.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not team_public_id:
            raise ValueError(f"Expected a non-empty value for `team_public_id` but received {team_public_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            path_template("/v1/teams/{team_public_id}/seats/revoke", team_public_id=team_public_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class SeatsResourceWithRawResponse:
    def __init__(self, seats: SeatsResource) -> None:
        self._seats = seats

        self.list = to_raw_response_wrapper(
            seats.list,
        )
        self.assign = to_raw_response_wrapper(
            seats.assign,
        )
        self.revoke = to_raw_response_wrapper(
            seats.revoke,
        )


class AsyncSeatsResourceWithRawResponse:
    def __init__(self, seats: AsyncSeatsResource) -> None:
        self._seats = seats

        self.list = async_to_raw_response_wrapper(
            seats.list,
        )
        self.assign = async_to_raw_response_wrapper(
            seats.assign,
        )
        self.revoke = async_to_raw_response_wrapper(
            seats.revoke,
        )


class SeatsResourceWithStreamingResponse:
    def __init__(self, seats: SeatsResource) -> None:
        self._seats = seats

        self.list = to_streamed_response_wrapper(
            seats.list,
        )
        self.assign = to_streamed_response_wrapper(
            seats.assign,
        )
        self.revoke = to_streamed_response_wrapper(
            seats.revoke,
        )


class AsyncSeatsResourceWithStreamingResponse:
    def __init__(self, seats: AsyncSeatsResource) -> None:
        self._seats = seats

        self.list = async_to_streamed_response_wrapper(
            seats.list,
        )
        self.assign = async_to_streamed_response_wrapper(
            seats.assign,
        )
        self.revoke = async_to_streamed_response_wrapper(
            seats.revoke,
        )
