import random
from sympy import isprime
import json


def get_random_prime(n):
    while True:
        number = random.getrandbits(n)
        if isprime(number):
            return number


def fast_mod_exp(a, b, m):
    r = 1
    while b > 0:
        if b & 1:
            r *= a
            r %= m
        a *= a
        a %= m
        b >>= 1
    return r


def logarithm(q, p):
    while True:
        for a in range(2, p):
            if fast_mod_exp(a, q, p) == 1:
                return a


def gen_shared_parameters(n):
    q = get_random_prime(n)
    k = 0
    p = (2**k) * q + 1
    while True:
        if isprime(p):
            break
        k += 1
        p = (2**k) * q + 1

    a = logarithm(q, p)

    return p, q, a


def main():
    print(gen_shared_parameters(64))

if __name__ == '__main__':
    main()