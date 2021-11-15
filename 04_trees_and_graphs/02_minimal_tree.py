from binarySearchTree import binarySearchTree as bst

def minimalTree(arr: list, tree=bst()) -> bst:
    '''
        time complexity: o(nlogn)
        recursive algo to divide tree into half
        append the middle element
    '''
    length = len(arr)

    if length == 1:
        tree.append(arr[0])
        return tree
    
    tree.append(arr[length//2])

    minimalTree(arr[:length//2], tree)
    if length > 2:
        minimalTree(arr[(length//2)+1:], tree)

    return tree


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    tree = minimalTree(arr)
    print(tree.root)
