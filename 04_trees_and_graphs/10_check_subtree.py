from typing import Literal
from binarySearchTree import Node, binarySearchTree as bst


def findNode(t1: Node, t2: Node) -> Node | Literal[-1]:
    if t1 == t2:
        return t1
    
    if t1 > t2 and t1.left:
        return findNode(t1.left, t2)
    if t1 < t2 and t1.right:
        return findNode(t1.right, t2)

    return -1


def isEqual(t1: Node, t2: Node) -> bool:
    queue: list[list[Node]] = [ [t1, t2] ]

    # todo
    while queue:
        curr1, curr2 = queue[0]
        del queue[0]

        if curr1.left:
            if not curr2.left:
                return False
            if curr1.left != curr2.left:
                return False

            queue.append([curr1.left, curr2.left])

        elif curr2.left:
            return False

        if curr1.right:
            if not curr2.right:
                return False
            if curr1.right != curr2.right:
                return False

            queue.append([curr1.right, curr2.right])
        
        elif curr2.right:
            return False
    
    return True


def isSubtree(t1: bst, t2: bst) -> bool:
    root: Node = findNode(t1.root, t2.root)

    if root == -1:
        return False

    # todo
    return isEqual(root, t2.root)


if __name__ == '__main__':
    t1 = bst(8, 3, 10, 1, 6, 14, 4, 7, 13)
    t2 = bst(6, 4, 7)

    print(isSubtree(t1, t2))
