import sys


def diff(a, b):
    if a == b:
        return 0
    else:
        return 1


def edit_distance_bu(A, B):
    n = len(A)
    m = len(B)
    D = [[0 for _ in range(m + 1)] for __ in range(n + 1)]
    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j
    for i in range(n):
        for j in range(m):
            c = diff(A[i], B[j])
            D[i + 1][j + 1] = min(D[i][j+1] + 1, D[i+1][j] + 1, D[i][j] + c)
    return D[n][m]


def main():
    global A, B, D
    A = sys.stdin.readline().strip()
    B = sys.stdin.readline().strip()
    result = edit_distance_bu(A, B)
    print(result)


if __name__ == "__main__":
    main()