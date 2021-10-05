def inputMatrix(N):
    matrix, row = [], []

    for i in range(N):
        row = list(map(int, input().split()))
        matrix.append(row)

    return matrix


def matrixTranspose(N, M, matrix):
    matrix = list(zip(*matrix))

    for l in matrix:
        print(l)


if __name__ == "__main__":
    N, M = tuple(map(int, input().split()))
    matrix = inputMatrix(N)
    matrixTranspose(N, M, matrix)