import random
from math import gcd, log
from sympy import isprime


def get_random_prime(n):
    while True:
        number = random.getrandbits(n)
        if isprime(number):
            return number


def logarithm(q, p):
    for a in range(2, p):
        # print(a, q, p)
        if pow(a, q, p) == 1:
            return a
    return None
    # k = 0
    # while True:
    #     a = log((2**k) * p + 1, q)
    #     print(a)
    #     if a % 1 == 0:
    #         return int(a)


def keygen():
    q = get_random_prime(32)
    k = 10
    p = (2**k) * q + 1
    while True:
        if isprime(p):
            break
        k += 1
        # q = get_random_prime(16)
        p = (2**k) * q + 1

    print(q, p)
    a = logarithm(q, p)
    s = random.randint(0, q-1)
    return p, q, a, s


def main():
    # print(get_random_prime(128))
    p, q, a, s = keygen()
    print(p, q, a, s)


if __name__ == '__main__':
    main()


# p = 2^k * q + 1
