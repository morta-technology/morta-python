# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..project import Project
from ..._models import BaseModel
from ..table_join import TableJoin
from .table_column import TableColumn

__all__ = ["Table"]


class Table(BaseModel):
    allow_comments: Optional[bool] = FieldInfo(alias="allowComments", default=None)

    autodesk_bim360_model_properties: Optional[object] = FieldInfo(alias="autodeskBim360ModelProperties", default=None)

    columns: Optional[List[TableColumn]] = None

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    default_view_id: Optional[str] = FieldInfo(alias="defaultViewId", default=None)

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)

    failed_sync_attempts: Optional[int] = FieldInfo(alias="failedSyncAttempts", default=None)

    folder_id: Optional[str] = FieldInfo(alias="folderId", default=None)
    """The hub folder the resource is in; null at the hub's top level."""

    is_deleted: Optional[bool] = FieldInfo(alias="isDeleted", default=None)

    is_synced: Optional[bool] = FieldInfo(alias="isSynced", default=None)

    is_syncing: Optional[object] = FieldInfo(alias="isSyncing", default=None)

    joins: Optional[List[TableJoin]] = None

    keep_colours_in_sync: Optional[bool] = FieldInfo(alias="keepColoursInSync", default=None)

    keep_validations_in_sync: Optional[bool] = FieldInfo(alias="keepValidationsInSync", default=None)

    last_sync: Optional[datetime] = FieldInfo(alias="lastSync", default=None)

    locked_from_duplication: Optional[bool] = FieldInfo(alias="lockedFromDuplication", default=None)

    name: Optional[str] = None

    project_name: Optional[str] = FieldInfo(alias="projectName", default=None)

    project_public_id: Optional[str] = FieldInfo(alias="projectPublicId", default=None)

    projects: Optional[List[Project]] = None

    public_id: Optional[str] = FieldInfo(alias="publicId", default=None)

    sync_all_hubs: Optional[bool] = FieldInfo(alias="syncAllHubs", default=None)

    sync_hourly_frequency: Optional[int] = FieldInfo(alias="syncHourlyFrequency", default=None)

    sync_project_ids: Optional[List[str]] = FieldInfo(alias="syncProjectIds", default=None)

    sync_provider: Optional[
        Literal[
            "viewpoint", "aconex", "autodesk", "procore", "revizto", "morta", "asite", "sharepoint", "asta", "dalux"
        ]
    ] = FieldInfo(alias="syncProvider", default=None)

    sync_type: Optional[
        Literal[
            "hubs",
            "resources",
            "users",
            "documents",
            "workflows",
            "comments",
            "table data",
            "rfis",
            "checklists",
            "columns",
            "issues",
            "forms",
            "mail",
            "sheets",
            "reviews",
            "members",
            "models",
            "tasks",
            "forms_headers",
            "forms_fields",
            "forms_templates",
            "tasks_headers",
            "tasks_fields",
            "resource_permissions",
            "workpackages",
            "inspection_plans",
            "inspection_plan_items",
            "locations",
        ]
    ] = FieldInfo(alias="syncType", default=None)

    sync_view_ids: Optional[List[str]] = FieldInfo(alias="syncViewIds", default=None)

    type: Optional[str] = None
    """Deprecated: the name of the folder the resource is in ("" at the top level).

    Use folderId.
    """

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
