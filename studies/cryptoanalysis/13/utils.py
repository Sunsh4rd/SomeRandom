from random import randint
import decimal


def isqrt(x):
    if x < 0:
        raise ValueError('square root not defined for negative numbers')
    n = int(x)
    if n == 0:
        return 0
    a, b = divmod(n.bit_length(), 2)
    x = 2**(a+b)
    while True:
        y = (x + n//x)//2
        if y >= x:
            return x
        x = y


def euclid(a, b):
    r = a % b
    while r != 0:
        a, b = b, r
        r = a % b
    return b


def eeuclid(a, b):
    r0, r1 = a, b
    x0, x1 = 1, 0
    y0, y1 = 0, 1

    q, r2 = r0 // r1, r0 % r1
    while r2 != 0:
        x1, x0 = x0 - q * x1, x1
        y1, y0 = y0 - q * y1, y1

        r1, r0 = r2, r1
        q, r2 = r0 // r1, r0 % r1

    return r1, x1, y1


def legendre(a, n):
    a %= n
    if a == 0:
        return 0
    elif a == 1:
        return 1
    return pow(a, (n - 1) // 2, n)


def fac2k(a):
    k = 0
    while a & 1 == 0:
        a >>= 1
        k += 1
    return a, k


def miller_rabin(n):
    r, s = fac2k(n - 1)
    a = randint(2, n - 2)
    y = pow(a, r, n)

    if y != 1 and y != n - 1:
        j = 1
        while j <= s - 1 and y != n - 1:
            y = (y * y) % n
            if y == 1:
                return False
            j += 1
        if y != n - 1:
            return False
    return True


def is_prime(n, rounds=10):
    if n > 5:
        for _ in range(rounds):
            if not miller_rabin(n):
                return False
        return True
    return n in [2, 3, 5]


def gen_primes(count):
    container = []
    a = 2
    while len(container) < count:
        if is_prime(a):
            container.append(a)
        a += 1
    return container


def gen_chain_fraction(p, q):
    a = p // q
    yield a

    while p != q:
        p, q = q, p - q * a
        a = p // q
        yield a


def gen_square_chain_fraction(n):
    a0 = decimal.Decimal(n).sqrt()
    r0 = isqrt(n)
    yield r0
    ratio0 = 1
    numenator0 = 0

    while True:
        numenator1 = r0 * ratio0 - numenator0
        ratio1 = (n - numenator1 * numenator1) // ratio0
        if ratio1 == 0:
            raise ValueError('Число является полным квадратом')
        r1 = int((a0 + decimal.Decimal(numenator1)) / decimal.Decimal(ratio1))

        yield r1
        r0, ratio0, numenator0 = r1, ratio1, numenator1


def gen_convergent(generator):
    p0, p1 = 0, 1
    q0, q1 = 1, 0

    while True:
        ai = next(generator)
        pi = ai * p1 + p0
        qi = ai * q1 + q0
        yield pi, qi
        p0, p1, q0, q1 = p1, pi, q1, qi


def get_inverse(a, m):
    if a == 0:
        return 0
    if euclid(a, m) != 1:
        raise ValueError('Не существует обратного элемента для a={} по модулю m={}'.format(a, m))
    d, x, y = eeuclid(a, m)
    assert d == 1
    return x % m


def ratio(p, q, m):
    return (p * get_inverse(q, m)) % m


# def dixon_modified(n, base):
#     h = len(base)
#
#     idx = 0
#     while True:
#         ps, alphas, es = [], [], []
#         while len(ps) < h + 1:
#             b = randint(isqrt(n), n)
#             a = pow(b, 2, n)
#             if a > n - a:
#                 a = -(n - a)
#             smooth, alpha, e = is_b_smooth(a, base)
#             if smooth:
#                 ps.append(b)
#                 alphas.append(alpha)
#                 es.append(e)
#
#         p = check_bi(n, base, ps, alphas, es)
#         if p != -1:
#             return p
#
#         idx += 1
#         if idx % MAX_ITERATIONS_DIXON == 0:
#             ans = input('Прошло {} итераций алгоритма. Продолжать? (y/n) '.format(idx))
#             if ans.lower() != 'y':
#                 return -1
#
#
# def dixon_usual(n, base):
#     h = len(base)
#
#     idx = 0
#     while True:
#         ps, alphas, es = [], [], []
#
#         while len(ps) < h + 1:
#             b = randint(isqrt(n), n)
#             if b in ps:
#                 continue
#             a = pow(b, 2, n)
#             smooth, alpha, e = is_b_smooth(a, base)
#             if smooth:
#                 ps.append(b)
#                 alphas.append(alpha)
#                 es.append(e)
#
#         p = check_bi(n, base, ps, alphas, es)
#         if p != -1:
#             return p
#
#         idx += 1
#         if idx % MAX_ITERATIONS_DIXON == 0:
#             ans = input('Прошло {} итераций алгоритма. Продолжать? (y/n) '.format(idx))
#             if ans.lower() != 'y':
#                 return -1