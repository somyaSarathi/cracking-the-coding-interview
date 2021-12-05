from binarySearchTree import Node, binarySearchTree as bst


def printList(lst: list) -> None:
    print('{', end=' ')

    for ele in lst:
        if ele == lst[-1]:
            print(ele, end=' ')
        else:
            print(ele, end=', ')

    print('}')
    return


def pathSum(root: Node, k: int, path: list=[]) -> None:
    if root is None:
        return

    path.append(root.data)

    if root.left:
        pathSum(root.left, k, path)

    if root.right:
        pathSum(root.right, k, path)

    sum: int = 0
    for i in range(len(path)-1, -1, -1):
        sum += path[i]

        if sum > k:
            break
        if sum == k:
            printList(path[i:])
            
    path.pop()
    return


'''
         (8)
       /     \
    (3)      (10)
   /   \        \
 (1)   (6)      (14)
      /  \       /
    (4)  (7)   (13)
'''


if __name__ == '__main__':
    k: int = 24
    tree = bst(8, 3, 10, 1, 6, 14, 4, 7, 13)

    pathSum(tree.root, 17) # 8 3 6
