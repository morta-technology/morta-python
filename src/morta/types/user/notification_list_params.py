# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["NotificationListParams"]


class NotificationListParams(TypedDict, total=False):
    next_page_token: Annotated[str, PropertyInfo(alias="nextPageToken")]
    """Opaque token for the next page from a previous response"""

    page: int
    """Page number (ignored when nextPageToken is given)"""

    size: int
    """Page size (max 100)"""

    unread_only: Annotated[bool, PropertyInfo(alias="unreadOnly")]
    """Only return unread notifications"""
