class Node:
    def __init__(self, data, next=None) -> None:
        self.data = data
        self.next = next
        return

    def __del__(self) -> object:
        return self.data


class singly:
    head = None
    tail = None
    length = 0
    llist = []

    def __init__(self) -> None:
        return


    def __del__(self) -> None:
        return


    def __len__(self) -> int:
        return self.length


    def __str__(self) -> str:
        return  '-> ' + ' -> '.join(map(str, self.llist))


    def __eq__(self, o: object) -> bool:
        if self.llist == o.llist:
            return True

        return False


    def __gt__(self, o: object) -> bool:
        if len(self) > len(o):
            return True

        return False


    def __lt__(self, o: object) -> bool:
        if len(self) < len(o):
            return True

        return False

    
    def __ge__(self, o: object) -> bool:
        if len(self) >= len(o):
            return True

        return False


    def __le__(self, o: object) -> bool:
        if len(self) <= len(o):
            return True

        return False


    def push(self, data: object) -> None:
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            self.llist.append(data)
            self.length += 1
            return

        node = Node(data)
        self.tail.next = node
        self.tail = self.tail.next
        self.llist.append(data)
        self.length += 1
        return


    def pop(self) -> object:
        if self.head == None:
            return

        itr = self.head
        toDelete = self.tail
        while itr.next.next != None:
            itr = itr.next

        itr.next = None
        self.tail = itr
        data = self.llist.pop()
        self.length -= 1
        del toDelete
        return data