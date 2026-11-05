# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UserToIntegration"]


class UserToIntegration(BaseModel):
    access_token: Optional[str] = FieldInfo(alias="accessToken", default=None)

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)

    provider: Optional[str] = None

    refresh_token: Optional[str] = FieldInfo(alias="refreshToken", default=None)

    region: Optional[str] = None
