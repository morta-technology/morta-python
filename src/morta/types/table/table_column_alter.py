# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TableColumnAlter"]


class TableColumnAlter(BaseModel):
    date_conversion_format: Optional[
        Literal[
            "DD/MM/YYYY",
            "MM/DD/YYYY",
            "YYYY-MM-DD",
            "DD-Mon-YY",
            "DD/MM/YYYY HH:mm:ss",
            "DD/MM/YYYY HH:mm",
            "MM/DD/YYYY HH:mm:ss",
            "MM/DD/YYYY HH:mm",
            "YYYY-MM-DDTHH:mm:ss",
            "YYYY-MM-DDTHH:mm",
            "YYYY-MM-DD HH:mm:ss",
            "YYYY-MM-DD HH:mm",
            "DD-Mon-YY HH:mm:ss",
            "DD-Mon-YY HH:mm",
        ]
    ] = FieldInfo(alias="dateConversionFormat", default=None)

    run_script_on_all_cells: Optional[bool] = FieldInfo(alias="runScriptOnAllCells", default=None)
