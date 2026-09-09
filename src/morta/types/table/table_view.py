# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from .sort import Sort
from .chart import Chart
from .group import Group
from .colour import Colour
from .filter import Filter
from ..draftjs import Draftjs
from .row_lock import RowLock
from ..._models import BaseModel
from ..summary_user import SummaryUser
from .views.table_view_column import TableViewColumn
from .table_view_configuration_parent_view import TableViewConfigurationParentView

__all__ = ["TableView", "ConfigurationParentView", "PersonalViewOwner"]

ConfigurationParentView: TypeAlias = Union[TableViewConfigurationParentView, Optional[object]]

PersonalViewOwner: TypeAlias = Union[SummaryUser, Optional[object]]


class TableView(BaseModel):
    name: str

    allow_contributor_delete: Optional[bool] = FieldInfo(alias="allowContributorDelete", default=None)

    calendar_settings: Optional[object] = FieldInfo(alias="calendarSettings", default=None)

    chart_settings: Optional[Chart] = FieldInfo(alias="chartSettings", default=None)

    collapsed_group_view: Optional[bool] = FieldInfo(alias="collapsedGroupView", default=None)

    colour_settings: Optional[List[Colour]] = FieldInfo(alias="colourSettings", default=None)

    columns: Optional[List[TableViewColumn]] = None

    configuration_parent_view: Optional[ConfigurationParentView] = FieldInfo(
        alias="configurationParentView", default=None
    )

    description: Optional[Draftjs] = None

    disable_new_row: Optional[bool] = FieldInfo(alias="disableNewRow", default=None)

    disable_sync_csv: Optional[bool] = FieldInfo(alias="disableSyncCsv", default=None)

    display_comment_rows: Optional[int] = FieldInfo(alias="displayCommentRows", default=None)

    display_validation_error_rows: Optional[int] = FieldInfo(alias="displayValidationErrorRows", default=None)

    filter_settings: Optional[List[Filter]] = FieldInfo(alias="filterSettings", default=None)

    frozen_index: Optional[int] = FieldInfo(alias="frozenIndex", default=None)

    group_settings: Optional[List[Group]] = FieldInfo(alias="groupSettings", default=None)

    is_default: Optional[bool] = FieldInfo(alias="isDefault", default=None)

    is_personal_view: Optional[bool] = FieldInfo(alias="isPersonalView", default=None)

    locked_from_duplication: Optional[bool] = FieldInfo(alias="lockedFromDuplication", default=None)

    matrix_settings: Optional[object] = FieldInfo(alias="matrixSettings", default=None)

    personal_view_owner: Optional[PersonalViewOwner] = FieldInfo(alias="personalViewOwner", default=None)

    public_id: Optional[str] = FieldInfo(alias="publicId", default=None)

    row_height: Optional[int] = FieldInfo(alias="rowHeight", default=None)

    row_lock_settings: Optional[List[RowLock]] = FieldInfo(alias="rowLockSettings", default=None)

    sort_settings: Optional[List[Sort]] = FieldInfo(alias="sortSettings", default=None)

    transpose_settings: Optional[object] = FieldInfo(alias="transposeSettings", default=None)

    tree_group_view: Optional[bool] = FieldInfo(alias="treeGroupView", default=None)

    type: Optional[int] = None

    unpack_multiselect_group_view: Optional[bool] = FieldInfo(alias="unpackMultiselectGroupView", default=None)
