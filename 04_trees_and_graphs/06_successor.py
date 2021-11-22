from binarySearchTree import Node, binarySearchTree as bst


def successor(root: Node, key: int, stack: list = []):
    if root.left:
        stack = successor(root.left, key, stack)

    if stack:
        if stack[len(stack)-1] == key:
            print(root)
            exit(0)

        if root.data > key:
        	exit(0)

    stack.append(root.data)

    if root.right:
        stack = successor(root.right, key, stack)

    return stack


'''
    1 2 3 4 5 7 13 19 21 23 45 62

               (3)
               ↙ ↘
             (2) (4)
             ↙     ↘
           (1)     (5)
                     ↘
                     (7)
                       ↘
                      (19)
                      ↙  ↘
                   (13)  (45)
                         ↙  ↘
                      (21)  (62)
                         ↘
                        (23)
'''


if __name__ == '__main__':
    tree: bst = bst(3, 4, 5, 2, 1, 7, 19, 45, 21, 62, 23, 13)
    successor(tree.root, 23)  # 45
