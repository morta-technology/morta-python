# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.user import notification_list_params, notification_update_params
from ..._base_client import make_request_options
from ...types.user.notification_list_response import NotificationListResponse
from ...types.user.notification_update_response import NotificationUpdateResponse
from ...types.user.notification_read_all_response import NotificationReadAllResponse

__all__ = ["NotificationsResource", "AsyncNotificationsResource"]


class NotificationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return NotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return NotificationsResourceWithStreamingResponse(self)

    def update(
        self,
        notification_id: str,
        *,
        dismissed: bool | Omit = omit,
        read: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationUpdateResponse:
        """
        Mark one of the current user's notifications read/unread or dismissed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not notification_id:
            raise ValueError(f"Expected a non-empty value for `notification_id` but received {notification_id!r}")
        return self._patch(
            path_template("/v1/user/notifications/{notification_id}", notification_id=notification_id),
            body=maybe_transform(
                {
                    "dismissed": dismissed,
                    "read": read,
                },
                notification_update_params.NotificationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationUpdateResponse,
        )

    def list(
        self,
        *,
        next_page_token: str | Omit = omit,
        page: int | Omit = omit,
        size: int | Omit = omit,
        unread_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationListResponse:
        """
        Paginated notification feed for the current user, newest first

        Args:
          next_page_token: Opaque token for the next page from a previous response

          page: Page number (ignored when nextPageToken is given)

          size: Page size (max 100)

          unread_only: Only return unread notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/user/notifications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "next_page_token": next_page_token,
                        "page": page,
                        "size": size,
                        "unread_only": unread_only,
                    },
                    notification_list_params.NotificationListParams,
                ),
            ),
            cast_to=NotificationListResponse,
        )

    def read_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationReadAllResponse:
        """Mark every unread notification of the current user as read"""
        return self._post(
            "/v1/user/notifications/read-all",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationReadAllResponse,
        )


class AsyncNotificationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNotificationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNotificationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNotificationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return AsyncNotificationsResourceWithStreamingResponse(self)

    async def update(
        self,
        notification_id: str,
        *,
        dismissed: bool | Omit = omit,
        read: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationUpdateResponse:
        """
        Mark one of the current user's notifications read/unread or dismissed

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not notification_id:
            raise ValueError(f"Expected a non-empty value for `notification_id` but received {notification_id!r}")
        return await self._patch(
            path_template("/v1/user/notifications/{notification_id}", notification_id=notification_id),
            body=await async_maybe_transform(
                {
                    "dismissed": dismissed,
                    "read": read,
                },
                notification_update_params.NotificationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationUpdateResponse,
        )

    async def list(
        self,
        *,
        next_page_token: str | Omit = omit,
        page: int | Omit = omit,
        size: int | Omit = omit,
        unread_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationListResponse:
        """
        Paginated notification feed for the current user, newest first

        Args:
          next_page_token: Opaque token for the next page from a previous response

          page: Page number (ignored when nextPageToken is given)

          size: Page size (max 100)

          unread_only: Only return unread notifications

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/user/notifications",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "next_page_token": next_page_token,
                        "page": page,
                        "size": size,
                        "unread_only": unread_only,
                    },
                    notification_list_params.NotificationListParams,
                ),
            ),
            cast_to=NotificationListResponse,
        )

    async def read_all(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NotificationReadAllResponse:
        """Mark every unread notification of the current user as read"""
        return await self._post(
            "/v1/user/notifications/read-all",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NotificationReadAllResponse,
        )


class NotificationsResourceWithRawResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.update = to_raw_response_wrapper(
            notifications.update,
        )
        self.list = to_raw_response_wrapper(
            notifications.list,
        )
        self.read_all = to_raw_response_wrapper(
            notifications.read_all,
        )


class AsyncNotificationsResourceWithRawResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.update = async_to_raw_response_wrapper(
            notifications.update,
        )
        self.list = async_to_raw_response_wrapper(
            notifications.list,
        )
        self.read_all = async_to_raw_response_wrapper(
            notifications.read_all,
        )


class NotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: NotificationsResource) -> None:
        self._notifications = notifications

        self.update = to_streamed_response_wrapper(
            notifications.update,
        )
        self.list = to_streamed_response_wrapper(
            notifications.list,
        )
        self.read_all = to_streamed_response_wrapper(
            notifications.read_all,
        )


class AsyncNotificationsResourceWithStreamingResponse:
    def __init__(self, notifications: AsyncNotificationsResource) -> None:
        self._notifications = notifications

        self.update = async_to_streamed_response_wrapper(
            notifications.update,
        )
        self.list = async_to_streamed_response_wrapper(
            notifications.list,
        )
        self.read_all = async_to_streamed_response_wrapper(
            notifications.read_all,
        )
