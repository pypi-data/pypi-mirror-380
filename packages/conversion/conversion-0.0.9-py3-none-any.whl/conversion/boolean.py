"""
String to boolean conversion
"""

from .compat import str2bool

__all__ = ["convert_bool"]


def convert_bool(value):
    """
    Returns the value as a boolean

    The value is converted into a boolean if possible. ValueError is raised
    when the value cannot be converted.
    """
    if value == "":
        return False

    return bool(str2bool(value))
