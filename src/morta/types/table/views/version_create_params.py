# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["VersionCreateParams"]


class VersionCreateParams(TypedDict, total=False):
    html: Required[str]

    publish: bool
