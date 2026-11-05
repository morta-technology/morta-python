# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import path_template, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_custom_raw_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.table.views import export_list_params, export_create_params

__all__ = ["ExportResource", "AsyncExportResource"]


class ExportResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ExportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return ExportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ExportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return ExportResourceWithStreamingResponse(self)

    def create(
        self,
        view_id: str,
        *,
        colour: Iterable[object] | Omit = omit,
        display_comment_rows: int | Omit = omit,
        filter: Iterable[object] | Omit = omit,
        format: Literal["csv", "xlsx"] | Omit = omit,
        hidden: SequenceNotStr[str] | Omit = omit,
        process_id: str | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Same as the GET variant, with the options in a JSON body so many filters or
        colour rules don't make the URL too long. `filter` and `colour` are lists of
        objects, `hidden` a list of column UUIDs, and `sort` a list of `ColumnName:asc`
        / `ColumnName:desc` strings.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        extra_headers = {
            "Accept": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            **(extra_headers or {}),
        }
        return self._post(
            path_template("/v1/table/views/{view_id}/export", view_id=view_id),
            body=maybe_transform(
                {
                    "colour": colour,
                    "display_comment_rows": display_comment_rows,
                    "filter": filter,
                    "format": format,
                    "hidden": hidden,
                    "process_id": process_id,
                    "sort": sort,
                    "timezone": timezone,
                },
                export_create_params.ExportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BinaryAPIResponse,
        )

    def list(
        self,
        view_id: str,
        *,
        colour: str | Omit = omit,
        filter: str | Omit = omit,
        format: Literal["csv", "xlsx"] | Omit = omit,
        hidden: str | Omit = omit,
        process_id: str | Omit = omit,
        sort: str | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Download the rows of a table view as a CSV file (`format=csv`, the default) or
        as an Excel workbook (`format=xlsx`). The view's saved filters always apply; the
        request's filters, sort and hidden columns narrow and order the export. An Excel
        workbook keeps the view's look: colour rules, header colours, column widths and
        row heights, number and date formats, and clickable links. Excel holds at most
        1,048,575 rows; larger exports must use CSV. Use the POST variant when the
        filters would make the URL long.

        Args:
          colour: URL encoded JSON colour rule to use instead of the view's saved rules (xlsx
              only). Repeat for more rules.

          filter: URL encoded JSON filter, as for the CSV download. Repeat for more filters.

          format: The file format.

          hidden: The UUID of a column to leave out. Repeat for more columns.

          process_id: The UUID of the document the view is exported from, for document variable
              filters.

          sort: Sort as `ColumnName:asc` or `ColumnName:desc`. Repeat for more sorts.

          timezone: IANA time zone, such as Europe/London, that Excel shows dates and times in (xlsx
              only). Defaults to UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        extra_headers = {
            "Accept": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            **(extra_headers or {}),
        }
        return self._get(
            path_template("/v1/table/views/{view_id}/export", view_id=view_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "colour": colour,
                        "filter": filter,
                        "format": format,
                        "hidden": hidden,
                        "process_id": process_id,
                        "sort": sort,
                        "timezone": timezone,
                    },
                    export_list_params.ExportListParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncExportResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncExportResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncExportResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncExportResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return AsyncExportResourceWithStreamingResponse(self)

    async def create(
        self,
        view_id: str,
        *,
        colour: Iterable[object] | Omit = omit,
        display_comment_rows: int | Omit = omit,
        filter: Iterable[object] | Omit = omit,
        format: Literal["csv", "xlsx"] | Omit = omit,
        hidden: SequenceNotStr[str] | Omit = omit,
        process_id: str | Omit = omit,
        sort: SequenceNotStr[str] | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Same as the GET variant, with the options in a JSON body so many filters or
        colour rules don't make the URL too long. `filter` and `colour` are lists of
        objects, `hidden` a list of column UUIDs, and `sort` a list of `ColumnName:asc`
        / `ColumnName:desc` strings.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        extra_headers = {
            "Accept": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            **(extra_headers or {}),
        }
        return await self._post(
            path_template("/v1/table/views/{view_id}/export", view_id=view_id),
            body=await async_maybe_transform(
                {
                    "colour": colour,
                    "display_comment_rows": display_comment_rows,
                    "filter": filter,
                    "format": format,
                    "hidden": hidden,
                    "process_id": process_id,
                    "sort": sort,
                    "timezone": timezone,
                },
                export_create_params.ExportCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def list(
        self,
        view_id: str,
        *,
        colour: str | Omit = omit,
        filter: str | Omit = omit,
        format: Literal["csv", "xlsx"] | Omit = omit,
        hidden: str | Omit = omit,
        process_id: str | Omit = omit,
        sort: str | Omit = omit,
        timezone: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Download the rows of a table view as a CSV file (`format=csv`, the default) or
        as an Excel workbook (`format=xlsx`). The view's saved filters always apply; the
        request's filters, sort and hidden columns narrow and order the export. An Excel
        workbook keeps the view's look: colour rules, header colours, column widths and
        row heights, number and date formats, and clickable links. Excel holds at most
        1,048,575 rows; larger exports must use CSV. Use the POST variant when the
        filters would make the URL long.

        Args:
          colour: URL encoded JSON colour rule to use instead of the view's saved rules (xlsx
              only). Repeat for more rules.

          filter: URL encoded JSON filter, as for the CSV download. Repeat for more filters.

          format: The file format.

          hidden: The UUID of a column to leave out. Repeat for more columns.

          process_id: The UUID of the document the view is exported from, for document variable
              filters.

          sort: Sort as `ColumnName:asc` or `ColumnName:desc`. Repeat for more sorts.

          timezone: IANA time zone, such as Europe/London, that Excel shows dates and times in (xlsx
              only). Defaults to UTC.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        extra_headers = {
            "Accept": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            **(extra_headers or {}),
        }
        return await self._get(
            path_template("/v1/table/views/{view_id}/export", view_id=view_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "colour": colour,
                        "filter": filter,
                        "format": format,
                        "hidden": hidden,
                        "process_id": process_id,
                        "sort": sort,
                        "timezone": timezone,
                    },
                    export_list_params.ExportListParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class ExportResourceWithRawResponse:
    def __init__(self, export: ExportResource) -> None:
        self._export = export

        self.create = to_custom_raw_response_wrapper(
            export.create,
            BinaryAPIResponse,
        )
        self.list = to_custom_raw_response_wrapper(
            export.list,
            BinaryAPIResponse,
        )


class AsyncExportResourceWithRawResponse:
    def __init__(self, export: AsyncExportResource) -> None:
        self._export = export

        self.create = async_to_custom_raw_response_wrapper(
            export.create,
            AsyncBinaryAPIResponse,
        )
        self.list = async_to_custom_raw_response_wrapper(
            export.list,
            AsyncBinaryAPIResponse,
        )


class ExportResourceWithStreamingResponse:
    def __init__(self, export: ExportResource) -> None:
        self._export = export

        self.create = to_custom_streamed_response_wrapper(
            export.create,
            StreamedBinaryAPIResponse,
        )
        self.list = to_custom_streamed_response_wrapper(
            export.list,
            StreamedBinaryAPIResponse,
        )


class AsyncExportResourceWithStreamingResponse:
    def __init__(self, export: AsyncExportResource) -> None:
        self._export = export

        self.create = async_to_custom_streamed_response_wrapper(
            export.create,
            AsyncStreamedBinaryAPIResponse,
        )
        self.list = async_to_custom_streamed_response_wrapper(
            export.list,
            AsyncStreamedBinaryAPIResponse,
        )
