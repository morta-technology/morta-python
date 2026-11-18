# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["SelectOptionRetrieveCheckParams"]


class SelectOptionRetrieveCheckParams(TypedDict, total=False):
    view_id: Required[str]

    values: Required[str]
    """A JSON-encoded list of up to 1000 values to check."""
