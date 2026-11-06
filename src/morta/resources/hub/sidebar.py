# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.hub import sidebar_containers_params
from ..._base_client import make_request_options
from ...types.hub.sidebar_containers_response import SidebarContainersResponse

__all__ = ["SidebarResource", "AsyncSidebarResource"]


class SidebarResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SidebarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return SidebarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SidebarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return SidebarResourceWithStreamingResponse(self)

    def containers(
        self,
        hub_id: str,
        *,
        containers: SequenceNotStr[Optional[str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SidebarContainersResponse:
        """
        Read the direct child folders and the documents and tables of up to 50 sidebar
        containers: folders, or the hub's top level (null). Entries have the same shape
        as the hub's `hubFolders` and `sidebarResources`. A container that doesn't
        exist, or that isn't in your sidebar, is listed in `removed` instead. Same
        access rules as getting the hub. Lets a client that sees every folder re-read
        only the folders a `resources_updated` event names.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hub_id:
            raise ValueError(f"Expected a non-empty value for `hub_id` but received {hub_id!r}")
        return self._post(
            path_template("/v1/hub/{hub_id}/sidebar/containers", hub_id=hub_id),
            body=maybe_transform({"containers": containers}, sidebar_containers_params.SidebarContainersParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SidebarContainersResponse,
        )


class AsyncSidebarResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSidebarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSidebarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSidebarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return AsyncSidebarResourceWithStreamingResponse(self)

    async def containers(
        self,
        hub_id: str,
        *,
        containers: SequenceNotStr[Optional[str]],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SidebarContainersResponse:
        """
        Read the direct child folders and the documents and tables of up to 50 sidebar
        containers: folders, or the hub's top level (null). Entries have the same shape
        as the hub's `hubFolders` and `sidebarResources`. A container that doesn't
        exist, or that isn't in your sidebar, is listed in `removed` instead. Same
        access rules as getting the hub. Lets a client that sees every folder re-read
        only the folders a `resources_updated` event names.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hub_id:
            raise ValueError(f"Expected a non-empty value for `hub_id` but received {hub_id!r}")
        return await self._post(
            path_template("/v1/hub/{hub_id}/sidebar/containers", hub_id=hub_id),
            body=await async_maybe_transform(
                {"containers": containers}, sidebar_containers_params.SidebarContainersParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SidebarContainersResponse,
        )


class SidebarResourceWithRawResponse:
    def __init__(self, sidebar: SidebarResource) -> None:
        self._sidebar = sidebar

        self.containers = to_raw_response_wrapper(
            sidebar.containers,
        )


class AsyncSidebarResourceWithRawResponse:
    def __init__(self, sidebar: AsyncSidebarResource) -> None:
        self._sidebar = sidebar

        self.containers = async_to_raw_response_wrapper(
            sidebar.containers,
        )


class SidebarResourceWithStreamingResponse:
    def __init__(self, sidebar: SidebarResource) -> None:
        self._sidebar = sidebar

        self.containers = to_streamed_response_wrapper(
            sidebar.containers,
        )


class AsyncSidebarResourceWithStreamingResponse:
    def __init__(self, sidebar: AsyncSidebarResource) -> None:
        self._sidebar = sidebar

        self.containers = async_to_streamed_response_wrapper(
            sidebar.containers,
        )
