from json import dump, load
from math import gcd
from random import getrandbits, randint
from sympy import isprime, factorint


def get_primitive_root(p):
    # fact = []
    # phi = p-1
    # n = phi
    # for i in range(2, int(n**0.5)+1):
    #     if n % i == 0:
    #         fact.append(i)
    #         while n % i == 0:
    #             n //= i

    # if n > 1:
    #     fact.append(n)
    phi = p-1
    fact = factorint(phi)
    print(fact)
    fact_l = [[k]*v for k,v in fact.items()]
    print(fact_l)
    
    for res in range(2, p+1):
        ok = True
        i = 0
        while i < len(fact) and ok:
            ok &= pow(res, phi // fact[i], p) != 1
            i += 1
        if ok:
            return res
    return None


def gen_shared_params():
    l = int(input('Длина числа p: '))
    pi = getrandbits(l)
    p = pi
    k = 0
    while True:
        if isprime(p):
            break
        k += 1
        # q = get_random_prime(16)
        p = (2**k) * pi + 1
    print(p)
    g = get_primitive_root(p)
    print(f'p = {p}, g = {g}')
    with open('chaum_parameters/p.json', 'w', encoding='utf-8') as pw:
        dump({'p': p}, pw, indent=4)
    with open('chaum_parameters/g.json', 'w', encoding='utf-8') as gw:
        dump({'g': g}, gw, indent=4)


def gen_private_params():
    l = int(input('Длина числа x: '))
    x = getrandbits(l)
    with open('chaum_parameters/p.json', 'r', encoding='utf-8') as pr:
        p = load(pr)['p']
    with open('chaum_parameters/g.json', 'r', encoding='utf-8') as gr:
        g = load(gr)['g']
    while True:
        if gcd(x, p-1) == 1:
            break
        x = getrandbits(l)
    y = pow(g, x, p)
    print(f'x = {x}, y = {y}')
    with open('chaum_parameters/public_key.json', 'w', encoding='utf-8') as pubw:
        dump({'p': p, 'g': g, 'y': y}, pubw, indent=4)
    with open('chaum_parameters/private_key.json', 'w', encoding='utf-8') as privw:
        dump({'x': x}, privw, indent=4)


def sign():
    with open('chaum_parameters/to_sign.json', 'r', encoding='utf-8') as tsr:
        me = load(tsr)['message']
    m = hash(me)
    with open('chaum_parameters/p.json', 'r', encoding='utf-8') as pr:
        p = load(pr)['p']
    with open('chaum_parameters/private_key.json', 'r', encoding='utf-8') as privr:
        x = load(privr)['x']
    sign = pow(m, x, p)
    print(f'z = {sign}')
    with open('chaum_parameters/signed.json', 'w', encoding='utf-8') as signedw:
        dump({'message': me, 'signature': sign}, signedw, indent=4)


def verify():
    with open('chaum_parameters/signed.json', 'r', encoding='utf-8') as signedr:
        data = load(signedr)
        m, z = hash(data['message']), data['signature']
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
    with open('chaum_parameters/private_key.json', 'r', encoding='utf-8') as privr:
        x = load(privr)['x']
    t = pow(x, -1, p-1)
    with open('chaum_parameters/t.json', 'w', encoding='utf-8') as tw:
        dump({'t': t}, tw, indent=4)
    d = pow(c, t, p)
    with open('chaum_parameters/d.json', 'w', encoding='utf-8') as dw:
        dump({'d': d}, dw, indent=4)
    print(f't = {t}, d = {d}')
    print('Подпись подлинная' if d % p == (pow(m, a, p)*pow(g, b, p)) %
          p else 'Подпись не подлинная')


def main():
    while True:
        opt = input(
            '0 - Генерация общих параметров\n1 - Генерация индивидуальных параметров\n2 - Генрация подписи\n3 - Проверка подписи\n')
        if opt == '0':
            gen_shared_params()
        elif opt == '1':
            gen_private_params()
        elif opt == '2':
            sign()
        elif opt == '3':
            verify()
        else:
            break


if __name__ == '__main__':
    main()
