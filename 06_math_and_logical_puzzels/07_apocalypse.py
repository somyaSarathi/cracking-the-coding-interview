import math
import random


def ratio(x: int, y: int) -> str:
    return f'{x//math.gcd(x, y)}:{y//math.gcd(x, y)}'


def nFamilies(n: int) -> str:
    boy = girl = 0
    for _ in range(n):
        boy += oneFamily()
        girl += 1
    
    return ratio(girl, boy)


def oneFamily() -> int:
    boy: int = 0
    while random.choice(['b', 'g']) != 'g':
        boy += 1

    return boy


if __name__ == '__main__':
    n = int(input())
    print(nFamilies(n))
    exit(0)
