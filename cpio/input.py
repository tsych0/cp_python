from cpio.types import Chars, Binary, Lines, Words

# @code begin
import sys
from array import array
from typing import Any

# Global input state for ultra-fast reading
_INPUT_LINES: Any = None
_LINE_INDEX = 0
_CURRENT_LINE_TOKENS = []
_TOKEN_INDEX = 0


def _init_input_lines():
    global _INPUT_LINES, _LINE_INDEX
    if _INPUT_LINES is None:
        _INPUT_LINES = sys.stdin.read().strip().split("\n")
        _LINE_INDEX = 0


def _advance_line():
    global _LINE_INDEX, _CURRENT_LINE_TOKENS, _TOKEN_INDEX
    if _LINE_INDEX >= len(_INPUT_LINES):
        _CURRENT_LINE_TOKENS = []
        _TOKEN_INDEX = 0
        return

    _CURRENT_LINE_TOKENS = _INPUT_LINES[_LINE_INDEX].split()
    _LINE_INDEX += 1
    _TOKEN_INDEX = 0


def _next_token():
    global _TOKEN_INDEX
    if _TOKEN_INDEX >= len(_CURRENT_LINE_TOKENS):
        _advance_line()
        if not _CURRENT_LINE_TOKENS:
            return ""

    if _TOKEN_INDEX < len(_CURRENT_LINE_TOKENS):
        token = _CURRENT_LINE_TOKENS[_TOKEN_INDEX]
        _TOKEN_INDEX += 1
        return token
    return ""


def _next_int():
    return int(_next_token())


def _next_str():
    return _next_token()


def _read_remaining_line_as_ints():
    """Read all remaining tokens in current line as integers"""
    global _TOKEN_INDEX
    if _TOKEN_INDEX >= len(_CURRENT_LINE_TOKENS):
        _advance_line()

    if not _CURRENT_LINE_TOKENS:
        return array("q", [])

    # Get remaining tokens from current line
    remaining = _CURRENT_LINE_TOKENS[_TOKEN_INDEX:]
    _TOKEN_INDEX = len(_CURRENT_LINE_TOKENS)  # Mark line as consumed

    return array("q", [int(x) for x in remaining])


def _read_remaining_line_as_strs():
    """Read all remaining tokens in current line as strings"""
    global _TOKEN_INDEX
    if _TOKEN_INDEX >= len(_CURRENT_LINE_TOKENS):
        _advance_line()

    if not _CURRENT_LINE_TOKENS:
        return []

    # Get remaining tokens from current line
    remaining = _CURRENT_LINE_TOKENS[_TOKEN_INDEX:]
    _TOKEN_INDEX = len(_CURRENT_LINE_TOKENS)  # Mark line as consumed

    return remaining


def _read_remaining_line_as_floats():
    """Read all remaining tokens in current line as floats"""
    global _TOKEN_INDEX
    if _TOKEN_INDEX >= len(_CURRENT_LINE_TOKENS):
        _advance_line()

    if not _CURRENT_LINE_TOKENS:
        return array("d", [])

    # Get remaining tokens from current line
    remaining = _CURRENT_LINE_TOKENS[_TOKEN_INDEX:]
    _TOKEN_INDEX = len(_CURRENT_LINE_TOKENS)  # Mark line as consumed

    return array("d", [float(x) for x in remaining])


# Pre-compiled pattern cache
_PATTERN_CACHE = {}

# Type handlers
_BASIC_TYPES = {
    "int": lambda: _next_int(),
    "str": lambda: _next_str(),
    "float": lambda: float(_next_str()),
    "char": lambda: (_next_str() + " ")[0],
}

_ARRAY_TYPES = {
    "ints": lambda: _read_remaining_line_as_ints(),
    "strs": lambda: _read_remaining_line_as_strs(),
    "floats": lambda: _read_remaining_line_as_floats(),
    "chars": lambda: Chars(array("w", _next_str())),
    "binary": lambda: Binary(array("h", [int(c) for c in _next_str() if c in "01"])),
}


def _is_var_name(section):
    """Ultra-fast variable name detection"""
    section = section.strip()

    # Fast rejection
    if any(c in section for c in "*[]():"):
        return False
    if section in _BASIC_TYPES or section in _ARRAY_TYPES:
        return False
    if section.startswith(("Words[", "Lines[")):
        return False

    # All tokens must be valid identifiers
    return all(part.replace("_", "a").isalnum() for part in section.split())


def _compile_pattern(pattern):
    """Compile pattern to executable operations"""
    if pattern in _PATTERN_CACHE:
        return _PATTERN_CACHE[pattern]

    sections = [s.strip() for s in pattern.split(";") if s.strip()]
    ops = []

    for section in sections:
        if _is_var_name(section):
            names = section.split()
            ops.append(("vars", names))
        else:
            ops.append(("parse", section))

    _PATTERN_CACHE[pattern] = ops
    return ops


def _execute_pattern(ops):
    """Execute compiled pattern operations"""
    results = []
    variables = {}

    for op_type, param in ops:
        if op_type == "vars":
            if len(param) == 1:
                val = _next_int()
                variables[param[0]] = val
                results.append(val)
            else:
                # Multiple variables on same line
                vals = _read_remaining_line_as_ints()
                for i, name in enumerate(param):
                    if i < len(vals):
                        variables[name] = vals[i]
                        results.append(vals[i])
        else:  # op_type == 'parse'
            results.append(_parse_section(param, variables))

    return results


def _parse_section(section, variables):
    """Parse a single section"""
    if "*" not in section:
        return _parse_type(section)

    count_part, type_part = section.split("*", 1)
    count_part = count_part.strip()

    if count_part.isdigit():
        count = int(count_part)
    else:
        count = variables.get(count_part, 1)

    items = [_parse_type(type_part.strip()) for _ in range(count)]
    return Lines(items)


def _parse_type(type_spec):
    """Parse type specification"""
    type_spec = type_spec.strip()

    # Basic types - fastest path
    if type_spec in _BASIC_TYPES:
        return _BASIC_TYPES[type_spec]()

    # Array types
    if type_spec in _ARRAY_TYPES:
        return _ARRAY_TYPES[type_spec]()

    # Structured types
    if type_spec.startswith("Words["):
        return _parse_words(type_spec)
    if type_spec.startswith("Lines["):
        return _parse_lines(type_spec)

    # Fallback
    return _next_str()


def _parse_words(type_spec):
    """Parse Words[type] specification"""
    inner = type_spec[6:-1]

    if ":" in inner:
        item_type, count_str = inner.split(":", 1)
        count = int(count_str.strip())

        if item_type.strip() == "int":
            vals = [_next_int() for _ in range(count)]
        elif item_type.strip() == "float":
            vals = [float(_next_str()) for _ in range(count)]
        else:
            vals = [_next_str() for _ in range(count)]
    else:
        # Read all tokens from current line
        if inner.strip() == "int":
            vals = _read_remaining_line_as_ints()
        elif inner.strip() == "float":
            vals = _read_remaining_line_as_floats()
        else:
            vals = _read_remaining_line_as_strs()

    return Words(vals)


def _parse_lines(type_spec):
    """Parse Lines[type] specification"""
    inner = type_spec[6:-1].strip()
    count = _next_int()
    items = [_parse_type(inner) for _ in range(count)]
    return Lines(items)


# @code end
