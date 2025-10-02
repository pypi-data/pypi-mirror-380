from typing import Any, Dict, List


def encode(obj: Any, indent: int = 0) -> str:
    if obj is None:
        return "null"
    elif isinstance(obj, bool):
        return "true" if obj else "false"
    elif isinstance(obj, int):
        return str(obj)
    elif isinstance(obj, float):
        return str(obj)
    elif isinstance(obj, str):
        return encode_string(obj)
    elif isinstance(obj, dict):
        return encode_object(obj, indent)
    elif isinstance(obj, list):
        return encode_array(obj, indent)
    else:
        raise TypeError(f"Object of type {type(obj).__name__} is not MAML serializable")


def encode_string(s: str) -> str:
    if "\n" in s:
        if s.endswith("\n"):
            return '"""\n' + s + '"""'
        else:
            return '"""\n' + s + '\n"""'

    result = ['"']
    for ch in s:
        if ch == '"':
            result.append('\\"')
        elif ch == "\\":
            result.append("\\\\")
        elif ch == "\b":
            result.append("\\b")
        elif ch == "\f":
            result.append("\\f")
        elif ch == "\n":
            result.append("\\n")
        elif ch == "\r":
            result.append("\\r")
        elif ch == "\t":
            result.append("\\t")
        elif ord(ch) < 0x20 or ord(ch) == 0x7F:
            result.append(f"\\u{ord(ch):04x}")
        else:
            result.append(ch)
    result.append('"')
    return "".join(result)


def is_valid_identifier(s: str) -> bool:
    if not s:
        return False
    for ch in s:
        if not (ch.isalnum() or ch in ("_", "-")):
            return False
    return True


def encode_object(obj: Dict[str, Any], indent: int = 0) -> str:
    if not obj:
        return "{}"

    lines = ["{"]
    items = list(obj.items())
    # TODO: might want to sort keys for consistent output?
    for i, (key, value) in enumerate(items):
        if is_valid_identifier(key) and not key.isdigit():
            key_str = key
        else:
            key_str = encode_string(key)

        value_str = encode(value, indent + 2)
        lines.append(f"  {key_str}: {value_str}")

    lines.append("}")
    return "\n".join(lines)


def encode_array(arr: List[Any], indent: int = 0) -> str:
    if not arr:
        return "[]"

    lines = ["["]
    for i, item in enumerate(arr):
        value_str = encode(item, indent + 2)
        lines.append(f"  {value_str}")

    lines.append("]")
    return "\n".join(lines)
