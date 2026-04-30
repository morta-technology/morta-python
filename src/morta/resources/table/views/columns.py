# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.table.views import (
    column_add_params,
    column_update_params,
    column_distinct_params,
    column_ai_formula_helper_params,
)
from ....types.base_request_context_param import BaseRequestContextParam
from ....types.table.views.column_add_response import ColumnAddResponse
from ....types.table.select_options_lookup_param import SelectOptionsLookupParam
from ....types.table.views.column_update_response import ColumnUpdateResponse
from ....types.table.views.column_distinct_response import ColumnDistinctResponse
from ....types.table.views.column_formula_info_response import ColumnFormulaInfoResponse
from ....types.table.views.column_ai_formula_helper_response import ColumnAIFormulaHelperResponse

__all__ = ["ColumnsResource", "AsyncColumnsResource"]


class ColumnsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ColumnsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return ColumnsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ColumnsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return ColumnsResourceWithStreamingResponse(self)

    def update(
        self,
        column_id: str,
        *,
        view_id: str,
        aggregate: int | Omit = omit,
        alter_options: column_update_params.AlterOptions | Omit = omit,
        context: BaseRequestContextParam | Omit = omit,
        date_format: Optional[str] | Omit = omit,
        decimal_places: int | Omit = omit,
        description: column_update_params.Description | Omit = omit,
        display_link: bool | Omit = omit,
        display_validation_error: bool | Omit = omit,
        export_width: Optional[int] | Omit = omit,
        formula: Optional[str] | Omit = omit,
        formula_enabled: bool | Omit = omit,
        hard_validation: bool | Omit = omit,
        header_background_color: Optional[str] | Omit = omit,
        header_text_color: Optional[str] | Omit = omit,
        is_indexed: bool | Omit = omit,
        is_joined: Optional[bool] | Omit = omit,
        is_synced: bool | Omit = omit,
        kind: Literal[
            "text",
            "datetime",
            "date",
            "link",
            "multilink",
            "select",
            "multiselect",
            "integer",
            "float",
            "percentage",
            "tag",
            "variable",
            "attachment",
            "phone",
            "email",
            "vote",
            "checkbox",
            "duration",
        ]
        | Omit = omit,
        kind_options: SelectOptionsLookupParam | Omit = omit,
        locked: bool | Omit = omit,
        name: str | Omit = omit,
        public_id: str | Omit = omit,
        required: bool | Omit = omit,
        script: Optional[str] | Omit = omit,
        script_enabled: bool | Omit = omit,
        sort_order: int | Omit = omit,
        string_validation: Optional[str] | Omit = omit,
        thousand_separator: bool | Omit = omit,
        validation_message: Optional[str] | Omit = omit,
        validation_no_blanks: bool | Omit = omit,
        validation_no_duplicates: bool | Omit = omit,
        width: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ColumnUpdateResponse:
        """
        Update a specific column in a table view.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        if not column_id:
            raise ValueError(f"Expected a non-empty value for `column_id` but received {column_id!r}")
        return self._put(
            path_template("/v1/table/views/{view_id}/columns/{column_id}", view_id=view_id, column_id=column_id),
            body=maybe_transform(
                {
                    "aggregate": aggregate,
                    "alter_options": alter_options,
                    "context": context,
                    "date_format": date_format,
                    "decimal_places": decimal_places,
                    "description": description,
                    "display_link": display_link,
                    "display_validation_error": display_validation_error,
                    "export_width": export_width,
                    "formula": formula,
                    "formula_enabled": formula_enabled,
                    "hard_validation": hard_validation,
                    "header_background_color": header_background_color,
                    "header_text_color": header_text_color,
                    "is_indexed": is_indexed,
                    "is_joined": is_joined,
                    "is_synced": is_synced,
                    "kind": kind,
                    "kind_options": kind_options,
                    "locked": locked,
                    "name": name,
                    "public_id": public_id,
                    "required": required,
                    "script": script,
                    "script_enabled": script_enabled,
                    "sort_order": sort_order,
                    "string_validation": string_validation,
                    "thousand_separator": thousand_separator,
                    "validation_message": validation_message,
                    "validation_no_blanks": validation_no_blanks,
                    "validation_no_duplicates": validation_no_duplicates,
                    "width": width,
                },
                column_update_params.ColumnUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ColumnUpdateResponse,
        )

    def add(
        self,
        view_id: str,
        *,
        locked: bool,
        required: bool,
        sort_order: int,
        aggregate: int | Omit = omit,
        alter_options: column_add_params.AlterOptions | Omit = omit,
        context: BaseRequestContextParam | Omit = omit,
        date_format: Optional[str] | Omit = omit,
        decimal_places: int | Omit = omit,
        description: column_add_params.Description | Omit = omit,
        display_link: bool | Omit = omit,
        display_validation_error: bool | Omit = omit,
        export_width: Optional[int] | Omit = omit,
        formula: Optional[str] | Omit = omit,
        formula_enabled: bool | Omit = omit,
        hard_validation: bool | Omit = omit,
        header_background_color: Optional[str] | Omit = omit,
        header_text_color: Optional[str] | Omit = omit,
        is_indexed: bool | Omit = omit,
        is_joined: Optional[bool] | Omit = omit,
        is_synced: bool | Omit = omit,
        kind: Literal[
            "text",
            "datetime",
            "date",
            "link",
            "multilink",
            "select",
            "multiselect",
            "integer",
            "float",
            "percentage",
            "tag",
            "variable",
            "attachment",
            "phone",
            "email",
            "vote",
            "checkbox",
            "duration",
        ]
        | Omit = omit,
        kind_options: SelectOptionsLookupParam | Omit = omit,
        name: str | Omit = omit,
        public_id: str | Omit = omit,
        script: Optional[str] | Omit = omit,
        script_enabled: bool | Omit = omit,
        string_validation: Optional[str] | Omit = omit,
        thousand_separator: bool | Omit = omit,
        validation_message: Optional[str] | Omit = omit,
        validation_no_blanks: bool | Omit = omit,
        validation_no_duplicates: bool | Omit = omit,
        width: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ColumnAddResponse:
        """
        Add a new column to a specific table view.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return self._post(
            path_template("/v1/table/views/{view_id}/columns", view_id=view_id),
            body=maybe_transform(
                {
                    "locked": locked,
                    "required": required,
                    "sort_order": sort_order,
                    "aggregate": aggregate,
                    "alter_options": alter_options,
                    "context": context,
                    "date_format": date_format,
                    "decimal_places": decimal_places,
                    "description": description,
                    "display_link": display_link,
                    "display_validation_error": display_validation_error,
                    "export_width": export_width,
                    "formula": formula,
                    "formula_enabled": formula_enabled,
                    "hard_validation": hard_validation,
                    "header_background_color": header_background_color,
                    "header_text_color": header_text_color,
                    "is_indexed": is_indexed,
                    "is_joined": is_joined,
                    "is_synced": is_synced,
                    "kind": kind,
                    "kind_options": kind_options,
                    "name": name,
                    "public_id": public_id,
                    "script": script,
                    "script_enabled": script_enabled,
                    "string_validation": string_validation,
                    "thousand_separator": thousand_separator,
                    "validation_message": validation_message,
                    "validation_no_blanks": validation_no_blanks,
                    "validation_no_duplicates": validation_no_duplicates,
                    "width": width,
                },
                column_add_params.ColumnAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ColumnAddResponse,
        )

    def ai_formula_helper(
        self,
        column_id: str,
        *,
        view_id: str,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ColumnAIFormulaHelperResponse:
        """
        Get AI formula helper for a specific column in a table view.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        if not column_id:
            raise ValueError(f"Expected a non-empty value for `column_id` but received {column_id!r}")
        return self._post(
            path_template(
                "/v1/table/views/{view_id}/column/{column_id}/ai-formula-helper", view_id=view_id, column_id=column_id
            ),
            body=maybe_transform({"text": text}, column_ai_formula_helper_params.ColumnAIFormulaHelperParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ColumnAIFormulaHelperResponse,
        )

    def distinct(
        self,
        column_id: str,
        *,
        view_id: str,
        filter: str | Omit = omit,
        group_columns: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ColumnDistinctResponse:
        """
        Retrieve the unique/distinct values for a specific column in a table view.

        Args:
          filter: Filters to apply to the data retrieval.

          group_columns: Optional columns to group the distinct values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        if not column_id:
            raise ValueError(f"Expected a non-empty value for `column_id` but received {column_id!r}")
        return self._get(
            path_template(
                "/v1/table/views/{view_id}/column/{column_id}/distinct", view_id=view_id, column_id=column_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "filter": filter,
                        "group_columns": group_columns,
                    },
                    column_distinct_params.ColumnDistinctParams,
                ),
            ),
            cast_to=ColumnDistinctResponse,
        )

    def formula_info(
        self,
        column_id: str,
        *,
        view_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ColumnFormulaInfoResponse:
        """
        Retrieve formula information for a specific column in a table view.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        if not column_id:
            raise ValueError(f"Expected a non-empty value for `column_id` but received {column_id!r}")
        return self._get(
            path_template(
                "/v1/table/views/{view_id}/column/{column_id}/formula-info", view_id=view_id, column_id=column_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ColumnFormulaInfoResponse,
        )


class AsyncColumnsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncColumnsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncColumnsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncColumnsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return AsyncColumnsResourceWithStreamingResponse(self)

    async def update(
        self,
        column_id: str,
        *,
        view_id: str,
        aggregate: int | Omit = omit,
        alter_options: column_update_params.AlterOptions | Omit = omit,
        context: BaseRequestContextParam | Omit = omit,
        date_format: Optional[str] | Omit = omit,
        decimal_places: int | Omit = omit,
        description: column_update_params.Description | Omit = omit,
        display_link: bool | Omit = omit,
        display_validation_error: bool | Omit = omit,
        export_width: Optional[int] | Omit = omit,
        formula: Optional[str] | Omit = omit,
        formula_enabled: bool | Omit = omit,
        hard_validation: bool | Omit = omit,
        header_background_color: Optional[str] | Omit = omit,
        header_text_color: Optional[str] | Omit = omit,
        is_indexed: bool | Omit = omit,
        is_joined: Optional[bool] | Omit = omit,
        is_synced: bool | Omit = omit,
        kind: Literal[
            "text",
            "datetime",
            "date",
            "link",
            "multilink",
            "select",
            "multiselect",
            "integer",
            "float",
            "percentage",
            "tag",
            "variable",
            "attachment",
            "phone",
            "email",
            "vote",
            "checkbox",
            "duration",
        ]
        | Omit = omit,
        kind_options: SelectOptionsLookupParam | Omit = omit,
        locked: bool | Omit = omit,
        name: str | Omit = omit,
        public_id: str | Omit = omit,
        required: bool | Omit = omit,
        script: Optional[str] | Omit = omit,
        script_enabled: bool | Omit = omit,
        sort_order: int | Omit = omit,
        string_validation: Optional[str] | Omit = omit,
        thousand_separator: bool | Omit = omit,
        validation_message: Optional[str] | Omit = omit,
        validation_no_blanks: bool | Omit = omit,
        validation_no_duplicates: bool | Omit = omit,
        width: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ColumnUpdateResponse:
        """
        Update a specific column in a table view.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        if not column_id:
            raise ValueError(f"Expected a non-empty value for `column_id` but received {column_id!r}")
        return await self._put(
            path_template("/v1/table/views/{view_id}/columns/{column_id}", view_id=view_id, column_id=column_id),
            body=await async_maybe_transform(
                {
                    "aggregate": aggregate,
                    "alter_options": alter_options,
                    "context": context,
                    "date_format": date_format,
                    "decimal_places": decimal_places,
                    "description": description,
                    "display_link": display_link,
                    "display_validation_error": display_validation_error,
                    "export_width": export_width,
                    "formula": formula,
                    "formula_enabled": formula_enabled,
                    "hard_validation": hard_validation,
                    "header_background_color": header_background_color,
                    "header_text_color": header_text_color,
                    "is_indexed": is_indexed,
                    "is_joined": is_joined,
                    "is_synced": is_synced,
                    "kind": kind,
                    "kind_options": kind_options,
                    "locked": locked,
                    "name": name,
                    "public_id": public_id,
                    "required": required,
                    "script": script,
                    "script_enabled": script_enabled,
                    "sort_order": sort_order,
                    "string_validation": string_validation,
                    "thousand_separator": thousand_separator,
                    "validation_message": validation_message,
                    "validation_no_blanks": validation_no_blanks,
                    "validation_no_duplicates": validation_no_duplicates,
                    "width": width,
                },
                column_update_params.ColumnUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ColumnUpdateResponse,
        )

    async def add(
        self,
        view_id: str,
        *,
        locked: bool,
        required: bool,
        sort_order: int,
        aggregate: int | Omit = omit,
        alter_options: column_add_params.AlterOptions | Omit = omit,
        context: BaseRequestContextParam | Omit = omit,
        date_format: Optional[str] | Omit = omit,
        decimal_places: int | Omit = omit,
        description: column_add_params.Description | Omit = omit,
        display_link: bool | Omit = omit,
        display_validation_error: bool | Omit = omit,
        export_width: Optional[int] | Omit = omit,
        formula: Optional[str] | Omit = omit,
        formula_enabled: bool | Omit = omit,
        hard_validation: bool | Omit = omit,
        header_background_color: Optional[str] | Omit = omit,
        header_text_color: Optional[str] | Omit = omit,
        is_indexed: bool | Omit = omit,
        is_joined: Optional[bool] | Omit = omit,
        is_synced: bool | Omit = omit,
        kind: Literal[
            "text",
            "datetime",
            "date",
            "link",
            "multilink",
            "select",
            "multiselect",
            "integer",
            "float",
            "percentage",
            "tag",
            "variable",
            "attachment",
            "phone",
            "email",
            "vote",
            "checkbox",
            "duration",
        ]
        | Omit = omit,
        kind_options: SelectOptionsLookupParam | Omit = omit,
        name: str | Omit = omit,
        public_id: str | Omit = omit,
        script: Optional[str] | Omit = omit,
        script_enabled: bool | Omit = omit,
        string_validation: Optional[str] | Omit = omit,
        thousand_separator: bool | Omit = omit,
        validation_message: Optional[str] | Omit = omit,
        validation_no_blanks: bool | Omit = omit,
        validation_no_duplicates: bool | Omit = omit,
        width: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ColumnAddResponse:
        """
        Add a new column to a specific table view.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        return await self._post(
            path_template("/v1/table/views/{view_id}/columns", view_id=view_id),
            body=await async_maybe_transform(
                {
                    "locked": locked,
                    "required": required,
                    "sort_order": sort_order,
                    "aggregate": aggregate,
                    "alter_options": alter_options,
                    "context": context,
                    "date_format": date_format,
                    "decimal_places": decimal_places,
                    "description": description,
                    "display_link": display_link,
                    "display_validation_error": display_validation_error,
                    "export_width": export_width,
                    "formula": formula,
                    "formula_enabled": formula_enabled,
                    "hard_validation": hard_validation,
                    "header_background_color": header_background_color,
                    "header_text_color": header_text_color,
                    "is_indexed": is_indexed,
                    "is_joined": is_joined,
                    "is_synced": is_synced,
                    "kind": kind,
                    "kind_options": kind_options,
                    "name": name,
                    "public_id": public_id,
                    "script": script,
                    "script_enabled": script_enabled,
                    "string_validation": string_validation,
                    "thousand_separator": thousand_separator,
                    "validation_message": validation_message,
                    "validation_no_blanks": validation_no_blanks,
                    "validation_no_duplicates": validation_no_duplicates,
                    "width": width,
                },
                column_add_params.ColumnAddParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ColumnAddResponse,
        )

    async def ai_formula_helper(
        self,
        column_id: str,
        *,
        view_id: str,
        text: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ColumnAIFormulaHelperResponse:
        """
        Get AI formula helper for a specific column in a table view.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        if not column_id:
            raise ValueError(f"Expected a non-empty value for `column_id` but received {column_id!r}")
        return await self._post(
            path_template(
                "/v1/table/views/{view_id}/column/{column_id}/ai-formula-helper", view_id=view_id, column_id=column_id
            ),
            body=await async_maybe_transform(
                {"text": text}, column_ai_formula_helper_params.ColumnAIFormulaHelperParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ColumnAIFormulaHelperResponse,
        )

    async def distinct(
        self,
        column_id: str,
        *,
        view_id: str,
        filter: str | Omit = omit,
        group_columns: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ColumnDistinctResponse:
        """
        Retrieve the unique/distinct values for a specific column in a table view.

        Args:
          filter: Filters to apply to the data retrieval.

          group_columns: Optional columns to group the distinct values.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        if not column_id:
            raise ValueError(f"Expected a non-empty value for `column_id` but received {column_id!r}")
        return await self._get(
            path_template(
                "/v1/table/views/{view_id}/column/{column_id}/distinct", view_id=view_id, column_id=column_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "filter": filter,
                        "group_columns": group_columns,
                    },
                    column_distinct_params.ColumnDistinctParams,
                ),
            ),
            cast_to=ColumnDistinctResponse,
        )

    async def formula_info(
        self,
        column_id: str,
        *,
        view_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ColumnFormulaInfoResponse:
        """
        Retrieve formula information for a specific column in a table view.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not view_id:
            raise ValueError(f"Expected a non-empty value for `view_id` but received {view_id!r}")
        if not column_id:
            raise ValueError(f"Expected a non-empty value for `column_id` but received {column_id!r}")
        return await self._get(
            path_template(
                "/v1/table/views/{view_id}/column/{column_id}/formula-info", view_id=view_id, column_id=column_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ColumnFormulaInfoResponse,
        )


class ColumnsResourceWithRawResponse:
    def __init__(self, columns: ColumnsResource) -> None:
        self._columns = columns

        self.update = to_raw_response_wrapper(
            columns.update,
        )
        self.add = to_raw_response_wrapper(
            columns.add,
        )
        self.ai_formula_helper = to_raw_response_wrapper(
            columns.ai_formula_helper,
        )
        self.distinct = to_raw_response_wrapper(
            columns.distinct,
        )
        self.formula_info = to_raw_response_wrapper(
            columns.formula_info,
        )


class AsyncColumnsResourceWithRawResponse:
    def __init__(self, columns: AsyncColumnsResource) -> None:
        self._columns = columns

        self.update = async_to_raw_response_wrapper(
            columns.update,
        )
        self.add = async_to_raw_response_wrapper(
            columns.add,
        )
        self.ai_formula_helper = async_to_raw_response_wrapper(
            columns.ai_formula_helper,
        )
        self.distinct = async_to_raw_response_wrapper(
            columns.distinct,
        )
        self.formula_info = async_to_raw_response_wrapper(
            columns.formula_info,
        )


class ColumnsResourceWithStreamingResponse:
    def __init__(self, columns: ColumnsResource) -> None:
        self._columns = columns

        self.update = to_streamed_response_wrapper(
            columns.update,
        )
        self.add = to_streamed_response_wrapper(
            columns.add,
        )
        self.ai_formula_helper = to_streamed_response_wrapper(
            columns.ai_formula_helper,
        )
        self.distinct = to_streamed_response_wrapper(
            columns.distinct,
        )
        self.formula_info = to_streamed_response_wrapper(
            columns.formula_info,
        )


class AsyncColumnsResourceWithStreamingResponse:
    def __init__(self, columns: AsyncColumnsResource) -> None:
        self._columns = columns

        self.update = async_to_streamed_response_wrapper(
            columns.update,
        )
        self.add = async_to_streamed_response_wrapper(
            columns.add,
        )
        self.ai_formula_helper = async_to_streamed_response_wrapper(
            columns.ai_formula_helper,
        )
        self.distinct = async_to_streamed_response_wrapper(
            columns.distinct,
        )
        self.formula_info = async_to_streamed_response_wrapper(
            columns.formula_info,
        )
