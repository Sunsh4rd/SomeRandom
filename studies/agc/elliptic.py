from itertools import product
from random import randint, choice

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
    end = (1 << n)-1
    print(begin, end, bin(begin), bin(end))
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
    print(ns)
    opts = []
    for n in ns:
        if n % 2 == 0:
            # print(n)
            r = n // 2
            if isprime(r):
                # print(r)
                opts.append((n, r, 2))
        if n % 4 == 0:
            # print(n)
            r = n // 4
            if isprime(r):
                # print(r)
                opts.append((n, r, 4))
    print(opts)
    if len(opts) == 0:
        return None
    return choice(opts)


def verify_p(p, r, m):
    return p != r and bool(sum((pow(p, i, r) != 1 for i in range(1, m+1))))


def legendre(a, p):
    res = pow(a, (p-1)//2, p)
    if res == p-1:
        return -1
    if res == 1:
        return 1
    # if a > p or a < 0:
    #     r = a % p
    #     return legendre(r,p)

    # if 0 < a < p

    # if a == 1:
    #     return 1
    # if a % 2 == 0:
    #     return legendre(a // 2, p) * (-1) ** ((p * 2 - 1) // 8)
    # if a % 2 == 1 and a != 1:
    #     return legendre(p % a, a) * (-1) ** ((a - 1) * ((p - 1) // 4))


def gen_point(p, n, r):
    # a, b = factorize(65129)
    # n,r,k = verify_n(65129, a, b) # verify_n(p,a,b)
    # print(n,r)
    # while True:
    # x0, y0 = randint(1,p-1), randint(1,p-1)
    for x0 in range(1, p):
        for y0 in range(2, p):
            a_c = (((pow(y0, 2, p) - pow(x0, 3, p)) % p) * pow(x0, -1, p)) % p
            if n == 2*r:
                print(2, a_c)
                if legendre(a_c, p) == -1:
                    print(a_c, 'not')
                    break
            if n == 4*r:
                print(4, a_c)
                if legendre(a_c, p) == 1:
                    print('is')
                    break
        break
    else:
        return None, None, None
    return x0, y0, a_c


def pp(x1, y1, x2, y2, a, p):
    if x1 == x2 and -y1 % p == y2:
        return None
    if x1 == x2:
        alpha = ((3*x1*x1 + a) * pow(2*y1, -1, p)) % p
    else:
        alpha = ((y1 - y2) * pow(x1 - x2, -1, p)) % p
    # print(alpha, end=' ')
    x3 = (pow(alpha, 2, p)-x1-x2) % p
    y3 = (alpha*(x1-x3) - y1) % p
    return x3, y3


def main():
    m = 5
    l = int(input('Длина числа p: '))
    while True:
        p = gen_char_n_bits(l)
        print(p)
        a, b = factorize(p)
        print(a, b)
        ver_n = verify_n(p, a, b)
        print(ver_n)
        if ver_n is None:
            continue
        n = ver_n[0]
        r = ver_n[1]
        print(r)
        ver_p = verify_p(p, r, m)
        print(ver_p)
        if not ver_p:
            continue
        break

    print(p, ver_n, ver_p, 'steps 1-4 ok')

    while True:
        x0, y0, a_c = gen_point(p, n, r)
        print(x0, y0)
        if x0 is None and y0 is None:
            continue
        p0 = (x0, y0)
        for _ in range(n):
            try:
                np = pp(*p0, x0, y0, a_c, p)
                p0 = (np[0], np[1])
                print(p0)
            except Exception as e:
                print('...')
                break
        print(f'mod {p}, p0 = {x0},{y0}, pinf = {p0}')
        break


if __name__ == '__main__':
    main()
