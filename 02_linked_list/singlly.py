class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class singlly:
    length = 0
    tail = None
    head = None
    string = ''

    def __init__(self, head=None):

        if head != None:
            self.head = Node(head)
        
        if self.head != None:
            self.tail = self.head
            self.string += '→ ' + str(head)
            self.length += 1
            return


    def __str__(self):
        return self.string

    
    def __len__(self):
        return self.length


    def push(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            self.string += '→ ' + str(data)
            self.length += 1
            return

        self.tail.next = Node(data)
        self.tail = self.tail.next

        self.string += ' → ' + str(data)
        self.length += 1

        return


    def pop(self):
        if self.head == None:
            return

        itr = self.head

        while itr:
            if itr.next.next == None:
                self.tail = itr
                break
            itr = itr.next

        data = itr.next.data
        itr.next = None

        self.string = self.string[0 : -len(str(data)) - 3]
        self.length -= 1

        return data

    
    def unshift(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
            self.string += '→ ' + str(data)
            self.length += 1
            return

        newHead = Node(data, self.head)
        self.head = newHead

        self.string = f'→ {str(data)} {self.string}'
        self.length += 1

        return

    def shift(self):
        if self.head == None:
            return
        
        data = self.head.data
        newHead = self.head.next
        self.head = newHead

        self.string = self.string[len(str(data)) + 3 : ]
        self.length -= 1

        return