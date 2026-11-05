# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .user5 import User5
from ...._models import BaseModel

__all__ = ["CustomViewVersion", "CreatedBy"]

CreatedBy: TypeAlias = Union[User5, Optional[object]]


class CustomViewVersion(BaseModel):
    id: Optional[str] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    created_by: Optional[CreatedBy] = FieldInfo(alias="createdBy", default=None)

    has_thumbnail: Optional[object] = FieldInfo(alias="hasThumbnail", default=None)

    is_latest: Optional[object] = FieldInfo(alias="isLatest", default=None)

    is_published: Optional[bool] = FieldInfo(alias="isPublished", default=None)

    prompt: Optional[str] = None

    published_at: Optional[datetime] = FieldInfo(alias="publishedAt", default=None)

    source: Optional[str] = None

    summary: Optional[str] = None

    title: Optional[str] = None
