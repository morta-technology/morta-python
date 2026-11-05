# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.organisation import api_key_update_params, api_key_api_key_params
from ...types.user.api_key import APIKey
from ...types.organisation.api_key_retrieve_api_key_response import APIKeyRetrieveAPIKeyResponse

__all__ = ["APIKeyResource", "AsyncAPIKeyResource"]


class APIKeyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> APIKeyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return APIKeyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIKeyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return APIKeyResourceWithStreamingResponse(self)

    def update(
        self,
        api_key_public_id: str,
        *,
        organisation_public_id: str,
        access_level: Literal[0, 1],
        document_restrictions: Optional[SequenceNotStr[str]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        project_restrictions: Optional[SequenceNotStr[str]] | Omit = omit,
        site_restrictions: Optional[SequenceNotStr[str]] | Omit = omit,
        table_restrictions: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """
        Update an API key for the service account associated with the specified
        organisation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organisation_public_id:
            raise ValueError(
                f"Expected a non-empty value for `organisation_public_id` but received {organisation_public_id!r}"
            )
        if not api_key_public_id:
            raise ValueError(f"Expected a non-empty value for `api_key_public_id` but received {api_key_public_id!r}")
        return self._put(
            path_template(
                "/v1/organisation/{organisation_public_id}/api-key/{api_key_public_id}",
                organisation_public_id=organisation_public_id,
                api_key_public_id=api_key_public_id,
            ),
            body=maybe_transform(
                {
                    "access_level": access_level,
                    "document_restrictions": document_restrictions,
                    "name": name,
                    "project_restrictions": project_restrictions,
                    "site_restrictions": site_restrictions,
                    "table_restrictions": table_restrictions,
                },
                api_key_update_params.APIKeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    def delete(
        self,
        api_key_public_id: str,
        *,
        organisation_public_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an API key for the service account associated with the specified
        organisation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organisation_public_id:
            raise ValueError(
                f"Expected a non-empty value for `organisation_public_id` but received {organisation_public_id!r}"
            )
        if not api_key_public_id:
            raise ValueError(f"Expected a non-empty value for `api_key_public_id` but received {api_key_public_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template(
                "/v1/organisation/{organisation_public_id}/api-key/{api_key_public_id}",
                organisation_public_id=organisation_public_id,
                api_key_public_id=api_key_public_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def api_key(
        self,
        organisation_public_id: str,
        *,
        access_level: Literal[0, 1],
        document_restrictions: Optional[SequenceNotStr[str]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        project_restrictions: Optional[SequenceNotStr[str]] | Omit = omit,
        site_restrictions: Optional[SequenceNotStr[str]] | Omit = omit,
        table_restrictions: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """
        Create a new API key for the service account associated with the specified
        organisation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organisation_public_id:
            raise ValueError(
                f"Expected a non-empty value for `organisation_public_id` but received {organisation_public_id!r}"
            )
        return self._post(
            path_template(
                "/v1/organisation/{organisation_public_id}/api-key", organisation_public_id=organisation_public_id
            ),
            body=maybe_transform(
                {
                    "access_level": access_level,
                    "document_restrictions": document_restrictions,
                    "name": name,
                    "project_restrictions": project_restrictions,
                    "site_restrictions": site_restrictions,
                    "table_restrictions": table_restrictions,
                },
                api_key_api_key_params.APIKeyAPIKeyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    def retrieve_api_key(
        self,
        organisation_public_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyRetrieveAPIKeyResponse:
        """
        Retrieve all API keys for the service account associated with the specified
        organisation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organisation_public_id:
            raise ValueError(
                f"Expected a non-empty value for `organisation_public_id` but received {organisation_public_id!r}"
            )
        return self._get(
            path_template(
                "/v1/organisation/{organisation_public_id}/api-key", organisation_public_id=organisation_public_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyRetrieveAPIKeyResponse,
        )


class AsyncAPIKeyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAPIKeyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIKeyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIKeyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return AsyncAPIKeyResourceWithStreamingResponse(self)

    async def update(
        self,
        api_key_public_id: str,
        *,
        organisation_public_id: str,
        access_level: Literal[0, 1],
        document_restrictions: Optional[SequenceNotStr[str]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        project_restrictions: Optional[SequenceNotStr[str]] | Omit = omit,
        site_restrictions: Optional[SequenceNotStr[str]] | Omit = omit,
        table_restrictions: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """
        Update an API key for the service account associated with the specified
        organisation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organisation_public_id:
            raise ValueError(
                f"Expected a non-empty value for `organisation_public_id` but received {organisation_public_id!r}"
            )
        if not api_key_public_id:
            raise ValueError(f"Expected a non-empty value for `api_key_public_id` but received {api_key_public_id!r}")
        return await self._put(
            path_template(
                "/v1/organisation/{organisation_public_id}/api-key/{api_key_public_id}",
                organisation_public_id=organisation_public_id,
                api_key_public_id=api_key_public_id,
            ),
            body=await async_maybe_transform(
                {
                    "access_level": access_level,
                    "document_restrictions": document_restrictions,
                    "name": name,
                    "project_restrictions": project_restrictions,
                    "site_restrictions": site_restrictions,
                    "table_restrictions": table_restrictions,
                },
                api_key_update_params.APIKeyUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    async def delete(
        self,
        api_key_public_id: str,
        *,
        organisation_public_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Delete an API key for the service account associated with the specified
        organisation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organisation_public_id:
            raise ValueError(
                f"Expected a non-empty value for `organisation_public_id` but received {organisation_public_id!r}"
            )
        if not api_key_public_id:
            raise ValueError(f"Expected a non-empty value for `api_key_public_id` but received {api_key_public_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template(
                "/v1/organisation/{organisation_public_id}/api-key/{api_key_public_id}",
                organisation_public_id=organisation_public_id,
                api_key_public_id=api_key_public_id,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def api_key(
        self,
        organisation_public_id: str,
        *,
        access_level: Literal[0, 1],
        document_restrictions: Optional[SequenceNotStr[str]] | Omit = omit,
        name: Optional[str] | Omit = omit,
        project_restrictions: Optional[SequenceNotStr[str]] | Omit = omit,
        site_restrictions: Optional[SequenceNotStr[str]] | Omit = omit,
        table_restrictions: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """
        Create a new API key for the service account associated with the specified
        organisation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organisation_public_id:
            raise ValueError(
                f"Expected a non-empty value for `organisation_public_id` but received {organisation_public_id!r}"
            )
        return await self._post(
            path_template(
                "/v1/organisation/{organisation_public_id}/api-key", organisation_public_id=organisation_public_id
            ),
            body=await async_maybe_transform(
                {
                    "access_level": access_level,
                    "document_restrictions": document_restrictions,
                    "name": name,
                    "project_restrictions": project_restrictions,
                    "site_restrictions": site_restrictions,
                    "table_restrictions": table_restrictions,
                },
                api_key_api_key_params.APIKeyAPIKeyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    async def retrieve_api_key(
        self,
        organisation_public_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyRetrieveAPIKeyResponse:
        """
        Retrieve all API keys for the service account associated with the specified
        organisation.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not organisation_public_id:
            raise ValueError(
                f"Expected a non-empty value for `organisation_public_id` but received {organisation_public_id!r}"
            )
        return await self._get(
            path_template(
                "/v1/organisation/{organisation_public_id}/api-key", organisation_public_id=organisation_public_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyRetrieveAPIKeyResponse,
        )


class APIKeyResourceWithRawResponse:
    def __init__(self, api_key: APIKeyResource) -> None:
        self._api_key = api_key

        self.update = to_raw_response_wrapper(
            api_key.update,
        )
        self.delete = to_raw_response_wrapper(
            api_key.delete,
        )
        self.api_key = to_raw_response_wrapper(
            api_key.api_key,
        )
        self.retrieve_api_key = to_raw_response_wrapper(
            api_key.retrieve_api_key,
        )


class AsyncAPIKeyResourceWithRawResponse:
    def __init__(self, api_key: AsyncAPIKeyResource) -> None:
        self._api_key = api_key

        self.update = async_to_raw_response_wrapper(
            api_key.update,
        )
        self.delete = async_to_raw_response_wrapper(
            api_key.delete,
        )
        self.api_key = async_to_raw_response_wrapper(
            api_key.api_key,
        )
        self.retrieve_api_key = async_to_raw_response_wrapper(
            api_key.retrieve_api_key,
        )


class APIKeyResourceWithStreamingResponse:
    def __init__(self, api_key: APIKeyResource) -> None:
        self._api_key = api_key

        self.update = to_streamed_response_wrapper(
            api_key.update,
        )
        self.delete = to_streamed_response_wrapper(
            api_key.delete,
        )
        self.api_key = to_streamed_response_wrapper(
            api_key.api_key,
        )
        self.retrieve_api_key = to_streamed_response_wrapper(
            api_key.retrieve_api_key,
        )


class AsyncAPIKeyResourceWithStreamingResponse:
    def __init__(self, api_key: AsyncAPIKeyResource) -> None:
        self._api_key = api_key

        self.update = async_to_streamed_response_wrapper(
            api_key.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            api_key.delete,
        )
        self.api_key = async_to_streamed_response_wrapper(
            api_key.api_key,
        )
        self.retrieve_api_key = async_to_streamed_response_wrapper(
            api_key.retrieve_api_key,
        )
