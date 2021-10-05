def oneAway(a, b):
    replace = 0
    
    if len(a) + 1 == len(b):
        return isEdited(b, a)

    if len(a) - 1 == len(b):
        return isEdited(a, b)

    if len(a) == len(b):
        return isReplaced(a, b)

    return False


def isEdited(a, b):
    flag = 0

    for i in range(len(a)):
        if a[i] != b[i-flag]:
            flag += 1
            if flag > 1:
                return False
    
    return True


def isReplaced(a, b):
    flag = 0

    for i in range(len(a)):
        if a[i] != b[i]:
            flag += 1
            if flag > 1:
                return False

    return True


if __name__ == "__main__":
    a, b = input().split()
    print(oneAway(a, b))