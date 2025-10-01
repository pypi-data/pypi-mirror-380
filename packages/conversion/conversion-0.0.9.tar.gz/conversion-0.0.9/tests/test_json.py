import pytest

from json import JSONDecodeError

from conversion import convert_json


def test_json_dict():
    """
    Ensure json decoding works
    """
    assert {"test": "fool"} == convert_json('{"test": "fool"}')


def test_json_list():
    """
    Ensure json decoding works
    """
    assert ["test", "fool"] == convert_json('["test", "fool"]')


def test_json_with_error():
    """
    Ensure json error is raised
    """
    with pytest.raises(JSONDecodeError):
        convert_json('["test"')


def test_json_with_error_suppressed():
    """
    Just return the input when not raising an exception
    """
    assert '["test"' == convert_json('["test"', raise_exceptions=False)
