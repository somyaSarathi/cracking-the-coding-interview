import math
import time


def magicalIndex(n: int, arr: list[int]):
    count = 0
    for i in range(n):
        if i == arr[i]: count += 1
    
    return count if count else -1


if __name__ == '__main__':
    START_TIME = time.time()

    # input
    n = int(input().strip())
    arr = [ int(x) for x in input().strip().split() ]

    print(magicalIndex(n, arr))

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)