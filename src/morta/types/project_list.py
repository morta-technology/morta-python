# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ProjectList", "User"]


class User(BaseModel):
    email: Optional[str] = None

    firebase_user_id: Optional[str] = FieldInfo(alias="firebaseUserId", default=None)

    kind: Optional[str] = None

    name: Optional[str] = None

    public_id: Optional[str] = FieldInfo(alias="publicId", default=None)


class ProjectList(BaseModel):
    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    role: Optional[str] = None

    role_assigned_method: Optional[str] = FieldInfo(alias="roleAssignedMethod", default=None)

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)

    user: Optional[User] = None
