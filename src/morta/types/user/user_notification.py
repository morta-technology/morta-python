# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..project import Project
from ..._models import BaseModel
from ..summary_user import SummaryUser

__all__ = ["UserNotification"]


class UserNotification(BaseModel):
    actor: Optional[SummaryUser] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    data: Optional[object] = None

    dismissed_at: Optional[datetime] = FieldInfo(alias="dismissedAt", default=None)

    notification_type: Optional[str] = FieldInfo(alias="notificationType", default=None)

    project: Optional[Project] = None

    public_id: Optional[str] = FieldInfo(alias="publicId", default=None)

    read_at: Optional[datetime] = FieldInfo(alias="readAt", default=None)

    reference_type: Optional[str] = FieldInfo(alias="referenceType", default=None)
