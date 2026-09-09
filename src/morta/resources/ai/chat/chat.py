# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Mapping, cast

import httpx

from ...._files import deepcopy_with_paths
from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import extract_files, maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ....types.ai import chat_create_params
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._streaming import Stream, AsyncStream
from .conversations import (
    ConversationsResource,
    AsyncConversationsResource,
    ConversationsResourceWithRawResponse,
    AsyncConversationsResourceWithRawResponse,
    ConversationsResourceWithStreamingResponse,
    AsyncConversationsResourceWithStreamingResponse,
)
from ...._base_client import make_request_options
from ....types.ai.chat_create_response import ChatCreateResponse

__all__ = ["ChatResource", "AsyncChatResource"]


class ChatResource(SyncAPIResource):
    @cached_property
    def conversations(self) -> ConversationsResource:
        return ConversationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> ChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return ChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return ChatResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        message: str,
        conversation_id: str | Omit = omit,
        document_context_id: str | Omit = omit,
        table_view_context_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Stream[ChatCreateResponse]:
        """Send a message to Morta AI.

        Returns a stream of SSE events. Accepts either
        application/json or multipart/form-data (for file uploads). For multipart, send
        JSON fields in a 'data' form field and files in 'files'.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        body = deepcopy_with_paths(
            {
                "message": message,
                "conversation_id": conversation_id,
                "document_context_id": document_context_id,
                "table_view_context_id": table_view_context_id,
            },
            [["files", "<array>"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["files", "<array>"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/v1/ai/chat",
            body=maybe_transform(body, chat_create_params.ChatCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
            stream=True,
            stream_cls=Stream[ChatCreateResponse],
        )


class AsyncChatResource(AsyncAPIResource):
    @cached_property
    def conversations(self) -> AsyncConversationsResource:
        return AsyncConversationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncChatResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncChatResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncChatResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return AsyncChatResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        message: str,
        conversation_id: str | Omit = omit,
        document_context_id: str | Omit = omit,
        table_view_context_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncStream[ChatCreateResponse]:
        """Send a message to Morta AI.

        Returns a stream of SSE events. Accepts either
        application/json or multipart/form-data (for file uploads). For multipart, send
        JSON fields in a 'data' form field and files in 'files'.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "text/event-stream", **(extra_headers or {})}
        body = deepcopy_with_paths(
            {
                "message": message,
                "conversation_id": conversation_id,
                "document_context_id": document_context_id,
                "table_view_context_id": table_view_context_id,
            },
            [["files", "<array>"]],
        )
        files = extract_files(cast(Mapping[str, object], body), paths=[["files", "<array>"]])
        if files:
            # It should be noted that the actual Content-Type header that will be
            # sent to the server will contain a `boundary` parameter, e.g.
            # multipart/form-data; boundary=---abc--
            extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/v1/ai/chat",
            body=await async_maybe_transform(body, chat_create_params.ChatCreateParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=str,
            stream=True,
            stream_cls=AsyncStream[ChatCreateResponse],
        )


class ChatResourceWithRawResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.create = to_raw_response_wrapper(
            chat.create,
        )

    @cached_property
    def conversations(self) -> ConversationsResourceWithRawResponse:
        return ConversationsResourceWithRawResponse(self._chat.conversations)


class AsyncChatResourceWithRawResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.create = async_to_raw_response_wrapper(
            chat.create,
        )

    @cached_property
    def conversations(self) -> AsyncConversationsResourceWithRawResponse:
        return AsyncConversationsResourceWithRawResponse(self._chat.conversations)


class ChatResourceWithStreamingResponse:
    def __init__(self, chat: ChatResource) -> None:
        self._chat = chat

        self.create = to_streamed_response_wrapper(
            chat.create,
        )

    @cached_property
    def conversations(self) -> ConversationsResourceWithStreamingResponse:
        return ConversationsResourceWithStreamingResponse(self._chat.conversations)


class AsyncChatResourceWithStreamingResponse:
    def __init__(self, chat: AsyncChatResource) -> None:
        self._chat = chat

        self.create = async_to_streamed_response_wrapper(
            chat.create,
        )

    @cached_property
    def conversations(self) -> AsyncConversationsResourceWithStreamingResponse:
        return AsyncConversationsResourceWithStreamingResponse(self._chat.conversations)
