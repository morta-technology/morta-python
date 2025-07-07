# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

from .._models import BaseModel

__all__ = ["UserRetrieveResponse"]


class UserRetrieveResponse(BaseModel):
    data: Optional["User"] = None

    metadata: Optional[object] = None
    """Metadata object"""


from .user.user import User
