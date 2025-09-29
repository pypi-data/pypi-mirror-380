import argparse
import dataclasses
import types
import typing
from typing import Any, Callable, Optional, Tuple, Type, TypeVar

import cmd2

from .field import _DeclFormSpecifier, _FieldDecls
from .namespace import Namespace
from .parser import ArgumentParser


# ################################ TYPING ######################################


TSELF = TypeVar("TSELF", cmd2.Cmd, cmd2.CommandSet)
TARGUMENT = TypeVar("TARGUMENT", bound=object)
TRETURN = TypeVar("TRETURN", Optional[bool], bool, None)


# ################################ METACLASS ###################################


class _cmdcommand(type):

    # ################## DECORATOR #########################

    def __call__(
        cls,
        argtype: Type[TARGUMENT],
        /,
    ) -> Callable[
        [Callable[[TSELF, TARGUMENT], TRETURN]],
        Callable[[TSELF, TARGUMENT], TRETURN],
    ]:
        """Decorate as command function."""

        if hasattr(argtype, "_cmdargparse_command_decorator"):
            return getattr(argtype, "_cmdargparse_command_decorator")

        parser = ArgumentParser()

        _dcfields = dataclasses.fields(
            argtype  # pyright: ignore[reportArgumentType]
        )

        default_form: _DeclFormSpecifier
        default_form = getattr(argtype, "_cmdargparse_default_form")

        for field in _dcfields:
            decls: _FieldDecls | None
            decls = field.metadata["decls"]

            name_or_flags = (
                ()  # Arguments are solely specified using the 'dest' keyword.
                if decls is None
                else argparse_name_or_flags(
                    field.name,
                    decls,
                    default_form=default_form,
                )
            )

            args: dict[str, Any]
            args = field.metadata["args"]

            assert "dest" not in args, (
                "Specifying 'dest' directly is not supported."
                # <format-break>
            )
            args["dest"] = field.name

            if (
                args.get("action", None)
                in ("store_true", "store_false", "store_const")
                # <format-break>
            ):
                # Remove arguments for 'const' and 'type' if specified.
                if args["action"] != "store_const":
                    args.pop("const", ...)
                args.pop("type", ...)

                parser.add_argument(*name_or_flags, **args)

                continue

            # Resolve the type from the fields type annotation.
            if args.get("type", None) is None:
                args["type"] = argparse_type(field.type)

            # Remove custom unspecified arguments.
            if args.get("choicesmap", None) is None:
                args.pop("choicesmap", ...)

            parser.add_argument(*name_or_flags, **args)

        setattr(
            argtype,
            "_cmdargparse_command_decorator",
            _cmdargparse_command_decorator := cmd2.with_argparser(
                parser,
                ns_provider=cls.namespace_provider(argtype),
            ),
        )

        return _cmdargparse_command_decorator  # type: ignore

    # ################## HELPERS ###########################

    @staticmethod
    def namespace_provider(
        argtype: Type[TARGUMENT],
        /,
    ) -> Callable[
        [cmd2.Cmd | cmd2.CommandSet],
        argparse.Namespace,
    ]:
        # Inherit all attributes that are assumed to be constants.
        # (This includes all uppercase attributes not starting with an '_'.)
        namespace = {
            attr: getattr(argtype, attr)
            for attr in dir(argtype)
            if (
                not attr.startswith("_")
                and attr.isupper()
                # <format-break>
            )
        }

        def _provider(cmd: cmd2.Cmd | cmd2.CommandSet) -> Namespace:
            return Namespace(**namespace)

        return _provider


# ################################ CLASS #######################################


class cmdcommand(metaclass=_cmdcommand):

    pass


# ################################ HELPERS #####################################


def argparse_name_or_flags(
    field: str,
    /,
    decls: _FieldDecls,
    *,
    default_form: _DeclFormSpecifier,
) -> Tuple[str, ...]:
    (decl, altdecl) = (decls.decl, decls.altdecl)

    form = decls.form or default_form
    more_decls = decls.more_decls or ()

    # In the augmented declaration specification format the automatically
    # derived declaration is replaced if it has the same form.
    if (decl is None and altdecl is not None) and (
        (form == "-" and not altdecl.startswith("--"))
        or (form == "--" and altdecl.startswith("--"))
    ):
        decl, altdecl = altdecl, None

    return tuple(
        _decl
        for _decl in (
            decl or (form + field),
            altdecl,
            *more_decls,
        )
        if _decl is not None
    )


def argparse_type(type: Any, /) -> Type[Any]:
    if isinstance(type, str):
        raise TypeError("forward reference type annotations are not supported")

    origin = typing.get_origin(type)
    if origin is None:
        return type

    if origin is typing.Annotated:
        (argtype, *_) = typing.get_args(type)
        return argparse_type(argtype)

    # We assume the first argument of the union type is the primary type that
    # should be passed to the `argparse` module.
    if isinstance(type, types.UnionType):
        (argtype, *_) = typing.get_args(type)
        return argtype
    elif origin is typing.Union:
        (argtype, *_) = typing.get_args(type)
        return argtype

    raise TypeError("unsupported type annotation")
