# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["NotificationReadAllResponse", "Data"]


class Data(BaseModel):
    updated: Optional[int] = None


class NotificationReadAllResponse(BaseModel):
    data: Optional[Data] = None

    metadata: Optional[object] = None
