# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ....._utils import PropertyInfo

__all__ = ["SelectOptionRetrieveSelectOptionsParams"]


class SelectOptionRetrieveSelectOptionsParams(TypedDict, total=False):
    view_id: Required[str]

    after: str
    """The `next` of the page before."""

    dependency_values: Annotated[str, PropertyInfo(alias="dependencyValues")]
    """JSON list of the row's dependency values, in order. Leave out for every option."""

    search: str
    """Words every option holds, in any order or case.

    Only the first 10 words of the first 200 characters are looked for.
    """

    size: int
    """The most options to return."""
