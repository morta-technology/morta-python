# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["CalendarSettingsParam"]


class CalendarSettingsParam(TypedDict, total=False):
    end_column_public_id: Annotated[Optional[str], PropertyInfo(alias="endColumnPublicId")]

    label_column_public_id: Annotated[Optional[str], PropertyInfo(alias="labelColumnPublicId")]

    start_column_public_id: Annotated[Optional[str], PropertyInfo(alias="startColumnPublicId")]
