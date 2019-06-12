import sys


def lis_bottom_up(A, n):
    D = [1 for _ in range(n)]
    for i in range(n):
        for j in range(i):
            if A[j] <= A[i] and A[i] % A[j] == 0 and D[j] + 1 > D[i]:
                D[i] = D[j] + 1
    ans = 0
    for i in range(n):
        ans = max(ans, D[i])
    return ans


def main():
    n = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split()))
    print(lis_bottom_up(A, n))


if __name__ == "__main__":
    main()
