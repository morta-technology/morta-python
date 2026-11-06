# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["ChartParam"]


class ChartParam(TypedDict, total=False):
    aggregate: Optional[Literal["sum", "count", "avg", "earliest", "latest"]]

    chart_type: Annotated[
        Literal[
            "bar",
            "horizontal-bar",
            "stacked-bar",
            "stacked-horizontal-bar",
            "clustered-bar",
            "clustered-horizontal-bar",
            "grouped-bar",
            "area",
            "line",
            "multiaxis-line",
            "pie",
            "doughnut",
            "polar-area",
            "radar",
            "scatter",
            "bubble",
            "gantt",
            "s-curve",
            "card",
        ],
        PropertyInfo(alias="chartType"),
    ]

    column_gantt_deadline_id: Annotated[Optional[str], PropertyInfo(alias="columnGanttDeadlineId")]

    column_gantt_end_date_id: Annotated[Optional[str], PropertyInfo(alias="columnGanttEndDateId")]

    column_gantt_start_date_id: Annotated[Optional[str], PropertyInfo(alias="columnGanttStartDateId")]

    column_label_id: Annotated[Optional[str], PropertyInfo(alias="columnLabelId")]

    column_stack_id: Annotated[Optional[str], PropertyInfo(alias="columnStackId")]

    column_value_ids: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="columnValueIds")]

    max_categories: Annotated[Optional[int], PropertyInfo(alias="maxCategories")]

    show_card_label: Annotated[bool, PropertyInfo(alias="showCardLabel")]

    show_legend: Annotated[bool, PropertyInfo(alias="showLegend")]

    show_percentage: Annotated[bool, PropertyInfo(alias="showPercentage")]

    show_title: Annotated[bool, PropertyInfo(alias="showTitle")]

    show_values: Annotated[bool, PropertyInfo(alias="showValues")]

    sort_aggregate: Annotated[Optional[Literal["asc", "desc"]], PropertyInfo(alias="sortAggregate")]
