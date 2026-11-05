# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["ColumnValidateFormulaParams"]


class ColumnValidateFormulaParams(TypedDict, total=False):
    view_id: Required[str]

    formula: Required[str]
