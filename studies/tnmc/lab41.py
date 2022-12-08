from math import ceil, factorial, gcd, sqrt
from random import choice, randint


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


def factorize(n):
    factors = {}
    if n < 0:
        factors[-1] = 1
        n = abs(n)
    i = 2
    while i * i <= n:
        if n % i == 0:
            count = 0
            while n % i == 0:
                n //= i
                count += 1
            factors[i] = count
        i += 1
    if n > 1:
        factors[n] = 1
    return factors


def min_quad_residue(n, p):
    if abs(pow(p, 2, n)) < abs(pow(p, 2) - n * int(ceil(pow(p, 2) / n))):
        P_mod = pow(p, 2, n)
    else:
        P_mod = pow(p, 2) - n * int(ceil(pow(p, 2) / n))
    return P_mod


def get_factors(n, p, P_mods, D, all_factors):
    P_mod = min_quad_residue(n, p)
    P_mods.append(P_mod)
    factors = factorize(P_mod)

    for item in factors:
        if factors[item] % 2 == 0 and item not in D:
            D.append(item)
        else:
            if item not in all_factors.keys():
                all_factors[item] = 0
            all_factors[item] += 1
    return P_mods, D, all_factors


def get_vector(P_mods, D):
    e = {}
    for j in range(len(P_mods)):
        num = P_mods[j]
        cnt_div = []
        for div in D:
            if div == -1:
                if num >= 0:
                    cnt_div.append(0)
                else:
                    num //= div
                    cnt_div.append(1)
                continue
            count = 0
            while num % div == 0:
                num //= div
                count += 1
            cnt_div.append(count)
        if num == 1:
            e[j] = cnt_div
        j += 1
    return e


def init(e):
    all_keys = sorted(e.keys())
    len_e = len(e.keys())
    len_vec = {}
    all_cnt = [0]
    for i in range(1, len_e + 1):
        cnt = factorial(len_e) // (factorial(i) * factorial(len_e - i))
        all_cnt.append(cnt)
        len_vec[i] = []
    return all_cnt, len_vec, all_keys, 1


def generate_K(e, len_e, len_d, all_keys, all_cnt, len_vec):
    null_vector = [0] * len_e
    while True:
        if len(len_vec[len_e]) == all_cnt[len_e]:
            return None, len_vec
        vector = []
        while len(vector) != len_e:
            key = choice(all_keys)
            if key not in vector:
                vector.append(key)
        if sorted(vector) in len_vec[len_e]:
            continue
        len_vec[len_e].append(sorted(vector))
        res_vector = [0] * len_d
        for key_e in sorted(vector):
            for j in range(len(e[key_e])):
                res_vector[j] = (res_vector[j] + e[key_e][j]) % 2
        if res_vector == null_vector:
            return sorted(vector), len_vec


def continued_fraction(n):
    P_1 = 1
    P = [int(sqrt(n))]
    a = [int(sqrt(n))]
    x = [sqrt(n) - a[0]]
    P_mods = []
    D = [-1]
    all_factors = {}

    P_mods, D, all_factors = get_factors(n, P[0], P_mods, D, all_factors)

    i = 1

    while True:
        a.append(int(1 / x[i - 1]))
        x.append(1 / x[i - 1] - a[i])
        if i - 2 < 0:
            P.append((a[i] * P[i - 1] + P_1) % n)
        else:
            P.append((a[i] * P[i - 1] + P[i - 2]) % n)

        P_mods, D, all_factors = get_factors(n, P[i], P_mods, D, all_factors)

        if i >= 2:
            for item in all_factors:
                if all_factors[item] >= 2 and item not in D:
                    D.append(item)

            D.sort()

            e = get_vector(P_mods, D)

            all_cnt, len_vec, all_keys, len_e = init(e)

            while len_e <= len(all_keys):
                K, len_vec = generate_K(e, len_e, len(
                    D), all_keys, all_cnt, len_vec)

                if K is None:
                    len_e += 1
                    continue

                s = 1
                for k in K:
                    s = (s * P[k]) % n
                t = 1
                for j in range(len(D)):
                    y = 0
                    for k in K:
                        y += e[k][j]
                    y //= 2
                    t = (t * pow(D[j], y)) % n

                q = gcd(s - t, n)
                if q != n and q != 1:
                    return q

        i += 1


def main():
    print("Число n = ", end='')
    n = int(input())

    if n < 0 or miller_rabin(n, 5):
        print("Введено неправильное значение числа n")
        exit()

    sqrt_n = int(sqrt(n))
    if pow(sqrt_n, 2) == n:
        print("Введено неправильное значение числа n")
        exit()
    p = continued_fraction(n)
    if p is not None:
        print("Нетривиальный делитель p = {}".format(str(p)))
    else:
        print("Делитель не найден")


if __name__ == '__main__':
    main()
