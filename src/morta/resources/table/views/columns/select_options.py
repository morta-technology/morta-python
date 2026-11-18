# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ....._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ....._utils import path_template, maybe_transform, async_maybe_transform
from ....._compat import cached_property
from ....._resource import SyncAPIResource, AsyncAPIResource
from ....._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ....._base_client import make_request_options
from .....types.table.views.columns import (
    select_option_retrieve_check_params,
    select_option_retrieve_select_options_params,
)
from .....types.table.views.columns.select_option_retrieve_check_response import SelectOptionRetrieveCheckResponse
from .....types.table.views.columns.select_option_retrieve_select_options_response import (
    SelectOptionRetrieveSelectOptionsResponse,
)

__all__ = ["SelectOptionsResource", "AsyncSelectOptionsResource"]


class SelectOptionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SelectOptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return SelectOptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SelectOptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return SelectOptionsResourceWithStreamingResponse(self)

    def retrieve_check(
        self,
        column_id: str,
        *,
        view_id: str,
        values: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SelectOptionRetrieveCheckResponse:
        """
        Which of the given values are options of a select column that takes them from
        another table.

        Args:
          values: A JSON-encoded list of up to 1000 values to check.

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
                "/v1/table/views/{view_id}/column/{column_id}/select-options/check",
                view_id=view_id,
                column_id=column_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"values": values}, select_option_retrieve_check_params.SelectOptionRetrieveCheckParams
                ),
            ),
            cast_to=SelectOptionRetrieveCheckResponse,
        )

    def retrieve_select_options(
        self,
        column_id: str,
        *,
        view_id: str,
        after: str | Omit = omit,
        dependency_values: str | Omit = omit,
        search: str | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SelectOptionRetrieveSelectOptionsResponse:
        """
        A page of the options of a select column that takes them from another table, in
        order. Used for sources too big to send with the table (cachedOptionsPartial).

        Args:
          after: The `next` of the page before.

          dependency_values: JSON list of the row's dependency values, in order. Leave out for every option.

          search: Words every option holds, in any order or case. Only the first 10 words of the
              first 200 characters are looked for.

          size: The most options to return.

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
                "/v1/table/views/{view_id}/column/{column_id}/select-options", view_id=view_id, column_id=column_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "after": after,
                        "dependency_values": dependency_values,
                        "search": search,
                        "size": size,
                    },
                    select_option_retrieve_select_options_params.SelectOptionRetrieveSelectOptionsParams,
                ),
            ),
            cast_to=SelectOptionRetrieveSelectOptionsResponse,
        )


class AsyncSelectOptionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSelectOptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSelectOptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSelectOptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return AsyncSelectOptionsResourceWithStreamingResponse(self)

    async def retrieve_check(
        self,
        column_id: str,
        *,
        view_id: str,
        values: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SelectOptionRetrieveCheckResponse:
        """
        Which of the given values are options of a select column that takes them from
        another table.

        Args:
          values: A JSON-encoded list of up to 1000 values to check.

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
                "/v1/table/views/{view_id}/column/{column_id}/select-options/check",
                view_id=view_id,
                column_id=column_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"values": values}, select_option_retrieve_check_params.SelectOptionRetrieveCheckParams
                ),
            ),
            cast_to=SelectOptionRetrieveCheckResponse,
        )

    async def retrieve_select_options(
        self,
        column_id: str,
        *,
        view_id: str,
        after: str | Omit = omit,
        dependency_values: str | Omit = omit,
        search: str | Omit = omit,
        size: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SelectOptionRetrieveSelectOptionsResponse:
        """
        A page of the options of a select column that takes them from another table, in
        order. Used for sources too big to send with the table (cachedOptionsPartial).

        Args:
          after: The `next` of the page before.

          dependency_values: JSON list of the row's dependency values, in order. Leave out for every option.

          search: Words every option holds, in any order or case. Only the first 10 words of the
              first 200 characters are looked for.

          size: The most options to return.

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
                "/v1/table/views/{view_id}/column/{column_id}/select-options", view_id=view_id, column_id=column_id
            ),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "after": after,
                        "dependency_values": dependency_values,
                        "search": search,
                        "size": size,
                    },
                    select_option_retrieve_select_options_params.SelectOptionRetrieveSelectOptionsParams,
                ),
            ),
            cast_to=SelectOptionRetrieveSelectOptionsResponse,
        )


class SelectOptionsResourceWithRawResponse:
    def __init__(self, select_options: SelectOptionsResource) -> None:
        self._select_options = select_options

        self.retrieve_check = to_raw_response_wrapper(
            select_options.retrieve_check,
        )
        self.retrieve_select_options = to_raw_response_wrapper(
            select_options.retrieve_select_options,
        )


class AsyncSelectOptionsResourceWithRawResponse:
    def __init__(self, select_options: AsyncSelectOptionsResource) -> None:
        self._select_options = select_options

        self.retrieve_check = async_to_raw_response_wrapper(
            select_options.retrieve_check,
        )
        self.retrieve_select_options = async_to_raw_response_wrapper(
            select_options.retrieve_select_options,
        )


class SelectOptionsResourceWithStreamingResponse:
    def __init__(self, select_options: SelectOptionsResource) -> None:
        self._select_options = select_options

        self.retrieve_check = to_streamed_response_wrapper(
            select_options.retrieve_check,
        )
        self.retrieve_select_options = to_streamed_response_wrapper(
            select_options.retrieve_select_options,
        )


class AsyncSelectOptionsResourceWithStreamingResponse:
    def __init__(self, select_options: AsyncSelectOptionsResource) -> None:
        self._select_options = select_options

        self.retrieve_check = async_to_streamed_response_wrapper(
            select_options.retrieve_check,
        )
        self.retrieve_select_options = async_to_streamed_response_wrapper(
            select_options.retrieve_select_options,
        )
