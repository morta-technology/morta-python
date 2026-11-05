# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

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
from ...types.hub import folder_move_params, folder_create_params, folder_update_params
from ..._base_client import make_request_options
from ...types.hub.folder_move_response import FolderMoveResponse
from ...types.hub.folder_create_response import FolderCreateResponse
from ...types.hub.folder_delete_response import FolderDeleteResponse
from ...types.hub.folder_update_response import FolderUpdateResponse

__all__ = ["FoldersResource", "AsyncFoldersResource"]


class FoldersResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FoldersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return FoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FoldersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return FoldersResourceWithStreamingResponse(self)

    def create(
        self,
        hub_id: str,
        *,
        name: str,
        parent_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderCreateResponse:
        """Create a folder in the hub sidebar, at the top level or inside `parentId`.

        Hub
        Owners only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hub_id:
            raise ValueError(f"Expected a non-empty value for `hub_id` but received {hub_id!r}")
        return self._post(
            path_template("/v1/hub/{hub_id}/folders", hub_id=hub_id),
            body=maybe_transform(
                {
                    "name": name,
                    "parent_id": parent_id,
                },
                folder_create_params.FolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderCreateResponse,
        )

    def update(
        self,
        folder_id: str,
        *,
        hub_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderUpdateResponse:
        """Rename a folder in the hub sidebar.

        Hub Owners only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hub_id:
            raise ValueError(f"Expected a non-empty value for `hub_id` but received {hub_id!r}")
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._put(
            path_template("/v1/hub/{hub_id}/folders/{folder_id}", hub_id=hub_id, folder_id=folder_id),
            body=maybe_transform({"name": name}, folder_update_params.FolderUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderUpdateResponse,
        )

    def delete(
        self,
        folder_id: str,
        *,
        hub_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderDeleteResponse:
        """Delete a folder from the hub sidebar.

        Its documents, tables and subfolders move
        up to its parent; nothing inside it is deleted. Hub Owners only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hub_id:
            raise ValueError(f"Expected a non-empty value for `hub_id` but received {hub_id!r}")
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return self._delete(
            path_template("/v1/hub/{hub_id}/folders/{folder_id}", hub_id=hub_id, folder_id=folder_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderDeleteResponse,
        )

    def move(
        self,
        hub_id: str,
        *,
        items: Iterable[folder_move_params.Item],
        index: Optional[int] | Omit = omit,
        parent_folder_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderMoveResponse:
        """
        Move folders, documents and tables into `parentFolderId` (the hub's top level
        when null) at `index` (appended when null). Validates every item first, so a bad
        item moves nothing. Hub Owners can move anything; other hub members can move
        only documents and tables they own (not folders), into the top level or a folder
        they can see. A target folder or item the caller can't see in their sidebar is
        answered with 404, exactly like an id that doesn't exist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hub_id:
            raise ValueError(f"Expected a non-empty value for `hub_id` but received {hub_id!r}")
        return self._post(
            path_template("/v1/hub/{hub_id}/folders/move", hub_id=hub_id),
            body=maybe_transform(
                {
                    "items": items,
                    "index": index,
                    "parent_folder_id": parent_folder_id,
                },
                folder_move_params.FolderMoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderMoveResponse,
        )


class AsyncFoldersResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFoldersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFoldersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return AsyncFoldersResourceWithStreamingResponse(self)

    async def create(
        self,
        hub_id: str,
        *,
        name: str,
        parent_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderCreateResponse:
        """Create a folder in the hub sidebar, at the top level or inside `parentId`.

        Hub
        Owners only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hub_id:
            raise ValueError(f"Expected a non-empty value for `hub_id` but received {hub_id!r}")
        return await self._post(
            path_template("/v1/hub/{hub_id}/folders", hub_id=hub_id),
            body=await async_maybe_transform(
                {
                    "name": name,
                    "parent_id": parent_id,
                },
                folder_create_params.FolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderCreateResponse,
        )

    async def update(
        self,
        folder_id: str,
        *,
        hub_id: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderUpdateResponse:
        """Rename a folder in the hub sidebar.

        Hub Owners only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hub_id:
            raise ValueError(f"Expected a non-empty value for `hub_id` but received {hub_id!r}")
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._put(
            path_template("/v1/hub/{hub_id}/folders/{folder_id}", hub_id=hub_id, folder_id=folder_id),
            body=await async_maybe_transform({"name": name}, folder_update_params.FolderUpdateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderUpdateResponse,
        )

    async def delete(
        self,
        folder_id: str,
        *,
        hub_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderDeleteResponse:
        """Delete a folder from the hub sidebar.

        Its documents, tables and subfolders move
        up to its parent; nothing inside it is deleted. Hub Owners only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hub_id:
            raise ValueError(f"Expected a non-empty value for `hub_id` but received {hub_id!r}")
        if not folder_id:
            raise ValueError(f"Expected a non-empty value for `folder_id` but received {folder_id!r}")
        return await self._delete(
            path_template("/v1/hub/{hub_id}/folders/{folder_id}", hub_id=hub_id, folder_id=folder_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderDeleteResponse,
        )

    async def move(
        self,
        hub_id: str,
        *,
        items: Iterable[folder_move_params.Item],
        index: Optional[int] | Omit = omit,
        parent_folder_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderMoveResponse:
        """
        Move folders, documents and tables into `parentFolderId` (the hub's top level
        when null) at `index` (appended when null). Validates every item first, so a bad
        item moves nothing. Hub Owners can move anything; other hub members can move
        only documents and tables they own (not folders), into the top level or a folder
        they can see. A target folder or item the caller can't see in their sidebar is
        answered with 404, exactly like an id that doesn't exist.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hub_id:
            raise ValueError(f"Expected a non-empty value for `hub_id` but received {hub_id!r}")
        return await self._post(
            path_template("/v1/hub/{hub_id}/folders/move", hub_id=hub_id),
            body=await async_maybe_transform(
                {
                    "items": items,
                    "index": index,
                    "parent_folder_id": parent_folder_id,
                },
                folder_move_params.FolderMoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderMoveResponse,
        )


class FoldersResourceWithRawResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

        self.create = to_raw_response_wrapper(
            folders.create,
        )
        self.update = to_raw_response_wrapper(
            folders.update,
        )
        self.delete = to_raw_response_wrapper(
            folders.delete,
        )
        self.move = to_raw_response_wrapper(
            folders.move,
        )


class AsyncFoldersResourceWithRawResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

        self.create = async_to_raw_response_wrapper(
            folders.create,
        )
        self.update = async_to_raw_response_wrapper(
            folders.update,
        )
        self.delete = async_to_raw_response_wrapper(
            folders.delete,
        )
        self.move = async_to_raw_response_wrapper(
            folders.move,
        )


class FoldersResourceWithStreamingResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

        self.create = to_streamed_response_wrapper(
            folders.create,
        )
        self.update = to_streamed_response_wrapper(
            folders.update,
        )
        self.delete = to_streamed_response_wrapper(
            folders.delete,
        )
        self.move = to_streamed_response_wrapper(
            folders.move,
        )


class AsyncFoldersResourceWithStreamingResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

        self.create = async_to_streamed_response_wrapper(
            folders.create,
        )
        self.update = async_to_streamed_response_wrapper(
            folders.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            folders.delete,
        )
        self.move = async_to_streamed_response_wrapper(
            folders.move,
        )
