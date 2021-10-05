def isPalindromePermutation(s):
    word_dict = {}
    even = 0
    odd = 0

    for ch in s:
        if ch in word_dict:
            word_dict[ch] += 1
        else:
            word_dict[ch] = 1

    for word in word_dict.values():
        if word%2 == 0:
            even += 1
        else:
            odd += 1

    if(odd > 1):
        return False

    return True
    

if __name__ == "__main__":
    s = input().replace(" ", "").replace("-", "").lower()
    
    if(isPalindromePermutation(s)):
        print("Given string is a palindrome permutation")
    else:
        print("Given string is not a palindrome permutation")
