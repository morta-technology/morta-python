# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from ..draftjs_param import DraftjsParam
from .table_column_alter_param import TableColumnAlterParam
from .select_options_lookup_param import SelectOptionsLookupParam

__all__ = ["TableColumnParam", "AlterOptions", "Description"]

AlterOptions: TypeAlias = Union[TableColumnAlterParam, Optional[object]]

Description: TypeAlias = Union[DraftjsParam, Optional[object]]


class TableColumnParam(TypedDict, total=False):
    aggregate: int

    alter_options: Annotated[AlterOptions, PropertyInfo(alias="alterOptions")]

    date_format: Annotated[Optional[str], PropertyInfo(alias="dateFormat")]

    decimal_places: Annotated[int, PropertyInfo(alias="decimalPlaces")]

    description: Description

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
    ]

    kind_options: Annotated[SelectOptionsLookupParam, PropertyInfo(alias="kindOptions")]

    name: str

    public_id: Annotated[str, PropertyInfo(alias="publicId")]

    script: Optional[str]

    script_enabled: Annotated[bool, PropertyInfo(alias="scriptEnabled")]

    thousand_separator: Annotated[bool, PropertyInfo(alias="thousandSeparator")]

    width: int
