from linkedList import *

def removeDups(ll):
    newll = LinkedList()
    words = {}
    itr = ll.head

    while itr.next != None:
        try:
            if words[itr.data] == 1:
                pass

        except Exception:
            words[itr.data] = 1
            newll.push(itr.data)

        itr = itr.next

    return newll


if __name__ == '__main__':

    ll = LinkedList()
    x = map(int, input().split())

    for i in x:
        ll.push(i)

    print(removeDups(ll))