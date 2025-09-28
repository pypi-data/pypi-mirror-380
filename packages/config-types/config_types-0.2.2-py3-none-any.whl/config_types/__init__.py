from typing import TypeAlias

ModuleAttribueRef: TypeAlias = str
"""
Used mainly as entrypoint for an application or to swap in another class. The
object reference is separated by a colon.
"""

DottedPath: TypeAlias = str
"""String that resolves to a python module (f.e. `logging.config')."""
DottedPathAttribute: TypeAlias = str
"""
Used mainly as entrypoint for an application or to swap in another class. The
object reference is the last part of the dotted path.
"""
IsTrue: TypeAlias = str
"""String representing True for use in `os.environ`: ok, yes, 1 and true"""
IsFalse: TypeAlias = str
"""String representing False for use in `os.environ`: not, no, 0 and false"""
RelativeUrlRef: TypeAlias = str
"""
URL that is strictly relative. Meant to be prepended with a well-known URL, that
is different depending the environment, such as the static URL for static
assets.
"""
