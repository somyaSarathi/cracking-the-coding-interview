def compress(s):
    start, end = 0, 0
    compressed = []
    
    for i in range(len(s)):
        if i != 0 and s[i] != s[i-1]:
            if end - start > 1:
                compressed.append(s[start] + str(end-start))
            else:
                compressed.append(s[start])
            
            start, end = i, i

        end += 1
    
    if end - start > 1:
        compressed.append(s[start] + str(end-start))
    else:
        compressed.append(s[start])

    return ''.join(compressed)


if __name__ == "__main__":
    s = input()
    print(compress(s))
