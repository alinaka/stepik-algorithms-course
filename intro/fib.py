"""
Задача: небольшое число Фибоначчи
"""


def fib(n):
    assert n > 0
    n0, n1 = 0, 1
    for i in range(n - 1):
        n0, n1 = n1, n0 + n1
    return n1


# n = int(input())
# print(fib(n))

"""
Задача: последняя цифра большого числа Фибоначчи
"""


def fib_digit(n):
    n0, n1 = 0, 1
    for _ in range(1, n):
        n0, n1 = n1, (n0 + n1) % 10
    return b


# n = int(input())
# print(fib_digit(n))

"""
Задача: огромное число Фибоначчи по модулю
"""


def find_pisano(fib_count, divisor):
    """
    Returns list of modulos (Pisano numbers) for a given Fibonacci number count and divisor.
    The modulos are periodic, the period depends on a divisor.
    :param n: Fibonacci number count
    :param m: divisor for a Fibonacci number
    :return: list of modulos for Fibonacci numbers divided by the m
    """
    pisano = [0, 1]
    if divisor == 1:
        return pisano[:1]
    if fib_count <= 1:
        return pisano
    n0, n1 = 0, 1
    for _ in range(divisor * 6):
        n0, n1 = n1, (n0 + n1) % divisor
        pisano.append(n1)
        if pisano[-1] == 1 and pisano[-2] == 0:
            break
    return pisano[:-2]


def fib_mod(n, m):
    pisano = find_pisano(n, m)
    return pisano[n % len(pisano)]


def test():
    assert fib_mod(10, 2) == 1
    assert fib_mod(10, 1) == 0
    assert fib_mod(1, 542) == 0

# n, m = map(int, input().split())
# print(fib_mod(n, m))
