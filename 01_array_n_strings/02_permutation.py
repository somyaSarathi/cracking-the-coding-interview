from collections import Set

def isPermutation(a, b):

    if a == b:
        return True

    elif Set(a) == Set(b):
        return True

    return False
    

if __name__ == "__main__":
    a = input()
    b = input()

    if(isPermutation(a, b)):
        print("String B is permutation of String A")
    else:
        print("String B is not permutation of String A")