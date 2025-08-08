from cpio.input import *
from cpio.types import *

# @code begin
from typing import Any


class PatternParser:
    """Complete pattern parser for all competitive programming scenarios"""

    def __init__(self, input_reader: CPInput):
        self.input_reader = input_reader
        self.variables = {}

    def parse_pattern(self, pattern: str) -> list:
        """Parse comprehensive pattern format"""
        sections = [s.strip() for s in pattern.split(";") if s.strip()]
        results = []

        if not sections:
            return results

        for section in sections:
            if self._is_variable_declaration(section):
                # Variables like 'n m k'
                var_names = section.split()
                if len(var_names) == 1:
                    value = self.input_reader.read_int()
                    self.variables[var_names[0]] = value
                    results.append(value)
                else:
                    values = self.input_reader.read_ints()
                    for i, name in enumerate(var_names):
                        if i < len(values):
                            self.variables[name] = values[i]
                            results.append(values[i])
            else:
                # Direct type or section
                results.append(self._parse_section(section))

        return results

    @staticmethod
    def _is_variable_declaration(section: str) -> bool:
        """Distinguish variables from type specs"""
        # Known type keywords
        known_types = {
            "int",
            "str",
            "float",
            "char",
            "binary",
            "ints",
            "strs",
            "floats",
            "chars",
        }

        # Contains special characters = type spec
        if any(char in section for char in "*[]():"):
            return False

        # Is a known type = type spec
        if section.strip() in known_types:
            return False

        # Starts with structured type = type spec
        if section.strip().startswith(("Words[", "Lines[")):
            return False

        # All parts are valid variable names
        parts = section.split()
        return all(
            part.replace("_", "a").isalnum() and part not in known_types
            for part in parts
        )

    def _parse_section(self, section: str) -> Any:
        """Parse any section (with or without repetition)"""
        if "*" not in section:
            return self._parse_type_spec(section)

        count_part, type_part = section.split("*", 1)
        count_part = count_part.strip()

        # Resolve count
        if count_part.isdigit():
            count = int(count_part)
        else:
            count = self.variables.get(count_part, 0)

        # Parse repeated items
        items = []
        for _ in range(count):
            items.append(self._parse_type_spec(type_part.strip()))
        return Lines(items)

    def _parse_type_spec(self, type_spec: str) -> Any:
        """Parse single type specification"""
        type_spec = type_spec.strip()

        # Basic types
        if type_spec == "int":
            return self.input_reader.read_int()
        elif type_spec == "str":
            return self.input_reader.read_str()
        elif type_spec == "float":
            return float(self.input_reader.read_str())
        elif type_spec == "char":
            line = self.input_reader.read_str()
            return line[0] if line else ""

        # Collection types
        elif type_spec == "ints":
            return self.input_reader.read_ints()
        elif type_spec == "strs":
            return self.input_reader.read_strs()
        elif type_spec == "floats":
            return self.input_reader.read_floats()
        elif type_spec == "chars":
            return self.input_reader.read_chars()
        elif type_spec == "binary":
            return self.input_reader.read_binary()

        # Structured types
        elif type_spec.startswith("Words[") and type_spec.endswith("]"):
            return self._parse_words_type(type_spec)
        elif type_spec.startswith("Lines[") and type_spec.endswith("]"):
            return self._parse_lines_type(type_spec)

        # Fallback
        return self.input_reader.read_str()

    def _parse_words_type(self, type_spec: str) -> Words:
        """Parse Words[type] or Words[type:count]"""
        inner = type_spec[6:-1]

        if ":" in inner:
            # Words[int:3] - exactly 3 items
            item_type, count_str = inner.split(":", 1)
            expected_count = int(count_str.strip())

            if item_type.strip() == "int":
                values = self.input_reader.read_ints()[:expected_count]
            elif item_type.strip() == "float":
                values = self.input_reader.read_floats()[:expected_count]
            else:
                values = self.input_reader.read_strs()[:expected_count]

            assert (
                len(values) == expected_count
            ), f"expected {expected_count} items, got {len(values)}"
        else:
            # Words[int] - variable number
            if inner.strip() == "int":
                values = self.input_reader.read_ints()
            elif inner.strip() == "float":
                values = self.input_reader.read_floats()
            else:
                values = self.input_reader.read_strs()

        return Words(values)

    def _parse_lines_type(self, type_spec: str) -> Lines:
        """Parse Lines[type] - read count then that many lines"""
        inner = type_spec[6:-1]
        count = self.input_reader.read_int()
        items = []
        for _ in range(count):
            items.append(self._parse_type_spec(inner.strip()))
        return Lines(items)


# @code end
