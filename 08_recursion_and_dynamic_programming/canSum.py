import math
import time

from numpy import number


# number can be used as many times
def canSum(target: int, nums: int, memo=None):
    if memo is None:
        memo = {}
        
    if target in memo: return memo[target]
    if target == 0: return True
    if target < 0: return False

    for num in nums:
        if canSum(target-num, nums, memo):
            memo[target] = True
            return True
    
    memo[target] = False
    return False


if __name__ == '__main__':
    START_TIME = time.time()

    # input
    print(canSum(7, [2, 3]))
    print(canSum(7, [5, 3, 4, 7]))
    print(canSum(7, [2, 4]))
    print(canSum(8, [2, 3, 5]))
    print(canSum(300, [7, 14]))

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)