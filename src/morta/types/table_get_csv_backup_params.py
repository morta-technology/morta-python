# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["TableGetCsvBackupParams"]


class TableGetCsvBackupParams(TypedDict, total=False):
    date: Required[str]
    """The date of the backup to retrieve"""
