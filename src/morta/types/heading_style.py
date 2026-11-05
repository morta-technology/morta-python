# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["HeadingStyle"]


class HeadingStyle(BaseModel):
    bold: Optional[bool] = None

    colour: Optional[str] = None

    font_size: Optional[float] = FieldInfo(alias="fontSize", default=None)

    italic: Optional[bool] = None

    level: Optional[int] = None

    numbering_style: Optional[int] = FieldInfo(alias="numberingStyle", default=None)

    public_id: Optional[str] = FieldInfo(alias="publicId", default=None)

    start_at0: Optional[bool] = FieldInfo(alias="startAt0", default=None)

    underline: Optional[bool] = None
