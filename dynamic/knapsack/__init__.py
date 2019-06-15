def knapsack(W, w, n):
    D = [[0]*(n + 1) for _ in range(W + 1)]
    for i in range(W+1):
        D[i][0] = 0

    for i in range(n+1):
        D[0][i] = 0
    for i in range(1, n + 1):
        for j in range(1, W + 1):
            D[j][i] = D[j][i - 1]
            if w[i - 1] <= j:
                D[j][i] = max(D[j][i], D[j - w[i-1]][i-1] + w[i-1])
    return D[W][n]


def main():
    W, n = map(int, input().split())
    w = list(map(int, input().split()))
    print(knapsack(W, w, n))


if __name__ == '__main__':
    main()
