import math
import time


def permuteUnique(string: str) -> list[str]:
    if len(string) <= 1: return [ string ]

    per = set()
    permutations = permuteUnique(string[:-1])
    for permutation in permutations:
        for  i in range(len(permutation)+1):
            per.add(permutation[:i]+string[-1]+permutation[i:])

    return list(per)


if __name__ == '__main__':
    # input
    string = input().strip()
    
    START_TIME = time.time()
    print(permuteUnique(string))

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)