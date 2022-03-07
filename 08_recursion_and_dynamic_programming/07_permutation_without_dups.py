import math
import time


# top-down
def permute(string: str) -> list[str]:
    # base case
    if len(string) <= 1: return [ string ]

    per = []
    permutations = permute(string[:-1])
    for permutation in permutations:
        for  i in range(len(permutation)+1):
            per.append(permutation[:i]+string[-1]+permutation[i:])

    return per
 

if __name__ == '__main__': 
    START_TIME = time.time()

    # input
    string = input().strip()
    print(permute(string))

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)