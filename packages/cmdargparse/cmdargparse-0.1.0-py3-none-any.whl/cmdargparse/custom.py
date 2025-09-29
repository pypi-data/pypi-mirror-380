import argparse
from typing import (
    TYPE_CHECKING,
    Annotated,
    Any,
    Generic,
    Protocol,
    Self,
    Sequence,
    TypeAlias,
    TypeIs,
    TypeVar,
)

from .namespace import Namespace
from .parser import ArgumentParser


# ################################ GLOBALS #####################################


__all__ = (
    # fmt: off
    "TANY",
    "decorator",
    "is_single_value", "is_multiple_values",
    # fmt: on
)


# ################################ TYPING ######################################


T = TypeVar("T")
T_ct = TypeVar("T_ct", contravariant=True)

TANY: TypeAlias = Any


# ################################ DECORATORS ##################################


class _ArgparseActionDunderCallCallable(Protocol):
    def __call__(
        _self,
        self: Annotated[Any, Self],
        parser: argparse.ArgumentParser,
        namespace: argparse.Namespace,
        values: str | Sequence[Any] | None,
        option_string: str | None = None,
    ) -> None: ...


class _ActionDunderCallCallable(Protocol, Generic[T_ct]):
    def __call__(
        _self,
        self: Annotated[Any, Self],
        parser: ArgumentParser,
        namespace: Namespace,
        values: Sequence[T_ct] | T_ct,
        option_string: str | None = None,
    ) -> None: ...


class decorator:

    @staticmethod
    def call(
        func: _ActionDunderCallCallable[T_ct],
        /,
    ) -> Annotated[Any, _ArgparseActionDunderCallCallable]:
        """Supresses `reportIncompatibleMethodOverride` on `Action.__call__`."""
        return func  # pyright: ignore[reportReturnType]


# ################################ FUNCTIONS ###################################


def is_single_value(
    values: Sequence[TANY] | TANY,
    /,
) -> TypeIs[TANY]:
    """Typing helper for the `values` argument of `Action.__call__`."""
    # The `argparse` module passes multiple values as a list.
    return not isinstance(values, list)


def is_multiple_values(
    values: Sequence[TANY] | TANY,
    /,
) -> TypeIs[Sequence[TANY]]:
    """Typing helper for the `values` argument of `Action.__call__`."""
    # The `argparse` module passes multiple values as a list.
    return isinstance(values, list)


# ################################ TEMPALTES ###################################
if TYPE_CHECKING:

    class ActionTemplate(argparse.Action):

        def __init__(
            self,
            *args: Annotated[Any, "passthrough"],
            **kwargs: Annotated[Any, "passthrough"],
        ) -> None:
            assert not args, (
                "There should be no positional arguments if not explicitly "
                "specified. (The `argparse` module passes by keyword.)"
            )
            super().__init__(*args, **kwargs)

        @decorator.call
        def __call__(
            self,
            parser: ArgumentParser,
            namespace: Namespace,
            values: Sequence[TANY] | TANY,
            option_string: str | None = None,
        ) -> None: ...
