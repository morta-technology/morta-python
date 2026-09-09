# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from ..create_organisation_user_param import CreateOrganisationUserParam

__all__ = ["SiteCreateParams"]


class SiteCreateParams(TypedDict, total=False):
    name: str

    team_id: Annotated[Optional[str], PropertyInfo(alias="teamId")]

    users: Iterable[CreateOrganisationUserParam]
