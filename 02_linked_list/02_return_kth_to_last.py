from singlly import *

def returnK(ll, k):
    itr = ll.head

    for i in range(len(ll) - k):
        itr = itr.next

    return itr.data


if __name__ == '__main__':
    ll = singlly()
    k = int(input())
    inpt = map(int, input().split())

    for x in inpt:
        ll.push(x)

    print(returnK(ll, k))