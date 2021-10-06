def shiftRight(s):
    return s[len(s) - 1] + s[:-1]

def isSubstring_dp(s1, s2, memo, n):

    if memo == s1 and n > 1:
        return False
    if s1 == s2:
        return True

    return isSubstring_dp(shiftRight(s1), s2, memo, n+1)

if __name__ == "__main__":
    s1, s2 = input(), input()
    
    if isSubstring_dp(s1, s2, s1, 1):
        print("Yes")
    else:
        print("Yes")