from stack import *

class sortedStack(Stack):
    def __init__(self) -> None:
        super().__init__()
        self.temp = Stack()

    def push(self, item) -> None:
        if self.is_empty() or item < self.peek():
            super().push(item)
            return

        while self.peek() is not None and item > self.peek():
            self.temp.push(self.pop())

        super().push(item)

        while self.temp:
            super().push(self.temp.pop())

        return