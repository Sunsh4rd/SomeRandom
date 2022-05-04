import math
import random
from bigint import Bigint


def int_to_list_of_digits(x):
    return list(map(int, str(x)))[::-1]


def miller_rabin(n, k):
    if n == Bigint([3]):
        return True

    n1 = (n - Bigint([1]))[0]
    # print(n)
    q = n1
    t = None
    s = 0
    while True:
        q, r = divmod(q, Bigint([2]))
        # print(q, r)
        s += 1
        if divmod(q, Bigint([2]))[1] != Bigint([0]):
            t = q
            # print(t)
            break

    # print('s=', s)
    for _ in range(k):
        a = Bigint(int_to_list_of_digits(random.randint(2, int(str(n))-2)))
        # print(a, t, n)
        x = pow(a, t, n)
        # print(a, t, x)
        # print(type(x))
        if x == Bigint([1]) or x == n1:
            continue

        for _ in range(s-1):
            x = pow(x, Bigint([2]), n)
            if not isinstance(x, Bigint):
                x = Bigint(int_to_list_of_digits(x))
            if x == Bigint([1]):
                return False
            if x == n1:
                break

        if x != n1:
            return False

    return True


def gen_digits(k):
    halfk = k // 2
    x1, x2 = 1 << halfk-1, (1 << halfk) - 1
    # print('xs', x1, x2)
    it = 0
    while True:
        if it == x2-x1:
            print('Число не найдено')
            return None
        q = Bigint(int_to_list_of_digits(random.randint(x1, x2)))
        s = Bigint(int_to_list_of_digits(random.randint(x1, x2)))
        p = q*s + Bigint([1])
        # print('p', p, s, q)
        if divmod(q, Bigint([2]))[1] == Bigint([0]):
            # print('q even')
            continue
        if q == Bigint([1]):
            # print('q 1')
            continue
        if miller_rabin(q, int(math.log2(int(str(q))))) and divmod(s, Bigint([2]))[1] == Bigint([0]) and p < (Bigint([2])*q + Bigint([1])) * (Bigint([2])*q + Bigint([1])) and pow(Bigint([2]), q*s, p) == Bigint([1]) and pow(Bigint([2]), s, p) != Bigint([1]):
            # print(f'p = {p}, q = {q}, s = {s}')
            return p


def main():
    # print(miller_rabin(Bigint([3]), 2))
    k = int(input('k = '))
    print(gen_digits(k))


if __name__ == '__main__':
    main()
