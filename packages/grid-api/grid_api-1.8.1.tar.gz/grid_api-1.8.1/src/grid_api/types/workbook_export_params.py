# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "WorkbookExportParams",
    "Apply",
    "ApplyTarget",
    "ApplyTargetReferenceObject",
    "GoalSeek",
    "GoalSeekControlCell",
    "GoalSeekControlCellReferenceObject",
    "GoalSeekTargetCell",
    "GoalSeekTargetCellReferenceObject",
]


class WorkbookExportParams(TypedDict, total=False):
    apply: Optional[Iterable[Apply]]
    """Cells to update before exporting"""

    goal_seek: Annotated[Optional[GoalSeek], PropertyInfo(alias="goalSeek")]
    """Goal seek.

    Use this to calculate the required input value for a formula to achieve a
    specified target result. This is particularly useful when the desired outcome is
    known, but the corresponding input is not.
    """


class ApplyTargetReferenceObject(TypedDict, total=False):
    cells: Required[str]
    """Unprefixed A1-style range, id, or name"""

    sheet: Required[Optional[str]]
    """Name of the sheet to reference"""


ApplyTarget: TypeAlias = Union[str, ApplyTargetReferenceObject]


class Apply(TypedDict, total=False):
    target: Required[ApplyTarget]
    """Reference for the cell to write to"""

    value: Required[Union[float, str, bool, None]]
    """Value to write to the target cell"""


class GoalSeekControlCellReferenceObject(TypedDict, total=False):
    cells: Required[str]
    """Unprefixed A1-style range, id, or name"""

    sheet: Required[Optional[str]]
    """Name of the sheet to reference"""


GoalSeekControlCell: TypeAlias = Union[str, GoalSeekControlCellReferenceObject]


class GoalSeekTargetCellReferenceObject(TypedDict, total=False):
    cells: Required[str]
    """Unprefixed A1-style range, id, or name"""

    sheet: Required[Optional[str]]
    """Name of the sheet to reference"""


GoalSeekTargetCell: TypeAlias = Union[str, GoalSeekTargetCellReferenceObject]


class GoalSeek(TypedDict, total=False):
    control_cell: Required[Annotated[GoalSeekControlCell, PropertyInfo(alias="controlCell")]]
    """Reference for the cell that will contain the solution"""

    target_cell: Required[Annotated[GoalSeekTargetCell, PropertyInfo(alias="targetCell")]]
    """Reference for the cell that contains the formula you want to resolve"""

    target_value: Required[Annotated[float, PropertyInfo(alias="targetValue")]]
    """The value you want the formula to return"""
