from singly import *

def isPalindrome(ll: Singly) -> bool:
    if ll.head == None:
        raise IndexError('linked list is empty')

    itr = ll.head
    length = len(ll)

    for i in range(length//2):
        if itr != ll.llist[length-i-1]:
            return False

        itr = itr.nxt

    return True


if __name__ == '__main__':
    l = map(int, input().split())
    ll = Singly(l)

    if isPalindrome(ll):
        print('It is a palindrome')

    else:
        print("It's not a palindrome")
