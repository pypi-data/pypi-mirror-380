import dataclasses
import functools
from typing import (
    TYPE_CHECKING,
    Callable,
    ClassVar,
    Type,
    TypeVar,
    dataclass_transform,
    overload,
)

from .field import _DeclFormSpecifier
from .namespace import Namespace


# ################################ TYPING ######################################


T = TypeVar("T")


# ################################ METACLASS ###################################


class _cmdargument(type):

    # ################## DEFAULTS ##########################

    _cmdargparse_default_form: ClassVar = "-"

    @classmethod
    def default_form(cls, form: _DeclFormSpecifier, /) -> None:
        """Sets the global default declaration form specifier."""

        cls._cmdargparse_default_form = form

    # ################## DECORATOR #########################

    @overload
    @dataclass_transform(eq_default=False)
    def __call__(
        cls,
        _cls: Type[T],
        /,
    ) -> Type[T]: ...

    @overload
    @dataclass_transform(eq_default=False)
    def __call__(
        cls,
        /,
        *,
        form: _DeclFormSpecifier,
    ) -> Callable[[Type[T]], Type[T]]: ...

    @dataclass_transform(eq_default=False)
    def __call__(
        cls,
        _cls: Type[T] | None = None,
        /,
        *,
        form: _DeclFormSpecifier | None = None,
    ) -> Callable[[Type[T]], Type[T]] | Type[T]:
        """
        Decorate as command argument object.

        :param form:
            The default declaration form specifier.
        """

        if _cls is None:
            return functools.partial(
                cls.__call__,
                default=form,
            )  # type: ignore

        setattr(
            _cls,
            "_cmdargparse_default_form",
            form or cls._cmdargparse_default_form,
        )

        return dataclasses.dataclass(
            init=False,
            repr=False,
            eq=False,
        )(_cls)


# ################################ CLASS #######################################


class cmdargument(
    # Allow the type checker to find the namespace attributes.
    (Namespace if TYPE_CHECKING else object),
    metaclass=_cmdargument,
):
    pass
