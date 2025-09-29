"""Tomling writer module"""

def _write_value(value, indent=4):
    if isinstance(value, str): # Check if str
        escaped = value.replace('"', '\\"')
        return f'"{escaped}"'

    if isinstance(value, bool): # Check if bool
        return "true" if value else "false"

    if isinstance(value, (int, float)): # Check if int/float
        return str(value)

    if isinstance(value, list): # Check if list
        # Check if all items are dicts --> inline array of tables
        if value and all(isinstance(x, dict) for x in value):
            items = ", ".join(_write_value(x, indent) for x in value)
            return f"[{items}]"

        # Otherwise return regular multi-line array
        items = ",\n".join(" " * indent + _write_value(x, indent) for x in value)
        return f"[\n{items},\n]"

    if isinstance(value, dict):
        # Inline table for simple dicts
        items = ", ".join(f"{k}={_write_value(v, indent)}" for k, v in value.items())
        return f"{{{items}}}"

    return str(value) # Fallback

def _write_dict(d, parent_path=None):
    if parent_path is None:
        parent_path = []

    lines = []

    for k, v in d.items():
        current_path = parent_path = [k]

        if isinstance(v, dict):
            # Leaf table: Has at least one non-dict value
            has_values = any(not isinstance(value, dict) for value in v.values())

            if has_values:
                table_name = ".".join(current_path)
                lines.append("") # Blank line before header
                lines.append(f"[{table_name}]")
                for subk, subv in v.items():
                    if isinstance(subv, dict):
                        lines.append(f"{subk} = {_write_value(subv)}") # Inline table
                    else:
                        lines.append(f"{subk} = {_write_value(subv)}")
            else:
                # Intermediate dict --> Recurse without printing header
                lines.append(_write_dict(v, current_path))
        else:
            # Top-level key=value
            lines.append(f"{k} = {_write_value(v)}")

    return "\n".join(lines)

def write_toml(data: dict) -> str:
    """Converts json to toml

    Args:
        data (dict): The dict you want to convert

    Returns:
        str: Formatted toml string
    """
    return _write_dict(data)
