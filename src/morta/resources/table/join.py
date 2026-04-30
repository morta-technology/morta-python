# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.table import join_create_params, join_update_params
from ..._base_client import make_request_options
from ...types.base_request_context_param import BaseRequestContextParam
from ...types.table.join_create_response import JoinCreateResponse
from ...types.table.join_delete_response import JoinDeleteResponse
from ...types.table.join_update_response import JoinUpdateResponse
from ...types.table.table_column_join_param import TableColumnJoinParam

__all__ = ["JoinResource", "AsyncJoinResource"]


class JoinResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> JoinResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return JoinResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> JoinResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return JoinResourceWithStreamingResponse(self)

    def create(
        self,
        table_id: str,
        *,
        context: BaseRequestContextParam | Omit = omit,
        data_columns: SequenceNotStr[str] | Omit = omit,
        is_one_to_many: bool | Omit = omit,
        join_columns: Iterable[TableColumnJoinParam] | Omit = omit,
        join_view_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JoinCreateResponse:
        """
        Create a join between two tables.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id:
            raise ValueError(f"Expected a non-empty value for `table_id` but received {table_id!r}")
        return self._post(
            path_template("/v1/table/{table_id}/join", table_id=table_id),
            body=maybe_transform(
                {
                    "context": context,
                    "data_columns": data_columns,
                    "is_one_to_many": is_one_to_many,
                    "join_columns": join_columns,
                    "join_view_id": join_view_id,
                },
                join_create_params.JoinCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JoinCreateResponse,
        )

    def update(
        self,
        join_id: str,
        *,
        table_id: str,
        context: BaseRequestContextParam | Omit = omit,
        data_columns: SequenceNotStr[str] | Omit = omit,
        is_one_to_many: bool | Omit = omit,
        join_columns: Iterable[TableColumnJoinParam] | Omit = omit,
        join_view_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JoinUpdateResponse:
        """
        Update an existing join on a table.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id:
            raise ValueError(f"Expected a non-empty value for `table_id` but received {table_id!r}")
        if not join_id:
            raise ValueError(f"Expected a non-empty value for `join_id` but received {join_id!r}")
        return self._put(
            path_template("/v1/table/{table_id}/join/{join_id}", table_id=table_id, join_id=join_id),
            body=maybe_transform(
                {
                    "context": context,
                    "data_columns": data_columns,
                    "is_one_to_many": is_one_to_many,
                    "join_columns": join_columns,
                    "join_view_id": join_view_id,
                },
                join_update_params.JoinUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JoinUpdateResponse,
        )

    def delete(
        self,
        join_id: str,
        *,
        table_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JoinDeleteResponse:
        """
        Delete a join from a table.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id:
            raise ValueError(f"Expected a non-empty value for `table_id` but received {table_id!r}")
        if not join_id:
            raise ValueError(f"Expected a non-empty value for `join_id` but received {join_id!r}")
        return self._delete(
            path_template("/v1/table/{table_id}/join/{join_id}", table_id=table_id, join_id=join_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JoinDeleteResponse,
        )


class AsyncJoinResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncJoinResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncJoinResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncJoinResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return AsyncJoinResourceWithStreamingResponse(self)

    async def create(
        self,
        table_id: str,
        *,
        context: BaseRequestContextParam | Omit = omit,
        data_columns: SequenceNotStr[str] | Omit = omit,
        is_one_to_many: bool | Omit = omit,
        join_columns: Iterable[TableColumnJoinParam] | Omit = omit,
        join_view_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JoinCreateResponse:
        """
        Create a join between two tables.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id:
            raise ValueError(f"Expected a non-empty value for `table_id` but received {table_id!r}")
        return await self._post(
            path_template("/v1/table/{table_id}/join", table_id=table_id),
            body=await async_maybe_transform(
                {
                    "context": context,
                    "data_columns": data_columns,
                    "is_one_to_many": is_one_to_many,
                    "join_columns": join_columns,
                    "join_view_id": join_view_id,
                },
                join_create_params.JoinCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JoinCreateResponse,
        )

    async def update(
        self,
        join_id: str,
        *,
        table_id: str,
        context: BaseRequestContextParam | Omit = omit,
        data_columns: SequenceNotStr[str] | Omit = omit,
        is_one_to_many: bool | Omit = omit,
        join_columns: Iterable[TableColumnJoinParam] | Omit = omit,
        join_view_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JoinUpdateResponse:
        """
        Update an existing join on a table.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id:
            raise ValueError(f"Expected a non-empty value for `table_id` but received {table_id!r}")
        if not join_id:
            raise ValueError(f"Expected a non-empty value for `join_id` but received {join_id!r}")
        return await self._put(
            path_template("/v1/table/{table_id}/join/{join_id}", table_id=table_id, join_id=join_id),
            body=await async_maybe_transform(
                {
                    "context": context,
                    "data_columns": data_columns,
                    "is_one_to_many": is_one_to_many,
                    "join_columns": join_columns,
                    "join_view_id": join_view_id,
                },
                join_update_params.JoinUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JoinUpdateResponse,
        )

    async def delete(
        self,
        join_id: str,
        *,
        table_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> JoinDeleteResponse:
        """
        Delete a join from a table.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not table_id:
            raise ValueError(f"Expected a non-empty value for `table_id` but received {table_id!r}")
        if not join_id:
            raise ValueError(f"Expected a non-empty value for `join_id` but received {join_id!r}")
        return await self._delete(
            path_template("/v1/table/{table_id}/join/{join_id}", table_id=table_id, join_id=join_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=JoinDeleteResponse,
        )


class JoinResourceWithRawResponse:
    def __init__(self, join: JoinResource) -> None:
        self._join = join

        self.create = to_raw_response_wrapper(
            join.create,
        )
        self.update = to_raw_response_wrapper(
            join.update,
        )
        self.delete = to_raw_response_wrapper(
            join.delete,
        )


class AsyncJoinResourceWithRawResponse:
    def __init__(self, join: AsyncJoinResource) -> None:
        self._join = join

        self.create = async_to_raw_response_wrapper(
            join.create,
        )
        self.update = async_to_raw_response_wrapper(
            join.update,
        )
        self.delete = async_to_raw_response_wrapper(
            join.delete,
        )


class JoinResourceWithStreamingResponse:
    def __init__(self, join: JoinResource) -> None:
        self._join = join

        self.create = to_streamed_response_wrapper(
            join.create,
        )
        self.update = to_streamed_response_wrapper(
            join.update,
        )
        self.delete = to_streamed_response_wrapper(
            join.delete,
        )


class AsyncJoinResourceWithStreamingResponse:
    def __init__(self, join: AsyncJoinResource) -> None:
        self._join = join

        self.create = async_to_streamed_response_wrapper(
            join.create,
        )
        self.update = async_to_streamed_response_wrapper(
            join.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            join.delete,
        )
