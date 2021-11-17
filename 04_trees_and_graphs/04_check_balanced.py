from binarySearchTree import Node, binarySearchTree as bst

def isBalanced(root: Node, diff: int=0) -> bool:
    if diff > 1:
        return False
    
    if root.left and root.right:
        return isBalanced(root.left, diff) and isBalanced(root.right, diff)

    elif root.left or root.right:
        diff += 1
        if root.left:
            return isBalanced(root.left, diff)
        else:
            return isBalanced(root.right, diff)

    return True


if __name__ == '__main__':
    tree = bst(3, 4, 2, 1, 5, 0, 6)
    print(isBalanced(tree.root))