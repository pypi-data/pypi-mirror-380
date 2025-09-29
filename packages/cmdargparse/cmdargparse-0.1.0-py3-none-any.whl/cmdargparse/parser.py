from typing import Annotated, Any

import cmd2


# ################################ PARSER ######################################


class ArgumentParser(cmd2.Cmd2ArgumentParser):

    # Registers a custom argparse argument parameter.
    #   https://cmd2.readthedocs.io/en/stable/api/argparse_custom/#cmd2.argparse_custom.register_argparse_argument_parameter
    #   ```
    #     def register_argparse_argument_parameter(
    #         param_name: str,
    #         param_type: Optional[Type[Any]],
    #     ) -> None: ...
    #   ```

    def __init__(
        self,
        *args: Annotated[Any, "passthrough"],
        **kwargs: Annotated[Any, "passthrough"],
    ) -> None:
        super(cmd2.Cmd2ArgumentParser, self).__init__(*args, **kwargs)

        from .actions import StoreAction

        self.register("action", None, StoreAction)
        self.register("action", "store", StoreAction)
        # self.register('action', 'store_const', _StoreConstAction)
        # self.register('action', 'store_true', _StoreTrueAction)
        # self.register('action', 'store_false', _StoreFalseAction)
        # self.register('action', 'append', _AppendAction)
        # self.register('action', 'append_const', _AppendConstAction)
        # self.register('action', 'count', _CountAction)
        # self.register('action', 'help', _HelpAction)
        # self.register('action', 'version', _VersionAction)
        # self.register('action', 'parsers', _SubParsersAction)
        # self.register('action', 'extend', _ExtendAction)
