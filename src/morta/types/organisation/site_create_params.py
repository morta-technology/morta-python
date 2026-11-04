# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..create_organisation_user_param import CreateOrganisationUserParam

__all__ = ["SiteCreateParams"]


class SiteCreateParams(TypedDict, total=False):
    team_id: Required[Annotated[str, PropertyInfo(alias="teamId")]]

    name: str

    users: Iterable[CreateOrganisationUserParam]
