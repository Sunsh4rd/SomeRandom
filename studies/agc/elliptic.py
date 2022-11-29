from itertools import product
from random import randint, choice

from sympy import isprime
import matplotlib.pyplot as plt


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
            r = n // 2
            if isprime(r):
                opts.append((n, r, 2))
        if n % 4 == 0:
            r = n // 4
            if isprime(r):
                continue
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


def gen_point(p, n, r):
    while True:
        x0, y0 = randint(1, p-1), randint(1, p-1)
    # for x0 in range(1, p):
    #     for y0 in range(1, p):
        a_c = (((pow(y0, 2, p) - pow(x0, 3, p)) % p) * pow(x0, -1, p)) % p
        if n == 2*r:
            print(2, a_c)
            if legendre(-a_c, p) == -1:
                print(a_c, 'not')
                break
        if n == 4*r:
            print(4, a_c)
            if legendre(-a_c, p) == 1:
                print(a_c, 'is')
                break
    # else:
    #     return None, None, None
    return x0, y0, a_c


def pp(x1, y1, x2, y2, a, p):
    if x1 == x2 and -y1 % p == y2:
        return None
    if x1 == x2:
        alpha = ((3*x1*x1 + a) * pow(2*y1, -1, p)) % p
    else:
        alpha = ((y1 - y2) * pow(x1 - x2, -1, p)) % p
    # print(alpha)
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
        c_n = ver_n[2]
        print(r)
        ver_p = verify_p(p, r, m)
        print(ver_p)
        if not ver_p:
            continue
        break

    # print(p, ver_n, ver_p, 'steps 1-4 ok')

    while True:
        x0, y0, a_c = gen_point(p, n, r)
        if x0 is None and y0 is None:
            continue
        p0 = (x0, y0)
        print('1 x0 y0', x0, y0)
        print(
            f'N = {n}, p = {p}, (x0, y0) = {p0}, A = {a_c}, r = {r}, c_n = {c_n}')
        for i in range(n):
            try:
                np = pp(*p0, x0, y0, a_c, p)
                p0 = (np[0], np[1])
                print(f'{i+2} x0 y0', p0)
            except Exception as e:
                print('...')
                break
        if i+2 != n:
            continue
        else:
            break

    q = (x0, y0)
    print('1 q', q)
    nq = pp(*q, x0, y0, a_c, p)
    q = (nq[0], nq[1])
    print('2 q', q)
    if c_n == 4:
        nq = pp(*q, q[0], q[1], a_c, p)
        q = nq
        print('4 q', q)
    qi = (q[0], q[1])
    xs, ys = [], []
    xs.append(qi[0])
    ys.append(qi[1])
    for i in range(r):
        try:
            np = pp(*q, qi[0], qi[1], a_c, p)
            q = (np[0], np[1])
            print(f'{i+2} q', q)
            xs.append(q[0])
            ys.append(q[1])
        except Exception as e:
            print('...')
            break
    print(n, r, len(xs), len(ys))
    print(xs, ys)
    plt.scatter(xs, ys)
    plt.show()

    # print('i', i)
    # print(f'mod {p}, p0 = {x0},{y0}, pinf = {p0}')
    # xs, ys = [], []
    # if n == 2*r:
    #     np = pp(*q,x0,y0,a_c,p)
    #     q = (np[0],np[1])
    # elif n == 4*r:
    #     for _ in range(3):
    #         np = pp(*q, x0, y0, a_c, p)
    #         q = (np[0], np[1])
    # print('Q', q)
    # xs.append(q[0])
    # ys.append(q[1])
    # for i in range(r):
    #         try:
    #             np = pp(*q, q[0], q[1], a_c, p)
    #             q = (np[0], np[1])
    #             print(f'{i+2} Q',q)
    #             xs.append(q[0])
    #             ys.append(q[1])
    #         except Exception as e:
    #             print('...')
    #             break
    # print(n, r, len(xs), len(ys))
    # print(xs, ys)
    # plt.scatter(xs, ys)
    # plt.show()


if __name__ == '__main__':
    main()
