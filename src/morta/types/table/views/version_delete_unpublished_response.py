# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ...._models import BaseModel

__all__ = ["VersionDeleteUnpublishedResponse", "Data"]


class Data(BaseModel):
    deleted: Optional[int] = None


class VersionDeleteUnpublishedResponse(BaseModel):
    data: Optional[Data] = None
