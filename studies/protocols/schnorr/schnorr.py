import random
from sympy import isprime
import json


def get_random_prime(n):
    while True:
        number = random.getrandbits(n)
        if isprime(number):
            return number


def fast_mod_exp(a, b, m):
    r = 1
    while b > 0:
        if b & 1:
            r *= a
            r %= m
        a *= a
        a %= m
        b >>= 1
    return r


def logarithm(q, p):
    while True:
        for a in range(2, p):
            if fast_mod_exp(a, q, p) == 1:
                return a


def gen_shared_parameters(n):
    q = get_random_prime(n)
    k = 0
    p = (2**k) * q + 1
    while True:
        if isprime(p):
            break
        k += 1
        p = (2**k) * q + 1

    a = logarithm(q, p)

    return p, q, a


def main():

    while True:
        opt = input('''Выберите шаг протокола:
0 - Генерация общих параметров
1 - Генерация закрытого и открытого ключа Пегги(доказывабщая сторона)
2 - Пегги(доказывающая сторона) вычисляет х
3 - Пегги(доказывающая сторона) посылает х Виктору(проверяющая сторона)
4 - Виктор(проверяющая сторона) посылает Пегги(доказывающая сторона) случайное число 0 < e < 2^(t-1)
5 - Пегги(доказывающая сторона) вычисляет y = (r + se) mod q и отправляет y Виктору(проверяющая сторона)
6 - Виктор(проверяющая сторона) проверяет x = a^y*v^e mod p
7 - Выход
''')

        match opt:
            case '0':
                n = int(input('Длина числа p: '))
                with open('schnorr_parameters/shared_parameters.json', 'w') as sp:
                    p, q, a = gen_shared_parameters(n)
                    json.dump({
                        'p': p,
                        'q': q,
                        'a': a
                    }, sp, indent=4)

            case '1':
                with open('schnorr_parameters/shared_parameters.json', 'r') as sp:
                    shared = json.load(sp)
                    p, q, a = shared['p'], shared['q'], shared['a']
                    s = random.randint(1, q-1)
                    v = pow(a, -s, p)
                with open('schnorr_parameters/peggy_pub_key.json', 'w') as pub:
                    json.dump({
                        'v': v
                    }, pub, indent=4)
                with open('schnorr_parameters/peggy_priv_key.json', 'w') as priv:
                    json.dump({
                        's': s,
                    }, priv, indent=4)

            case '2':
                with open('schnorr_parameters/shared_parameters.json', 'r') as sp:
                    shared = json.load(sp)
                    p, q, a = shared['p'], shared['q'], shared['a']
                    r = random.randint(1, q-1)
                    with open('schnorr_parameters/peggy_round_parameters.json', 'w') as rp:
                        json.dump({
                            'r': r
                        }, rp, indent=4)
                    x = pow(a, r, p)
                    with open('schnorr_parameters/peggy_to_victor2.json', 'w') as pv2:
                        json.dump({
                            'x': x
                        }, pv2, indent=4)

            case '3':
                print('P -> V: x')

            case '4':
                with open('schnorr_parameters/victor_to_peggy3.json', 'w') as vp3:
                    t = int(input('Длина t: '))
                    e = random.randint(0, 2**(t-1))
                    json.dump({
                        'e': e
                    }, vp3, indent=4)

            case '5':
                with open('schnorr_parameters/peggy_priv_key.json', 'r') as priv:
                    s = json.load(priv)['s']

                    with open('schnorr_parameters/shared_parameters.json', 'r') as py:
                        q = json.load(py)['q']
                    with open('schnorr_parameters/victor_to_peggy3.json', 'r') as vp3:
                        e = json.load(vp3)['e']
                    with open('schnorr_parameters/peggy_round_parameters.json', 'r') as r:
                        r = json.load(r)['r']
                        y = (r + s*e) % q
                        with open('schnorr_parameters/peggy_to_victor.json', 'w') as pv4:
                            json.dump({
                                'y': y
                            }, pv4, indent=4)

            case '6':
                with open('schnorr_parameters/shared_parameters.json', 'r') as sp:
                    shared = json.load(sp)
                    a, p = shared['a'], shared['p']
                    with open('schnorr_parameters/peggy_to_victor.json', 'r') as pv4:
                        y = json.load(pv4)['y']
                    with open('schnorr_parameters/peggy_pub_key.json', 'r') as pub:
                        v = json.load(pub)['v']
                    with open('schnorr_parameters/victor_to_peggy3.json', 'r') as vp3:
                        e = json.load(vp3)['e']
                    with open('schnorr_parameters/peggy_to_victor2.json', 'r') as pv2:
                        x = json.load(pv2)['x']
                        if x == (pow(a, y, p) * pow(v, e, p)) % p:
                            print('Аутентификация пройдена')
                        else:
                            print('Аутентификация не пройдена')

            case '7':
                break

            case _:
                print('Ошибка, попробуйте другой вариант!')


if __name__ == '__main__':
    main()


# p = 2^k * q + 1
