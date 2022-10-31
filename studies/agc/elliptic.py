from itertools import product
from random import randint

from sympy import isprime


# def miller_rabin(n, k):
#     if n == 3:
#         return True

#     n1 = n - 1
#     q = n1
#     t = None
#     s = 0
#     while True:
#         q //= 2
#         s += 1
#         if q % 2 != 0:
#             t = q
#             break

#     for _ in range(k):
#         a = randint(2, int(str(n))-2)
#         x = pow(a, t, n)
#         if x == 1 or x == n1:
#             continue

#         for _ in range(s-1):
#             x = pow(x, 2, n)
#             # if not isinstance(x, Bigint):
#             #     x = Bigint(int_to_list_of_digits(x))
#             if x == 1:
#                 return False
#             if x == n1:
#                 break

#         if x != n1:
#             return False

#     return True


def gen_char_n_bits(n):
    begin = 1 << n-1
    end = 1 << n
    print(begin, end, bin(begin), bin(end-1))
    while True:
        p = randint(begin, end)
        if p % 4 == 1 and isprime(p):
            return p


def factorize(p):
    for a, b in product(range(1, int(p**0.5)+1), repeat=2):
        if a*a + b*b == p:
            return a, b


def verify_n(p, a, b):
    ns = [p + 1 + 2*a, p + 1 + 2*b, p + 1 - 2*a, p + 1 - 2*b]
    return ns


def main():
    p = gen_char_n_bits(16)
    print(p)

    a, b = factorize(65129)
    print(a, b)

    print(verify_n(65129, a, b))


if __name__ == '__main__':
    main()
