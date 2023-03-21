from typing import Any
from .style import in_orange, in_red


def info(obj: Any, ):
    print(_with_preamble('[INFO]', _handle_object_type(obj)))


def warn(obj: Any):
    print(in_orange(_with_preamble('[WARNING]', _handle_object_type(obj))))


def error(obj: Any):
    print(in_red(_with_preamble('[ERROR]', _handle_object_type(obj))))


def _handle_object_type(obj: Any) -> str:
    if isinstance(obj, Exception):
        return f'{type(obj)} {obj}'

    return str(obj)


def _with_preamble(preamble: str, obj: Any):
    return f'{preamble} {obj}'
