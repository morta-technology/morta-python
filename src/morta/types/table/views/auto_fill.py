# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["AutoFill"]


class AutoFill(BaseModel):
    type: Literal[
        "created_time", "created_by", "row_id", "autonumber", "last_modified_time", "last_modified_by", "previous_value"
    ]

    columns: Optional[List[str]] = None

    fill_gaps: Optional[bool] = FieldInfo(alias="fillGaps", default=None)
