# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo
from .draftjs_param import DraftjsParam
from .base_request_context_param import BaseRequestContextParam
from .table.views.auto_fill_param import AutoFillParam
from .table.table_column_join_param import TableColumnJoinParam
from .table.table_column_alter_param import TableColumnAlterParam
from .table.select_options_lookup_param import SelectOptionsLookupParam
from .table_join_imported_columns1_param import TableJoinImportedColumns1Param

__all__ = ["TableCreateParams", "Column", "ColumnAlterOptions", "ColumnAutoFill", "ColumnDescription", "Join"]


class TableCreateParams(TypedDict, total=False):
    columns: Required[Iterable[Column]]

    name: Required[str]

    project_id: Required[Annotated[str, PropertyInfo(alias="projectId")]]

    context: BaseRequestContextParam

    folder_id: Annotated[Optional[str], PropertyInfo(alias="folderId")]

    joins: Iterable[Join]


ColumnAlterOptions: TypeAlias = Union[TableColumnAlterParam, Optional[object]]

ColumnAutoFill: TypeAlias = Union[AutoFillParam, Optional[object]]

ColumnDescription: TypeAlias = Union[DraftjsParam, Optional[object]]


class Column(TypedDict, total=False):
    aggregate: int

    alter_options: Annotated[ColumnAlterOptions, PropertyInfo(alias="alterOptions")]

    auto_fill: Annotated[ColumnAutoFill, PropertyInfo(alias="autoFill")]

    date_format: Annotated[Optional[str], PropertyInfo(alias="dateFormat")]

    decimal_places: Annotated[int, PropertyInfo(alias="decimalPlaces")]

    default_value: Annotated[Optional[str], PropertyInfo(alias="defaultValue")]

    description: ColumnDescription

    display_link: Annotated[bool, PropertyInfo(alias="displayLink")]

    export_width: Annotated[Optional[int], PropertyInfo(alias="exportWidth")]

    formula: Optional[str]

    formula_enabled: Annotated[bool, PropertyInfo(alias="formulaEnabled")]

    header_background_color: Annotated[Optional[str], PropertyInfo(alias="headerBackgroundColor")]

    header_text_color: Annotated[Optional[str], PropertyInfo(alias="headerTextColor")]

    is_indexed: Annotated[bool, PropertyInfo(alias="isIndexed")]

    is_joined: Annotated[Optional[bool], PropertyInfo(alias="isJoined")]

    is_synced: Annotated[bool, PropertyInfo(alias="isSynced")]

    kind: Literal[
        "text",
        "datetime",
        "date",
        "link",
        "multilink",
        "select",
        "multiselect",
        "integer",
        "float",
        "percentage",
        "tag",
        "variable",
        "attachment",
        "phone",
        "email",
        "vote",
        "checkbox",
        "duration",
        "json",
    ]

    kind_options: Annotated[SelectOptionsLookupParam, PropertyInfo(alias="kindOptions")]

    name: str

    public_id: Annotated[str, PropertyInfo(alias="publicId")]

    thousand_separator: Annotated[bool, PropertyInfo(alias="thousandSeparator")]

    width: int


class Join(TypedDict, total=False):
    data_columns: Annotated[Iterable[TableJoinImportedColumns1Param], PropertyInfo(alias="dataColumns")]

    is_one_to_many: Annotated[bool, PropertyInfo(alias="isOneToMany")]

    join_columns: Annotated[Iterable[TableColumnJoinParam], PropertyInfo(alias="joinColumns")]

    join_table_name: Annotated[str, PropertyInfo(alias="joinTableName")]

    join_view_id: Annotated[str, PropertyInfo(alias="joinViewId")]

    join_view_name: Annotated[str, PropertyInfo(alias="joinViewName")]
