from typing import Literal
from binarySearchTree import Node


# O(hm)
# h = height of the tree
# m = length of list (list.copy())
def parentList(root: Node, node: Node) -> list[int] | Literal[-1]:
    '''
        returns list of parents in order for node
    '''
    queue: list[Node] = [ root ]
    parent: dict = { root.data: [] }

    while queue:
        curr = queue[0]
        del queue[0]

        if curr == node:
            return parent[curr.data]

        # iteration
        if curr.left:
            queue.append(curr.left)
            parent[curr.left.data] = parent[curr.data].copy()
            parent[curr.left.data].append(curr.data)

            if curr.left == node:
                return parent[curr.left.data]

        if curr.right:
            queue.append(curr.right)
            parent[curr.right.data] = parent[curr.data].copy()
            parent[curr.right.data].append(curr.data)

            if curr.right == node:
                return parent[curr.right.data]

    return -1

# O(nm+2h)
# n > m
# n = lenght of list (set conversation)
# m = length of list (iterating each element)
# h = height of the tree (h = log(n) to n)
def commonAncestor(root: Node, node1: Node, node2: Node) -> int:
    '''
        returns the first common parent for node1 and node2
    '''
    parent1: list[int] = parentList(root, node1)
    parent2: list[int] = parentList(root, node2)

    if parent1 == -1 or parent2 == -1:
        return -1

    if len(parent1) > len(parent2):
        parent1 = set(parent1)

        for parent in parent2:
            if parent in parent1:
                return parent

    else:
        parent2 = set(parent2)

        for parent in parent1:
            if parent in parent2:
                return parent

    return -1


'''
        (3)
       ↙    ↘
     (6)     (8)
   ↙  ↘      ↙   ↘ 
(10) (21)   (13) (11)
           ↙   ↘ 
        (14)   (24)
'''


if __name__ == '__main__':
    # binary Tree
    root: Node = Node(3)
    root.left = Node(6)
    root.right = Node(8)

    root.left.left = Node(10)
    root.left.right = Node(21)

    root.right.left = Node(13)
    root.right.right = Node(11)

    root.right.left.left = Node(14)
    root.right.left.right = Node(24)

    #                          21               24
    print(commonAncestor(root, root.left.right, root.right.left.right))
