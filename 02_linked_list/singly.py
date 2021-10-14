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

        if type(data) == list or type(data) == tuple or type(data) == map:
            for x in data:
                self.push(x)

            return

        self.head = Node(data)
        self.tail = self.head
        self.llist.append(data)
        self.length += 1
        return


    def __str__(self) -> str:
        string = '→ '
        itr = self.head

        while itr != None:
            string += str(itr.data) + ' → '
            itr = itr.nxt

        return string


    def __repr__(self) -> str:
        return f"'{self.__str__()}'"


    def __len__(self) -> int:
        return self.length

    
    def __eq__(self, o: object) -> bool:
        if self.llist == o.llist:
            return True

        return False


    def __gt__(self, o: object) -> bool:
        if self.length > o.length:
            return True

        return False

    
    def __ge__(self, o: object) -> bool:
        if self.length >= o.length:
            return True

        return False


    def __lt__(self, o: object) -> bool:
        if self.length < o.length:
            return True

        return False


    def __le__(self, o: object) -> bool:
        if self.length <= o.length:
            return True

        return False


    def push(self, data) -> None:
        if data == None:
            raise TypeError('expected a non None object')
            
        if type(data) == list or type(data) == tuple or type(data) == map:
            for x in data:
                self.push(x)

            return

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
        if data == None:
            raise TypeError('expected a non None object')

        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            self.length += 1
            self.llist.append(data)

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


    def insert(self, index: int, data):
        if data == None or index == None:
            raise TypeError('expected a none None object')

        if index >= self.length:
            raise IndexError('linked list index out of range')
        
        itr = self.head
        for i in range(index-1):
            itr = itr.nxt

        shiftNode = itr.nxt
        node = Node(data, shiftNode)
        itr.nxt = node

        self.llist.insert(index, data)
        self.length += 1

        return self


    def removeAT(self, index: int):
        if index >= self.length:
            raise IndexError('linked list index out of range')
        
        itr = self.head
        for i in range(index-1):
            itr = itr.nxt

        data = itr.nxt.data
        itr.nxt = itr.nxt.nxt
        self.length -= 1

        return data


    def remove(self, data):
        itr = self.head

        while itr != None:
            if itr.nxt == data:
                itr.nxt = itr.nxt.nxt
                self.length -= 1
                self.llist.remove(data)
                return data

            itr = itr.nxt
        
        raise ValueError('Singly.remove(x): x not in list')