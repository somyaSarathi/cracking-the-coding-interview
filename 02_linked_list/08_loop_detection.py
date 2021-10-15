from singly import *

def isLoop(ll: Singly):
    fast = slow = ll.head

    while slow:
        fast = fast.nxt.nxt
        slow = slow.nxt

        if fast is slow:
            break

    slow = ll.head

    while fast is not slow:
        fast = fast.nxt
        slow = slow.nxt

    return fast.data