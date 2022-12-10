import math
import random
import pyprimes

def MR(p, k):
    s = p - 1
    m = 0
    while s % 2 == 0:
        s //= 2
        m += 1
    i = 0
    while i <= k:
        a = random.randint(2, p - 2)
        from math import gcd
        while gcd(a, p) != 1:
            a = random.randint(2, p - 2)
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

def gen_primes(c):
    primes = []
    n = 2
    while len(primes) < c:
        if pyprimes.miller_rabin(n, math.ceil(math.log2(n))):
            primes.append(n)
            n += 1
        else:
            n += 1
    return primes

def p_1_pollard_method(n, s):
    base = gen_primes(s)
    a = random.randint(2, n - 2)
    if (s == 1):
        print("Делитель не найден.")
        exit(0)
    from math import gcd
    d = gcd(a, n)
    if d >= 2:
        print("Нетривиальный делитель p = {} числа n".format(str(d), str(n)))
        exit(0)
    for i in range(len(base)):
        l = int(math.log(n) // math.log(base[i]))
        a = pow(a, pow(base[i], l), n)
    d = gcd(a - 1, n)
    if d == 1 or d == n:
        p_1_pollard_method(n, s)
        print("Нетривиальный делитель p = {} числа n".format(str(d), str(n)))
    else:
        print("Делитель не найден.")
        exit(0)

def main():
    n = int(input("Введите число n: "))
    if MR(n, math.ceil(math.log2(n))):
        print("Число - простое!")
        exit(0)
    s = int(input("Введите число B: "))
    p_1_pollard_method(n, s)

if __name__ == '__main__':
    main()
