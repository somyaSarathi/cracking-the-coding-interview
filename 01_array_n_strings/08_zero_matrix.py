def inputMatrix(N):
    matrix, row = [], []

    for i in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

    return matrix


def zeroMatrix(N, M, a):
    for l in a:
        if 0 in l:
            l = [0]*M

        print(l)


if __name__ == "__main__":
    N, M = tuple(map(int, input().split()))
    a = inputMatrix(N)
    zeroMatrix(N, M, a)