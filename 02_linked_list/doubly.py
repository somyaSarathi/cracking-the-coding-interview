class Node:
    def __init__(self, data, prv=None, nxt=None):
        if data == None:
            raise TypeError('expected a none None object')

        self.data = data
        self.prv = prv
        self.nxt = nxt


    def __str__(self) -> str:
        return str(self.data)


    def __repr__(self) -> str:
        return f"'{self.__str__()}'"


    def __eq__(self, o: object) -> bool:
        if self.data == o:
            return True

        if type(o) == type(self) and self.data == o.data:
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


class Doubly:
    head = None
    tail = None
    length = 0

    def __init__(self, *args) -> None:
        for arg in args:
            if arg == None:
                raise TypeError('expected a none None object')

            self.push(arg)

    
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


    def __iter__(self):
        itr = self.head

        while itr:
            yield itr
            itr = itr.nxt


    def __eq__(self, o: object) -> bool:
        if type(self) != type(o):
            raise TypeError('expected a doubly object')

        if len(self) != len(o):
            return False

        itr1 = self.head
        itr2 = o.head

        while itr1:
            if itr1.data != itr2.data:
                return False

            itr1 = itr1.nxt
            itr2 = itr2.nxt

        return True


    def __gt__(self, o: object) -> bool:
        if type(self) != type(o):
            raise TypeError('expected a doubly object')

        if len(self) > len(o):
            return True

        return False


    def __ge__(self, o: object) -> bool:
        if type(self) != type(o):
            raise TypeError('expected a doubly object')

        if len(self) > len(o) or self == o:
            return True

        return False


    def __lt__(self, o: object) -> bool:
        if type(self) != type(o):
            raise TypeError('expected a doubly object')

        if self.length < o.length:
            return True

        return False


    def __le__(self, o: object) -> bool:
        if type(self) != type(o):
            raise TypeError('expected a doubly object')

        if self.length < o.length or self == o:
            return True

        return False


    def push(self, value) -> None:
        """
            Append object to the end of the linked list.\n
            Raises TypeError if value is None.
        """

        if value == None:
            raise TypeError('expected a none None object')

        if type(value) == list or type(value) == tuple or type(value) == map:
            for x in value:
                self.push(x)

            return

        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
            self.length += 1

            return

        node = Node(value)
        self.tail.nxt = node

        node.prv = self.tail
        self.tail = node
        self.length += 1

        return


    def pop(self):
        """
            Remove and return item at the end.\n
            Raises IndexError if liked list is empty.
        """
        if self.head == None:
            raise IndexError('linked list is empty')

        data = self.tail.data
        self.tail = self.tail.prv
        self.tail.nxt = None
        self.length -= 1

        return data


    def pushL(self, value) -> None:
        """
            Inserts node to the left of linked list.\n
            Raises TypeError if value is None.
        """
        if value == None:
            raise TypeError('expected a none None object')

        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
            self.length += 1

        node = Node(value, nxt=self.head)
        self.head.prv = node
        self.head = node
        self.length += 1

        return


    def popL(self) -> None:
        """
            Removes the first element.
        """
        if self.head == None:
            raise IndexError('linked list is empty')

        data = self.head.data
        self.head = self.head.nxt
        self.head.prv = None
        self.length -= 1

        return data


    def insert(self, idx: int, value):
        """
            Insert object before index.\n
            Raises TypeError if value is None
            Raises IndexError if index out of range.
        """
        if value == None:
            raise TypeError('expected a none None object')

        if idx > len(self):
            raise IndexError('linked list out of range')

        if idx == len(self):
            self.push(value)

        if idx == 0:
            self.pushL(value)

        if idx <= len(self)//2:
            itr = self.head
            while idx > 1:
                itr = itr.nxt
                idx -= 1

            node = Node(value, itr, itr.nxt)
            itr.nxt.prv = node
            itr.nxt = node
            self.length += 1

            return

        idx = len(self) - idx
        itr = self.tail
        while idx:
            itr = itr.prv
            idx -= 1

        node = Node(value, itr, itr.nxt)
        itr.nxt.prv = node
        itr.nxt = node
        self.length += 1

        return


    def remove(self, value):
        """
            Remove first occurrence of value.\n
            Raises ValueError if the value is not present.
        """
        if value == None:
            raise TypeError('Singly.remove(x): x not in list')

        for x in self:
            if x == value:
                data = x.data

                x.prv.nxt = x.nxt
                x.nxt.prv = x.prv

                x = None
                self.length -= 1

                return data

        raise ValueError('Singly.remove(x): x not in list')


    def removeFrom(self, idx: int):
        """
            Remove from the index.\n
            Raises IndexError if imdex out of range.
        """
        if idx >= len(self):
            raise IndexError('index out of range')

        if idx == 0:
            self.popL()

        if idx == len(self)-1:
            self.pop()

        if idx <= len(self)//2:
            itr = self.head
            for i in range(idx):
                itr = itr.nxt

            data = itr.data
            itr.nxt.prv = itr.prv
            itr.prv.nxt = itr.nxt

            itr = None
            self.length -= 1

            return data

        idx = len(self)-idx-1
        itr = self.tail
        while idx:
            itr = itr.prv
            idx -= 1

        data = itr.data
        itr.nxt.prv = itr.prv
        itr.prv.nxt = itr.nxt

        itr = None
        self.length -= 1
