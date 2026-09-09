# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..base_request_context_param import BaseRequestContextParam

__all__ = ["SyncUpdateParams"]


class SyncUpdateParams(TypedDict, total=False):
    table_id: Required[str]

    type: Required[
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
    ]

    context: BaseRequestContextParam

    sync_all_hubs: Annotated[bool, PropertyInfo(alias="syncAllHubs")]

    sync_fields: Annotated[Dict[str, object], PropertyInfo(alias="syncFields")]
