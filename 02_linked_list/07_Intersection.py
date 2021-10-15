from singly import *

def intersect(l1: Singly, l2: Singly):
    if id(l1.tail) == id(l2.tail):
        return True
    
    return False


if __name__ == '__main__':
    l1 = Singly([1, 2, 3, 4])
    l2 = Singly([9, 8, 7, 6])

    l1.push(5)
    l2.tail.nxt = l1.tail
    l2.tail = l2.tail.nxt

    if intersect(l1, l2):
        print('lists are intersecting')

    else:
        print("lists don't intersect")