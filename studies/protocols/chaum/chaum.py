from itertools import chain
from json import dump, load
from math import gcd
from random import getrandbits, randint, randrange
from sympy import isprime, factorint


first_primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]


def n_bit_random(n):
    return randrange(2**(n-1)+1, 2**n - 1)


def get_low_level_prime(n):
    while True:
        pc = n_bit_random(n)
        for divisor in first_primes_list:
            if pc % divisor == 0 and divisor**2 <= pc:
                break
        else:
            return pc


# def is_miller_rabin_passed(mrc):
#     maxDivisionsByTwo = 0
#     ec = mrc-1
#     while ec % 2 == 0:
#         ec >>= 1
#         maxDivisionsByTwo += 1
#     assert(2**maxDivisionsByTwo * ec == mrc-1)

#     def trialComposite(round_tester):
#         if pow(round_tester, ec, mrc) == 1:
#             return False
#         for i in range(maxDivisionsByTwo):
#             if pow(round_tester, 2**i * ec, mrc) == mrc-1:
#                 return False
#         return True

#     # Set number of trials here
#     numberOfRabinTrials = 20
#     for i in range(numberOfRabinTrials):
#         round_tester = randrange(2, mrc)
#         if trialComposite(round_tester):
#             return False
#     return True


# def get_primitive_root(p):
#     phi = p-1
#     fact = factorint(phi)
#     # print(fact)
#     fact_l = [[k]*v for k, v in fact.items()]
#     fact_l = list(chain(*fact_l))
#     # print(fact_l)

#     for res in range(2, p+1):
#         ok = True
#         i = 0
#         while i < len(fact_l) and ok:
#             ok &= pow(res, phi // fact_l[i], p) != 1
#             i += 1
#         if ok:
#             return res
#     return None


def check_element_is_primitive(element, p, q):
    return not pow(element, (p - 1) // q, p) == 1 and not pow(element, (p - 1) // 2, p) == 1


def get_g(p, q):
    g = randint(1, p - 1)
    while not check_element_is_primitive(g, p, q):
        g = randint(1, p - 1)
    return g


def gen_shared_params():
    l = int(input('Длина числа p: '))
    q = get_low_level_prime(l // 2)
    k = 0
    p = (2**k) * q + 1
    while True:
        if isprime(p):
            break
        k += 1
        p = (2**k) * q + 1
    g = get_g(p, q)
    print(f'p = {p}, g = {g}')
    with open('chaum_parameters/p.json', 'w', encoding='utf-8') as pw:
        dump({'p': p}, pw, indent=4)
    with open('chaum_parameters/g.json', 'w', encoding='utf-8') as gw:
        dump({'g': g}, gw, indent=4)


def gen_private_params():
    # l = int(input('Длина числа x: '))
    with open('chaum_parameters/p.json', 'r', encoding='utf-8') as pr:
        p = load(pr)['p']
    with open('chaum_parameters/g.json', 'r', encoding='utf-8') as gr:
        g = load(gr)['g']

    x = randint(2, p-1)
    while True:
        if gcd(x, p-1) == 1:
            break
        x = randint(2, p-1)
    y = pow(g, x, p)
    print(f'x = {x}, y = {y}')
    with open('chaum_parameters/public_key.json', 'w', encoding='utf-8') as pubw:
        dump({'p': p, 'g': g, 'y': y}, pubw, indent=4)
    with open('chaum_parameters/private_key.json', 'w', encoding='utf-8') as privw:
        dump({'x': x}, privw, indent=4)


def sign():
    with open('chaum_parameters/to_sign.txt', 'r', encoding='utf-8') as tsr:
        # me = load(tsr)['message']
        me = tsr.read()
    m = hash(me)
    with open('chaum_parameters/p.json', 'r', encoding='utf-8') as pr:
        p = load(pr)['p']
    with open('chaum_parameters/private_key.json', 'r', encoding='utf-8') as privr:
        x = load(privr)['x']
    sign = pow(m, x, p)
    print(f'z = {sign}')
    with open('chaum_parameters/signed.txt', 'w', encoding='utf-8') as signedw:
        signedw.write(f'{sign}')
        # dump({'message': me, 'signature': sign}, signedw, indent=4)


def verify3():
    with open('chaum_parameters/signed.txt', 'r', encoding='utf-8') as signedr:
        data = signedr.read().split()
        z = int(data[-1])
        print(z)
    with open('chaum_parameters/public_key.json', 'r', encoding='utf-8') as pubr:
        data = load(pubr)
        p, g, y = data['p'], data['g'], data['y']
    a, b = randint(2, p-1), randint(2, p-1)
    print(f'a = {a}, b = {b}')
    with open('chaum_parameters/ab.json', 'w', encoding='utf-8') as abw:
        dump({'a': a, 'b': b}, abw, indent=4)
    c = (pow(z, a, p) * pow(y, b, p)) % p
    print(f'c = {c}')
    with open('chaum_parameters/c.json', 'w', encoding='utf-8') as cw:
        dump({'c': c}, cw, indent=4)


def verify4():
    with open('chaum_parameters/public_key.json', 'r', encoding='utf-8') as pubr:
        data = load(pubr)
        p, g, y = data['p'], data['g'], data['y']
    with open('chaum_parameters/private_key.json', 'r', encoding='utf-8') as privr:
        x = load(privr)['x']
    t = pow(x, -1, p-1)
    with open('chaum_parameters/t.json', 'w', encoding='utf-8') as tw:
        dump({'t': t}, tw, indent=4)
    with open('chaum_parameters/c.json', 'r', encoding='utf-8') as cr:
        c = int(load(cr)['c'])
    d = pow(c, t, p)
    with open('chaum_parameters/d.json', 'w', encoding='utf-8') as dw:
        dump({'d': d}, dw, indent=4)
    print(f't = {t}, d = {d}')


def verify5():
    with open('chaum_parameters/d.json', 'r', encoding='utf-8') as dr:
        d = int(load(dr)['d'])
    with open('chaum_parameters/public_key.json', 'r', encoding='utf-8') as pubr:
        data = load(pubr)
        p, g, y = data['p'], data['g'], data['y']
    with open('chaum_parameters/ab.json', 'r', encoding='utf-8') as abr:
        data = load(abr)
        a, b = data['a'], data['b']
    with open('chaum_parameters/to_sign.txt', 'r', encoding='utf-8') as tsr:
        m = hash(tsr.read())
    print('Подпись подлинная' if d == (pow(m, a, p)*pow(g, b, p)) %
          p else 'Подпись не подлинная')


def main():
    while True:
        opt = input(
            '0 - Генерация общих параметров\n1 - Генерация индивидуальных параметров\n2 - Генрация подписи\n3 - Проверка подписи (шаг 3)\n4 - Проверка подписи (шаг 4)\n5 - Проверка подписи (шаг 5)\n')
        if opt == '0':
            gen_shared_params()
        elif opt == '1':
            gen_private_params()
        elif opt == '2':
            sign()
        elif opt == '3':
            verify3()
        elif opt == '4':
            verify4()
        elif opt == '5':
            verify5()
        else:
            break


if __name__ == '__main__':
    main()
