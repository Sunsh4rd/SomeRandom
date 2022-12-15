from math import gcd
from random import getrandbits, randint

from sympy import isprime, jacobi_symbol


def get_random_prime(n):
    while True:
        number = getrandbits(n)
        if isprime(number):
            return number


def step1():
    l = int(input('Длина числа n: '))
    # r, s = 1, 1
    q = get_random_prime(l)
    k=0
    p = (2**k) * q + 1
    while True:
        if isprime(p):
            break
        k += 1
        p = (2**k) * q + 1
    n = p*q
    x = randint(1,n-1)
    while gcd(x,n) != 1:
        x = randint(1,n-1)
    x0 = pow(x,2,n)
    x1 = pow(x0,2,n)
    return n,x,x0,x1

def get_u(n):
    u = randint(1,n-1)
    while jacobi_symbol(u,n) != -1:
        u = randint(1,n-1)
    return u


def main():
    n,x,x0,x1 = step1()
    print(n,x,x0,x1)
    guess = randint(0,1)
    # u=get_u(n)
    if pow(x,2,n) == x0 and pow(x0,2,n) == x1:
        print('bob wins')
    else:
        print('alice wins')



if __name__ == '__main__':
    main()
