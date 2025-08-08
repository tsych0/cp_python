"""
USAGE EXAMPLES:
- Single values: @sol('str'), @sol('int'), @sol('n m')
- Collections: @sol('strs'), @sol('ints')
- Exact counts: @sol('Words[str:3]'), @sol('Words[int:2]')
- Fixed repetitions: @sol('4*Words[int]'), @sol('3*str')
- Variable-driven: @sol('n; n*Words[int]'), @sol('n m; n*int; m*str')
- Complex: @sol('n m q; n*Words[int]; m*str; q*Words[int:2]')
"""

from cpio.patternparser import *

# @code begin
from typing import Callable
from functools import wraps
from io import StringIO


def sol(pattern: str):
    """Main decorator for competitive programming problems"""

    def decorator(func: Callable):
        @wraps(func)
        def wrapper():
            input_reader = CPInput()
            parser = PatternParser(input_reader)
            results = parser.parse_pattern(pattern)
            result = func(*results)
            print(result)

        return wrapper

    return decorator


def sol_n(pattern: str):
    """Decorator for multiple test cases"""

    def decorator(func: Callable):
        @wraps(func)
        def wrapper():
            input_reader = CPInput()
            t = input_reader.read_int()
            output_lines = []
            for _ in range(t):
                parser = PatternParser(input_reader)
                results = parser.parse_pattern(pattern)
                result = func(*results)
                output_lines.append(f"{result}\n")
            sys.stdout.write("".join(output_lines))

        return wrapper

    return decorator


def test_with_input(input_str: str, pattern: str):
    """Helper for testing patterns"""

    def decorator(func):
        @wraps(func)
        def wrapper():
            input_reader = CPInput(StringIO(input_str))
            parser = PatternParser(input_reader)
            results = parser.parse_pattern(pattern)
            result = func(*results)
            print(f"Result: {result}")
            return result

        return wrapper

    return decorator


def lines_of(items: list) -> Lines:
    """Create Lines from list"""
    return Lines(items)


def words_of(items: list) -> Words:
    """Create Words from list"""
    return Words(items)


def grid_of(rows: list[list]) -> Lines[Words]:
    """Create grid from list of lists"""
    return lines_of([words_of(row) for row in rows])


def bool_yes_no(value: bool) -> Bool:
    """Create Yes/No boolean"""
    return Bool(value)


def bool_yes_no_caps(value: bool) -> BOOL:
    """Create YES/NO boolean"""
    return BOOL(value)


def debug(*args, **kwargs):
    """Output to stderr"""
    print(*args, file=sys.stderr, **kwargs)


# @code end

# Example usage
if __name__ == "__main__":
    # Single string
    @sol("str")
    def example1(s):
        return f"Hello {s}!"

    # Three exact strings
    @sol("Words[str:3]")
    def example2(words):
        return f"Got: {words.items}"

    # Four lines of integers
    @sol("4*Words[int]")
    def example3(lines):
        return sum(sum(line.items) for line in lines)

    # Variable + fixed pattern
    @sol("n; n*Words[int:4]")
    def example4(n, lines):
        return n + sum(sum(line.items) for line in lines)
