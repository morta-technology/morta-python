# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TableJoinImportedColumns1Param"]


class TableJoinImportedColumns1Param(TypedDict, total=False):
    source_column_id: Annotated[str, PropertyInfo(alias="sourceColumnId")]

    source_column_name: Annotated[str, PropertyInfo(alias="sourceColumnName")]

    target_column_id: Annotated[str, PropertyInfo(alias="targetColumnId")]
