# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ColumnRetrieveBrokenFormulasResponse", "Data"]


class Data(BaseModel):
    name: Optional[str] = None

    public_id: Optional[str] = FieldInfo(alias="publicId", default=None)


class ColumnRetrieveBrokenFormulasResponse(BaseModel):
    data: Optional[List[Data]] = None

    metadata: Optional[object] = None
