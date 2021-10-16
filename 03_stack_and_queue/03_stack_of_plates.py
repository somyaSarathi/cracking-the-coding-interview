from collections import deque

class SetOfSet:
    def __init__(self, threshold: int) -> None:
        self.items: list = [deque()]
        self.threshold: int = threshold
        self.idx = 0
        return


    def __str__(self) -> str:
        return self.items.__str__()


    def push(self, val) -> None:
        if self.threshold == len(self.items[self.idx]):
            self.idx += 1
            self.items.append(deque())
        
        self.items[self.idx].append(val)
        return


    def pop(self):
        if self.items[self.idx]:
            val = self.items[self.idx].pop()
            return val

        if self.idx == 0:
            raise IndexError('stack is empty')

        del self.items[self.idx]
        self.idx -= 1
        val = self.items[self.idx].pop()
        return val
