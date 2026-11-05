# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .seats import (
    SeatsResource,
    AsyncSeatsResource,
    SeatsResourceWithRawResponse,
    AsyncSeatsResourceWithRawResponse,
    SeatsResourceWithStreamingResponse,
    AsyncSeatsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["TeamsResource", "AsyncTeamsResource"]


class TeamsResource(SyncAPIResource):
    @cached_property
    def seats(self) -> SeatsResource:
        return SeatsResource(self._client)

    @cached_property
    def with_raw_response(self) -> TeamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return TeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TeamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return TeamsResourceWithStreamingResponse(self)


class AsyncTeamsResource(AsyncAPIResource):
    @cached_property
    def seats(self) -> AsyncSeatsResource:
        return AsyncSeatsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncTeamsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/morta-technology/morta-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTeamsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTeamsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/morta-technology/morta-python#with_streaming_response
        """
        return AsyncTeamsResourceWithStreamingResponse(self)


class TeamsResourceWithRawResponse:
    def __init__(self, teams: TeamsResource) -> None:
        self._teams = teams

    @cached_property
    def seats(self) -> SeatsResourceWithRawResponse:
        return SeatsResourceWithRawResponse(self._teams.seats)


class AsyncTeamsResourceWithRawResponse:
    def __init__(self, teams: AsyncTeamsResource) -> None:
        self._teams = teams

    @cached_property
    def seats(self) -> AsyncSeatsResourceWithRawResponse:
        return AsyncSeatsResourceWithRawResponse(self._teams.seats)


class TeamsResourceWithStreamingResponse:
    def __init__(self, teams: TeamsResource) -> None:
        self._teams = teams

    @cached_property
    def seats(self) -> SeatsResourceWithStreamingResponse:
        return SeatsResourceWithStreamingResponse(self._teams.seats)


class AsyncTeamsResourceWithStreamingResponse:
    def __init__(self, teams: AsyncTeamsResource) -> None:
        self._teams = teams

    @cached_property
    def seats(self) -> AsyncSeatsResourceWithStreamingResponse:
        return AsyncSeatsResourceWithStreamingResponse(self._teams.seats)
