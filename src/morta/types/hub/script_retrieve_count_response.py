# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["ScriptRetrieveCountResponse", "Data"]


class Data(BaseModel):
    count: Optional[int] = None


class ScriptRetrieveCountResponse(BaseModel):
    data: Optional[Data] = None

    metadata: Optional[object] = None
