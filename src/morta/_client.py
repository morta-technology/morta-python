# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import TYPE_CHECKING, Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import is_given, get_async_library
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import MortaError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import hub, user, table, document, permissions, integrations, notifications, comment_thread
    from .resources.hub.hub import HubResource, AsyncHubResource
    from .resources.user.user import UserResource, AsyncUserResource
    from .resources.permissions import PermissionsResource, AsyncPermissionsResource
    from .resources.table.table import TableResource, AsyncTableResource
    from .resources.integrations import IntegrationsResource, AsyncIntegrationsResource
    from .resources.notifications import NotificationsResource, AsyncNotificationsResource
    from .resources.document.document import DocumentResource, AsyncDocumentResource
    from .resources.comment_thread.comment_thread import CommentThreadResource, AsyncCommentThreadResource

__all__ = ["Timeout", "Transport", "ProxiesTypes", "RequestOptions", "Morta", "AsyncMorta", "Client", "AsyncClient"]


class Morta(SyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous Morta client instance.

        This automatically infers the `api_key` argument from the `MORTA_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("MORTA_API_KEY")
        if api_key is None:
            raise MortaError(
                "The api_key client option must be set either by passing api_key to the client or by setting the MORTA_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("MORTA_BASE_URL")
        if base_url is None:
            base_url = f"https://api.morta.io"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def user(self) -> UserResource:
        from .resources.user import UserResource

        return UserResource(self)

    @cached_property
    def hub(self) -> HubResource:
        from .resources.hub import HubResource

        return HubResource(self)

    @cached_property
    def table(self) -> TableResource:
        from .resources.table import TableResource

        return TableResource(self)

    @cached_property
    def document(self) -> DocumentResource:
        from .resources.document import DocumentResource

        return DocumentResource(self)

    @cached_property
    def notifications(self) -> NotificationsResource:
        from .resources.notifications import NotificationsResource

        return NotificationsResource(self)

    @cached_property
    def comment_thread(self) -> CommentThreadResource:
        from .resources.comment_thread import CommentThreadResource

        return CommentThreadResource(self)

    @cached_property
    def permissions(self) -> PermissionsResource:
        from .resources.permissions import PermissionsResource

        return PermissionsResource(self)

    @cached_property
    def integrations(self) -> IntegrationsResource:
        from .resources.integrations import IntegrationsResource

        return IntegrationsResource(self)

    @cached_property
    def with_raw_response(self) -> MortaWithRawResponse:
        return MortaWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MortaWithStreamedResponse:
        return MortaWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncMorta(AsyncAPIClient):
    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncMorta client instance.

        This automatically infers the `api_key` argument from the `MORTA_API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("MORTA_API_KEY")
        if api_key is None:
            raise MortaError(
                "The api_key client option must be set either by passing api_key to the client or by setting the MORTA_API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("MORTA_BASE_URL")
        if base_url is None:
            base_url = f"https://api.morta.io"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

    @cached_property
    def user(self) -> AsyncUserResource:
        from .resources.user import AsyncUserResource

        return AsyncUserResource(self)

    @cached_property
    def hub(self) -> AsyncHubResource:
        from .resources.hub import AsyncHubResource

        return AsyncHubResource(self)

    @cached_property
    def table(self) -> AsyncTableResource:
        from .resources.table import AsyncTableResource

        return AsyncTableResource(self)

    @cached_property
    def document(self) -> AsyncDocumentResource:
        from .resources.document import AsyncDocumentResource

        return AsyncDocumentResource(self)

    @cached_property
    def notifications(self) -> AsyncNotificationsResource:
        from .resources.notifications import AsyncNotificationsResource

        return AsyncNotificationsResource(self)

    @cached_property
    def comment_thread(self) -> AsyncCommentThreadResource:
        from .resources.comment_thread import AsyncCommentThreadResource

        return AsyncCommentThreadResource(self)

    @cached_property
    def permissions(self) -> AsyncPermissionsResource:
        from .resources.permissions import AsyncPermissionsResource

        return AsyncPermissionsResource(self)

    @cached_property
    def integrations(self) -> AsyncIntegrationsResource:
        from .resources.integrations import AsyncIntegrationsResource

        return AsyncIntegrationsResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncMortaWithRawResponse:
        return AsyncMortaWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMortaWithStreamedResponse:
        return AsyncMortaWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": f"Bearer {api_key}"}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class MortaWithRawResponse:
    _client: Morta

    def __init__(self, client: Morta) -> None:
        self._client = client

    @cached_property
    def user(self) -> user.UserResourceWithRawResponse:
        from .resources.user import UserResourceWithRawResponse

        return UserResourceWithRawResponse(self._client.user)

    @cached_property
    def hub(self) -> hub.HubResourceWithRawResponse:
        from .resources.hub import HubResourceWithRawResponse

        return HubResourceWithRawResponse(self._client.hub)

    @cached_property
    def table(self) -> table.TableResourceWithRawResponse:
        from .resources.table import TableResourceWithRawResponse

        return TableResourceWithRawResponse(self._client.table)

    @cached_property
    def document(self) -> document.DocumentResourceWithRawResponse:
        from .resources.document import DocumentResourceWithRawResponse

        return DocumentResourceWithRawResponse(self._client.document)

    @cached_property
    def notifications(self) -> notifications.NotificationsResourceWithRawResponse:
        from .resources.notifications import NotificationsResourceWithRawResponse

        return NotificationsResourceWithRawResponse(self._client.notifications)

    @cached_property
    def comment_thread(self) -> comment_thread.CommentThreadResourceWithRawResponse:
        from .resources.comment_thread import CommentThreadResourceWithRawResponse

        return CommentThreadResourceWithRawResponse(self._client.comment_thread)

    @cached_property
    def permissions(self) -> permissions.PermissionsResourceWithRawResponse:
        from .resources.permissions import PermissionsResourceWithRawResponse

        return PermissionsResourceWithRawResponse(self._client.permissions)

    @cached_property
    def integrations(self) -> integrations.IntegrationsResourceWithRawResponse:
        from .resources.integrations import IntegrationsResourceWithRawResponse

        return IntegrationsResourceWithRawResponse(self._client.integrations)


class AsyncMortaWithRawResponse:
    _client: AsyncMorta

    def __init__(self, client: AsyncMorta) -> None:
        self._client = client

    @cached_property
    def user(self) -> user.AsyncUserResourceWithRawResponse:
        from .resources.user import AsyncUserResourceWithRawResponse

        return AsyncUserResourceWithRawResponse(self._client.user)

    @cached_property
    def hub(self) -> hub.AsyncHubResourceWithRawResponse:
        from .resources.hub import AsyncHubResourceWithRawResponse

        return AsyncHubResourceWithRawResponse(self._client.hub)

    @cached_property
    def table(self) -> table.AsyncTableResourceWithRawResponse:
        from .resources.table import AsyncTableResourceWithRawResponse

        return AsyncTableResourceWithRawResponse(self._client.table)

    @cached_property
    def document(self) -> document.AsyncDocumentResourceWithRawResponse:
        from .resources.document import AsyncDocumentResourceWithRawResponse

        return AsyncDocumentResourceWithRawResponse(self._client.document)

    @cached_property
    def notifications(self) -> notifications.AsyncNotificationsResourceWithRawResponse:
        from .resources.notifications import AsyncNotificationsResourceWithRawResponse

        return AsyncNotificationsResourceWithRawResponse(self._client.notifications)

    @cached_property
    def comment_thread(self) -> comment_thread.AsyncCommentThreadResourceWithRawResponse:
        from .resources.comment_thread import AsyncCommentThreadResourceWithRawResponse

        return AsyncCommentThreadResourceWithRawResponse(self._client.comment_thread)

    @cached_property
    def permissions(self) -> permissions.AsyncPermissionsResourceWithRawResponse:
        from .resources.permissions import AsyncPermissionsResourceWithRawResponse

        return AsyncPermissionsResourceWithRawResponse(self._client.permissions)

    @cached_property
    def integrations(self) -> integrations.AsyncIntegrationsResourceWithRawResponse:
        from .resources.integrations import AsyncIntegrationsResourceWithRawResponse

        return AsyncIntegrationsResourceWithRawResponse(self._client.integrations)


class MortaWithStreamedResponse:
    _client: Morta

    def __init__(self, client: Morta) -> None:
        self._client = client

    @cached_property
    def user(self) -> user.UserResourceWithStreamingResponse:
        from .resources.user import UserResourceWithStreamingResponse

        return UserResourceWithStreamingResponse(self._client.user)

    @cached_property
    def hub(self) -> hub.HubResourceWithStreamingResponse:
        from .resources.hub import HubResourceWithStreamingResponse

        return HubResourceWithStreamingResponse(self._client.hub)

    @cached_property
    def table(self) -> table.TableResourceWithStreamingResponse:
        from .resources.table import TableResourceWithStreamingResponse

        return TableResourceWithStreamingResponse(self._client.table)

    @cached_property
    def document(self) -> document.DocumentResourceWithStreamingResponse:
        from .resources.document import DocumentResourceWithStreamingResponse

        return DocumentResourceWithStreamingResponse(self._client.document)

    @cached_property
    def notifications(self) -> notifications.NotificationsResourceWithStreamingResponse:
        from .resources.notifications import NotificationsResourceWithStreamingResponse

        return NotificationsResourceWithStreamingResponse(self._client.notifications)

    @cached_property
    def comment_thread(self) -> comment_thread.CommentThreadResourceWithStreamingResponse:
        from .resources.comment_thread import CommentThreadResourceWithStreamingResponse

        return CommentThreadResourceWithStreamingResponse(self._client.comment_thread)

    @cached_property
    def permissions(self) -> permissions.PermissionsResourceWithStreamingResponse:
        from .resources.permissions import PermissionsResourceWithStreamingResponse

        return PermissionsResourceWithStreamingResponse(self._client.permissions)

    @cached_property
    def integrations(self) -> integrations.IntegrationsResourceWithStreamingResponse:
        from .resources.integrations import IntegrationsResourceWithStreamingResponse

        return IntegrationsResourceWithStreamingResponse(self._client.integrations)


class AsyncMortaWithStreamedResponse:
    _client: AsyncMorta

    def __init__(self, client: AsyncMorta) -> None:
        self._client = client

    @cached_property
    def user(self) -> user.AsyncUserResourceWithStreamingResponse:
        from .resources.user import AsyncUserResourceWithStreamingResponse

        return AsyncUserResourceWithStreamingResponse(self._client.user)

    @cached_property
    def hub(self) -> hub.AsyncHubResourceWithStreamingResponse:
        from .resources.hub import AsyncHubResourceWithStreamingResponse

        return AsyncHubResourceWithStreamingResponse(self._client.hub)

    @cached_property
    def table(self) -> table.AsyncTableResourceWithStreamingResponse:
        from .resources.table import AsyncTableResourceWithStreamingResponse

        return AsyncTableResourceWithStreamingResponse(self._client.table)

    @cached_property
    def document(self) -> document.AsyncDocumentResourceWithStreamingResponse:
        from .resources.document import AsyncDocumentResourceWithStreamingResponse

        return AsyncDocumentResourceWithStreamingResponse(self._client.document)

    @cached_property
    def notifications(self) -> notifications.AsyncNotificationsResourceWithStreamingResponse:
        from .resources.notifications import AsyncNotificationsResourceWithStreamingResponse

        return AsyncNotificationsResourceWithStreamingResponse(self._client.notifications)

    @cached_property
    def comment_thread(self) -> comment_thread.AsyncCommentThreadResourceWithStreamingResponse:
        from .resources.comment_thread import AsyncCommentThreadResourceWithStreamingResponse

        return AsyncCommentThreadResourceWithStreamingResponse(self._client.comment_thread)

    @cached_property
    def permissions(self) -> permissions.AsyncPermissionsResourceWithStreamingResponse:
        from .resources.permissions import AsyncPermissionsResourceWithStreamingResponse

        return AsyncPermissionsResourceWithStreamingResponse(self._client.permissions)

    @cached_property
    def integrations(self) -> integrations.AsyncIntegrationsResourceWithStreamingResponse:
        from .resources.integrations import AsyncIntegrationsResourceWithStreamingResponse

        return AsyncIntegrationsResourceWithStreamingResponse(self._client.integrations)


Client = Morta

AsyncClient = AsyncMorta
