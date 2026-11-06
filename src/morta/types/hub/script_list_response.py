# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ScriptListResponse", "Data"]


class Data(BaseModel):
    column_name: Optional[str] = FieldInfo(alias="columnName", default=None)

    column_public_id: Optional[str] = FieldInfo(alias="columnPublicId", default=None)

    script_updated_at: Optional[datetime] = FieldInfo(alias="scriptUpdatedAt", default=None)

    table_name: Optional[str] = FieldInfo(alias="tableName", default=None)

    table_public_id: Optional[str] = FieldInfo(alias="tablePublicId", default=None)

    view_public_id: Optional[str] = FieldInfo(alias="viewPublicId", default=None)


class ScriptListResponse(BaseModel):
    data: Optional[List[Data]] = None

    metadata: Optional[object] = None
