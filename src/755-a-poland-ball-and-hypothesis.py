# Created by Ayush Biswas at 2025/08/09 16:52
# https://codeforces.com/problemset/problem/755/A
from cpio.cpio import sol

# @code begin


def is_prime(n: int):
    for k in range(2, int(n**0.5) + 1):
        if n % k == 0:
            return False
    return True


@sol("n")
def solution(n: int) -> int:
    return next(i for i in range(1, 10**3) if not is_prime(i * n + 1))


solution()

# @code end
