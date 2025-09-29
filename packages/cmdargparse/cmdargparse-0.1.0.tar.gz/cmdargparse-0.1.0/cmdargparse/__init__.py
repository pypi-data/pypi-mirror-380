import cmd2 as _cmd2

from .argument import cmdargument
from .command import cmdcommand
from .field import cmdfield
from .namespace import Namespace
from .parser import ArgumentParser


_cmd2.set_default_argument_parser_type(ArgumentParser)
