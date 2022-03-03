import math
import time
from typing import Literal


#  1 1 1 1
#  0 1 0 1
#  1 0 0 1
#  1 0 1 1
def isPath(grid, r, c):
    try:
        return bool(grid[r][c])
    except IndexError:
        return False


def findPath(grid: list[list[int]], r: int=0, c: int=0) -> (list[list[int]] | Literal[-1]):
    queue = [ [0, 0] ]
    visited = set()
    path = { '0 0': [[0, 0]] }

    while queue:
        n, m = queue[0]
        del queue[0]
        visited.add(f'{n} {m}')

        if n == r-1 and m == c-1:
            return path[f'{n} {m}']+[[n, m]]

        # right
        if isPath(grid, n, m+1):
            if f'{n} {m+1}' not in visited:
                queue.append([n, m+1])
                path[f'{n} {m+1}'] = path[f'{n} {m}']+[[n, m+1]]

        # down
        if isPath(grid, n+1, m):
            if f'{n+1} {m}' not in visited:
                queue.append([n+1, m])
                path[f'{n+1} {m}'] = path[f'{n} {m}']+[[n+1, m]]
    
    return -1


if __name__ == '__main__':
    START_TIME = time.time()

    # input
    n, m = map(int, input().strip().split())

    grid = []
    for i in range(n):
        grid.append([ int(x) for x in input().strip().split() ])

    if not grid[0][0] == 0:
        print(findPath(grid, n, m))
    else: print(-1)

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)
