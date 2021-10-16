from stack import *

class minStack(Stack):
    def __init__(self):
        super().__init__()
        self.minVal = Stack()

    def push(self, val):
        super().push(val)
        if not self.minVal or val <= self.minimum():
            self.minVal.push(val)

    def pop(self):
        val = super().pop()
        if val == self.minimum():
            self.minVal.pop()

        return val

    def minimum(self):
        return self.minVal.peek()