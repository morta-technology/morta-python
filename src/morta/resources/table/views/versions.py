# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.table.views import version_create_params, version_update_params, version_restore_params
from ....types.table.views.version_list_response import VersionListResponse
from ....types.table.views.version_create_response import VersionCreateResponse
from ....types.table.views.version_update_response import VersionUpdateResponse
from ....types.table.views.version_restore_response import VersionRestoreResponse
from ....types.table.views.version_retrieve_response import VersionRetrieveResponse
from ....types.table.views.version_delete_unpublished_response import VersionDeleteUnpublishedResponse

__all__ = ["VersionsResource", "AsyncVersionsResource"]


class VersionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> VersionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return VersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> VersionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return VersionsResourceWithStreamingResponse(self)

    def create(
        self,
        view_id: str,
        *,
        html: str,
        publish: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionCreateResponse:
        """
        Save HTML as the newest version of a Custom View's page, held to the same checks
        as MortaAI's pages, and with publish, publish it straight away (for example to
        copy a template hub's page to project hubs). A page binds its own table's
        columns by their IDs, so a page copied from another table needs each column ID
        swapped for the ID of this table's column of the same name (GET
        /v1/table/{id}/columns lists them); one that still binds another table's columns
        is refused, naming the swaps. The table's owners see the newest version;
        everyone else sees the published one. Publishing is logged as a view update.
        Only Owners of the table can add one.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return self._post(
            path_template("/v1/table/views/{view_id}/versions", view_id=view_id),
            body=maybe_transform(
                {
                    "html": html,
                    "publish": publish,
                },
                version_create_params.VersionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionCreateResponse,
        )

    def retrieve(
        self,
        version_id: str,
        *,
        view_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionRetrieveResponse:
        """One version of a Custom View's page, with its HTML.

        Only Owners of the table can
        read it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        return self._get(
            path_template("/v1/table/views/{view_id}/versions/{version_id}", view_id=view_id, version_id=version_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionRetrieveResponse,
        )

    def update(
        self,
        version_id: str,
        *,
        view_id: str,
        summary: Optional[str] | Omit = omit,
        thumbnail: str | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionUpdateResponse:
        """
        Set a version's title (at most 80 characters) or description of its changes (at
        most 300), or both, shown with it in the view's Versions list in place of what
        MortaAI wrote; empty or null clears one. Or set its thumbnail, a small picture
        of its page shown with it in the list, which the webapp takes the first time an
        owner's browser shows the version, as a PNG, JPEG or WebP data URL of at most
        120,000 characters (GET /v1/table/views/{viewId}/versions/{versionId}/thumbnail
        returns the image). A version keeps its first picture, so once it has one a
        thumbnail changes nothing. Only Owners of the table can set them.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        return self._put(
            path_template("/v1/table/views/{view_id}/versions/{version_id}", view_id=view_id, version_id=version_id),
            body=maybe_transform(
                {
                    "summary": summary,
                    "thumbnail": thumbnail,
                    "title": title,
                },
                version_update_params.VersionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionUpdateResponse,
        )

    def list(
        self,
        view_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionListResponse:
        """
        Every version of a Custom View's page kept, newest first, without their HTML.
        Every save of the page adds one; the newest 50 are kept, plus the published one
        if it's older. Only Owners of the table can list them.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return self._get(
            path_template("/v1/table/views/{view_id}/versions", view_id=view_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionListResponse,
        )

    def delete(
        self,
        version_id: str,
        *,
        view_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete one version of a Custom View's page for good.

        The published version can't
        be deleted, as it's the page everyone sees; publish another first. Deleting the
        newest makes the one before it the newest, which the table's owners then see.
        Only Owners of the table can delete one.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/table/views/{view_id}/versions/{version_id}", view_id=view_id, version_id=version_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def delete_unpublished(
        self,
        view_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionDeleteUnpublishedResponse:
        """
        Delete every version of a Custom View's page newer than the published one (every
        version, when none is published), so the table's owners see the published page
        again. Every version saved since the last publish is deleted for good, whether
        MortaAI or the API saved it; the published version and older ones stay. Only
        Owners of the table can discard them.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return self._delete(
            path_template("/v1/table/views/{view_id}/versions/unpublished", view_id=view_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionDeleteUnpublishedResponse,
        )

    def restore(
        self,
        version_id: str,
        *,
        view_id: str,
        delete_newer: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionRestoreResponse:
        """Make an older version the page again.

        It's copied to the top as the newest
        version and published, with its title, description and picture, so the table's
        owners and MortaAI carry on from it. The versions made after it stay below as
        history, or with deleteNewer are deleted for good (the one that was published
        too). Logged as a view update. Only Owners of the table can restore one.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        return self._post(
            path_template(
                "/v1/table/views/{view_id}/versions/{version_id}/restore", view_id=view_id, version_id=version_id
            ),
            body=maybe_transform({"delete_newer": delete_newer}, version_restore_params.VersionRestoreParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionRestoreResponse,
        )

    def retrieve_thumbnail(
        self,
        version_id: str,
        *,
        view_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        The small picture of a version's page shown with it in the view's Versions list,
        as a PNG, JPEG or WebP image (set with thumbnail on PUT
        /v1/table/views/{viewId}/versions/{versionId}). A version's picture doesn't
        change once set, so the browser keeps it for a day. Only Owners of the table can
        read it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        extra_headers = {"Accept": "image/jpeg", **(extra_headers or {})}
        return self._get(
            path_template(
                "/v1/table/views/{view_id}/versions/{version_id}/thumbnail", view_id=view_id, version_id=version_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncVersionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncVersionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncVersionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncVersionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return AsyncVersionsResourceWithStreamingResponse(self)

    async def create(
        self,
        view_id: str,
        *,
        html: str,
        publish: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionCreateResponse:
        """
        Save HTML as the newest version of a Custom View's page, held to the same checks
        as MortaAI's pages, and with publish, publish it straight away (for example to
        copy a template hub's page to project hubs). A page binds its own table's
        columns by their IDs, so a page copied from another table needs each column ID
        swapped for the ID of this table's column of the same name (GET
        /v1/table/{id}/columns lists them); one that still binds another table's columns
        is refused, naming the swaps. The table's owners see the newest version;
        everyone else sees the published one. Publishing is logged as a view update.
        Only Owners of the table can add one.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return await self._post(
            path_template("/v1/table/views/{view_id}/versions", view_id=view_id),
            body=await async_maybe_transform(
                {
                    "html": html,
                    "publish": publish,
                },
                version_create_params.VersionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionCreateResponse,
        )

    async def retrieve(
        self,
        version_id: str,
        *,
        view_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionRetrieveResponse:
        """One version of a Custom View's page, with its HTML.

        Only Owners of the table can
        read it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        return await self._get(
            path_template("/v1/table/views/{view_id}/versions/{version_id}", view_id=view_id, version_id=version_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionRetrieveResponse,
        )

    async def update(
        self,
        version_id: str,
        *,
        view_id: str,
        summary: Optional[str] | Omit = omit,
        thumbnail: str | Omit = omit,
        title: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionUpdateResponse:
        """
        Set a version's title (at most 80 characters) or description of its changes (at
        most 300), or both, shown with it in the view's Versions list in place of what
        MortaAI wrote; empty or null clears one. Or set its thumbnail, a small picture
        of its page shown with it in the list, which the webapp takes the first time an
        owner's browser shows the version, as a PNG, JPEG or WebP data URL of at most
        120,000 characters (GET /v1/table/views/{viewId}/versions/{versionId}/thumbnail
        returns the image). A version keeps its first picture, so once it has one a
        thumbnail changes nothing. Only Owners of the table can set them.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        return await self._put(
            path_template("/v1/table/views/{view_id}/versions/{version_id}", view_id=view_id, version_id=version_id),
            body=await async_maybe_transform(
                {
                    "summary": summary,
                    "thumbnail": thumbnail,
                    "title": title,
                },
                version_update_params.VersionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionUpdateResponse,
        )

    async def list(
        self,
        view_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionListResponse:
        """
        Every version of a Custom View's page kept, newest first, without their HTML.
        Every save of the page adds one; the newest 50 are kept, plus the published one
        if it's older. Only Owners of the table can list them.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return await self._get(
            path_template("/v1/table/views/{view_id}/versions", view_id=view_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionListResponse,
        )

    async def delete(
        self,
        version_id: str,
        *,
        view_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Delete one version of a Custom View's page for good.

        The published version can't
        be deleted, as it's the page everyone sees; publish another first. Deleting the
        newest makes the one before it the newest, which the table's owners then see.
        Only Owners of the table can delete one.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/table/views/{view_id}/versions/{version_id}", view_id=view_id, version_id=version_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def delete_unpublished(
        self,
        view_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionDeleteUnpublishedResponse:
        """
        Delete every version of a Custom View's page newer than the published one (every
        version, when none is published), so the table's owners see the published page
        again. Every version saved since the last publish is deleted for good, whether
        MortaAI or the API saved it; the published version and older ones stay. Only
        Owners of the table can discard them.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return await self._delete(
            path_template("/v1/table/views/{view_id}/versions/unpublished", view_id=view_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionDeleteUnpublishedResponse,
        )

    async def restore(
        self,
        version_id: str,
        *,
        view_id: str,
        delete_newer: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> VersionRestoreResponse:
        """Make an older version the page again.

        It's copied to the top as the newest
        version and published, with its title, description and picture, so the table's
        owners and MortaAI carry on from it. The versions made after it stay below as
        history, or with deleteNewer are deleted for good (the one that was published
        too). Logged as a view update. Only Owners of the table can restore one.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        return await self._post(
            path_template(
                "/v1/table/views/{view_id}/versions/{version_id}/restore", view_id=view_id, version_id=version_id
            ),
            body=await async_maybe_transform(
                {"delete_newer": delete_newer}, version_restore_params.VersionRestoreParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=VersionRestoreResponse,
        )

    async def retrieve_thumbnail(
        self,
        version_id: str,
        *,
        view_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        The small picture of a version's page shown with it in the view's Versions list,
        as a PNG, JPEG or WebP image (set with thumbnail on PUT
        /v1/table/views/{viewId}/versions/{versionId}). A version's picture doesn't
        change once set, so the browser keeps it for a day. Only Owners of the table can
        read it.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        if not version_id:
            raise ValueError(f"Expected a non-empty value for `version_id` but received {version_id!r}")
        extra_headers = {"Accept": "image/jpeg", **(extra_headers or {})}
        return await self._get(
            path_template(
                "/v1/table/views/{view_id}/versions/{version_id}/thumbnail", view_id=view_id, version_id=version_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class VersionsResourceWithRawResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.create = to_raw_response_wrapper(
            versions.create,
        )
        self.retrieve = to_raw_response_wrapper(
            versions.retrieve,
        )
        self.update = to_raw_response_wrapper(
            versions.update,
        )
        self.list = to_raw_response_wrapper(
            versions.list,
        )
        self.delete = to_raw_response_wrapper(
            versions.delete,
        )
        self.delete_unpublished = to_raw_response_wrapper(
            versions.delete_unpublished,
        )
        self.restore = to_raw_response_wrapper(
            versions.restore,
        )
        self.retrieve_thumbnail = to_custom_raw_response_wrapper(
            versions.retrieve_thumbnail,
            BinaryAPIResponse,
        )


class AsyncVersionsResourceWithRawResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.create = async_to_raw_response_wrapper(
            versions.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            versions.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            versions.update,
        )
        self.list = async_to_raw_response_wrapper(
            versions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            versions.delete,
        )
        self.delete_unpublished = async_to_raw_response_wrapper(
            versions.delete_unpublished,
        )
        self.restore = async_to_raw_response_wrapper(
            versions.restore,
        )
        self.retrieve_thumbnail = async_to_custom_raw_response_wrapper(
            versions.retrieve_thumbnail,
            AsyncBinaryAPIResponse,
        )


class VersionsResourceWithStreamingResponse:
    def __init__(self, versions: VersionsResource) -> None:
        self._versions = versions

        self.create = to_streamed_response_wrapper(
            versions.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            versions.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            versions.update,
        )
        self.list = to_streamed_response_wrapper(
            versions.list,
        )
        self.delete = to_streamed_response_wrapper(
            versions.delete,
        )
        self.delete_unpublished = to_streamed_response_wrapper(
            versions.delete_unpublished,
        )
        self.restore = to_streamed_response_wrapper(
            versions.restore,
        )
        self.retrieve_thumbnail = to_custom_streamed_response_wrapper(
            versions.retrieve_thumbnail,
            StreamedBinaryAPIResponse,
        )


class AsyncVersionsResourceWithStreamingResponse:
    def __init__(self, versions: AsyncVersionsResource) -> None:
        self._versions = versions

        self.create = async_to_streamed_response_wrapper(
            versions.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            versions.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            versions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            versions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            versions.delete,
        )
        self.delete_unpublished = async_to_streamed_response_wrapper(
            versions.delete_unpublished,
        )
        self.restore = async_to_streamed_response_wrapper(
            versions.restore,
        )
        self.retrieve_thumbnail = async_to_custom_streamed_response_wrapper(
            versions.retrieve_thumbnail,
            AsyncStreamedBinaryAPIResponse,
        )
