from binarySearchTree import Node, binarySearchTree as bst

def isBST(root:Node):
    if not root.left and not root.right:
        return True

    left = right = True

    if root.left:
        if not root >= root.left:
            return False

        left = isBST(root.left)

    if root.right:
        if not root < root.right:
            return False

        right = isBST(root.right)

    return left and right


if __name__ == '__main__':
    tree = bst(4, 3, 5, 6, 7, 5, 9)

    root = Node(3)
    root.left = Node(5)
    root.right = Node(2)
    root.left.left = Node(1)
    root.left.right = Node(2)
    root.right.left = Node(8)

    print(isBST(tree.root))
    print(isBST(root))
