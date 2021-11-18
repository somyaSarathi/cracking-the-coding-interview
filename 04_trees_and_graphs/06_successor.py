from binarySearchTree import Node, binarySearchTree as bst

def inOrder(root: Node, key: int, stack=[]) -> int:
    if root.left:
        stack = inOrder(root.left, key, stack)

    if root == key:
        print(stack.pop())
        exit(0)

    stack.append(root)

    if root.right:
        stack = inOrder(root.right, key, stack)

    return stack


if __name__ == '__main__':
    tree = bst(3, 4, 5, 2, 1, 7, 19, 23, 45, 21, 62, 23, 13)
    inOrder(tree.root, 23)