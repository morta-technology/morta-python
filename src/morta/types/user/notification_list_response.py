# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .user_notification import UserNotification

__all__ = ["NotificationListResponse", "Metadata"]


class Metadata(BaseModel):
    next_page_token: Optional[str] = None

    size: Optional[int] = None

    total: Optional[int] = None

    unread_count: Optional[int] = None


class NotificationListResponse(BaseModel):
    data: Optional[List[UserNotification]] = None

    metadata: Optional[Metadata] = None
