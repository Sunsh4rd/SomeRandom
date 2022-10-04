import random
from math import gcd


def ext_euclid(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return y0


def miller_rabin(p, k):
    s = p - 1
    m = 0
    while s % 2 == 0:
        s //= 2
        m += 1
    i = 0
    while i <= k:
        from random import randint
        a = randint(2, p - 2)
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


def root(n, p):
    n %= p

    s = p - 1
    r = 0

    while s % 2 == 0:
        s //= 2
        r += 1

    l = pow(n, s, p)
    w = pow(n, (s + 1) // 2, p)

    mod = l
    m = 0
    while mod != 1:
        mod = pow(mod, 2, p)
        m += 1

    z = 2
    while legendre_symb(z, p) != -1:
        z += 1

    yd_l = pow(pow(z, s, p), pow(2, r - m), p)
    yd_w = pow(pow(z, s, p), pow(2, r - m - 1), p)

    while l != 1:
        l = l * yd_l % p
        w = w * yd_w % p

    return w


def tochki(p, A, Q, r):
    if r > pow(2, 15):
        return
    x = [None, None]
    xx = []
    yy = []
    xx.append(Q[0])
    yy.append(Q[1])
    with open('tochki.txt', 'w') as tochki:
        for i in range(r):
            x = slojenie(x, Q, A, p)
            tochki.write(str(x) + '\n')
            if x[0] is not None:
                xx.append(x[0])
                yy.append(x[1])
    import matplotlib.pyplot as plot
    plot.figure(figsize=(6, 6), facecolor='pink')
    plot.scatter(xx, yy, c='black')
    plot.show()


def ymnojenie(X, A, N, p):
    tocka = [None, None]
    x = [X[0], X[1]]
    binn = bin(N)[2:][::-1]
    for i in range(len(binn)):
        if binn[i] == '1':
            tocka = slojenie(tocka, x, A, p)
        x = slojenie(x, x, A, p)
    return [tocka[0], tocka[1]]


def slojenie(point1, point2, A, p):
    x1, y1 = point1
    x2, y2 = point2

    if [x1, y1] == [None, None]:
        return [x2, y2]

    if [x2, y2] == [None, None]:
        return [x1, y1]

    if x1 == x2 and y1 != y2 and pow(y1, 2, p) == pow(y2, 2, p):
        return [None, None]

    if x1 == x2:
        alpha = (3 * (pow(x1, 2, p)) + A) * ext_euclid(p, (2 * y1 % p)) % p
    else:
        alpha = ((y2 - y1) % p) * ext_euclid(p, (x2 - x1) % p) % p

    x3 = (-x1 - x2 + pow(alpha, 2, p)) % p
    y3 = (-y1 + alpha * (x1 - x3)) % p

    return [x3, y3]


def step6(X, A, N, p):
    x = ymnojenie(X, A, N, p)
    if x[0] is None and x[1] is None:
        return True
    return False


def step3(a, b, p):
    N = [p + 1 + 2 * a,
         p + 1 - 2 * a,
         p + 1 + 2 * b,
         p + 1 - 2 * b]

    i = 0

    r = None
    for i in range(len(N)):
        if N[i] % 2 == 0 and miller_rabin(N[i] // 2, 4):
            r = N[i] // 2
        if N[i] % 4 == 0 and miller_rabin(N[i] // 4, 4):
            r = N[i] // 4
        if r is not None:
            return N[i], r

    return None, None


def legendre_symb(D, p):
    Legendre = pow(D, (p - 1) // 2, p)
    if Legendre == p - 1:
        return -1
    elif Legendre == 0:
        return 0
    else:
        return 1


def alg753(D, p):

    while True:
        b = random(1, p-1)
        if legendre_symb(b * b - 4 * D) == 1:
            False


def alg781(D, p):

    Legendre = legendre_symb(-D, p)
    if Legendre == -1:
        return None, None

    u = root(-D, p)

    i = 0
    uu = []
    mm = []
    uu.append(u)
    mm.append(p)

    while True:
        mm.append(((uu[i] ** 2) + D) // mm[i])
        uu.append(min(uu[i] % mm[i + 1], (mm[i + 1] - uu[i]) % mm[i + 1]))
        if mm[i + 1] == 1:
            break
        i = i + 1

    aa = []
    bb = []
    for j in range(i):
        aa.append(0)
        bb.append(0)

    aa.append(uu[i])
    bb.append(1)

    while True:
        if i == 0:
            a = aa[i]
            b = bb[i]
            return a, b

        else:
            poloj = uu[i - 1] * aa[i] + D * bb[i]
            otr = -uu[i - 1] * aa[i] + D * bb[i]
            znamen = (aa[i] ** 2) + D * (bb[i] ** 2)

            if poloj % znamen == 0:
                aa[i - 1] = poloj // znamen
            else:
                aa[i - 1] = otr // znamen

            poloj = -aa[i] + uu[i - 1] * bb[i]
            znamen = -aa[i] - uu[i - 1] * bb[i]

            if poloj % znamen == 0:
                bb[i - 1] = poloj // znamen
            else:
                bb[i - 1] = otr // znamen
            i = i - 1


def genp(l):
    p = 4
    while p % 4 != 1 or not miller_rabin(p, 4):
        p = random.randint(2 ** (l - 1), 2 ** l - 1)
    return p


def steps1_4(l, m):
    while True:
        p = genp(l)
        D = 1

        a, b = alg781(D, p)

        if a is None or b is None:
            continue

        N, r = step3(a, b, p)

        if r is None or p == r:
            continue

        flag = False
        for i in range(1, m, +1):
            if pow(p, i, r) == 1:
                flag = True
                break
        if flag:
            continue

        break

    return p, N, r


def ellkrivaya(len_p, m):
    p, N, r = steps1_4(len_p, m)

    while True:
        x0 = random.randint(1, p - 1)
        y0 = random.randint(1, p - 1)

        A = ((y0 ** 2 - x0 ** 3) * ext_euclid(p, x0)) % p

        Legendre = legendre_symb(-A, p)
        if N == 2 * r:
            if Legendre != -1:
                continue
        elif N == 4 * r:
            if Legendre != 1:
                continue

        if not step6([x0, y0], A, N, p):
            continue

        Q = ymnojenie([x0, y0], A, N // r, p)

        break

    return p, A, Q, r


def main():

    while True:
        print("j = 1728")
        l = int(input("Введите длину l характеристики поля (длину p): "))
        if l < 6:
            print('Введенное значение l слишком мало. l<6')
        else:
            break
    m = int(input("Введите параметр безопасности m: "))
    p, A, Q, r = ellkrivaya(l, m)

    with open("ellkrivaya.txt", 'w') as result:
        result.write("j=1728" + '\n')
        result.write("y*y = x*x*x+a*x" + '\n')
        result.write("Длина l = " + str(l) + '\n')
        result.write("Параметр безопасности m = " + str(m) + '\n')
        result.write("Простое p = " + str(p) + '\n')
        result.write("Коэффициент A = " + str(A) + '\n')
        result.write("Точка Q = (" + str(Q[0]) + ", " + str(Q[1]) + ")" + '\n')
        result.write("r = " + str(r) + '\n')

    tochki(p, A, Q, r)


if __name__ == '__main__':
    main()
