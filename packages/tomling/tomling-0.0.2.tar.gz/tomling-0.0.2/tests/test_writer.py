"""Tests writer module"""
import dataclasses
from tomling.writer import _write_dict, _write_value, write_toml

@dataclasses.dataclass
class CustomObject:
    """For testing else branch"""
    def __str__(self):
        return "CustomObject"

def test_write_value():
    """Tests _write_value function
    """
    assert _write_value("hello") == '"hello"' # Tests str

    assert _write_value(True) == "true" # Tests true bool
    assert _write_value(False) == "false" # Tests false bool

    assert _write_value(123) == "123" # Tests int
    assert _write_value(3.14) == "3.14" # Tests float

    value = [1, 2, 3]
    expected = "[\n    1,\n    2,\n    3,\n]"
    assert _write_value(value) == expected # Tests list

    value = {"a": 1, "b": 2}
    result = _write_value(value)
    assert "{a=1, b=2}" == result # Tests inline dict

    value = [{"a": 1}, {"b": 2}]
    result = _write_value(value)
    assert result.startswith("[{") and "}" in result # Tests list of dicts

    obj = CustomObject()
    result = _write_value(obj)
    assert result == "CustomObject" # Test else branch

def test_write_dict():
    """Tests _write_dict function
    """
    # Simple dict
    data = {"x": 1, "y": {"z": 2}}
    toml_data = _write_dict(data)
    assert "[y]" in toml_data
    assert "z = 2" in toml_data
    assert "x = 1" in toml_data

    # Inline Table
    data = {"parent": {"child1": {"a": 1}, "child2": {"b": 2}}}
    result = _write_dict(data)
    assert "[child1]" in result
    assert "a = 1" in result
    assert "[child2]" in result
    assert "b = 2" in result

    # Test subv dict branch
    data = {
        "table": {
            "child": {"a": 1},
            "name": "Alice"
        }
    }

    result = _write_dict(data)
    assert "child = {a=1}" in result
    assert "[table]" in result

def test_write_toml():
    """Tests write_toml function
    """
    data = {"table": {"name": "Alice", "values": [1, 2, 3]}}
    toml_data = write_toml(data)
    assert "[table]" in toml_data
    assert "name = \"Alice\"" in toml_data
    assert "1" in toml_data
    assert "2" in toml_data
    assert "3" in toml_data
