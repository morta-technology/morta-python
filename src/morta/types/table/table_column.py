# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..draftjs import Draftjs
from ..._models import BaseModel
from .table_column_alter import TableColumnAlter
from .select_options_lookup import SelectOptionsLookup

__all__ = ["TableColumn", "AlterOptions", "Description"]

AlterOptions: TypeAlias = Union[TableColumnAlter, Optional[object]]

Description: TypeAlias = Union[Draftjs, Optional[object]]


class TableColumn(BaseModel):
    aggregate: Optional[int] = None

    alter_options: Optional[AlterOptions] = FieldInfo(alias="alterOptions", default=None)

    date_format: Optional[str] = FieldInfo(alias="dateFormat", default=None)

    decimal_places: Optional[int] = FieldInfo(alias="decimalPlaces", default=None)

    description: Optional[Description] = None

    display_link: Optional[bool] = FieldInfo(alias="displayLink", default=None)

    export_width: Optional[int] = FieldInfo(alias="exportWidth", default=None)

    formula: Optional[str] = None

    formula_enabled: Optional[bool] = FieldInfo(alias="formulaEnabled", default=None)

    header_background_color: Optional[str] = FieldInfo(alias="headerBackgroundColor", default=None)

    header_text_color: Optional[str] = FieldInfo(alias="headerTextColor", default=None)

    is_indexed: Optional[bool] = FieldInfo(alias="isIndexed", default=None)

    is_joined: Optional[bool] = FieldInfo(alias="isJoined", default=None)

    is_synced: Optional[bool] = FieldInfo(alias="isSynced", default=None)

    kind: Optional[
        Literal[
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
    ] = None

    kind_options: Optional[SelectOptionsLookup] = FieldInfo(alias="kindOptions", default=None)

    name: Optional[str] = None

    public_id: Optional[str] = FieldInfo(alias="publicId", default=None)

    script: Optional[str] = None

    script_enabled: Optional[bool] = FieldInfo(alias="scriptEnabled", default=None)

    thousand_separator: Optional[bool] = FieldInfo(alias="thousandSeparator", default=None)

    width: Optional[int] = None
