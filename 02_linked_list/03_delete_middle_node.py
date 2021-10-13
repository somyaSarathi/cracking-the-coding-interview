from singly import *

def deleteMiddleNode(ll: Singly):
    if ll.head == None or len(ll) <= 2:
        return ll

    n = len(ll)//2
    itr = ll.head

    if len(ll)%2 == 0:
        while n > 2:
            itr = itr.nxt
            n -= 1
            
        itr.nxt = itr.nxt.nxt
        del ll.llist[len(ll)/2-1]
        return ll

    while n > 1:
        itr = itr.nxt
        n -= 1

    itr.nxt = itr.nxt.nxt
    del ll.llist[len(ll)//2]

    return ll


if __name__ == '__main__':
    l = map(int, input().split())
    ll = Singly(l)

    print(deleteMiddleNode(ll))