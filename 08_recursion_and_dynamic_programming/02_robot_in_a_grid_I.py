import math
import time


def uniquePaths(m: int, n: int, memo: dict=None):
    if memo is None: memo = {}
    if (m, n) in memo: return memo[(m, n)]

    # base case
    if n == 0 or m == 0: return 0
    if n == 1 or m == 1: return 1

    memo[(m, n)] = 0
    memo[(m, n)] += uniquePaths(m-1, n, memo)
    memo[(m, n)] += uniquePaths(m, n-1, memo)

    return memo[(m, n)]


if __name__ == '__main__':
    START_TIME = time.time()

    # input
    m, n = [ int(x) for x in input().strip().split() ]
    print(uniquePaths(m, n))

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)