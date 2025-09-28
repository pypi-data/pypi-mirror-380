import re
from importlib import import_module
from types import ModuleType
from typing import Annotated
from typing import Callable

from pydantic import AfterValidator

__all__ = (
    "DottedPath",
    "IsFalse",
    "IsTrue",
    "RelativeUrlRef",
    "ModuleAttributeRef",
    "DottedPathAttribute",
)

re_dotted_path = re.compile(r"^[a-zA-Z_](\w|\.(?!\.))+$")
re_mod_attr = re.compile(r"^[a-zA-Z_](\w|\.(?!\.))+:\w+$")
ModuleAttribute = object | type[object] | Callable


def dotted_path(value: str) -> ModuleType:
    """Path reference to a python module"""
    if not re.search(re_dotted_path, value):
        if ".." in value:
            raise ValueError(f"{value}: Relative imports unsupported")
        raise ValueError(f"{value}: Incorrect python import reference")
    try:
        module = import_module(value)
    except ImportError as e:
        raise ValueError(f"{value}: Unable to import module") from e
    return module


def mod_attribute(value: str) -> ModuleAttribute:
    """Dotted path reference, with a colon marking the class or function name"""
    if not re.search(re_mod_attr, value):
        if ".." in value:
            raise ValueError(f"{value}: Relative imports unsupported")
        raise ValueError(
            f"{value}: Incorrect python entry point reference. Did you ensure to mark"
            f" the object name with a colon?"
        )
    mod_path, colon, attr = value.partition(":")
    return _get_module_attr(mod_path, attr)

def dotted_path_attribute(value: str) -> ModuleAttribute:
    """Dotted path reference, where the last part is a class or function name"""
    if not re.search(re_dotted_path, value):
        if ".." in value:
            raise ValueError(f"{value}: Relative imports unsupported")
        raise ValueError(f"{value}: Incorrect python import reference")

    mod_path, dot, attr = value.rpartition('.')
    return _get_module_attr(mod_path, attr)

def _get_module_attr(mod_path: str, attr: str) -> ModuleAttribute:
    try:
        module = import_module(mod_path)
    except ImportError as e:
        raise ValueError(f"{mod_path}: Unable to import module") from e

    try:
        return getattr(module, attr)
    except AttributeError as e:
        raise ValueError(f"{attr}: Unable to import object `{attr}' from `{mod_path}'")

def is_true(value: str) -> bool:
    """For a switch that defaults to false"""
    return value.lower() in ["yes", "on", "1", "true"]


def is_false(value: str) -> bool:
    """For a switch that defaults to true"""
    return value.lower() in ["no", "off", "0", "false"]


def relative_url(value: str) -> str:
    """
    A relative URL, that is meant to be prepended with an application specific
    path, to form the reference to a resource.
    The typical example is a resource within a collection of static assets,
    where the specific location of the static URL is depending on the
    environment.

    Discards paths starting with an http or ftp scheme (and their secure
    counterparts), a mailto scheme and a URL starting with a `/'.

    :param value: value to verify
    :return: the value somewhat normalised (double slashes stripped).
    """
    if value.lower().startswith(
        ("http://", "https://", "ftp://", "ftps://", "mailto:")
    ):
        raise ValueError("URL must be relative")
    if value.startswith("/"):
        raise ValueError("URL must be strictly relative: not an absolute path ref")

    if "//" in value:
        return re.sub(r"//+", "/", value)
    return value


DottedPath = Annotated[ModuleType, AfterValidator(dotted_path)]
IsTrue = Annotated[bool, AfterValidator(is_true)]
IsFalse = Annotated[bool, AfterValidator(is_false)]
RelativeUrlRef = Annotated[str, AfterValidator(relative_url)]
ModuleAttributeRef = Annotated[ModuleAttribute, AfterValidator(mod_attribute)]
DottedPathAttribute = Annotated[ModuleAttribute, AfterValidator(dotted_path_attribute)]
