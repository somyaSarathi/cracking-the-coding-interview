from collections import deque
from typing import Any

class multiStack:
    def __init__(self, total: int) -> None:
        self.arr: list = []

        for i in range(total):
            self.arr.append(deque())

        self.total = total
        self.arr.insert(0, None)
        return


    def push(self, stackNo: int, value) -> None:
        if stackNo > self.total:
            raise IndexError("stack do not exists")

        self.arr[stackNo].append(value)
        return


    def pop(self, stackNo: int):
        if stackNo > self.total:
            raise IndexError("stack do not exists")

        toReturn = self.arr[stackNo].pop()
        return toReturn


    def show(self):
        print(self.arr[1:])


if __name__ == '__main__':
    test = multiStack(4)
    test.push(2, 10)
    test.push(3, 20)
    test.push(4, 100)
    test.push(1, 5)
    test.push(2, 15)

    test.show()