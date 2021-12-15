from numba import jit
import math

@jit
def mersenne(p):
    return 2**p - 1


@jit
def lucas(m, p):
    k = 1
    s = 4
    while k != p-1:
        s = (s*s - 2) % m
        k += 1

    return s == 0


print(mersenne(3), lucas(mersenne(3), 3))
print(mersenne(5), lucas(mersenne(5), 5))
print(mersenne(7), lucas(mersenne(7), 7))
print(mersenne(13), lucas(mersenne(13), 13))
print(mersenne(17), lucas(mersenne(17), 17))
print(mersenne(19), lucas(mersenne(19), 19))
print(mersenne(31), lucas(mersenne(31), 31))


@jit
def factor(n):
    i = 2
    factor = []
    while i * i <= n:
        while n % i == 0:
            factor.append(i)
            n = n / i
        i = i + 1
    if n > 1:
        factor.append(n)
    return factor


@jit
def pocklington(a, n, q):
    return (a**n-1) % n == 1 and math.gcd(n, a**((n-1)/q) - 1 ) == 1

a = 100
ks = [3,5,7,13,17,19,31]
for k in ks:
    n = mersenne(k)
    f = factor(n - 1)
    q = f[-1]
    if q > math.sqrt(n) - 1 and a > 1:
        while not pocklington(a, n, q):
            a -= 1
    print(n, a)
