import random
from binarySearchTree import Node, binarySearchTree as bst


def inOrderQueue(root: Node, queue: list=[]) -> list[Node]:
    if root is None:
        return []

    if root.left:
        queue = inOrderQueue(root.left, queue)

    queue.append(root)

    if root.right:
        queue = inOrderQueue(root.right, queue)
    
    return queue


def getRandom(tree: bst) -> Node:
    '''
        returns an randome node from the tree.
    '''
    queue: list = inOrderQueue(tree.root)
    return random.choice(queue)


if __name__ == '__main__':
    tree = bst(19, 34, 26, 2, 45, 8, 43, 32)
    print(getRandom(tree))
