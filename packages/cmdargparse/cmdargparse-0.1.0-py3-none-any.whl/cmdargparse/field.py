import argparse
import dataclasses
from typing import (
    TYPE_CHECKING,
    Annotated,
    Any,
    Callable,
    Collection,
    Literal,
    Mapping,
    NamedTuple,
    Never,
    Sequence,
    Tuple,
    Type,
    TypeAlias,
    TypedDict,
    TypeVar,
    Union,
    Unpack,
    overload,
)

from .unset import Unset, isunset, on_unset


# NOTE Due to the complexity of the positional-only arguments of some overloads,
#      we disable the overload concistency check reporting.
# pyright: reportInconsistentOverload=false

# NOTE Some overloads are wrongfully (in my opinion) recognized as overlapping.
#      It most likely is caused by the unpacked typed dict used for additional
#      keyword arguments.
#      For now we just disable the overlapping overload reporting.
# pyright: reportOverlappingOverload=false


# ################################ TYPING ######################################


T = TypeVar("T")

TONCE: TypeAlias = Any


_FieldType: TypeAlias = Annotated[Any, dataclasses.Field]


_DeclFormSpecifier: TypeAlias = Literal["--", "-"]


# ################################ TYPES #######################################


class _FieldDecls(NamedTuple):

    form: _DeclFormSpecifier | None
    """Specifies the default form of the ... declaration."""

    decl: Annotated[
        str | None,
        Annotated[None, "[derived]"],
        Annotated[None, "[augmented]"],
        Annotated[str, "[explicit]"],
        Annotated[str, "[keyword]"],
    ]
    """Specifies the primary ... declaration."""

    altdecl: Annotated[
        str | None,
        Annotated[None, "[derived]"],
        Annotated[str, "[augmented]"],
        Annotated[str | None, "[explicit]"],
        Annotated[str | None, "[keyword]"],
    ]
    """Specifies the alternative ... declaration."""

    more_decls: Sequence[str] | None
    """Specifies additional ... declarations."""


class _DeclsCompatibleArgs(TypedDict, total=False):

    form: _DeclFormSpecifier
    """Specifies the default form of the ... declaration."""
    decls: Tuple[str, str] | str
    """Explicitly specifies all ... declarations."""
    more_decls: Sequence[str] | str
    """Specifies additional ... declarations."""


# ################################ METACLASS ###################################


class _cmdfield(type):

    # Declarations Specification Formats
    # - derived (default)
    #   The declaration name will be automatically derived from the field name.
    # - augmented
    #   The specified declaration will replace the automatically derived
    #   declaration if both have the same form. Otherwise it will be added as
    #   an additional declaration.
    # - explicit
    #   The specified declaration(s) (positional arguments) will replace the
    #   automatically derived declaration.
    # - keyword
    #   The specified declaration(s) (`decls` keyword argument) will replace the
    #   automatically derived declaration.

    # ################## ARGUMENT ##########################

    class _ArgumentArgs(TypedDict, total=False):

        type: Annotated[Any, Callable[[str], Annotated[Any, "FieldType"]]]

        help: str
        helpvar: str

    @overload
    # overload @ argument (required)
    def argument(
        cls,
        /,
        # *,
        **args: Unpack[_ArgumentArgs],
    ) -> _FieldType: ...

    @overload
    # overload @ argument with default
    def argument(
        cls,
        /,
        *,
        default: TONCE,
        **args: Unpack[_ArgumentArgs],
    ) -> _FieldType: ...

    @overload
    # overload @ choice argument (required)
    def argument(
        cls,
        /,
        choices: Collection[T],
        choicesmap: Mapping[T, T] | None = ...,
        # *,
        **args: Unpack[_ArgumentArgs],
    ) -> _FieldType: ...

    @overload
    # overload @ choice argument with default
    def argument(
        cls,
        /,
        choices: Collection[T],
        choicesmap: Mapping[T, T] | None = ...,
        *,
        default: TONCE,
        **args: Unpack[_ArgumentArgs],
    ) -> _FieldType: ...

    def argument(
        cls,
        /,
        choices: Collection[T] | None = None,
        choicesmap: Mapping[T, T] | None = None,
        *,
        default: TONCE | Unset = ~Unset,
        **args: Unpack[_ArgumentArgs],
    ) -> _FieldType:
        """
        Defines a command-line argument. (positional)

        :param choices:
            The restricted set of values allowed for the argument.
        :param choicesmap:
            Additional values allowed for the argument that each map to the
            specified value in the restricted set of values.
        :param default:
            The arguments default value if not specified.
            (Providing a default value makes the argument optional.)

        :param type:
            Explicitly specifies the `type` to be used by `argparse`.
            <br/> https://docs.python.org/3/library/argparse.html#type

        :param help:
            Brief description of the argument.
        :param helpvar:
            Reference name of the argument value in the help message.

        """
        return _argparse(
            None,
            nargs=("?" if not isunset(default) else None),
            choices=choices,
            choicesmap=choicesmap,
            default=on_unset(default, None),
            type=args.get("type", None),
            help=args.get("help", None),
            metavar=args.get("helpvar", None),
        )

    # ################## OPTION ############################

    class _OptionArgs(TypedDict, total=False):

        form: _DeclFormSpecifier
        decls: Tuple[str, str] | str
        more_decls: Sequence[str] | str

        type: Annotated[Any, Callable[[str], Annotated[Any, "FieldType"]]]

        required: bool

        help: str
        helpvar: str

    @overload
    # overload @ option [derived]
    def option(
        cls,
        /,
        # *,
        **args: Unpack[_OptionArgs],
    ) -> _FieldType: ...

    @overload
    # overload @ option [augmented]
    def option(
        cls,
        decl: str,
        /,
        # *,
        **args: Unpack[_OptionArgs],
    ) -> _FieldType: ...

    @overload
    # overload @ option [explicit]
    def option(
        cls,
        decl: str,
        altdecl: str,
        /,
        # *,
        **args: Unpack[_OptionArgs],
    ) -> _FieldType: ...

    @overload
    # overload @ option with default [derived]
    def option(
        cls,
        /,
        *,
        default: TONCE,
        **args: Unpack[_OptionArgs],
    ) -> _FieldType: ...

    @overload
    # overload @ option with default [augmented]
    def option(
        cls,
        decl: str,
        /,
        *,
        default: TONCE,
        **args: Unpack[_OptionArgs],
    ) -> _FieldType: ...

    @overload
    # overload @ option with default [explicit]
    def option(
        cls,
        decl: str,
        altdecl: str,
        /,
        *,
        default: TONCE,
        **args: Unpack[_OptionArgs],
    ) -> _FieldType: ...

    @overload
    # overload @ choice option [derived]
    def option(
        cls,
        /,
        choices: Collection[T],
        choicesmap: Mapping[T, T] | None = ...,
        # *,
        **args: Unpack[_OptionArgs],
    ) -> _FieldType: ...

    @overload
    # overload @ choice option [augmented]
    def option(
        cls,
        decl: str,
        /,
        choices: Collection[T],
        choicesmap: Mapping[T, T] | None = ...,
        # *,
        **args: Unpack[_OptionArgs],
    ) -> _FieldType: ...

    @overload
    # overload @ choice option [explicit]
    def option(
        cls,
        decl: str,
        altdecl: str,
        /,
        choices: Collection[T],
        choicesmap: Mapping[T, T] | None = ...,
        # *,
        **args: Unpack[_OptionArgs],
    ) -> _FieldType: ...

    @overload
    # overload @ choice option with default [derived]
    def option(
        cls,
        /,
        choices: Collection[T],
        choicesmap: Mapping[T, T] | None = ...,
        *,
        default: TONCE,
        **args: Unpack[_OptionArgs],
    ) -> _FieldType: ...

    @overload
    # overload @ choice option with default [augmented]
    def option(
        cls,
        decl: str,
        /,
        choices: Collection[T],
        choicesmap: Mapping[T, T] | None = ...,
        *,
        default: TONCE,
        **args: Unpack[_OptionArgs],
    ) -> _FieldType: ...

    @overload
    # overload @ choice option with default [explicit]
    def option(
        cls,
        decl: str,
        altdecl: str,
        /,
        choices: Collection[T],
        choicesmap: Mapping[T, T] | None = ...,
        *,
        default: TONCE,
        **args: Unpack[_OptionArgs],
    ) -> _FieldType: ...

    def option(
        cls,
        decl: str | None = None,
        altdecl: str | None = None,
        /,
        choices: Collection[T] | None = None,
        choicesmap: Mapping[T, T] | None = None,
        *,
        default: TONCE | Unset = ~Unset,
        **args: Unpack[_OptionArgs],
    ) -> _FieldType:
        """
        Defines a command-line option. (non-positional, value-bound)

        :param decl:
            Specifies the primary option declaration.
        :param altdecl:
            Specifies the alternative option declaration.

        :param choices:
            The restricted set of values allowed for the option.
        :param choicesmap:
            Additional values allowed for the option that each map to the
            specified value in the restricted set of values.
        :param default:
            The options default value if not specified.

        :param form:
            Specifies the default form of the option declaration.
        :param decls:
            Explicitly specifies all option declarations.
        :param more_decls:
            Specifies additional option declarations.

        :param type:
            Explicitly specifies the `type` to be used by `argparse`.
            <br/> https://docs.python.org/3/library/argparse.html#type

        :param required:
            Marks the option as required.

        :param help:
            Brief description of the option.
        :param helpvar:
            Reference name of the option value in the help message.

        """
        if decl is None:
            decl, altdecl, choices = (
                # 0 arguments
                (None, None, None)
            )  # type: ignore
        elif altdecl is None:
            decl, altdecl, choices = (
                # 1 argument
                (decl, None, None)
                if isinstance(decl, str)
                else (None, None, decl)
            )  # type: ignore
        elif choices is None:
            decl, altdecl, choices = (
                # 2 arguments
                (decl, altdecl, None)
                if isinstance(decl, str)
                else (decl, None, altdecl)
            )  # type: ignore
        else:
            decl, altdecl, choices = (
                # 3 arguments
                (decl, altdecl, choices)
            )  # type: ignore
        return _argparse(
            _decls(decl, altdecl, args),
            nargs=("?" if not isunset(default) else None),
            choices=choices,
            choicesmap=choicesmap,
            default=on_unset(default, None),
            required=args.get("required", False),
            type=args.get("type", None),
            help=args.get("help", None),
            metavar=args.get("helpvar", None),
        )

    # ################## FLAG ##############################

    class _FlagArgs(TypedDict, total=False):

        form: _DeclFormSpecifier
        decls: Tuple[str, str] | str
        more_decls: Sequence[str] | str

        type: Annotated[Any, Callable[[str], Annotated[Any, "FieldType"]]]

        help: str

    @overload
    # overload @ flag [derived]
    def flag(
        cls,
        /,
        # *,
        **args: Unpack[_FlagArgs],
    ) -> _FieldType: ...

    @overload
    # overload @ flag [augmented]
    def flag(
        cls,
        decl: str,
        /,
        # *,
        **args: Unpack[_FlagArgs],
    ) -> _FieldType: ...

    @overload
    # overload @ flag [explicit]
    def flag(
        cls,
        decl: str,
        altdecl: str,
        /,
        # *,
        **args: Unpack[_FlagArgs],
    ) -> _FieldType: ...

    @overload
    # overload @ inverse flag [derived]
    def flag(
        cls,
        /,
        *,
        invert: bool,
        **args: Unpack[_FlagArgs],
    ) -> _FieldType: ...

    @overload
    # overload @ inverse flag [augmented]
    def flag(
        cls,
        decl: str,
        /,
        *,
        invert: bool,
        **args: Unpack[_FlagArgs],
    ) -> _FieldType: ...

    @overload
    # overload @ inverse flag [explicit]
    def flag(
        cls,
        decl: str,
        altdecl: str,
        /,
        *,
        invert: bool,
        **args: Unpack[_FlagArgs],
    ) -> _FieldType: ...

    @overload
    # overload @ constant-valued flag [derived]
    def flag(
        cls,
        /,
        *,
        const: TONCE,
        **args: Unpack[_FlagArgs],
    ) -> _FieldType: ...

    @overload
    # overload @ constant-valued flag [augmented]
    def flag(
        cls,
        decl: str,
        /,
        *,
        const: TONCE,
        **args: Unpack[_FlagArgs],
    ) -> _FieldType: ...

    @overload
    # overload @ constant-valued flag [explicit]
    def flag(
        cls,
        decl: str,
        altdecl: str,
        /,
        *,
        const: TONCE,
        **args: Unpack[_FlagArgs],
    ) -> _FieldType: ...

    def flag(
        cls,
        decl: str | None = None,
        altdecl: str | None = None,
        /,
        *,
        invert: bool = False,
        const: TONCE | Unset = ~Unset,
        **args: Unpack[_FlagArgs],
    ) -> _FieldType:
        """
        Defines a command-line flag. (non-positional, non-value)

        :param decl:
            Specifies the primary flag declaration.
        :param altdecl:
            Specifies the alternative flag declaration.

        :param invert:
            Sets the value `False` instead of `True` if the flag is specified.
        :param const:
            The value to set if the flag is specified.

        :param form:
            Specifies the default form of the flag declaration.
        :param decls:
            Explicitly specifies all flag declarations.
        :param more_decls:
            Specifies additional flag declarations.

        :param type:
            Explicitly specifies the `type` to be used by `argparse`.
            <br/> https://docs.python.org/3/library/argparse.html#type

        :param help:
            Brief description of the flag.

        """
        return _argparse(
            _decls(decl, altdecl, args),
            action=(
                ("store_false" if invert else "store_true")
                if isunset(const)
                else "store_const"
            ),
            const=on_unset(const, None),
            type=args.get("type", None),
            help=args.get("help", None),
        )


# ################################ CLASS #######################################


class cmdfield(metaclass=_cmdfield):

    pass


# ################################ ARGPARSE ####################################
# https://docs.python.org/3/library/argparse.html#the-add-argument-method

if TYPE_CHECKING:

    def _argparse(
        decls: _FieldDecls | None,
        /,
        *,
        # ####### argparse #############
        action: Union[
            Type[argparse.Action],
            Literal[
                "store",
                "store_const",
                "store_true",
                "store_false",
                "append",
                "append_const",
                "count",
                "help",
                "version",
                "extend",
            ],
            Annotated[Never, "<unspecified>"],
        ] = ...,
        nargs: Union[
            Annotated[int, "N"],
            Literal["?", "*", "+"],
            Annotated[None, "<unspecified>"],
        ] = ...,
        const: Union[
            Annotated[Any, TONCE],
            Annotated[None, "<unspecified>"],
        ] = ...,
        default: Union[
            Annotated[Any, TONCE],
            Annotated[None, "<unspecified>"],
        ] = ...,
        type: Union[
            Annotated[Any, Callable[[str], Annotated[Any, "FieldType"]]],
            Annotated[None, "<unspecified>"],
        ] = ...,
        choices: Union[
            Collection[Annotated[Any, T]],
            Annotated[None, "<unspecified>"],
        ] = ...,
        required: Union[
            bool,
            Annotated[Never, "<unspecified>"],
        ] = ...,
        help: Union[
            str,
            Annotated[None, "<unspecified>"],
        ] = ...,
        metavar: Union[
            Tuple[str, ...] | str,
            Annotated[None, "<unspecified>"],
        ] = ...,
        dest: Annotated[
            Never, "Specifying 'dest' directly is not supported."
        ] = ...,
        deprecated: Union[
            bool,
            Annotated[Never, "<unspecified>"],
        ] = ...,
        version: Union[
            str,
            Annotated[Never, "<unspecified>"],
        ] = ...,
        # ####### custom ###############
        choicesmap: Union[
            Mapping[Annotated[Any, T], Annotated[Any, T, "choices"]],
            Annotated[None, "<unspecified>"],
        ] = ...,
    ) -> _FieldType: ...

else:

    def _argparse(
        decls: Any,
        **args: Any,
    ) -> _FieldType:
        return dataclasses.field(
            init=False,
            repr=False,
            compare=False,
            metadata={
                "decls": decls,
                "args": args,
            },
        )


def _decls(
    decl: str | None,
    altdecl: str | None,
    /,
    args: _DeclsCompatibleArgs,
) -> _FieldDecls:
    (form, decls, more_decls) = (
        args.get("form", None),
        args.get("decls", None),
        args.get("more_decls", None),
    )

    if isinstance(more_decls, str):
        more_decls = (more_decls,)

    if decls is not None:
        # Declaration Specification Format: [keyword]

        if decl is not None or altdecl is not None:
            raise ValueError(
                "Declarations cannot be specified using the positional "
                "arguments if the 'decls' keyword argument is specified."
            )

        (_decl, _altdecl) = (
            (decls, None)
            if isinstance(decls, str)
            else decls
            # <format-break>
        )
        if (
            (_decl and not _decl.startswith("-"))
            or (_altdecl and not _altdecl.startswith("-"))
            # <format-break>
        ):
            raise ValueError(
                "All declarations must start with either '--' or '-'."
            )

        return _FieldDecls(None, _decl, _altdecl, more_decls)

    elif decl is None and altdecl is None:
        # Declaration Specification Format: [derived]

        return _FieldDecls(form, None, None, more_decls)

    elif decl is not None and altdecl is not None:
        # Declaration Specification Format: [explicit]

        if not decl.startswith("-") or not altdecl.startswith("-"):
            raise ValueError(
                "All declarations must start with either '--' or '-'."
            )
        elif (
            (decl.startswith("--") and altdecl.startswith("--"))
            or (not decl.startswith("--") and not altdecl.startswith("--"))
            # <format-break>
        ):
            raise ValueError(
                "Declarations specified using the positional arguments must "
                "have different forms."
            )

        return _FieldDecls(form, decl, altdecl, more_decls)

    else:
        # Declaration Specification Format: [augmented]
        assert decl is not None and altdecl is None, (
            "The augmented declaration specification format should always have "
            "'decl' specified and 'altdecl' unspecified."
        )

        if not decl.startswith("-"):
            raise ValueError(
                "All declarations must start with either '--' or '-'."
            )

        return _FieldDecls(form, None, decl, more_decls)
