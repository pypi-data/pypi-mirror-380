[![PyPI version](https://img.shields.io/pypi/v/tomling?color=green)](https://pypi.org/project/tomling)
[![codecov](https://codecov.io/gh/devs-des1re/tomling/branch/main/graph/badge.svg?token=YOUR_CODECOV_TOKEN)](https://codecov.io/gh/devs-des1re/tomling)
![pylint](https://img.shields.io/badge/pylint-10.00-green)

tomling
===
Tomling is a library which can be used to convert `toml` format to `json` format and `json` format to `toml` format.

How to install?
===
To install you must have Python `3.10` and `pip` install.

```
pip install tomling
```

or 

```
python -m pip install tomling
```

Snippets
===
This is for function `read_toml`
```py
from tomling import read_toml

# Basic TOML to JSON
toml_data = """
name = "Alice"
age = 30
is_admin = true
"""
json_result = read_toml(toml_data)
print(json_result)
# Output: {"name": "Alice", "age": 30, "is_admin": true}

# Multi-line arrays
toml_data = """
values = [
    1,
    2,
    3
]
"""
json_result = read_toml(toml_data)
print(json_result)  # {"values": [1, 2, 3]}

# Array of tables
toml_data = """
[[fruit]]
name = "apple"
color = "red"

[[fruit]]
name = "banana"
color = "yellow"
"""
json_result = read_toml(toml_data)
print(json_result)
# {"fruit": [{"name": "apple", "color": "red"}, {"name": "banana", "color": "yellow"}]}

# Handling escaped characters
toml_data = 'text = "Hello\\nWorld"'
json_result = read_toml(toml_data)
print(json_result)  # {"text": "Hello\nWorld"}

# Bytes input
toml_bytes = b'name = "Alice"\nage = 30'
json_result = read_toml(toml_bytes)
print(json_result)  # {"name": "Alice", "age": 30}
```

This is for `write_toml`
```py
from tomling import write_toml

# Basic dict to TOML
data = {"user": {"name": "Bob", "active": False}}
toml_string = write_toml(data)
print(toml_string)
# Output:
# [user]
# name = "Bob"
# active = false

# Multi-line arrays
data = {"numbers": [10, 20, 30]}
toml_string = write_toml(data)
print(toml_string)
# Output:
# numbers = [
#     10,
#     20,
#     30,
# ]

# Inline tables
data = {
    "settings": {
        "resolution": {"width": 1920, "height": 1080},
        "fullscreen": True
    }
}
toml_string = write_toml(data)
print(toml_string)
# Output:
# [settings]
# resolution = {width=1920, height=1080}
# fullscreen = true

# Mixed content
data = {
    "game": {
        "name": "Tetris",
        "scores": [100, 200, 300],
        "options": {"sound": True, "difficulty": "hard"}
    }
}
toml_string = write_toml(data)
print(toml_string)
```

Contributing
===
If you have any suggestions, or have found bugs, **make sure** the suggestion/bug is not already been said and create a issue in the repository.