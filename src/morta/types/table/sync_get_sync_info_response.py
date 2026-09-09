# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SyncGetSyncInfoResponse", "Data"]


class Data(BaseModel):
    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)

    deleted_at: Optional[datetime] = FieldInfo(alias="deletedAt", default=None)

    failed_sync_attempts: Optional[int] = FieldInfo(alias="failedSyncAttempts", default=None)

    is_deleted: Optional[bool] = FieldInfo(alias="isDeleted", default=None)

    is_synced: Optional[bool] = FieldInfo(alias="isSynced", default=None)

    is_syncing: Optional[object] = FieldInfo(alias="isSyncing", default=None)

    last_sync: Optional[datetime] = FieldInfo(alias="lastSync", default=None)

    name: Optional[str] = None

    public_id: Optional[str] = FieldInfo(alias="publicId", default=None)

    sync_hourly_frequency: Optional[int] = FieldInfo(alias="syncHourlyFrequency", default=None)

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
        ]
    ] = FieldInfo(alias="syncType", default=None)

    type: Optional[str] = None

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)


class SyncGetSyncInfoResponse(BaseModel):
    data: Optional[Data] = None
