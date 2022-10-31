from random import getrandbits, randint
from math import log2
from sympy import isprime


def gen_p(n):
    while True:
        p = randint(2**(n-1), 2**n)
        if p % 2 != 0 and all(p % x != 0 for x in range(3, int(p**0.5)+1, 2)) and p % 4 == 1:
            break
    return p


def miller_rabin(n, k):
    if n == 3:
        return True

    n1 = n - 1
    q = n1
    t = None
    s = 0
    while True:
        q //= 2
        s += 1
        if q % 2 != 0:
            t = q
            break

    for _ in range(k):
        a = randint(2, int(str(n))-2)
        x = pow(a, t, n)
        if x == 1 or x == n1:
            continue

        for _ in range(s-1):
            x = pow(x, 2, n)
            # if not isinstance(x, Bigint):
            #     x = Bigint(int_to_list_of_digits(x))
            if x == 1:
                return False
            if x == n1:
                break

        if x != n1:
            return False

    return True


def gen_char_n_bits(n):
    p = getrandbits(n)
    while True:
        if p % 4 == 1 and miller_rabin(p, int(log2(p))):
            return p
        p = getrandbits(n)


for i in range(4, 100000):
    if isprime(i) != miller_rabin(i, int(log2(i))):
        print(i, miller_rabin(i,int(log2(i))), isprime(i))
        
