# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ....._models import BaseModel

__all__ = ["SelectOptionRetrieveSelectOptionsResponse", "Data"]


class Data(BaseModel):
    has_more: Optional[bool] = FieldInfo(alias="hasMore", default=None)

    next: Optional[str] = None
    """Passed back as `after` for the next page; null when there are no more."""

    options: Optional[List[str]] = None


class SelectOptionRetrieveSelectOptionsResponse(BaseModel):
    data: Optional[Data] = None

    metadata: Optional[Dict[str, object]] = None
