def isUniq(s):
    
    word_dict = {}
    LEN = len(s)

    for i in range(LEN//2):
        if s[i] not in word_dict.keys():
            word_dict[s[i]] = 1
        if s[LEN-i-1] not in word_dict.keys() and (LEN-i-1) != i:
            word_dict[s[LEN-i-1]] = 1
        else:
            return False

    return True


if __name__ == '__main__':
    s = input()
    
    if(isUniq(s)):
        print("String is unique")
    else:
        print("String is not unique")