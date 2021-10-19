class Node:
    def __init__(self, data, parent=None) -> None:
        if data==None:
            raise TypeError('expected a none None object')

        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        return


    def __str__(self) -> str:
        return str(self.data)


    def __repr__(self) -> str:
        return f"'{self.__str__()}'"


    def __del__(self) -> None:
        return


    def __eq__(self, o: object) -> bool:
        if type(self) is type(o):
            return (self.data == o.data)

        return (self.data == o)


    def __gt__(self, o: object) -> bool:
        if type(self) is type(o):
            return (self.data > o.data)

        return (self.data > o)


    def __lt__(self, o: object) -> bool:
        if type(self) is type(o):
            return (self.data < o.data)

        return (self.data < o)


    def __ge__(self, o: object) -> bool:
        if type(self) is type(o):
            return (self.data >= o.data)

        return (self.data >= o)


    def __le__(self, o: object) -> bool:
        if type(self) is type(o):
            return (self.data <= o.data)

        return (self.data <= o)



class binarySearchTree:
    def __init__(self) -> None:
        self.root = None
        self.nodes: int = 0
        return


    def append(self, arg):
        """
            inserts node to the tree.
        """
        if self.root is None:
            self.root = Node(arg)
            self.nodes += 1
            return

        itr = self.root

        while itr:
            if itr > arg:
                if itr.left is None:
                    itr.left = Node(arg, itr)
                    self.nodes += 1
                    return

                itr = itr.left

            elif itr == arg:
                return

            else:
                if itr.right is None:
                    itr.right = Node(arg, itr)
                    self.nodes += 1
                    return

                itr = itr.right


    def isNode(self, key) -> bool:
        """
            returns true if node exists
        """
        itr = self.root

        while itr:
            if itr == key:
                return True

            if itr > key:
                itr = itr.left

            else:
                itr = itr.right

        return False