"""Tests reader module"""
import json
import pytest
from tomling import _ensure_path, _read_value, _set_key, read_toml


def test_ensure_path_():
    """Tests _ensure_path function
    """
    d = {}
    result = _ensure_path(d, ["a", "b"])
    assert "a" in d
    assert "b" in d["a"]
    assert result == d["a"]["b"]

def test_set_key():
    """Tests _set_key function
    """
    # Simple Test
    d = {}
    _set_key(d, [], "x", 1)
    assert d["x"] == 1

    # Dotted Test
    d = {}
    _set_key(d, [], "y.z", 2)
    assert d["y"]["z"] == 2

    # Empty Test
    d = {}
    _set_key(d, [], None, 5) # Triggers "if not full: return"
    assert not d

@pytest.mark.parametrize("input_value, expected", [
    ("true", True),
    ("false", False),
    ("123", 123),
    ("123.45", 123.45),
    ("[1, 2, 3]", [1, 2, 3]),
    ("(1,2,3)", (1,2,3)),
    ('"hello"', "hello"),
    ("'world'", "world"),
    ("unquoted", "unquoted"),
    ('"Hello\nWorld"', "Hello\nWorld"),
    ("'Hello\nWorld'", "Hello\nWorld")
])
def test_read_value(input_value, expected):
    """Tests _read_value function

    Args:
        input_value (_type_): The input to convert
        expected (_type_): The expected conversion
    """
    # Test values
    assert _read_value(input_value) == expected # Checking if converts to write instance

def test_read_toml():
    """Tests read_toml function
    """

    # Test basic toml
    toml_data = 'name = "Alice"'
    result = read_toml(toml_data)
    assert '"Alice"' in result

    # Test bytes passing
    toml_data = b'name = "Alice"'
    result = read_toml(toml_data)
    assert '"Alice"' in result

    # Test array on tables toml
    toml_data = '''
[[fruit]]
name = "apple"
color = "red"
'''
    result = read_toml(toml_data)
    data = json.loads(result)
    assert data["fruit"]["name"] == "apple"
    assert data["fruit"]["color"] == "red"

    # Test multiline array edge
    toml_data = '''
values = [
    10,
    20,
    30
]
'''
    result = read_toml(toml_data)
    data = json.loads(result)
    assert data["values"] == [10, 20, 30]

    # Test stripped comments
    toml_data = 'key = "value" # comment'
    result = read_toml(toml_data)
    data = json.loads(result)
    assert data["key"] == "value"
