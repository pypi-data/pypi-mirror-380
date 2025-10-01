import pytest

from conversion import convert_list


def test_delimiter():
    """
    Ensure the delimiter kwarg is used
    """
    assert ["a", "b"] == convert_list("a:b", delimiter=":")


def test_empty_list():
    """
    Ensure an empty string returns an empty list
    """
    assert [] == convert_list("")


def test_exception_raised():
    """
    Ensure string conversion kwarg works
    """
    with pytest.raises(TypeError):
        convert_list(b"notstring", raise_exceptions=True)


def test_empty_list_on_none():
    """
    Ensure a null value returns an empty list
    """
    assert [] == convert_list(None)


def test_single_element():
    """
    Ensure a string without a delimiter is returned as a single element list
    """
    assert ["a"] == convert_list("a")


def test_split_and_stripped():
    """
    Ensure spaces are stripped off values
    """
    assert ["a", "b"] == convert_list("a, b")
