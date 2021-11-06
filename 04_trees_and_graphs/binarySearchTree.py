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
        """returs str(self)"""
        return str(self.data)


    def __repr__(self) -> str:
        """returs repr(self)"""
        return f"'{self.__str__()}'"


    def __del__(self) -> None:
        """deletes the nodes"""
        return


    def __eq__(self, o: object) -> bool:
        """returns Self == value"""
        if type(self) is type(o):
            return (self.data == o.data)

        return (self.data == o)


    def __gt__(self, o: object) -> bool:
        """returns Self > value"""
        if type(self) is type(o):
            return (self.data > o.data)

        return (self.data > o)


    def __lt__(self, o: object) -> bool:
        """returns Self < value"""
        if type(self) is type(o):
            return (self.data < o.data)

        return (self.data < o)


    def __ge__(self, o: object) -> bool:
        """returns Self >= value"""
        if type(self) is type(o):
            return (self.data >= o.data)

        return (self.data >= o)


    def __le__(self, o: object) -> bool:
        """returns Self <= value"""
        if type(self) is type(o):
            return (self.data <= o.data)

        return (self.data <= o)


    def __add__(self, o: object) -> object:
        if type(self) is type(o):
            return (self.data + o.data)

        return (self.data + o)


    def __iadd__(self, o: object) -> object:
        if type(self) is type(o):
            self.data += o.data
            return self

        self.data += o
        return self


    def __sub__(self, o: object) -> object:
        if type(self) is type(o):
            return (self.data - o.data)

        return (self.data - o)


    def __isub__(self, o: object) -> object:
        if type(self) is type(o):
            self.data -= o.data
            return self

        self.data -= o
        return self


    def __mul__(self, o: object) -> object:
        if type(self) is type(o):
            return (self.data * o.data)

        return (self.data * o)


    def __imul__(self, o: object) -> object:
        if type(self) is type(o):
            self.data *= o.data
            return self

        self.data *= o
        return self


    def __truediv__(self, o: object) -> object:
        if type(self) is type(o):
            return (self.data / o.data)

        return (self.data / o)


    def __itruediv__(self, o: object) -> object:
        if type(self) is type(o):
            self.data /= o.data
            return self

        self.data /= o
        return self


    def __floordiv__(self, o: object) -> object:
        if type(self) is type(o):
            return (self.data // o.data)

        return (self.data // o)


    def __ifloordiv__(self, o: object) -> object:
        if type(self) is type(o):
            self.data //= o.data
            return self

        self.data //= o
        return self


class binarySearchTree:
    def __init__(self, *args) -> None:
        """
            initializes the tree
        """
        self.root = None
        self.nodes: int = 0

        if args:
            for arg in args:
                self.append(arg)
        
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


    def displayInOrder(self, node=None) -> None:
        """
            displays the tree in order
        """
        if node is None:
            node = self.root

        if node.left:
            self.displayInOrder(node.left)

        print(node.data, end=' ')

        if node.right:
            self.displayInOrder(node.right)

        else:
            print('')

        return


    def displayPreOrder(self, node=None) -> None:
        """
            displays the tree in pre order
        """
        if node is None:
            node = self.root

        print(node.data, end=' ')

        if node.left:
            self.displayPreOrder(node.left)

        if node.right:
            self.displayPreOrder(node.right)

        else:
            print('')

        return


    def displayPostOrder(self, node=None) -> None:
        """
            displays the tree in post order
        """
        if node is None:
            node = self.root

        if node.left:
            self.displayPostOrder(node.left)

        if node.right:
            self.displayPostOrder(node.right)

        print(node.data, end=' ')

        return
