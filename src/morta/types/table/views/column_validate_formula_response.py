# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from ...._models import BaseModel

__all__ = ["ColumnValidateFormulaResponse", "Data", "DataDiagnostic"]


class DataDiagnostic(BaseModel):
    column: Optional[int] = None

    end: Optional[int] = None

    line: Optional[int] = None

    message: Optional[str] = None

    start: Optional[int] = None


class Data(BaseModel):
    diagnostic: Optional[DataDiagnostic] = None

    valid: Optional[bool] = None


class ColumnValidateFormulaResponse(BaseModel):
    data: Optional[Data] = None

    metadata: Optional[Dict[str, object]] = None
