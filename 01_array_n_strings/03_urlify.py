def urlify(s, length):
    return s[:length].replace(" ", "%20")
    

if __name__ == "__main__":
    s = input()
    length = int(input())

    print(urlify(s, length))