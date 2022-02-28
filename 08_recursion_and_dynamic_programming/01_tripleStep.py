import math
import time


def tripleStep(steps: int):
    memo = [0]+[-1]*steps
    memo[1] = 1
    memo[2] = 2
    memo[3] = 3

    return countWays(steps, memo)


#         _
#       _|3
#     _|2
#  ↓_|1 ___
#  0

# top-down
def countWays(steps: int, memo: list[int]):
    if steps <= 0: return 0
    if memo[steps] != -1: return memo[steps]
    
    memo[steps] = countWays(steps-1, memo) + countWays(steps-2, memo) + countWays(steps-3, memo)
    return memo[steps]


# bottom-up
def tripleSteps(steps: int):
    if steps == 0: return 0
    if steps == 1: return 1
    if steps == 2: return 2
    if steps == 3: return 3

    memo = [0, 1, 2, 3] + [-1]*(steps-3)
    for i in range(4, steps+1):
        memo[i] = memo[i-3] + memo[i-2] + memo[i-1]

    return memo[steps]


if __name__ == '__main__':
    START_TIME = time.time()

    # input
    print(tripleStep(4))
    print(tripleSteps(4))

    print(tripleStep(37))
    print(tripleSteps(37))

    print(tripleStep(100))
    print(tripleSteps(100))

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)