class Node:
    def __init__(self, data=None, prv=None, nxt=None):
        self.data = data
        self.prv = prv
        self.nxt = nxt


class doublly:
    head = None
    tail = None
    string = ''
    sequence = []

    def __init__(self, head=None) -> None:

        if head != None:
            self.head = Node(head)

        if self.head != None:
            self.tail = self.head
            self.string += '→ ' + str(head)
            self.sequence.append(head)
            self.length += 1

        return


    def __str__(self):
        return self.string


    def __len__(self):
        return len(self.sequence)


    def __add__(self, ll:object):
        pass


    def __iadd__(self, ll: object):
        
        newlist = self

        ll.head.prv = newlist.tail
        newlist.tail.nxt = ll.head
        newlist.tail = ll.tail

        newlist.length += ll.length
        newlist.string += ' ' + ll.string

        return newlist


    def __eq__(self, ll: object) -> bool:

        if self.string == ll.string:
            return True

        return False


    def __ne__(self, ll: object) -> bool:

        if self.string == ll.string:
            return False

        return True


    def __lt__(self, ll:object) -> bool:

        if len(self.sequence) < len(ll.sequence):
            return True

        return False


    def __gt__(self, ll:object) -> bool:

        if len(self.sequence) > len(ll.sequence):
            return True

        return False

    
    def __gt__(self, ll:object) -> bool:

        if len(self.sequence) >= len(ll.sequence):
            return True

        return False


    def __le__(self, ll:object) -> bool:

        if len(self.sequence) <= len(ll.sequence):
            return True

        return False


    def push(self, data) -> None:
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            self.string += '→ ' + str(data)
            self.sequence.append(data)
            return

        self.tail.next = Node(data, self.tail)
        self.tail = self.tail.next

        self.string += ' → ' + str(data)
        self.sequence.append(data)

        return


    def pop(self) -> None:
        if self.head == None:
            return

        data = self.tail.data
        self.tail = self.tail.prv
        self.tail.next = None

        self.string = self.string[0 : -len(str(data)) - 3]
        self.sequence.pop()

        return data


    def shift(self) -> None:
        if self.head == None:
            return

        data = self.head.data
        self.head = self.head.nxt
        self.head.prv = None

        self.string = self.string[len(str(data)) + 3 : ]
        self.sequence = self.sequence[1:]

        return data


    def unshift(self, data) -> None:
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            self.string += '→ ' + str(data)
            return

        newHead = Node(data, None, self.head)
        self.head = newHead

        self.string = f'→ {str(data)} {self.string}'
        self.sequence.insert(0, data)

        return
