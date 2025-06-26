# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["TableGetDuplicatedChildrenResponse"]


class TableGetDuplicatedChildrenResponse(BaseModel):
    data: Optional[List[object]] = None

    metadata: Optional[object] = None
