# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SessionListResponse", "Data"]


class Data(BaseModel):
    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    device_type: Optional[str] = FieldInfo(alias="deviceType", default=None)

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)

    ip_address: Optional[str] = FieldInfo(alias="ipAddress", default=None)

    platform: Optional[str] = None

    public_id: Optional[str] = FieldInfo(alias="publicId", default=None)

    user_agent: Optional[str] = FieldInfo(alias="userAgent", default=None)


class SessionListResponse(BaseModel):
    data: Optional[List[Data]] = None

    metadata: Optional[object] = None
