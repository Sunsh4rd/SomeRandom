import decimal
from math import gcd
from random import randint

from sympy import isprime


def rabin_miller(p, k):
    if p == 2 or p == 3:
        return True
    s, m = p - 1, 0
    while s % 2 == 0:
        s //= 2
        m += 1
    i = 0
    while i <= k:
        from random import randint
        a = randint(2, p - 2)
        from math import gcd
        while gcd(a, p) != 1:
            a = randint(2, p - 2)
        b = pow(a, s, p)
        if b == 1:
            continue
        if b == p - 1:
            i += 1
            continue
        flag = False
        for l in range(1, m):
            c = pow(a, (s * pow(2, l)), p)
            if c == p - 1:
                flag = True
                break
        if flag:
            i += 1
            continue
        else:
            return False
    return True


def generate_primes(k):
    p = randint(2 ** (k - 1), 2 ** k - 1)
    # while not rabin_miller(p, 10):
    while not isprime(p):
        p = randint(2 ** (k - 1), 2 ** k - 1)
    q = randint(2 ** (k - 1), 2 ** k - 1)
    # while not rabin_miller(q, 10):
    while not isprime(q):
        q = randint(2 ** (k - 1), 2 ** k - 1)
    return p, q


def gen_params():
    l = int(input('Длина чисел p и q: '))
    p, q = generate_primes(l)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = randint(2, phi - 1)
    while gcd(e, phi) != 1:
        e = randint(2, phi - 1)
    d = pow(e, -1, phi)
    with open('pq.txt', 'w', encoding='utf-8') as pq_w:
        pq_w.write(f'{p}\n{q}')
    with open('n.txt', 'w', encoding='utf-8') as n_w:
        n_w.write(f'{n}')
    with open('phi.txt', 'w', encoding='utf-8') as phi_w:
        phi_w.write(f'{phi}')
    with open('e.txt', 'w', encoding='utf-8') as e_w:
        e_w.write(f'{e}')
    with open('d.txt', 'w', encoding='utf-8') as d_w:
        d_w.write(f'{d}')


def euler():
    with open('n.txt', 'r', encoding='utf-8') as n_r:
        n = int(n_r.read())
    with open('phi.txt', 'r', encoding='utf-8') as phi_r:
        phi = int(phi_r.read())

    b = n - phi + 1
    c = n
    dis = b ** 2 - 4 * c

    with decimal.localcontext() as ctx:
        ctx.prec = len(str(n))
        x = decimal.Decimal(dis).sqrt()
        p, q = (b + x) // 2, (b - x) // 2
        assert p * q == n

    with open('eulerpq.txt', 'w', encoding='utf-8') as epq_w:
        epq_w.write(f'{p}\n{q}')


def representation(n):
    l, r = 1, len(bin(n)[2:])
    while r - l > 1:
        mid = l + (r - l) // 2
        if n % pow(2, mid) == 0:
            l = mid
        else:
            r = mid
    for f in range(r, l - 1, -1):
        if n % pow(2, f) == 0:
            return f, n // pow(2, f)


def exts():
    with open('n.txt', 'r', encoding='utf-8') as n_r:
        n = int(n_r.read())
    with open('e.txt', 'r', encoding='utf-8') as e_r:
        e = int(e_r.read())
    with open('d.txt', 'r', encoding='utf-8') as d_r:
        d = int(d_r.read())
    mult = e * d - 1
    f, s = representation(mult)
    assert s * 2 ** f == mult

    while True:
        a = randint(2, n - 2)
        u = pow(a, s, n)
        v = pow(u, 2, n)
        while v != 1:
            u, v = v, pow(u, 2, n)
        if u == -1:
            continue
        p, q = gcd(u - 1, n), gcd(u + 1, n)
        if p == n or q == n:
            continue
        assert p * q == n
        with open('extspq.txt', 'w', encoding='utf-8') as extspq_w:
            extspq_w.write(f'{p}\n{q}')
        break


def main():
    opt = input('1 - Генерация параметров\n'
                '2 - Разложение по значению функции эйлера\n'
                '3 - Разложение по известным показателям\n')
    if opt == '1':
        gen_params()
    elif opt == '2':
        euler()
    elif opt == '3':
        exts()


if __name__ == '__main__':
    main()
