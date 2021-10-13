from singly import *

def partition(ll: Singly, part: int):
    right, left = [], []

    for x in ll.llist:
        if x >= part:
            right.append(x)

        else:
            left.append(x)

    newll = Singly(left+right)
    return newll


if __name__ == '__main__':
    l = map(int, input().split())
    part = int(input())
    ll = Singly(l)

    print(partition(ll, part))