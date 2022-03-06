import math
import time


# APPROACH:
# - think of an binary tree.
# - start from the null set(root), and counter at 0 (0-n, where n is the length of arr)
# - create two branches by anding the counter index element(left) and wiouth adding the counter index element(right child).
# - repeat the same for child node.
# - when counter reach the end of the array append the final subset into a list.


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        self.allSubset = []
        self.arr = nums
        self.helper([])
        return self.allSubset
        
    def helper(self, sub: list[int], counter: int=0) -> None:
        if counter < len(self.arr):
            self.helper(sub, counter+1)
            self.helper(sub+[self.arr[counter]], counter+1)
            return None
        else:
            self.allSubset.append(sub)



if __name__ == '__main__':
    START_TIME = time.time()

    # input
    n = int(input().strip())
    arr = [ int(x) for x in input().strip().split() ]

    result = Solution()
    print(result.subsets(arr))

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)