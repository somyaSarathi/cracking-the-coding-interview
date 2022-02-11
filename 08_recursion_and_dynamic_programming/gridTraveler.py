import math
import time


# move only down or right
def gridTraveler_matrix(m: int, n: int, memo: list[int]=None) -> int:
    # base case
    if n == 1 or m == 1: return 1
    if n == 0 or m == 0: return 0

    if memo is None:
        memo = [ [None]*(n) for i in range(m) ]

    if memo[m-1][n-1] is None:
        memo[m-1][n-1] = gridTraveler_matrix(m-1, n, memo) + gridTraveler_matrix(m, n-1, memo)

    return memo[m-1][n-1]


# dict is more memory efficient
def gridTraveler_dict(m: int, n: int, memo={}) -> int:
    # base case
    if n == 1 or m == 1: return 1
    if n == 0 or m == 0: return 0

    try:
        return memo[m, n]
    except:
        memo[m, n] = gridTraveler_dict(m-1, n, memo) + gridTraveler_dict(m, n-1, memo)

    return memo[m, n]


if __name__ == '__main__':
    START_TIME = time.time()

    # input
    # m, n = [ int(x) for x in input() ]
    print(gridTraveler_matrix(18, 18))
    print(gridTraveler_dict(18, 18))

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)