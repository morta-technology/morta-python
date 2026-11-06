# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .create_organisation_user_param import CreateOrganisationUserParam

__all__ = ["OrganisationUpdateParams"]


class OrganisationUpdateParams(TypedDict, total=False):
    disable_personal_view_saving: Annotated[bool, PropertyInfo(alias="disablePersonalViewSaving")]

    enable_user_api_keys: Annotated[bool, PropertyInfo(alias="enableUserApiKeys")]

    enforce_login: Annotated[Optional[str], PropertyInfo(alias="enforceLogin")]

    idp_certificate: Annotated[Optional[str], PropertyInfo(alias="idpCertificate")]

    idp_issuer: Annotated[Optional[str], PropertyInfo(alias="idpIssuer")]

    idp_sso_url: Annotated[Optional[str], PropertyInfo(alias="idpSsoUrl")]

    name: str

    restrict_hub_creation: Annotated[bool, PropertyInfo(alias="restrictHubCreation")]

    restrict_sync_configuration: Annotated[bool, PropertyInfo(alias="restrictSyncConfiguration")]

    users: Iterable[CreateOrganisationUserParam]
