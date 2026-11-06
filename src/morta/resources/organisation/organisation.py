# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional

import httpx

from .site import (
    SiteResource,
    AsyncSiteResource,
    SiteResourceWithRawResponse,
    AsyncSiteResourceWithRawResponse,
    SiteResourceWithStreamingResponse,
    AsyncSiteResourceWithStreamingResponse,
)
from .user import (
    UserResource,
    AsyncUserResource,
    UserResourceWithRawResponse,
    AsyncUserResourceWithRawResponse,
    UserResourceWithStreamingResponse,
    AsyncUserResourceWithStreamingResponse,
)
from .teams import (
    TeamsResource,
    AsyncTeamsResource,
    TeamsResourceWithRawResponse,
    AsyncTeamsResourceWithRawResponse,
    TeamsResourceWithStreamingResponse,
    AsyncTeamsResourceWithStreamingResponse,
)
from ...types import organisation_update_params
from .api_key import (
    APIKeyResource,
    AsyncAPIKeyResource,
    APIKeyResourceWithRawResponse,
    AsyncAPIKeyResourceWithRawResponse,
    APIKeyResourceWithStreamingResponse,
    AsyncAPIKeyResourceWithStreamingResponse,
)
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
from ..._base_client import make_request_options
from ...types.organisation.organisation import Organisation
from ...types.create_organisation_user_param import CreateOrganisationUserParam
from ...types.organisation_retrieve_hubs_response import OrganisationRetrieveHubsResponse
from ...types.organisation_retrieve_sites_response import OrganisationRetrieveSitesResponse

__all__ = ["OrganisationResource", "AsyncOrganisationResource"]


class OrganisationResource(SyncAPIResource):
    @cached_property
    def api_key(self) -> APIKeyResource:
        return APIKeyResource(self._client)

    @cached_property
    def site(self) -> SiteResource:
        return SiteResource(self._client)

    @cached_property
    def teams(self) -> TeamsResource:
        return TeamsResource(self._client)

    @cached_property
    def user(self) -> UserResource:
        return UserResource(self._client)

    @cached_property
    def with_raw_response(self) -> OrganisationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return OrganisationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OrganisationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return OrganisationResourceWithStreamingResponse(self)

    def retrieve(
        self,
        organisation_public_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Organisation:
        """
        Retrieve details of a specific organisation by its public ID.

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
            path_template("/v1/organisation/{organisation_public_id}", organisation_public_id=organisation_public_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Organisation,
        )

    def update(
        self,
        organisation_public_id: str,
        *,
        disable_personal_view_saving: bool | Omit = omit,
        enable_user_api_keys: bool | Omit = omit,
        enforce_login: Optional[str] | Omit = omit,
        idp_certificate: Optional[str] | Omit = omit,
        idp_issuer: Optional[str] | Omit = omit,
        idp_sso_url: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        restrict_hub_creation: bool | Omit = omit,
        restrict_sync_configuration: bool | Omit = omit,
        users: Iterable[CreateOrganisationUserParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Organisation:
        """
        Update details of a specific organisation by its public ID.

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
        return self._put(
            path_template("/v1/organisation/{organisation_public_id}", organisation_public_id=organisation_public_id),
            body=maybe_transform(
                {
                    "disable_personal_view_saving": disable_personal_view_saving,
                    "enable_user_api_keys": enable_user_api_keys,
                    "enforce_login": enforce_login,
                    "idp_certificate": idp_certificate,
                    "idp_issuer": idp_issuer,
                    "idp_sso_url": idp_sso_url,
                    "name": name,
                    "restrict_hub_creation": restrict_hub_creation,
                    "restrict_sync_configuration": restrict_sync_configuration,
                    "users": users,
                },
                organisation_update_params.OrganisationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Organisation,
        )

    def retrieve_hubs(
        self,
        organisation_public_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganisationRetrieveHubsResponse:
        """
        Retrieve all hubs associated with a specific organisation by its public ID.

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
                "/v1/organisation/{organisation_public_id}/hubs", organisation_public_id=organisation_public_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganisationRetrieveHubsResponse,
        )

    def retrieve_sites(
        self,
        organisation_public_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganisationRetrieveSitesResponse:
        """
        Retrieve all sites belonging to the specified organisation.

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
                "/v1/organisation/{organisation_public_id}/sites", organisation_public_id=organisation_public_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganisationRetrieveSitesResponse,
        )


class AsyncOrganisationResource(AsyncAPIResource):
    @cached_property
    def api_key(self) -> AsyncAPIKeyResource:
        return AsyncAPIKeyResource(self._client)

    @cached_property
    def site(self) -> AsyncSiteResource:
        return AsyncSiteResource(self._client)

    @cached_property
    def teams(self) -> AsyncTeamsResource:
        return AsyncTeamsResource(self._client)

    @cached_property
    def user(self) -> AsyncUserResource:
        return AsyncUserResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOrganisationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOrganisationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOrganisationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return AsyncOrganisationResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        organisation_public_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Organisation:
        """
        Retrieve details of a specific organisation by its public ID.

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
            path_template("/v1/organisation/{organisation_public_id}", organisation_public_id=organisation_public_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Organisation,
        )

    async def update(
        self,
        organisation_public_id: str,
        *,
        disable_personal_view_saving: bool | Omit = omit,
        enable_user_api_keys: bool | Omit = omit,
        enforce_login: Optional[str] | Omit = omit,
        idp_certificate: Optional[str] | Omit = omit,
        idp_issuer: Optional[str] | Omit = omit,
        idp_sso_url: Optional[str] | Omit = omit,
        name: str | Omit = omit,
        restrict_hub_creation: bool | Omit = omit,
        restrict_sync_configuration: bool | Omit = omit,
        users: Iterable[CreateOrganisationUserParam] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Organisation:
        """
        Update details of a specific organisation by its public ID.

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
        return await self._put(
            path_template("/v1/organisation/{organisation_public_id}", organisation_public_id=organisation_public_id),
            body=await async_maybe_transform(
                {
                    "disable_personal_view_saving": disable_personal_view_saving,
                    "enable_user_api_keys": enable_user_api_keys,
                    "enforce_login": enforce_login,
                    "idp_certificate": idp_certificate,
                    "idp_issuer": idp_issuer,
                    "idp_sso_url": idp_sso_url,
                    "name": name,
                    "restrict_hub_creation": restrict_hub_creation,
                    "restrict_sync_configuration": restrict_sync_configuration,
                    "users": users,
                },
                organisation_update_params.OrganisationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Organisation,
        )

    async def retrieve_hubs(
        self,
        organisation_public_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganisationRetrieveHubsResponse:
        """
        Retrieve all hubs associated with a specific organisation by its public ID.

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
                "/v1/organisation/{organisation_public_id}/hubs", organisation_public_id=organisation_public_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganisationRetrieveHubsResponse,
        )

    async def retrieve_sites(
        self,
        organisation_public_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OrganisationRetrieveSitesResponse:
        """
        Retrieve all sites belonging to the specified organisation.

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
                "/v1/organisation/{organisation_public_id}/sites", organisation_public_id=organisation_public_id
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OrganisationRetrieveSitesResponse,
        )


class OrganisationResourceWithRawResponse:
    def __init__(self, organisation: OrganisationResource) -> None:
        self._organisation = organisation

        self.retrieve = to_raw_response_wrapper(
            organisation.retrieve,
        )
        self.update = to_raw_response_wrapper(
            organisation.update,
        )
        self.retrieve_hubs = to_raw_response_wrapper(
            organisation.retrieve_hubs,
        )
        self.retrieve_sites = to_raw_response_wrapper(
            organisation.retrieve_sites,
        )

    @cached_property
    def api_key(self) -> APIKeyResourceWithRawResponse:
        return APIKeyResourceWithRawResponse(self._organisation.api_key)

    @cached_property
    def site(self) -> SiteResourceWithRawResponse:
        return SiteResourceWithRawResponse(self._organisation.site)

    @cached_property
    def teams(self) -> TeamsResourceWithRawResponse:
        return TeamsResourceWithRawResponse(self._organisation.teams)

    @cached_property
    def user(self) -> UserResourceWithRawResponse:
        return UserResourceWithRawResponse(self._organisation.user)


class AsyncOrganisationResourceWithRawResponse:
    def __init__(self, organisation: AsyncOrganisationResource) -> None:
        self._organisation = organisation

        self.retrieve = async_to_raw_response_wrapper(
            organisation.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            organisation.update,
        )
        self.retrieve_hubs = async_to_raw_response_wrapper(
            organisation.retrieve_hubs,
        )
        self.retrieve_sites = async_to_raw_response_wrapper(
            organisation.retrieve_sites,
        )

    @cached_property
    def api_key(self) -> AsyncAPIKeyResourceWithRawResponse:
        return AsyncAPIKeyResourceWithRawResponse(self._organisation.api_key)

    @cached_property
    def site(self) -> AsyncSiteResourceWithRawResponse:
        return AsyncSiteResourceWithRawResponse(self._organisation.site)

    @cached_property
    def teams(self) -> AsyncTeamsResourceWithRawResponse:
        return AsyncTeamsResourceWithRawResponse(self._organisation.teams)

    @cached_property
    def user(self) -> AsyncUserResourceWithRawResponse:
        return AsyncUserResourceWithRawResponse(self._organisation.user)


class OrganisationResourceWithStreamingResponse:
    def __init__(self, organisation: OrganisationResource) -> None:
        self._organisation = organisation

        self.retrieve = to_streamed_response_wrapper(
            organisation.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            organisation.update,
        )
        self.retrieve_hubs = to_streamed_response_wrapper(
            organisation.retrieve_hubs,
        )
        self.retrieve_sites = to_streamed_response_wrapper(
            organisation.retrieve_sites,
        )

    @cached_property
    def api_key(self) -> APIKeyResourceWithStreamingResponse:
        return APIKeyResourceWithStreamingResponse(self._organisation.api_key)

    @cached_property
    def site(self) -> SiteResourceWithStreamingResponse:
        return SiteResourceWithStreamingResponse(self._organisation.site)

    @cached_property
    def teams(self) -> TeamsResourceWithStreamingResponse:
        return TeamsResourceWithStreamingResponse(self._organisation.teams)

    @cached_property
    def user(self) -> UserResourceWithStreamingResponse:
        return UserResourceWithStreamingResponse(self._organisation.user)


class AsyncOrganisationResourceWithStreamingResponse:
    def __init__(self, organisation: AsyncOrganisationResource) -> None:
        self._organisation = organisation

        self.retrieve = async_to_streamed_response_wrapper(
            organisation.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            organisation.update,
        )
        self.retrieve_hubs = async_to_streamed_response_wrapper(
            organisation.retrieve_hubs,
        )
        self.retrieve_sites = async_to_streamed_response_wrapper(
            organisation.retrieve_sites,
        )

    @cached_property
    def api_key(self) -> AsyncAPIKeyResourceWithStreamingResponse:
        return AsyncAPIKeyResourceWithStreamingResponse(self._organisation.api_key)

    @cached_property
    def site(self) -> AsyncSiteResourceWithStreamingResponse:
        return AsyncSiteResourceWithStreamingResponse(self._organisation.site)

    @cached_property
    def teams(self) -> AsyncTeamsResourceWithStreamingResponse:
        return AsyncTeamsResourceWithStreamingResponse(self._organisation.teams)

    @cached_property
    def user(self) -> AsyncUserResourceWithStreamingResponse:
        return AsyncUserResourceWithStreamingResponse(self._organisation.user)
