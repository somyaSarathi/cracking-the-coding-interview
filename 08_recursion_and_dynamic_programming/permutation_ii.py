import math
import time


class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        res = []
        perm = []
        count = { n:0 for n in nums }
        for n in nums:
            count[n] += 1
            
        def dfs():
            # base case
            if len(perm) == len(nums):
                res.append(perm.copy())
                return
            
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    
                    dfs()
                    
                    count[n] += 1
                    perm.pop()
                    
        dfs()
        return res


if __name__ == '__main__':
    # input
    nums = [ int(x) for x in input().strip().split() ]

    START_TIME = time.time()
    result = Solution()
    print(result.permuteUnique(nums))

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)