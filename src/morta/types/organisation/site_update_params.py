# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..create_organisation_user_param import CreateOrganisationUserParam

__all__ = ["SiteUpdateParams"]


class SiteUpdateParams(TypedDict, total=False):
    organisation_public_id: Required[str]

    name: str

    team_id: Annotated[Optional[str], PropertyInfo(alias="teamId")]

    users: Iterable[CreateOrganisationUserParam]
