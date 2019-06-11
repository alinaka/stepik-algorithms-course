import sys
from functools import cmp_to_key


def mycmp(left, right):
    if left[0] != right[0]:
        return -1 if left[0] < right[0] else 1
    else:
        return -1 if left[1] < right[1] else 1


def main():
    points = []
    n, m = map(int, sys.stdin.readline().strip().split())
    for _ in range(n):
        a, b = list(map(int, sys.stdin.readline().strip().split()))
        points.append((a, -1, -1))
        points.append((b, 1, -1))
    numbers = [0 for _ in range(m)]
    for i, number in enumerate(map(int, sys.stdin.readline().strip().split())):
        points.append((number, 0, i))
    points.sort(key=cmp_to_key(mycmp))
    curr = 0
    for p in points:
        if p[1] == -1:
            curr += 1
        elif p[1] == 1:
            curr -= 1
        elif p[1] == 0:
            numbers[p[2]] = curr
        else:
            raise TypeError
    for p in numbers:
        print(p, end=" ")


if __name__ == "__main__":
    main()