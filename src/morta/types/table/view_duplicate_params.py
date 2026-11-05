# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..base_request_context_param import BaseRequestContextParam

__all__ = ["ViewDuplicateParams"]


class ViewDuplicateParams(TypedDict, total=False):
    table_id: Required[str]

    context: BaseRequestContextParam

    custom_view_version: Annotated[Optional[str], PropertyInfo(alias="customViewVersion")]

    duplicate_permissions: Annotated[bool, PropertyInfo(alias="duplicatePermissions")]
