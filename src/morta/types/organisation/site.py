# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .user_to_site import UserToSite

__all__ = ["Site"]


class Site(BaseModel):
    admin_count: Optional[object] = FieldInfo(alias="adminCount", default=None)

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    hub_count: Optional[object] = FieldInfo(alias="hubCount", default=None)

    name: Optional[str] = None

    public_id: Optional[str] = FieldInfo(alias="publicId", default=None)

    team_id: Optional[object] = FieldInfo(alias="teamId", default=None)

    team_name: Optional[object] = FieldInfo(alias="teamName", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    users: Optional[List[UserToSite]] = None
