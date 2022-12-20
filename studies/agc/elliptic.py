from itertools import product
from json import dump
from random import randint, choice

from sympy import isprime, legendre_symbol
import matplotlib.pyplot as plt


def gen_char_n_bits(n):
    begin = 1 << n-1
    end = (1 << n)-1
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
    if len(opts) == 0:
        return None
    return choice(opts)


def verify_p(p, r, m):
    return p != r and all((pow(p, i, r) != 1 for i in range(1, m+1)))


def gen_point(p, n, r):
    while True:
        x0, y0 = randint(1, p-1), randint(1, p-1)
        a_c = (((pow(y0, 2, p) - pow(x0, 3, p)) % p) * pow(x0, -1, p)) % p
        if n == 2*r:
            if legendre_symbol(-a_c, p) == -1:
                break
        if n == 4*r:
            if legendre_symbol(-a_c, p) == 1:
                break
    return x0, y0, a_c


def pp(x1, y1, x2, y2, a, p):
    if x1 == x2 and -y1 % p == y2:
        return None
    if x1 == x2:
        alpha = ((3*x1*x1 + a) * pow(2*y1, -1, p)) % p
    else:
        alpha = ((y1 - y2) * pow(x1 - x2, -1, p)) % p
    x3 = (pow(alpha, 2, p)-x1-x2) % p
    y3 = (alpha*(x1-x3) - y1) % p
    return x3, y3


def gen_curve():
    m = 1
    l = int(input('Длина числа p: '))
    if l < 4:
        print('Невозможно сгенерировать кривую для p заданной длины')
        exit()
    while True:
        p = gen_char_n_bits(l)
        a, b = factorize(p)
        ver_n = verify_n(p, a, b)
        if ver_n is None:
            continue
        n = ver_n[0]
        r = ver_n[1]
        c_n = ver_n[2]
        ver_p = verify_p(p, r, m)
        if not ver_p:
            continue
        break

    while True:
        x0, y0, a_c = gen_point(p, n, r)
        if x0 is None and y0 is None:
            continue
        p0 = (x0, y0)
        for i in range(n):
            try:
                np = pp(*p0, x0, y0, a_c, p)
                p0 = (np[0], np[1])
            except Exception as e:
                break
        if i+2 != n:
            continue
        else:
            break

    q = (x0, y0)
    nq = pp(*q, x0, y0, a_c, p)
    q = (nq[0], nq[1])
    if c_n == 4:
        nq = pp(*q, q[0], q[1], a_c, p)
        q = nq
    qi = (q[0], q[1])
    with open('curve_params.json', 'w', encoding='utf-8') as cp:
        dump({'p': p, 'A': a_c, 'Q': qi, 'r': r}, cp, indent=4)

    with open('points.txt', 'w', encoding='utf-8') as points:
        xs, ys = [], []
        xs.append(qi[0])
        ys.append(qi[1])
        for i in range(r):
            try:
                np = pp(*q, qi[0], qi[1], a_c, p)
                q = (np[0], np[1])
                xs.append(q[0])
                ys.append(q[1])
            except Exception as e:
                break
        points.write('\n'.join(map(str, zip(xs, ys))))
        # print(n, r, len(xs), len(ys))
        # print(xs, ys)
        # plt.scatter(xs, ys)
        # plt.show()

    return p, a_c, qi, r


def main():
    print(gen_curve())


if __name__ == '__main__':
    main()
