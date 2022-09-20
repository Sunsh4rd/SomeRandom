import random
from math import gcd
from sympy import isprime


def get_random_prime(n):
    while True:
        number = random.getrandbits(n)
        if isprime(number):
            return number


def keygen():
    p = get_random_prime(1024)
    q = 4
    k = 1
    while not isprime(q):
        q = 2**(-k) * (p-1)
        k += 1

    return (p-1) % q, p, q


def main():
    t, p, q = keygen()
    print(t, p, q)


if __name__ == '__main__':
    main()


# p = 2^k * q + 1
