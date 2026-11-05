# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..base_request_context_param import BaseRequestContextParam

__all__ = ["DuplicateDuplicateParams"]


class DuplicateDuplicateParams(TypedDict, total=False):
    target_project_id: Required[Annotated[str, PropertyInfo(alias="targetProjectId")]]

    context: BaseRequestContextParam

    duplicate_linked_tables: Annotated[Optional[bool], PropertyInfo(alias="duplicateLinkedTables")]

    duplicate_permissions: Annotated[bool, PropertyInfo(alias="duplicatePermissions")]

    folder_id: Annotated[Optional[str], PropertyInfo(alias="folderId")]
    """A folder in the target hub to file the copy (and any tables copied with it) in.

    Omitted or null: a copy in the same hub goes in the original's folder, one in
    another hub at its top level.
    """

    lock_resource: Annotated[bool, PropertyInfo(alias="lockResource")]
