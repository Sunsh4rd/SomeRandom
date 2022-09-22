import random
from math import gcd
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


def keygen():
    p = get_random_prime(16)
    q = get_random_prime(8)
    while True:
        if (p - 1) % q == 0:
            break
        q = get_random_prime(8)

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
