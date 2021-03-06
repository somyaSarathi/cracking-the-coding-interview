from singly import *

def removeKthtoLast(k: int, ll):
    if len(ll) <= k:
        return

    n = len(ll) - k
    node = ll.head

    while n > 1:
        node = node.nxt
        n -= 1

    node.nxt = node.nxt.nxt
    del ll.llist[len(ll) - k]

    return ll


if __name__ == '__main__':
    k = int(input())
    l = map(int, input().split())
    ll = Singly(l)

    print(removeKthtoLast(k, ll))