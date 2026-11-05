# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel
from .duplicated_children import DuplicatedChildren

__all__ = ["DocumentGetDuplicatedChildrenResponse"]


class DocumentGetDuplicatedChildrenResponse(BaseModel):
    data: Optional[List[DuplicatedChildren]] = None

    metadata: Optional[object] = None
