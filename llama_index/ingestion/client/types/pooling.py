# This file was auto-generated by Fern from our API Definition.

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class Pooling(str, enum.Enum):
    """
    Enum of possible pooling choices with pooling behaviors.
    """

    CLS = "cls"
    MEAN = "mean"

    def visit(
        self, cls: typing.Callable[[], T_Result], mean: typing.Callable[[], T_Result]
    ) -> T_Result:
        if self is Pooling.CLS:
            return cls()
        if self is Pooling.MEAN:
            return mean()