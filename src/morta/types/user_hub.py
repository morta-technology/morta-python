# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["UserHub"]


class UserHub(BaseModel):
    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    email: Optional[str] = None

    name: Optional[str] = None

    public_id: Optional[str] = FieldInfo(alias="publicId", default=None)
