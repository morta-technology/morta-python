# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .organisation import organisation
from .organisation.user_to_site import UserToSite

__all__ = ["SiteSchemaWithOrg", "Organisation"]

Organisation: TypeAlias = Union[organisation.Organisation, Optional[object]]


class SiteSchemaWithOrg(BaseModel):
    admin_count: Optional[object] = FieldInfo(alias="adminCount", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    hub_count: Optional[object] = FieldInfo(alias="hubCount", default=None)

    name: Optional[str] = None

    organisation: Optional[Organisation] = None

    public_id: Optional[str] = FieldInfo(alias="publicId", default=None)

    team_id: Optional[object] = FieldInfo(alias="teamId", default=None)

    team_name: Optional[object] = FieldInfo(alias="teamName", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    users: Optional[List[UserToSite]] = None
