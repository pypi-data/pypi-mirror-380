import pytest

from conversion import convert_bool


def test_empty_string():
    """
    Specifically test that an empty string returns False
    """
    convert_bool("") == False


@pytest.mark.parametrize("value", ("no", "n", "false", "f", "0"))
def test_false(value):
    """
    Ensure all expected strings return False
    """

    assert convert_bool(value) == False


@pytest.mark.parametrize("value", ("yes", "y", "true", "t", "1"))
def test_true(value):
    """
    Ensure all expected strings return True
    """
    assert convert_bool(value)
