class Stack:
    def __init__(self) -> None:
        self.items = []

    def __len__(self) -> int:
        return len(self.items)

    def __bool__(self) -> bool:
        return bool(self.items)

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        if self.items:
            return self.items[-1]

        return None
