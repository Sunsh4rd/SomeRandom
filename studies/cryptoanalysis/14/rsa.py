from math import gcd, sqrt
from random import randrange, randint

from sympy import isprime

first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]


def n_bit_random(n):
    return randrange(2 ** (n - 1) + 1, 2 ** n - 1)


def get_low_level_prime(n):
    while True:
        pc = n_bit_random(n)
        for divisor in first_primes_list:
            if pc % divisor == 0 and divisor ** 2 <= pc:
                break
        else:
            return pc


def gen_params():
    l = int(input('Длина чисел p и q: '))
    q = get_low_level_prime(l)
    k = 0
    p = (2 ** k) * q + 1
    while True:
        if isprime(p):
            break
        k += 1
        p = (2 ** k) * q + 1
    n = p * q
    phi = (p - 1) * (q - 1)
    e = randint(1, phi)
    while True:
        if gcd(e, phi) == 1:
            break
        e = randint(1, phi)
    d = pow(e, -1, phi)
    print(f'{p=}\n{q=}\n{n=}\n{phi=}\n{e=}\n{d=}')

    dis = pow(n-phi+1,2) - 4*n
    print(sqrt(dis))
    print(((n-phi+1)+int(sqrt(dis)))//2)
    print(((n-phi+1)-int(sqrt(dis)))//2)

    ed1 = e*d - 1
    f = 0
    while ed1 % 2 == 0:
        f+=1
        ed1 //= 2
    while True:
        a = randint(2, n-2)
        u = pow(a,ed1,n)
        v = pow(u,2,n)
        while v !=1:
            u = v
            v = pow(u, 2, n)
            if u == -1:
                break
        else:
            print(gcd(u-1,n))
            print(gcd(u+1, n))
            break


def main():
    gen_params()


if __name__ == '__main__':
    main()
