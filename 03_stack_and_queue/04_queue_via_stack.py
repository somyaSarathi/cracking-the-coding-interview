class MyQueue:
    def __init__(self):
        self.s1: list = []
        self.s2: list = []
        pass

    def __len__(self):
        return len(self.s1)

    def __str__(self):
        return self.s1.__str__()

    def push(self, val):
        self.s2 = self.s1
        self.s1 = []
        self.s1.append(val)
        self.s1 += self.s2
        self.s2 = []
        pass

    def pop(self):
        self.s1.pop()
        pass