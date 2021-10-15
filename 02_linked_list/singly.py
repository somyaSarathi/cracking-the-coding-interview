class Node:
    def __init__(self, data=None, nxt=None):
        self.data = data
        self.nxt = nxt


    def __str__(self) -> str:
        return str(self.data)


    def __repr__(self) -> str:
        return f"'{self.__str__()}'"


    def __eq__(self, o: object) -> bool:
        if self.data == o or self.data == o.data:
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

    def __init__(self, value=None) -> None:
        self.llist = []

        if value == None:
            return

        if type(value) == list or type(value) == tuple or type(value) == map:
            for x in value:
                self.push(x)

            return

        self.head = Node(value)
        self.tail = self.head
        self.llist.append(value)
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


    def push(self, value) -> None:
        """
            Append object to the end of the list.\n
            Raises IndexError if value is None.
        """
        if value == None:
            raise TypeError('expected a non None object')
            
        if type(value) == list or type(value) == tuple or type(value) == map:
            for x in value:
                self.push(x)

            return

        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
            self.llist.append(value)
            self.length += 1
            return

        node = Node(value)
        self.tail.nxt = node
        self.tail = self.tail.nxt
        self.llist.append(value)
        self.length += 1
        return


    def pop(self):
        """
            Remove and return item at the end.\n
            Raises IndexError if liked list is empty.
        """
        if self.head == None:
            raise IndexError('linked list is empty')

        itr = self.head
        while itr.nxt.nxt != None:
            itr = itr.nxt

        data = itr.data
        self.tail = itr
        self.tail.nxt = None

        self.llist.pop()
        self.length -= 1

        return data


    def unshift(self, value) -> None:
        """
            Inserts node at the begining.\n
            Raises TypeError if value is None.
        """
        if value == None:
            raise TypeError('expected a non None object')

        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
            self.length += 1
            self.llist.append(value)

        node = Node(value, self.head)
        self.head = node
        self.llist.insert(0, value)
        self.length += 1


    def shift(self):
        """
            Removes the first element.
        """
        if self.head == None:
            raise IndexError('linked list is empty')

        data = self.head.data
        self.head = self.head.nxt
        self.llist = self.llist[1:]
        self.length -= 1

        return data


    def insert(self, index: int, value):
        """
            Insert object before index.\n
            Raises IndexError if index out of range.
        """
        if value == None or index == None:
            raise TypeError('expected a none None object')

        if index > self.length:
            raise IndexError('linked list index out of range')

        if index == self.length:
            self.push(value)
        
        itr = self.head
        for i in range(index-1):
            itr = itr.nxt

        shiftNode = itr.nxt
        node = Node(value, shiftNode)
        itr.nxt = node

        self.llist.insert(index, value)
        self.length += 1

        return self


    def removeFrom(self, index: int):
        """
            Remove from the index.\n
            Raises IndexError if index out of range.
        """
        if index >= self.length:
            raise IndexError('linked list index out of range')
        
        itr = self.head
        for i in range(index-1):
            itr = itr.nxt

        data = itr.nxt.data
        itr.nxt = itr.nxt.nxt
        del self.llist[index]
        self.length -= 1

        return data


    def remove(self, value):
        """
            Remove first occurrence of value.\n
            Raises ValueError if the value is not present.
        """
        itr = self.head

        while itr != None:
            if itr.nxt == value:
                itr.nxt = itr.nxt.nxt
                self.length -= 1
                self.llist.remove(value)
                return value

            itr = itr.nxt
        
        raise ValueError('Singly.remove(x): x not in list')