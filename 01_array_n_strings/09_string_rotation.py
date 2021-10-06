def shiftRight(s):
    return s[len(s) - 1] + s[:-1]

def isSubstring_dp(s1, s2, memo, n):

    if memo == s1 and n > 1:
        return False
    if s1 == s2:
        return True

    return isSubstring_dp(shiftRight(s1), s2, memo, n+1)


def isSubstring(s1, s2):

    if s1 == s2:
        return True

    for i in range(len(s2)):
        s1 = shiftRight(s1)

        if s1 == s2:
            return True

    return False


if __name__ == "__main__":
    s1, s2 = input(), input()

    if len(s1) == len(s2):
        if isSubstring_dp(s1, s2, s1, 1):
            print("Yes")
        else:
            print("No")
    else:
        print("No")