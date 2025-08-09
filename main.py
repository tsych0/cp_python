from cpio.cpio import sol_n

# @code begin


@sol_n("n; ints")
def solution(n: int, a: list[int]) -> int:
    return n * sum(a)


solution()

# @code end
