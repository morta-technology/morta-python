# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["HubFolder"]


class HubFolder(BaseModel):
    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    name: Optional[str] = None

    parent_id: Optional[str] = FieldInfo(alias="parentId", default=None)

    position: Optional[int] = None

    public_id: Optional[str] = FieldInfo(alias="publicId", default=None)
