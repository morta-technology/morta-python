# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel
from .user.user import User

__all__ = ["UserCreateResponse"]


class UserCreateResponse(BaseModel):
    data: Optional[User] = None

    metadata: Optional[object] = None
