# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo
from .table.table_column_param import TableColumnParam
from .base_request_context_param import BaseRequestContextParam
from .table.table_column_join_param import TableColumnJoinParam
from .table_join_imported_columns1_param import TableJoinImportedColumns1Param

__all__ = ["TableCreateParams", "Join"]


class TableCreateParams(TypedDict, total=False):
    columns: Required[Iterable[TableColumnParam]]

    name: Required[str]

    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    context: BaseRequestContextParam

    folder_id: Annotated[Optional[str], PropertyInfo(alias="folderId")]

    joins: Iterable[Join]

    type: Optional[str]
    """
    Deprecated: files the resource into the top-level folder of that name; creates
    it if missing (hub Owners only).
    """


class Join(TypedDict, total=False):
    data_columns: Annotated[Iterable[TableJoinImportedColumns1Param], PropertyInfo(alias="dataColumns")]

    is_one_to_many: Annotated[bool, PropertyInfo(alias="isOneToMany")]

    join_columns: Annotated[Iterable[TableColumnJoinParam], PropertyInfo(alias="joinColumns")]

    join_table_name: Annotated[str, PropertyInfo(alias="joinTableName")]

    join_view_id: Annotated[str, PropertyInfo(alias="joinViewId")]

    join_view_name: Annotated[str, PropertyInfo(alias="joinViewName")]
