# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["DocumentExportParams"]


class DocumentExportParams(TypedDict, total=False):
    iframe_links: Annotated[bool, PropertyInfo(alias="iframeLinks")]

    page_format: Annotated[Literal["A2", "A3", "A4", "letter", "legal"], PropertyInfo(alias="pageFormat")]

    page_orientation: Annotated[Literal["portrait", "landscape"], PropertyInfo(alias="pageOrientation")]

    set_default_format_and_orientation: Annotated[bool, PropertyInfo(alias="setDefaultFormatAndOrientation")]

    table_links: Annotated[bool, PropertyInfo(alias="tableLinks")]

    view_grids: Annotated[object, PropertyInfo(alias="viewGrids")]
    """Map of view public id to its frontend-computed grid layout."""
