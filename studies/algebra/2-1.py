from functools import reduce
import math
import random


def fact(n):
    acc = 1
    for i in range(1, n + 1):
        acc *= i
    return acc


def wilson(p):
    return (fact(p-1) + 1) % p == 0


def eratosphen(n):
    a = []
    for i in range(n + 1):
        a.append(i)
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    a = set(a)
    a.remove(0)
    a = list(a)
    return a


def factor(n):
    l = eratosphen(n)
    k = n
    pr = []
    while l.count(k) == 0:
        for x in l:
            if k % x == 0:
                pr.append(x)
                k = k/x
                break
    pr.append(int(k))
    return pr


def legendre(a, p):
    if p < 2:
        raise ValueError('p must not be < 2')
    if (a == 0) or (a == 1):
        return a
    if a % 2 == 0:
        r = legendre(a / 2, p)
        if int(p * p - 1) & 8 != 0:
            r *= -1
    else:
        r = legendre(p % a, a)
        if int((a - 1) * (p - 1)) & 4 != 0:
            r *= -1
    return r


def fermat(n):
    a = factor(n-1)
    test = [pow(ai, n-1) % n == 1 % n for ai in a]
    return reduce(lambda x, y: x & y, test)


def carmichael(p):
    if fermat(p):
        pr = factor(p)
        for x in pr:
            if pr.count(x) > 1:
                print(p, ' is Prime number')
                return ''
        if len(pr) <= 1:
            print(p, ' is Prime number')
        else:
            print(p, ' is Carmichael number')
    else:
        print(p, ' is Composite number')


def solovay_strassen(n, k):
    if n % 2 == 0:
        print(n, ' is Composite number')
        return ''
    for i in range(1, k+1):
        random.seed()
        a = random.randint(2, n-1)
        if math.gcd(a, n) > 1:
            print(n, ' is Composite number')
            return ''
        if ((a ** ((n-1)//2))) % n != legendre(a, n) % n:
            print(n, ' is Composite number')
            return ''
    print(n, ' is likely a Prime number')
    return ''


def miller_rabin(n, k):
    if n == 3:
        print(n, ' is Prime number')
    if n % 2 == 0:
        print(n, ' is Composite number')
        return ''
    s = 0
    t = n-1
    while t % 2 != 0:
        s += 1
        t = t//2
    i = 0
    f = 0
    while i < k:
        random.seed()
        a = random.randint(2, n-1)
        x = (a**t) % n
        if x == 1 or x == n-1:
            i += 1
            continue
        for j in range(0, s-1):
            x = (x**2) % n
            if x == 1:
                print(n, ' is Composite number')
            if x == n-1:
                i += 1
                break
        f = 1
    if f != 1:
        print(n, ' is likely a Prime number')
    else:
        print(n, ' is Composite number')


c = [0] * 10000


def coef(n):
    c[0] = 1
    for i in range(n):
        c[1 + i] = 1
        for j in range(i, 0, -1):
            c[j] = c[j - 1] - c[j]
        c[0] = -c[0]


def aks(n):
    coef(n)
    c[0] = c[0] + 1
    c[n] = c[n] - 1

    i = n
    while (i > -1 and c[i] % n == 0):
        i = i - 1

    return True if i < 0 else False


def main():
    print(wilson(561))
    print(fermat(561))
    carmichael(41041)
    solovay_strassen(41047, 50)
    miller_rabin(41047, 50)
    print(aks(561))


if __name__ == '__main__':
    main()
