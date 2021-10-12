from singly import *

def removeDups(ll):
    uniq = {}
    newll = Singly()
    itr = ll.llist

    for x in itr:
        try:
            if uniq[x] == 1:
                pass

        except Exception:
            uniq[x] = 1
            newll.push(x)

    return newll


if __name__ == '__main__':
    ll = Singly()
    arr = map(int, input().split())

    for a in arr:
        ll.push(a)

    print(removeDups(ll))