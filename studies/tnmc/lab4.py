from math import sqrt, log10, gcd
from random import randint


def miller_rabin(p, k):
    s = p - 1
    m = 0
    while s % 2 == 0:
        s //= 2
        m += 1
    i = 0
    while i <= k:
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


def poly(coef, x):
    ans = 0
    for n, c in enumerate(coef):
        ans += c*x**n
    return ans


def p_pollard(n, f, eps):
    T = int(sqrt(2 * sqrt(n) * log10(1 / eps))) + 1
    x = list()
    a = randint(1, n)
    i = 0
    while i < T:
        a = poly(f, a) % n
        x.append(a)
        for k in range(i):
            d = gcd((x[i] - x[k]) % n, n)
            if 1 < d < n:
                return d
            elif d == n:
                return None
            elif d == 1:
                continue
        i += 1


def p1_pollard(n):
    p = []
    x = 2
    while len(p) < 3 and x < n:
        if x < 4 or (x % 2 != 0 and miller_rabin(x, 5)):
            p.append(x)
        x += 1
    from random import randint
    a = randint(2, n - 2)
    from math import gcd
    d = gcd(a, n)
    if d >= 2:
        return d
    for i in range(len(p)):
        from math import log
        l = int(log(n) / log(p[i]))
        a = pow(a, p[i] ** l, n)
    d = gcd(a - 1, n)
    if d == 1 or d == n:
        return None
    else:
        return d


def main():
    print("Число n = ", end='')
    n = int(input())
    if n < 0 or miller_rabin(n, 5):
        print("Введено неправильное значение числа n")
        exit()
    eps = float(input("Введите значение eps\n"))
    if eps < 0 or eps > 1:
        print("Введено неправильное значение eps\n")
    print("Функция f, задаваемая коэффициентами = ", end='')
    f = list(map(int, input().split()))

    f.reverse()
    p = p_pollard(n, f, eps)

    if p is not None:
        print("Нетривиальный делитель p = {}".format(str(p)))
    else:
        print("Делитель не найден")

    p = p1_pollard(n)

    if p is not None:
        print("Нетривиальный делитель p = {} числа n = {}".format(str(p), str(n)))
    else:
        print("Делитель не найден")


if __name__ == '__main__':
    main()
