class Node:
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = nxt


    def __str__(self) -> str:
        return str(self.data)


    def __repr__(self) -> str:
        return f"'{self.__str__()}'"


    def __eq__(self, o: object) -> bool:
        if self.data == o:
            return True

        return False


    def __gt__(self, o: object) -> bool:
        if self.data > o.data:
            return True

        return False

    
    def __ge__(self, o: object) -> bool:
        if self.data >= o.data:
            return True

        return False


    def __lt__(self, o: object) -> bool:
        if self.data < o.data:
            return True

        return False


    def __le__(self, o: object) -> bool:
        if self.data <= o.data:
            return True

        return False


class Singly:
    head = Node()
    tail = None
    length = 0

    def __init__(self, data=None) -> None:
        self.llist = []

        if data == None:
            return

        if type(data) == list or type(data) == tuple:
            for x in data:
                self.push(x)

            return

        self.head = Node(data)
        self.tail = self.head
        self.llist.append(data)
        self.length += 1
        return


    def __str__(self) -> str:
        return '→ ' + ' → '.join(map(str, self.llist))


    def __repr__(self) -> str:
        return f"'{self.__str__()}'"

    
    def __eq__(self, o: object) -> bool:
        if self.llist == o.llist:
            return True

        return False


    def __gt__(self, o: object) -> bool:
        if self.llist > o.llist:
            return True

        return False

    
    def __ge__(self, o: object) -> bool:
        if self.llist >= o.llist:
            return True

        return False


    def __lt__(self, o: object) -> bool:
        if self.llist < o.llist:
            return True

        return False


    def __le__(self, o: object) -> bool:
        if self.llist <= o.llist:
            return True

        return False


    def push(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            self.llist.append(data)
            self.length += 1
            return

        node = Node(data)
        self.tail.nxt = node
        self.tail = self.tail.nxt
        self.llist.append(data)
        self.length += 1
        return


    def pop(self):
        if self.head == None:
            return

        itr = self.head
        while itr.nxt.nxt != None:
            itr = itr.nxt

        data = itr.data
        self.tail = itr
        self.tail.nxt = None

        self.llist.pop()
        self.length -= 1

        return data


    def unshift(self, data) -> None:
        node = Node(data, self.head)
        self.head = node
        self.llist.insert(0, data)
        self.length += 1


    def shift(self):
        if self.head == None:
            return

        data = self.head.data
        self.head = self.head.nxt
        self.llist = self.llist[1:]
        self.length -= 1

        return data
