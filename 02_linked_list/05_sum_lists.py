from singly import *

def sumLists(l1, l2):
    for i in range(len(l2)):
        l1[i] += l2[i]

    ll = Singly(l1)
    return ll


if __name__ == '__main__':
    inpt = map(int, input().split())
    l1 = Singly(inpt)

    inpt = map(int, input().split())
    l2 = Singly(inpt)

    if len(l1) >= len(l2):
        print(sumLists(l1.llist, l2.llist))
        exit(0)

    print(sumLists(l2.llist, l1.llist))
    exit(0)