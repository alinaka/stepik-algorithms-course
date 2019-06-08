import sys

inversion = 0


def merge(A, B):
    len_a = len(A)
    len_b = len(B)
    i, j = 0, 0
    result = []

    global inversion

    for _ in range(len_b + len_a):
        if i < len_a and j < len_b:
            if A[i] > B[j]:
                inversion += len_a - i
                result.append(B[j])
                j += 1
            else:
                result.append(A[i])
                i += 1
        else:
            if j < len_b:
                result += B[j:]
            else:
                result += A[i:]
            break
    return result


def merge_sort(A, l, r):
    if l < r:
        m = (l + r) // 2
        result = merge(merge_sort(A, l, m), merge_sort(A, m + 1, r))
        return result
    return [A[l]]


def main():
    n = int(sys.stdin.readline().strip())
    A = list(map(int, sys.stdin.readline().strip().split()))
    merge_sort(A, 0, n - 1)
    print(inversion)


if __name__ == "__main__":
    main()
