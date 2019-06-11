import sys


def count_sort(numbers, n, M):
    helper = [0 for _ in range(M + 1)]
    result = [0 for _ in range(n)]
    for number in numbers:
        helper[number] += 1
    for i in range(2, len(helper)):
        helper[i] = helper[i] + helper[i - 1]
    for j in range(n - 1, -1, -1):
        result[helper[numbers[j]]-1] = numbers[j]
        helper[numbers[j]] = helper[numbers[j]] - 1
    return result


def main():
    n = int(sys.stdin.readline().strip())
    numbers = list(map(int, sys.stdin.readline().strip().split()))
    result = count_sort(numbers, n, 10)

    for i in result:
        print(i, end=" ")


if __name__ == "__main__":
    main()
