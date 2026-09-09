# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ViewGetRowsResponse", "ViewGetRowsResponseItem"]


class ViewGetRowsResponseItem(BaseModel):
    public_id: Optional[str] = FieldInfo(alias="publicId", default=None)

    row_data: Optional[Dict[str, object]] = FieldInfo(alias="rowData", default=None)

    sort_order: Optional[float] = FieldInfo(alias="sortOrder", default=None)


ViewGetRowsResponse: TypeAlias = List[ViewGetRowsResponseItem]
