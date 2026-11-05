# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .user.user import User

__all__ = [
    "UserRetrieveMeResponse",
    "Data",
    "DataOrganisationMembership",
    "DataOrganisationMembershipAdmin",
    "DataTeam",
    "DataTeamManager",
]


class DataOrganisationMembershipAdmin(BaseModel):
    email: Optional[str] = None

    name: Optional[str] = None


class DataOrganisationMembership(BaseModel):
    """
    The organisation the user belongs to (by their organisation role, or else their email's domain) and its admins, who give paid seats. Null outside any organisation.
    """

    admins: Optional[List[DataOrganisationMembershipAdmin]] = None

    name: Optional[str] = None

    public_id: Optional[str] = FieldInfo(alias="publicId", default=None)


class DataTeamManager(BaseModel):
    email: Optional[str] = None

    name: Optional[str] = None


class DataTeam(BaseModel):
    """The organisation team the user's paid seat comes from. Null without one."""

    manager_names: Optional[List[str]] = FieldInfo(alias="managerNames", default=None)

    managers: Optional[List[DataTeamManager]] = None
    """The team's managers, who assign its seats."""

    org_name: Optional[str] = FieldInfo(alias="orgName", default=None)

    org_plan_tier: Optional[Literal["professional", "team", "scale_up"]] = FieldInfo(alias="orgPlanTier", default=None)

    org_public_id: Optional[str] = FieldInfo(alias="orgPublicId", default=None)

    team_name: Optional[str] = FieldInfo(alias="teamName", default=None)

    team_public_id: Optional[str] = FieldInfo(alias="teamPublicId", default=None)


class Data(User):
    """Fields only on the current user's own details."""

    organisation_membership: Optional[DataOrganisationMembership] = FieldInfo(
        alias="organisationMembership", default=None
    )
    """
    The organisation the user belongs to (by their organisation role, or else their
    email's domain) and its admins, who give paid seats. Null outside any
    organisation.
    """

    paid_seat_requested_at: Optional[datetime] = FieldInfo(alias="paidSeatRequestedAt", default=None)
    """
    When the user asked their organisation admins for a paid seat, in UTC, while
    they can't ask again: for 24 hours after. Null otherwise.
    """

    team: Optional[DataTeam] = None  # type: ignore
    """The organisation team the user's paid seat comes from. Null without one."""


class UserRetrieveMeResponse(BaseModel):
    data: Optional[Data] = None
    """Fields only on the current user's own details."""

    metadata: Optional[object] = None
    """The metadata object"""
