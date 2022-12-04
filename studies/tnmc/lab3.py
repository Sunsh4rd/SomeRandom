from math import gcd, log2
from random import randint


# def euclid_extended(a, b):
#     if a == 0:
#         return b, 0, 1
#     gcd, x1, y1 = euclid_extended(b % a, a)
#     x = y1 - (b // a) * x1
#     y = x1
#     return gcd, x, y


# def jacobi(a, n):
#     if (euclid_extended(a, n)[0] != 1):
#         return 0
#     if (a < 0):
#         return jacobi(-a, n) * -1 ** ((n - 1) // 2)
#     if a % 2 == 0:
#         return jacobi(a // 2, n) * (-1) ** ((n ** 2 - 1) // 8)
#     if a == 1:
#         return 1
#     if (a < n):
#         return jacobi(n, a) * (-1) ** ((a - 1) * ((n - 1) // 4))
#     return jacobi(a % n, n)


# def fermat(n):
#     a = randint(2, n - 2)
#     r = pow(a, (n-1), n)
#     if r == 1:
#         return 'Вероятно простое'
#     else:
#         return 'Составное'


# def solovay_strassen(n):
#     a = randint(2, n - 2)
#     r = pow(a, (n-1) // 2, n)
#     if r != 1 and r != n-1:
#         return 'Составное'
#     s = jacobi(a, n)
#     if r % n == s % n:
#         return 'Вероятно простое'
#     else:
#         return 'Составное'


# def miller_rabin(n, k):
#     s = 0
#     n_test = n - 1
#     while(n_test % 2 == 0):
#         s += 1
#         n_test //= 2
#     r = n_test
#     print(r)
#     i = 0
#     while True:
#         if i > k:
#             return 'Вероятно простое'
#         while True:
#             a = randint(2, n - 2)
#             if gcd(a, n) == 1:
#                 break
#         y = pow(a, r, n)
#         if y == 1:
#             continue
#         if y == n-1:
#             i += 1
#             continue
#         for l in range(1, s):
#             c = pow(a, r*2**l, n)
#             if c != n-1:
#                 return 'Составное'
#             else:
#                 break

#         else:
#             i+=1
#             continue

# j = 1
# if y != 1 and y != n - 1:
#     while j <= s - 1 and y != n - 1:
#         y = pow(y, 2, n)
#         if y == 1:
#             return 'Составное'
#         j += 1
# if y != n - 1:
#     return 'Составное'
# return 'Веротяно простое'


import time
from math import gcd, log
from random import randrange


def timer(f):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        ans = f(*args, **kwargs)
        end = time.perf_counter()
        print(f'Time: {(end - start) * 1000:.3f}ms')
        return ans
    return wrapper


def hlp_Ferma(a, n):
    ans = 1
    for i in range(1, n):
        ans = (ans * a) % n
    ans = (ans - 1) % n
    return ans


# @timer
def fermat(n, k):
    for i in range(k):
        a = randrange(n - 2) + 2
        if gcd(a, n) > 1:
            return 0
        tmp = hlp_Ferma(a, n)
        if tmp != 0:
            return 0
    return 1


def hlp(base, e, n):
    x, y = 1, base
    while e:
        if e % 2:
            x = (x * y) % n
        y = (y * y) % n
        e = e // 2
    return x % n


def Jacobi(a, n):
    if gcd(a, n) != 1:
        return 0
    t = 1
    a %= n
    while a:
        while not a % 2:
            a //= 2
            if n % 8 == 3 or n % 8 == 5:
                t = -t
        n, a = a, n
        if a % 4 == 3 and n % 4 == 3:
            t = -t
        a %= n
    if n == 1:
        return t


def solovay_strassen(n, k):
    if n < 2:
        return False
    if n != 2 and n % 2 == 0:
        return False

    for i in range(k):
        a = randrange(n - 1) + 1
        jacobian = (n + Jacobi(a, n)) % n
        mod = hlp(a, (n - 1) / 2, n)

        if jacobian == 0 or mod != jacobian:
            return False
    return True


def miller_rabin(n):
    if n == 2 or n == 3:
        return 1
    if not n % 2 and n == 1:
        return 0
    s, t, x = 0, n - 1, 0
    r1, r2 = 2, n - 2
    a, r = int(log(n, 2)), int(log(n, 2))

    while t and not t % 2:
        s += 1
        t /= 2

    for i in range(r):
        a = r1 + randrange(r2 - r1)
        x, j = 1, 1

        while j <= t:
            x = (x * a) % n
            j += 1

        if x == 1 or x == n - 1:
            continue

        for j in range(s - 1):
            x = (x * x) % n
            if x == 1:
                return 0
            if x == n - 1:
                break
        if x == n - 1:
            continue
        return 0
    return 1


def main():
    opt = input(
        '0 - Провека тестом Ферма\n1 - Проверка тестом Соловея-Штрассена\n2 - Проверка тестом Миллера-Рабина\n')
    n = int(input('Число для проверки = '))
    if opt == '0':
        r = fermat(n, 100)
        if r == 0:
            print('Результат проверки тестом Ферма: Составное')
        else:
            print('Результат проверки тестом Ферма: Вероятно простое')
    elif opt == '1':
        r = solovay_strassen(n, 100)
        if not r:
            print('Результат проверки тестом Соловея-Штрассена: Составное')
        else:
            print('Результат проверки тестом Соловея-Штрассена: Вероятно простое')
    elif opt == '2':
        r = miller_rabin(n)
        if not r:
            print('Результат проверки тестом Миллера-Рабина: Составное')
        else:
            print('Результат проверки тестом Миллера-Рабина: Вероятно простое')


if __name__ == '__main__':
    main()
