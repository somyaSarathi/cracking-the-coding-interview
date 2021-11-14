class Node:
    def __init__(self, data, parent=None) -> None:
        if data==None:
            raise TypeError('expected a none None object')

        self.data = data
        self.parent = parent
        self.left = None
        self.right = None
        return

    def __del__(self) -> None:
        """deletes the nodes"""
        return


    # string methods
    def __str__(self) -> str:
        """returs str(self)"""
        return str(self.data)


    def __repr__(self) -> str:
        """returs repr(self)"""
        return f"'{self.__str__()}'"


    # conditions
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


    # arithmetic operation
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


    # contional operators
    def __bool__(self) -> bool:
        return bool(self.data)


    # bitwise operators
    def __and__(self, o: object) -> object:
        if type(self) is type(o):
            return (self.data and o.data)

        return (self.data and o)


    def __or__(self, o: object) -> object:
        if type(self) is type(o):
            return (self.data or o.data)

        return (self.data or o)


    def __xor__(self, o: object) -> object:
        if type(self) is type(o):
            return (self.data ^ o.data)

        return (self.data ^ o)


    def __invert__(self) -> object:
        return ~self.data


    def __lshift__(self, o: object) -> object:
        if type(self) is type(o):
            return (self.data << o.data)

        return (self.data << o)


    def __ilshift__(self, o: object) -> object:
        if type(self) is type(o):
            self.data <<= o.data
            return self

        self.data <<= o
        return self


    def __rshift__(self, o: object) -> object:
        if type(self) is type(o):
            return (self.data >> o.data)

        return (self.data >> o)


    def __irshift__(self, o: object) -> object:
        if type(self) is type(o):
            self.data >>= o.data
            return self

        self.data >>= o
        return self


class binarySearchTree:
    def __init__(self, *args) -> None:
        """
            initializes the tree.
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
            if itr == arg:
                return

            if itr > arg:
                if itr.left is None:
                    itr.left = Node(arg, itr)
                    self.nodes += 1
                    return

                itr = itr.left

            else:
                if itr.right is None:
                    itr.right = Node(arg, itr)
                    self.nodes += 1
                    return

                itr = itr.right


    def isNode(self, key) -> bool:
        """
            returns true if node exists.
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
            displays the tree in order.
        """
        if node is None:
            if self.root is None:
                return
                
            node = self.root

        if node.left:
            self.displayInOrder(node.left)

        print(node.data, end=' ')

        if node.right:
            self.displayInOrder(node.right)

        return


    def displayPreOrder(self, node=None) -> None:
        """
            displays the tree in pre order.
        """
        if node is None:
            if self.root is None:
                return
                
            node = self.root

        print(node.data, end=' ')

        if node.left:
            self.displayPreOrder(node.left)

        if node.right:
            self.displayPreOrder(node.right)

        return


    def displayPostOrder(self, node=None) -> None:
        """
            displays the tree in post order.
        """
        if node is None:
            if self.root is None:
                return

            node = self.root

        if node.left:
            self.displayPostOrder(node.left)

        if node.right:
            self.displayPostOrder(node.right)

        print(node.data, end=' ')

        return


    def remove(self, key, root=None) -> None:
        '''
            removes the node from the tree.
        '''
        if not root:
            root = self.root

        while root:
            if root == key:
                # leaf node
                if (not root.left) and (not root.right):
                    if not root.parent:
                        self.root = None
                        self.nodes = 0
                        return

                    if root.parent.left == root:
                        root.parent.left = None
                    else:
                        root.parent.right = None
                    self.node -= 1
                    del root
                    return

                # one child
                if not root.left:
                    if not root.parent:
                        self.root = root.right
                        self.nodes -= 1
                        return

                    if root.parent.left == root:
                        root.parent.left = root.right
                    else:
                        root.parent.right = root.right
                    self.nodes -= 1
                    del root
                    return

                if not root.right:
                    if not root.parent:
                        self.root = root.left
                        self.nodes -= 1
                        return

                    if root.parent.left == root:
                        root.parent.left = root.left
                    else:
                        root.parent.right = root.left
                    self.nodes -= 1
                    del root
                    return

                # two childs
                self.root = self.min(root.right)
                self.remove(root.data, root.right)

            if root > key:
                root = root.left
            else:
                root = root.right

        return

    
    def min(self, root=None):
        '''
            returns the smallest value in the tree.
        '''
        if not root:
            root = self.root

        while root.left:
            root = root.left

        return root.data


    def max(self, root=None):
        '''
            returns the largest value in the tree.
        '''
        if not root:
            root = self.root
        
        while root.right:
            root = root.right

        return root
