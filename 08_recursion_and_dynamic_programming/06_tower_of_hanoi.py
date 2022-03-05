import math
import time


def towerOfHanoi(n: int, source: str, helper: str, destination: str) -> None:
    if n == 0: return
    towerOfHanoi(n-1, source, destination, helper)
    print(f'Moving disk {n} from {source} to {destination}')
    towerOfHanoi(n-1, helper, destination, source)


if __name__ == '__main__':
    START_TIME = time.time()

    # input
    n = int(input().strip())
    towerOfHanoi(n, 'A', 'B', 'C')

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)