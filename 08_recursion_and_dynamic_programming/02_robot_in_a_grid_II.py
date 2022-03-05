import math
import time


def isPath(grid: list[list[int]], r: int, c: int) -> bool:
    try: return not grid[r][c]
    except IndexError: return False


def uniquePaths(grid: list[list[int]], r: int=0, c: int=0, memo: dict={}) -> int:
    if memo is None: memo = dict()
    if (r, c) in memo: return memo(r, c)

    # base case
    if len(grid) == 0: return 0
    if grid[r][c] == 1: return 0
    if r == len(grid)-1 and c == len(grid[0])-1: return 1

    memo[(r, c)] = 0
    if r+1 < len(grid) and isPath(grid, r+1, c):
        memo[(r, c)] += uniquePaths(grid, r+1, c, memo)
    if c+1 < len(grid[0]) and isPath(grid, r, c+1):
        memo[(r, c)] += uniquePaths(grid, r, c+1, memo)

    return memo[(r, c)]


if __name__ == '__main__':
    START_TIME = time.time()

    # input
    m, n = [ int(x) for x in input().strip().split() ]
    grid = []

    for i in range(m):
        grid.append( [ int(x) for x in input().strip().split() ] )

    print(grid)
    print(uniquePaths(grid))

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)