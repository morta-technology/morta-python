# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["MatrixSettingsParam"]


class MatrixSettingsParam(TypedDict, total=False):
    data_column_widths: Annotated[Optional[Dict[str, int]], PropertyInfo(alias="dataColumnWidths")]

    data_field_column_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="dataFieldColumnIds")]

    field_column_width: Annotated[Optional[int], PropertyInfo(alias="fieldColumnWidth")]

    pivot_column_id: Annotated[Optional[str], PropertyInfo(alias="pivotColumnId")]

    row_label_column_ids: Annotated[SequenceNotStr[str], PropertyInfo(alias="rowLabelColumnIds")]
