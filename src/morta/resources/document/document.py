# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ...types import (
    document_create_params,
    document_export_params,
    document_update_params,
    document_retrieve_params,
    document_create_sections_params,
    document_get_deleted_sections_params,
    document_update_section_order_params,
    document_create_multiple_sections_params,
    document_update_multiple_sections_params,
    document_update_views_permissions_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from .duplicate import (
    DuplicateResource,
    AsyncDuplicateResource,
    DuplicateResourceWithRawResponse,
    AsyncDuplicateResourceWithRawResponse,
    DuplicateResourceWithStreamingResponse,
    AsyncDuplicateResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
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
from ..._base_client import make_request_options
from .section.section import (
    SectionResource,
    AsyncSectionResource,
    SectionResourceWithRawResponse,
    AsyncSectionResourceWithRawResponse,
    SectionResourceWithStreamingResponse,
    AsyncSectionResourceWithStreamingResponse,
)
from ...types.document_create_response import DocumentCreateResponse
from ...types.document_delete_response import DocumentDeleteResponse
from ...types.document_update_response import DocumentUpdateResponse
from ...types.document_restore_response import DocumentRestoreResponse
from ...types.base_request_context_param import BaseRequestContextParam
from ...types.document_retrieve_response import DocumentRetrieveResponse
from ...types.document_sync_template_response import DocumentSyncTemplateResponse
from ...types.document_create_sections_response import DocumentCreateSectionsResponse
from ...types.document.create_document_section_param import CreateDocumentSectionParam
from ...types.document_get_deleted_sections_response import DocumentGetDeletedSectionsResponse
from ...types.document_update_section_order_response import DocumentUpdateSectionOrderResponse
from ...types.document_get_duplicated_children_response import DocumentGetDuplicatedChildrenResponse
from ...types.document_create_multiple_sections_response import DocumentCreateMultipleSectionsResponse
from ...types.document_update_multiple_sections_response import DocumentUpdateMultipleSectionsResponse
from ...types.document_update_views_permissions_response import DocumentUpdateViewsPermissionsResponse

__all__ = ["DocumentResource", "AsyncDocumentResource"]


class DocumentResource(SyncAPIResource):
    @cached_property
    def duplicate(self) -> DuplicateResource:
        return DuplicateResource(self._client)

    @cached_property
    def section(self) -> SectionResource:
        return SectionResource(self._client)

    @cached_property
    def with_raw_response(self) -> DocumentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return DocumentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DocumentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return DocumentResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        project_id: str,
        type: str,
        context: BaseRequestContextParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentCreateResponse:
        """
        Create a new document in a specified hub

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/document",
            body=maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "type": type,
                    "context": context,
                },
                document_create_params.DocumentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentCreateResponse,
        )

    def retrieve(
        self,
        document_id: str,
        *,
        exclude_children: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentRetrieveResponse:
        """
        Retrieve detailed information of a specific document by its UUID

        Args:
          exclude_children: Flag to exclude child elements from the document response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._get(
            path_template("/v1/document/{document_id}", document_id=document_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"exclude_children": exclude_children}, document_retrieve_params.DocumentRetrieveParams
                ),
            ),
            cast_to=DocumentRetrieveResponse,
        )

    def update(
        self,
        document_id: str,
        *,
        allow_comments: bool | Omit = omit,
        context: BaseRequestContextParam | Omit = omit,
        description: document_update_params.Description | Omit = omit,
        expand_by_default: bool | Omit = omit,
        is_template: bool | Omit = omit,
        locked_template: bool | Omit = omit,
        logo: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        plaintext_description: Optional[str] | Omit = omit,
        type: Optional[str] | Omit = omit,
        variables: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentUpdateResponse:
        """
        Update an existing documents's details by document ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._put(
            path_template("/v1/document/{document_id}", document_id=document_id),
            body=maybe_transform(
                {
                    "allow_comments": allow_comments,
                    "context": context,
                    "description": description,
                    "expand_by_default": expand_by_default,
                    "is_template": is_template,
                    "locked_template": locked_template,
                    "logo": logo,
                    "name": name,
                    "plaintext_description": plaintext_description,
                    "type": type,
                    "variables": variables,
                },
                document_update_params.DocumentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUpdateResponse,
        )

    def delete(
        self,
        document_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentDeleteResponse:
        """
        Delete a document identified by its UUID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._delete(
            path_template("/v1/document/{document_id}", document_id=document_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentDeleteResponse,
        )

    def create_multiple_sections(
        self,
        document_id: str,
        *,
        sections: Iterable[CreateDocumentSectionParam],
        context: BaseRequestContextParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentCreateMultipleSectionsResponse:
        """
        Create multiple new sections within a specified document, each with an optional
        parent section

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._post(
            path_template("/v1/document/{document_id}/multiple-section", document_id=document_id),
            body=maybe_transform(
                {
                    "sections": sections,
                    "context": context,
                },
                document_create_multiple_sections_params.DocumentCreateMultipleSectionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentCreateMultipleSectionsResponse,
        )

    def create_sections(
        self,
        document_id: str,
        *,
        context: BaseRequestContextParam | Omit = omit,
        details: Iterable[CreateDocumentSectionParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentCreateSectionsResponse:
        """
        Create multiple new sections within a document

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._post(
            path_template("/v1/document/{document_id}/sections", document_id=document_id),
            body=maybe_transform(
                {
                    "context": context,
                    "details": details,
                },
                document_create_sections_params.DocumentCreateSectionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentCreateSectionsResponse,
        )

    def export(
        self,
        document_id: str,
        *,
        page_format: Literal["A1", "A2", "A3", "A4", "letter", "legal"] | Omit = omit,
        page_orientation: Literal["portrait", "landscape"] | Omit = omit,
        table_links: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Export a specific document by its UUID

        Args:
          page_format: Page format for the export

          page_orientation: Page orientation for the export

          table_links: Include table links in the export

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        extra_headers = {
            "Accept": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            **(extra_headers or {}),
        }
        return self._get(
            path_template("/v1/document/{document_id}/export", document_id=document_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "page_format": page_format,
                        "page_orientation": page_orientation,
                        "table_links": table_links,
                    },
                    document_export_params.DocumentExportParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )

    def get_deleted_sections(
        self,
        document_id: str,
        *,
        process_section_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentGetDeletedSectionsResponse:
        """
        Retrieve all deleted sections of a specific document, with an optional filter
        for a specific document section

        Args:
          process_section_id: Optional UUID of a specific document section to filter deleted sections

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._get(
            path_template("/v1/document/{document_id}/deletedsections", document_id=document_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"process_section_id": process_section_id},
                    document_get_deleted_sections_params.DocumentGetDeletedSectionsParams,
                ),
            ),
            cast_to=DocumentGetDeletedSectionsResponse,
        )

    def get_duplicated_children(
        self,
        document_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentGetDuplicatedChildrenResponse:
        """
        Get duplicated children of a document

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._get(
            path_template("/v1/document/{document_id}/duplicated-children", document_id=document_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentGetDuplicatedChildrenResponse,
        )

    def restore(
        self,
        document_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentRestoreResponse:
        """
        Restore a deleted document identified by its UUID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._put(
            path_template("/v1/document/{document_id}/restore", document_id=document_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentRestoreResponse,
        )

    def sync_template(
        self,
        document_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentSyncTemplateResponse:
        """
        Sync template changes to children of a document

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._get(
            path_template("/v1/document/{document_id}/sync-template", document_id=document_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentSyncTemplateResponse,
        )

    def update_multiple_sections(
        self,
        document_id: str,
        *,
        sections: Iterable[document_update_multiple_sections_params.Section],
        context: BaseRequestContextParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentUpdateMultipleSectionsResponse:
        """
        Update multiple existing document sections.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._put(
            path_template("/v1/document/{document_id}/update-multiple-section", document_id=document_id),
            body=maybe_transform(
                {
                    "sections": sections,
                    "context": context,
                },
                document_update_multiple_sections_params.DocumentUpdateMultipleSectionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUpdateMultipleSectionsResponse,
        )

    def update_section_order(
        self,
        document_id: str,
        *,
        context: BaseRequestContextParam | Omit = omit,
        process_sections: Iterable[document_update_section_order_params.ProcessSection] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentUpdateSectionOrderResponse:
        """
        Update the order of document sections within a document.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return self._put(
            path_template("/v1/document/{document_id}/changesectionorder", document_id=document_id),
            body=maybe_transform(
                {
                    "context": context,
                    "process_sections": process_sections,
                },
                document_update_section_order_params.DocumentUpdateSectionOrderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUpdateSectionOrderResponse,
        )

    def update_views_permissions(
        self,
        *,
        resource_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentUpdateViewsPermissionsResponse:
        """
        Update permissions for all views using as reference the permissions in a
        document.

        Args:
          resource_id: UUID of the document for which to retrieve permissions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/document/sync-views-permissions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {"resource_id": resource_id},
                    document_update_views_permissions_params.DocumentUpdateViewsPermissionsParams,
                ),
            ),
            cast_to=DocumentUpdateViewsPermissionsResponse,
        )


class AsyncDocumentResource(AsyncAPIResource):
    @cached_property
    def duplicate(self) -> AsyncDuplicateResource:
        return AsyncDuplicateResource(self._client)

    @cached_property
    def section(self) -> AsyncSectionResource:
        return AsyncSectionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDocumentResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDocumentResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDocumentResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return AsyncDocumentResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        project_id: str,
        type: str,
        context: BaseRequestContextParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentCreateResponse:
        """
        Create a new document in a specified hub

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/document",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "project_id": project_id,
                    "type": type,
                    "context": context,
                },
                document_create_params.DocumentCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentCreateResponse,
        )

    async def retrieve(
        self,
        document_id: str,
        *,
        exclude_children: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentRetrieveResponse:
        """
        Retrieve detailed information of a specific document by its UUID

        Args:
          exclude_children: Flag to exclude child elements from the document response

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._get(
            path_template("/v1/document/{document_id}", document_id=document_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"exclude_children": exclude_children}, document_retrieve_params.DocumentRetrieveParams
                ),
            ),
            cast_to=DocumentRetrieveResponse,
        )

    async def update(
        self,
        document_id: str,
        *,
        allow_comments: bool | Omit = omit,
        context: BaseRequestContextParam | Omit = omit,
        description: document_update_params.Description | Omit = omit,
        expand_by_default: bool | Omit = omit,
        is_template: bool | Omit = omit,
        locked_template: bool | Omit = omit,
        logo: Optional[str] | Omit = omit,
        name: Optional[str] | Omit = omit,
        plaintext_description: Optional[str] | Omit = omit,
        type: Optional[str] | Omit = omit,
        variables: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentUpdateResponse:
        """
        Update an existing documents's details by document ID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._put(
            path_template("/v1/document/{document_id}", document_id=document_id),
            body=await async_maybe_transform(
                {
                    "allow_comments": allow_comments,
                    "context": context,
                    "description": description,
                    "expand_by_default": expand_by_default,
                    "is_template": is_template,
                    "locked_template": locked_template,
                    "logo": logo,
                    "name": name,
                    "plaintext_description": plaintext_description,
                    "type": type,
                    "variables": variables,
                },
                document_update_params.DocumentUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUpdateResponse,
        )

    async def delete(
        self,
        document_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentDeleteResponse:
        """
        Delete a document identified by its UUID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._delete(
            path_template("/v1/document/{document_id}", document_id=document_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentDeleteResponse,
        )

    async def create_multiple_sections(
        self,
        document_id: str,
        *,
        sections: Iterable[CreateDocumentSectionParam],
        context: BaseRequestContextParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentCreateMultipleSectionsResponse:
        """
        Create multiple new sections within a specified document, each with an optional
        parent section

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._post(
            path_template("/v1/document/{document_id}/multiple-section", document_id=document_id),
            body=await async_maybe_transform(
                {
                    "sections": sections,
                    "context": context,
                },
                document_create_multiple_sections_params.DocumentCreateMultipleSectionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentCreateMultipleSectionsResponse,
        )

    async def create_sections(
        self,
        document_id: str,
        *,
        context: BaseRequestContextParam | Omit = omit,
        details: Iterable[CreateDocumentSectionParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentCreateSectionsResponse:
        """
        Create multiple new sections within a document

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._post(
            path_template("/v1/document/{document_id}/sections", document_id=document_id),
            body=await async_maybe_transform(
                {
                    "context": context,
                    "details": details,
                },
                document_create_sections_params.DocumentCreateSectionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentCreateSectionsResponse,
        )

    async def export(
        self,
        document_id: str,
        *,
        page_format: Literal["A1", "A2", "A3", "A4", "letter", "legal"] | Omit = omit,
        page_orientation: Literal["portrait", "landscape"] | Omit = omit,
        table_links: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Export a specific document by its UUID

        Args:
          page_format: Page format for the export

          page_orientation: Page orientation for the export

          table_links: Include table links in the export

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        extra_headers = {
            "Accept": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            **(extra_headers or {}),
        }
        return await self._get(
            path_template("/v1/document/{document_id}/export", document_id=document_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "page_format": page_format,
                        "page_orientation": page_orientation,
                        "table_links": table_links,
                    },
                    document_export_params.DocumentExportParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )

    async def get_deleted_sections(
        self,
        document_id: str,
        *,
        process_section_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentGetDeletedSectionsResponse:
        """
        Retrieve all deleted sections of a specific document, with an optional filter
        for a specific document section

        Args:
          process_section_id: Optional UUID of a specific document section to filter deleted sections

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._get(
            path_template("/v1/document/{document_id}/deletedsections", document_id=document_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"process_section_id": process_section_id},
                    document_get_deleted_sections_params.DocumentGetDeletedSectionsParams,
                ),
            ),
            cast_to=DocumentGetDeletedSectionsResponse,
        )

    async def get_duplicated_children(
        self,
        document_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentGetDuplicatedChildrenResponse:
        """
        Get duplicated children of a document

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._get(
            path_template("/v1/document/{document_id}/duplicated-children", document_id=document_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentGetDuplicatedChildrenResponse,
        )

    async def restore(
        self,
        document_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentRestoreResponse:
        """
        Restore a deleted document identified by its UUID

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._put(
            path_template("/v1/document/{document_id}/restore", document_id=document_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentRestoreResponse,
        )

    async def sync_template(
        self,
        document_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentSyncTemplateResponse:
        """
        Sync template changes to children of a document

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._get(
            path_template("/v1/document/{document_id}/sync-template", document_id=document_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentSyncTemplateResponse,
        )

    async def update_multiple_sections(
        self,
        document_id: str,
        *,
        sections: Iterable[document_update_multiple_sections_params.Section],
        context: BaseRequestContextParam | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentUpdateMultipleSectionsResponse:
        """
        Update multiple existing document sections.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._put(
            path_template("/v1/document/{document_id}/update-multiple-section", document_id=document_id),
            body=await async_maybe_transform(
                {
                    "sections": sections,
                    "context": context,
                },
                document_update_multiple_sections_params.DocumentUpdateMultipleSectionsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUpdateMultipleSectionsResponse,
        )

    async def update_section_order(
        self,
        document_id: str,
        *,
        context: BaseRequestContextParam | Omit = omit,
        process_sections: Iterable[document_update_section_order_params.ProcessSection] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentUpdateSectionOrderResponse:
        """
        Update the order of document sections within a document.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not document_id:
            raise ValueError(f"Expected a non-empty value for `document_id` but received {document_id!r}")
        return await self._put(
            path_template("/v1/document/{document_id}/changesectionorder", document_id=document_id),
            body=await async_maybe_transform(
                {
                    "context": context,
                    "process_sections": process_sections,
                },
                document_update_section_order_params.DocumentUpdateSectionOrderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DocumentUpdateSectionOrderResponse,
        )

    async def update_views_permissions(
        self,
        *,
        resource_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DocumentUpdateViewsPermissionsResponse:
        """
        Update permissions for all views using as reference the permissions in a
        document.

        Args:
          resource_id: UUID of the document for which to retrieve permissions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/document/sync-views-permissions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"resource_id": resource_id},
                    document_update_views_permissions_params.DocumentUpdateViewsPermissionsParams,
                ),
            ),
            cast_to=DocumentUpdateViewsPermissionsResponse,
        )


class DocumentResourceWithRawResponse:
    def __init__(self, document: DocumentResource) -> None:
        self._document = document

        self.create = to_raw_response_wrapper(
            document.create,
        )
        self.retrieve = to_raw_response_wrapper(
            document.retrieve,
        )
        self.update = to_raw_response_wrapper(
            document.update,
        )
        self.delete = to_raw_response_wrapper(
            document.delete,
        )
        self.create_multiple_sections = to_raw_response_wrapper(
            document.create_multiple_sections,
        )
        self.create_sections = to_raw_response_wrapper(
            document.create_sections,
        )
        self.export = to_custom_raw_response_wrapper(
            document.export,
            BinaryAPIResponse,
        )
        self.get_deleted_sections = to_raw_response_wrapper(
            document.get_deleted_sections,
        )
        self.get_duplicated_children = to_raw_response_wrapper(
            document.get_duplicated_children,
        )
        self.restore = to_raw_response_wrapper(
            document.restore,
        )
        self.sync_template = to_raw_response_wrapper(
            document.sync_template,
        )
        self.update_multiple_sections = to_raw_response_wrapper(
            document.update_multiple_sections,
        )
        self.update_section_order = to_raw_response_wrapper(
            document.update_section_order,
        )
        self.update_views_permissions = to_raw_response_wrapper(
            document.update_views_permissions,
        )

    @cached_property
    def duplicate(self) -> DuplicateResourceWithRawResponse:
        return DuplicateResourceWithRawResponse(self._document.duplicate)

    @cached_property
    def section(self) -> SectionResourceWithRawResponse:
        return SectionResourceWithRawResponse(self._document.section)


class AsyncDocumentResourceWithRawResponse:
    def __init__(self, document: AsyncDocumentResource) -> None:
        self._document = document

        self.create = async_to_raw_response_wrapper(
            document.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            document.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            document.update,
        )
        self.delete = async_to_raw_response_wrapper(
            document.delete,
        )
        self.create_multiple_sections = async_to_raw_response_wrapper(
            document.create_multiple_sections,
        )
        self.create_sections = async_to_raw_response_wrapper(
            document.create_sections,
        )
        self.export = async_to_custom_raw_response_wrapper(
            document.export,
            AsyncBinaryAPIResponse,
        )
        self.get_deleted_sections = async_to_raw_response_wrapper(
            document.get_deleted_sections,
        )
        self.get_duplicated_children = async_to_raw_response_wrapper(
            document.get_duplicated_children,
        )
        self.restore = async_to_raw_response_wrapper(
            document.restore,
        )
        self.sync_template = async_to_raw_response_wrapper(
            document.sync_template,
        )
        self.update_multiple_sections = async_to_raw_response_wrapper(
            document.update_multiple_sections,
        )
        self.update_section_order = async_to_raw_response_wrapper(
            document.update_section_order,
        )
        self.update_views_permissions = async_to_raw_response_wrapper(
            document.update_views_permissions,
        )

    @cached_property
    def duplicate(self) -> AsyncDuplicateResourceWithRawResponse:
        return AsyncDuplicateResourceWithRawResponse(self._document.duplicate)

    @cached_property
    def section(self) -> AsyncSectionResourceWithRawResponse:
        return AsyncSectionResourceWithRawResponse(self._document.section)


class DocumentResourceWithStreamingResponse:
    def __init__(self, document: DocumentResource) -> None:
        self._document = document

        self.create = to_streamed_response_wrapper(
            document.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            document.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            document.update,
        )
        self.delete = to_streamed_response_wrapper(
            document.delete,
        )
        self.create_multiple_sections = to_streamed_response_wrapper(
            document.create_multiple_sections,
        )
        self.create_sections = to_streamed_response_wrapper(
            document.create_sections,
        )
        self.export = to_custom_streamed_response_wrapper(
            document.export,
            StreamedBinaryAPIResponse,
        )
        self.get_deleted_sections = to_streamed_response_wrapper(
            document.get_deleted_sections,
        )
        self.get_duplicated_children = to_streamed_response_wrapper(
            document.get_duplicated_children,
        )
        self.restore = to_streamed_response_wrapper(
            document.restore,
        )
        self.sync_template = to_streamed_response_wrapper(
            document.sync_template,
        )
        self.update_multiple_sections = to_streamed_response_wrapper(
            document.update_multiple_sections,
        )
        self.update_section_order = to_streamed_response_wrapper(
            document.update_section_order,
        )
        self.update_views_permissions = to_streamed_response_wrapper(
            document.update_views_permissions,
        )

    @cached_property
    def duplicate(self) -> DuplicateResourceWithStreamingResponse:
        return DuplicateResourceWithStreamingResponse(self._document.duplicate)

    @cached_property
    def section(self) -> SectionResourceWithStreamingResponse:
        return SectionResourceWithStreamingResponse(self._document.section)


class AsyncDocumentResourceWithStreamingResponse:
    def __init__(self, document: AsyncDocumentResource) -> None:
        self._document = document

        self.create = async_to_streamed_response_wrapper(
            document.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            document.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            document.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            document.delete,
        )
        self.create_multiple_sections = async_to_streamed_response_wrapper(
            document.create_multiple_sections,
        )
        self.create_sections = async_to_streamed_response_wrapper(
            document.create_sections,
        )
        self.export = async_to_custom_streamed_response_wrapper(
            document.export,
            AsyncStreamedBinaryAPIResponse,
        )
        self.get_deleted_sections = async_to_streamed_response_wrapper(
            document.get_deleted_sections,
        )
        self.get_duplicated_children = async_to_streamed_response_wrapper(
            document.get_duplicated_children,
        )
        self.restore = async_to_streamed_response_wrapper(
            document.restore,
        )
        self.sync_template = async_to_streamed_response_wrapper(
            document.sync_template,
        )
        self.update_multiple_sections = async_to_streamed_response_wrapper(
            document.update_multiple_sections,
        )
        self.update_section_order = async_to_streamed_response_wrapper(
            document.update_section_order,
        )
        self.update_views_permissions = async_to_streamed_response_wrapper(
            document.update_views_permissions,
        )

    @cached_property
    def duplicate(self) -> AsyncDuplicateResourceWithStreamingResponse:
        return AsyncDuplicateResourceWithStreamingResponse(self._document.duplicate)

    @cached_property
    def section(self) -> AsyncSectionResourceWithStreamingResponse:
        return AsyncSectionResourceWithStreamingResponse(self._document.section)
