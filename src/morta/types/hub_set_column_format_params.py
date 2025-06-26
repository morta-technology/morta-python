# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["HubSetColumnFormatParams"]


class HubSetColumnFormatParams(TypedDict, total=False):
    hub_id: Required[str]

    body_kind: Required[Annotated[str, PropertyInfo(alias="kind")]]
