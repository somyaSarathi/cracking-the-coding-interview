import math
import time


# APPROACH:
# - think of an binary tree.
# - start from the null set(root), and counter at 0 (0-n, where n is the length of arr)
# - create two branches by anding the counter index element(left) and wiouth adding the counter index element(right child).
# - repeat the same for child node.
# - when counter reach the end of the array append the final subset into a list.


class Solution:
    def __init__(self, n: int, arr: list[int]) -> None:
        self.arr = arr
        self.n = n
        self.allSubset = []

    
    def __str__(self) -> str:
        self.subset()
        return self.allSubset.__str__()


    def subset(self, sub: list[int]=[], counter: int=0) -> None:
        if counter < self.n:
            self.subset(sub+[arr[counter]], counter+1)
            self.subset(sub, counter+1)
            return None
        else:
            self.allSubset.append(sub)



if __name__ == '__main__':
    START_TIME = time.time()

    # input
    n = int(input().strip())
    arr = [ int(x) for x in input().strip().split() ]

    result = Solution(n, arr)
    print(result)

    print(f'program executed in {time.time() - START_TIME} second(s)')
    exit(0)