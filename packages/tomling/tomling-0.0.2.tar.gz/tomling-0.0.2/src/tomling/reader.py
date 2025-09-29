"""Tomling reader module"""
import ast
import json
import re
from typing import Union


def _ensure_path(d: dict, path):
    """"""
    cur = d # Start at root dictionary
    for p in path:
        if p not in cur or not isinstance(cur[p], dict):
            cur[p] = {} # Create nested dictionary if missing
        cur = cur[p] # Move reference into nested dictionary
    return cur # Return innermost dictionary

def _set_key(d: dict, path, key, value):
    full = [] # Full path including table path and dotted key

    if path:
        full.extend(path) # Add current table path

    if isinstance(key, str) and "." in key:
        full.extend(k.strip() for k in key.split(".")) # Split dotted key
    elif key is not None:
        full.append(key) # Add simple key

    if not full:
        return # Nothing to set

    parent = _ensure_path(d, full[:-1]) # Ensure intermediate dicts exist
    parent[full[-1]] = value # Set value at final key

def _read_value(s: str):
    s = s.strip() # Remove surrounding whitespace

    # Check boolean
    if s.lower() == "true":
        return True

    if s.lower() == "false":
        return False

    # Check numbers, lists, tuples
    try:
        return ast.literal_eval(s)
    except Exception:
        if s.startswith('"') and s.endswith('"'):
            return s[1:-1].encode("utf-8").decode("unicode_escape") # Basic string

        if s.startswith("'") and s.endswith("'"):
            return s[1:-1] # Literal String

        return s # Fallback string

def read_toml(data: Union[str, bytes]) -> str:
    """Converts toml file to json

    Args:
        data (Union[str, bytes]): The toml file/str you want to pass

    Returns:
        str: Returns formatted json
    """
    if isinstance(data, (bytes, bytearray)):
        data = data.decode("utf-8") # Decodes bytes
    else:
        data = str(data)

    out = {}
    cur_path = []

    lines = data.splitlines()
    multi_line_key = None
    multi_line_value = []

    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#"):
            continue

        # Removes comments outside quotes
        m = re.match(r'(.*?)(?<!\\)#.*', line)
        if m:
            line = m.group(1).strip()

        # Add table header
        if line.startswith("[") and line.endswith("]"):
            inner = line[1:-1].strip()

            if inner.startswith("[") and inner.endswith("]"): # Array of tables
                inner = inner[1:-1].strip()

            cur_path = [p.strip() for p in inner.split(".")] if inner else []
            _ensure_path(out, cur_path)

            continue

        # Multi-line array continuation
        if multi_line_key:
            multi_line_value.append(line)

            if line.endswith("]"): # Array Ends
                full_value = "\n".join(multi_line_value)
                value = _read_value(full_value)

                _set_key(out, cur_path, multi_line_key, value)
                multi_line_key = None
                multi_line_value = []

        # Key = value
        if "=" in line:
            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip()

            if value.startswith("[") and not value.endswith("]"):
                multi_line_key = key # Start multi-line array
                multi_line_value = [value]

                continue

            value = _read_value(value)
            _set_key(out, cur_path, key, value)

            continue

    return json.dumps(out)
