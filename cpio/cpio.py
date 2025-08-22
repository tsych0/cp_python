"""
USAGE EXAMPLES:
- Single values: @sol('str'), @sol('int'), @sol('n m')
- Collections: @sol('strs'), @sol('ints')
- Exact counts: @sol('Words[str:3]'), @sol('Words[int:2]')
- Fixed repetitions: @sol('4*Words[int]'), @sol('3*str')
- Variable-driven: @sol('n; n*Words[int]'), @sol('n m; n*int; m*str')
- Complex: @sol('n m q; n*Words[int]; m*str; q*Words[int:2]')
"""

from cpio.input import (
    _next_int,
    _execute_pattern,
    _compile_pattern,
    _init_input_lines,
    _advance_line,
)

# @code begin
import sys
from typing import Callable
from functools import wraps


def sol(pattern: str):
    """Main decorator for competitive programming problems"""
    # Compile pattern at decoration time
    compiled_ops = _compile_pattern(pattern)

    def decorator(func: Callable):
        @wraps(func)
        def wrapper():
            global _INPUT_LINES, _LINE_INDEX, _CURRENT_LINE_TOKENS, _TOKEN_INDEX
            _init_input_lines()
            _LINE_INDEX = 0
            _CURRENT_LINE_TOKENS = []
            _TOKEN_INDEX = 0
            _advance_line()  # Load first line

            results = _execute_pattern(compiled_ops)
            result = func(*results)
            print(result)

        return wrapper

    return decorator


def sol_n(pattern: str):
    """Optimized decorator for multiple test cases"""
    # Compile pattern at decoration time
    compiled_ops = _compile_pattern(pattern)

    def decorator(func: Callable):
        @wraps(func)
        def wrapper():
            global _INPUT_LINES, _LINE_INDEX, _CURRENT_LINE_TOKENS, _TOKEN_INDEX
            _init_input_lines()
            _LINE_INDEX = 0
            _CURRENT_LINE_TOKENS = []
            _TOKEN_INDEX = 0
            _advance_line()  # Load first line

            t = _next_int()
            output_parts = []

            for _ in range(t):
                results = _execute_pattern(compiled_ops)
                result = func(*results)
                output_parts.append(str(result))

            # Single write operation
            print("\n".join(output_parts))

        return wrapper

    return decorator


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
