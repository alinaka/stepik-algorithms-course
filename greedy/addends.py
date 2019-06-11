def get_addends(n):
    k = 0
    while True:
        current = ((1 + k) * k / 2)
        if current > n:
            return k - 1
        elif current == n:
            return k
        k += 1
    return k, current


def main():
    n = int(input())
    k = get_addends(n)
    print(k)
    for item in range(1, k):
        print(item, end=' ')

    if (2 + k) * ((k + 1) / 2) != n:
        print(int(n - k * (k - 1) / 2))


if __name__ == "__main__":
    main()