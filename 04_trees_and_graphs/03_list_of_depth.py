from binarySearchTree import binarySearchTree as bst
from binarySearchTree import Node
from doubly import Doubly as ll

#         5
#      3     6
#    2  4      9
#  1         7
#              8


def depth(root: Node, lvlList: dict={}, idx: int=0):
    try:
        lvlList[idx].push(root.data)
    except KeyError:
        lvlList[idx] = ll()
        lvlList[idx].push(root.data)

    if root.left:
        depth(root.left, lvlList, idx+1)
    if root.right:
        depth(root.right, lvlList, idx+1)

    return lvlList


if __name__ == '__main__':
    tree = bst(5, 3, 6, 2, 1, 4, 9, 7, 8)
    lvlList = depth(tree.root)

    for lvl, nodes in lvlList.items():
        print(f'{lvl}: {nodes}')
