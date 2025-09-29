import argparse

import cmd2


# ################################ NAMESPACE ###################################


class Namespace(argparse.Namespace):

    def pfields(self, cmd: cmd2.Cmd, /) -> None:
        """Prints all fields using the feedback output function."""

        fields = tuple(
            attr
            for attr in self.__dict__
            if (
                # Skip all internalized attributes.
                not attr.startswith("_")
                # Skip all cmd2-related attributes.
                and not attr.startswith("cmd2")
            )
        )

        maxlen = max(
            len(attr)
            for attr in fields
            # <format-break>
        )

        cmd.pfeedback("[Namespace]")
        for name in fields:
            cmd.pfeedback(
                f"  {str.ljust(name, maxlen)!s} :  {self.__dict__[name]!r}"
            )
        if not fields:
            cmd.pfeedback("  (no fields)")
