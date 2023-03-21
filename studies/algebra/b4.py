import math
import numpy as np


def fermat_f(n):
    if(n & 1) == 0:
        return n // 2, 2

    a = math.ceil(math.sqrt(n))

    if(a * a == n):
        return a, a

    while True:
        b1 = a * a - n
        b = int(math.sqrt(b1))
        if(b * b == b1):
            break
        else:
            a += 1

    return a-b, a+b


print(fermat_f(57251))
print(fermat_f(16545))


def dixon(n):
    base = [2, 3, 5, 7]
    start = int(math.sqrt(n))
    pairs = []

    for i in range(start, n):
        for j in range(len(base)):
            lhs = i**2 % n
            rhs = base[j]**2 % n
            if lhs == rhs:
                pairs.append([i, base[j]])
    new = []

    for i in range(len(pairs)):
        x = pairs[i][0]
        y = pairs[i][1]
        if (x % n != y % n) and (x % n != -y % n):
            u = math.gcd(x + y, n)
            v = math.gcd(x - y, n)
            new.append((u, v))

    return new[0]


print(dixon(16545))
