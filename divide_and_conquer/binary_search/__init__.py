import sys


def find_index(array, n, k):
    l = 0
    r = n - 1
    while l <= r:
        m = (l + r) // 2
        if array[m] == k:
            return m + 1
        elif array[m] > k:
            r = m - 1
        else:
            l = m + 1
    return -1


def main():
    n, *array = map(int, sys.stdin.readline().strip().split())
    k, *numbers = map(int, sys.stdin.readline().strip().split())
    result = []
    for i in range(k):
        result.append(find_index(array, n, numbers[i]))
    for i in result:
        print(i, end=' ')


if __name__ == "__main__":
    main()
