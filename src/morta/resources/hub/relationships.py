# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

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

__all__ = ["RelationshipsResource", "AsyncRelationshipsResource"]


class RelationshipsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RelationshipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return RelationshipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RelationshipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return RelationshipsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        public_id: str,
        *,
        hub_id: str,
        kind: Literal["table", "document"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        The table's live columns, or the document's sections, and every relationship
        touching them (including those that run through the table's views). Hub owners
        only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hub_id:
            raise ValueError(f"Expected a non-empty value for `hub_id` but received {hub_id!r}")
        if not kind:
            raise ValueError(f"Expected a non-empty value for `kind` but received {kind!r}")
        if not public_id:
            raise ValueError(f"Expected a non-empty value for `public_id` but received {public_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template(
                "/v1/hub/{hub_id}/relationships/{kind}/{public_id}", hub_id=hub_id, kind=kind, public_id=public_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def list(
        self,
        hub_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Tables and documents of the hub with the relationships (dependencies) between
        them, aggregated per pair. Hub owners only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hub_id:
            raise ValueError(f"Expected a non-empty value for `hub_id` but received {hub_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._get(
            path_template("/v1/hub/{hub_id}/relationships", hub_id=hub_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncRelationshipsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRelationshipsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRelationshipsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRelationshipsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return AsyncRelationshipsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        public_id: str,
        *,
        hub_id: str,
        kind: Literal["table", "document"],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        The table's live columns, or the document's sections, and every relationship
        touching them (including those that run through the table's views). Hub owners
        only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hub_id:
            raise ValueError(f"Expected a non-empty value for `hub_id` but received {hub_id!r}")
        if not kind:
            raise ValueError(f"Expected a non-empty value for `kind` but received {kind!r}")
        if not public_id:
            raise ValueError(f"Expected a non-empty value for `public_id` but received {public_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template(
                "/v1/hub/{hub_id}/relationships/{kind}/{public_id}", hub_id=hub_id, kind=kind, public_id=public_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def list(
        self,
        hub_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Tables and documents of the hub with the relationships (dependencies) between
        them, aggregated per pair. Hub owners only.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not hub_id:
            raise ValueError(f"Expected a non-empty value for `hub_id` but received {hub_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._get(
            path_template("/v1/hub/{hub_id}/relationships", hub_id=hub_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class RelationshipsResourceWithRawResponse:
    def __init__(self, relationships: RelationshipsResource) -> None:
        self._relationships = relationships

        self.retrieve = to_raw_response_wrapper(
            relationships.retrieve,
        )
        self.list = to_raw_response_wrapper(
            relationships.list,
        )


class AsyncRelationshipsResourceWithRawResponse:
    def __init__(self, relationships: AsyncRelationshipsResource) -> None:
        self._relationships = relationships

        self.retrieve = async_to_raw_response_wrapper(
            relationships.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            relationships.list,
        )


class RelationshipsResourceWithStreamingResponse:
    def __init__(self, relationships: RelationshipsResource) -> None:
        self._relationships = relationships

        self.retrieve = to_streamed_response_wrapper(
            relationships.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            relationships.list,
        )


class AsyncRelationshipsResourceWithStreamingResponse:
    def __init__(self, relationships: AsyncRelationshipsResource) -> None:
        self._relationships = relationships

        self.retrieve = async_to_streamed_response_wrapper(
            relationships.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            relationships.list,
        )
