# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo
from .sort_param import SortParam
from .chart_param import ChartParam
from .group_param import GroupParam
from .colour_param import ColourParam
from .filter_param import FilterParam
from ..draftjs_param import DraftjsParam
from .row_lock_param import RowLockParam
from .matrix_settings_param import MatrixSettingsParam
from .calendar_settings_param import CalendarSettingsParam
from .transpose_settings_param import TransposeSettingsParam
from ..base_request_context_param import BaseRequestContextParam
from .views.update_table_view_column_param import UpdateTableViewColumnParam

__all__ = [
    "ViewUpdateParams",
    "CalendarSettings",
    "ChartSettings",
    "Description",
    "MatrixSettings",
    "TransposeSettings",
]


class ViewUpdateParams(TypedDict, total=False):
    allow_contributor_delete: Annotated[bool, PropertyInfo(alias="allowContributorDelete")]

    calendar_settings: Annotated[CalendarSettings, PropertyInfo(alias="calendarSettings")]

    chart_settings: Annotated[ChartSettings, PropertyInfo(alias="chartSettings")]

    collapsed_group_view: Annotated[bool, PropertyInfo(alias="collapsedGroupView")]

    colour_settings: Annotated[Iterable[ColourParam], PropertyInfo(alias="colourSettings")]

    columns: Iterable[UpdateTableViewColumnParam]

    context: BaseRequestContextParam

    description: Description

    disable_new_row: Annotated[bool, PropertyInfo(alias="disableNewRow")]

    disable_sync_csv: Annotated[bool, PropertyInfo(alias="disableSyncCsv")]

    display_comment_rows: Annotated[int, PropertyInfo(alias="displayCommentRows")]

    display_validation_error_rows: Annotated[Literal[0, 1, 2], PropertyInfo(alias="displayValidationErrorRows")]

    filter_settings: Annotated[Iterable[FilterParam], PropertyInfo(alias="filterSettings")]

    frozen_index: Annotated[int, PropertyInfo(alias="frozenIndex")]

    group_settings: Annotated[Iterable[GroupParam], PropertyInfo(alias="groupSettings")]

    matrix_settings: Annotated[MatrixSettings, PropertyInfo(alias="matrixSettings")]

    name: str

    row_height: Annotated[int, PropertyInfo(alias="rowHeight")]

    row_lock_settings: Annotated[Iterable[RowLockParam], PropertyInfo(alias="rowLockSettings")]

    sort_settings: Annotated[Iterable[SortParam], PropertyInfo(alias="sortSettings")]

    transpose_settings: Annotated[TransposeSettings, PropertyInfo(alias="transposeSettings")]

    tree_group_view: Annotated[bool, PropertyInfo(alias="treeGroupView")]

    type: int

    unpack_multiselect_group_view: Annotated[bool, PropertyInfo(alias="unpackMultiselectGroupView")]


CalendarSettings: TypeAlias = Union[CalendarSettingsParam, Optional[object]]

ChartSettings: TypeAlias = Union[ChartParam, Optional[object]]

Description: TypeAlias = Union[DraftjsParam, Optional[object]]

MatrixSettings: TypeAlias = Union[MatrixSettingsParam, Optional[object]]

TransposeSettings: TypeAlias = Union[TransposeSettingsParam, Optional[object]]
