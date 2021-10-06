class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    """
        mutable sequence\n
        if no value given creates an new empty Linked List
    """
    lenght = 0

    def __init__(self, head=None):
        self.head = head
        
        if head is not None:
            self.tail = self.head


    def __str__(self):
        if self.head is None:
            return "Empty"

        itr = self.head

        llstr = ''

        while itr:
            llstr +='→ ' + str(itr.data) + ' '
            itr = itr.next

        return llstr


    def len(self):
        """
            Returns the length of the Linked List
        """
        return self.lenght


    def unShift(self, data):
        """
            1. Initializes a head to an empty Linked List
            2. Appends data at the beginning of the Linked List
        """
        newNode = Node(data, self.head)
        self.head = newNode
        self.lenght += 1


    def shift(self):
        """
            1. Removes the first value in a Linked List
            2. Returns the removed value
        """
        data = self.head.data
        self.head = self.head.next

        return data


    def push(self, data):
        """
            Inserts value to the end of Linked List
        """

        if self.head is None:
            self.head = Node(data)
            return data

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(data)
        self.lenght += 1


    def pop(self):
        """
            1. Removes the last value from the Linked List
            2. Return the removed value
        """
        if self.head == None:
            return

        itr = self.head

        while itr:
            if (itr.next).next == None:
                break
            itr = itr.next

        data = itr.next.data
        itr.next = None
        self.lenght -= 1

        return data


    def append(self, data):
        """
            Appends the list of data at the end of Linked List
        """
        if type(data) is not list:
            return "Expected a list"
        for x in data:
            self.push(x)