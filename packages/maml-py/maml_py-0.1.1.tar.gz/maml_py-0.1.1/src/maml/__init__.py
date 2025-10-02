from typing import Any, Union, TextIO
from importlib.metadata import version, PackageNotFoundError
from .parser import Parser
from .exceptions import MAMLError, MAMLSyntaxError

try:
    __version__ = version("maml-py")
except PackageNotFoundError:
    __version__ = "unknown"
__all__ = ["loads", "load", "dumps", "dump", "MAMLError", "MAMLSyntaxError"]


def loads(s: str) -> Any:
    parser = Parser(s)
    return parser.parse()


def load(fp: TextIO) -> Any:
    return loads(fp.read())


def dumps(obj: Any) -> str:
    from .encoder import encode

    return encode(obj)


def dump(obj: Any, fp: TextIO) -> None:
    fp.write(dumps(obj))
