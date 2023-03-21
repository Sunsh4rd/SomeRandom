from json import dump, load
from math import gcd
from random import getrandbits, randint

from sympy import isprime


def get_attributes_as_j():
    with open('gq_parameters/attributes.json', 'r', encoding='utf-8') as attr:
        attributes = ''.join(load(attr)['attributes'])
        return int.from_bytes(bytes(attributes.encode()), byteorder='big')


def key_gen():
    len_p = int(input('Длина числа p: '))
    len_q = int(input('Длина числа q: '))
    j = get_attributes_as_j()
    p, q = getrandbits(len_p), getrandbits(len_q)
    while True:
        if not isprime(p) or not isprime(q) or p == q:
            p, q = getrandbits(len_p), getrandbits(len_q)
        else:
            break
    print(f'Сгенерированные числа p = {p}, q = {q}')
    n = p * q
    print(f'n = p*q = {n}')
    phi = (p-1) * (q-1)
    print(f'phi(n) = {phi}')
    e = randint(0, phi-1)
    while not gcd(e, phi) == 1:
        e = randint(0, phi-1)
    print(f'e = {e}')
    s = pow(e, -1, phi)
    print(f's = {s}')
    x = pow(j, -s, n)
    print(f'x = {x}')
    y = pow(x, e, n)
    print(f'y = {y}')
    with open('gq_parameters/public_key.json', 'w', encoding='utf-8') as pubk:
        dump({'n': n, 'e': e, 'y': y}, pubk, indent=4)
    with open('gq_parameters/x.json', 'w', encoding='utf-8') as privk:
        dump({'x': x}, privk, indent=4)
    return


def step1():
    with open('gq_parameters/public_key.json', 'r', encoding='utf-8') as pubk:
        data = load(pubk)
        n, e = data['n'], data['e']
    r = randint(2, n-2)
    print(f'r = {r}')
    with open('gq_parameters/r.json', 'w', encoding='utf-8') as rw:
        dump({'r': r}, rw, indent=4)
    a = pow(r, e, n)
    print(f'a = {a}')
    with open('gq_parameters/a.json', 'w', encoding='utf-8') as aw:
        dump({'a': a}, aw, indent=4)
    return


def step2():
    with open('gq_parameters/public_key.json', 'r', encoding='utf-8') as pubk:
        data = load(pubk)
        e = data['e']
    c = randint(1, e-2)
    print(f'c = {c}')
    with open('gq_parameters/c.json', 'w', encoding='utf-8') as cw:
        dump({'c': c}, cw, indent=4)
    return


def step3():
    with open('gq_parameters/public_key.json', 'r', encoding='utf-8') as pubk:
        data = load(pubk)
        n = data['n']
    with open('gq_parameters/r.json', 'r', encoding='utf-8') as rr:
        data = load(rr)
        r = data['r']
    with open('gq_parameters/c.json', 'r', encoding='utf-8') as cr:
        data = load(cr)
        c = data['c']
    with open('gq_parameters/x.json', 'r', encoding='utf-8') as xr:
        data = load(xr)
        x = data['x']
    z = (r % n * pow(x, c, n)) % n
    print(f'z = {z}')
    with open('gq_parameters/z.json', 'w', encoding='utf-8') as zw:
        dump({'z': z}, zw, indent=4)
    return


def step4():
    with open('gq_parameters/public_key.json', 'r', encoding='utf-8') as pubk:
        data = load(pubk)
        n, e, y = data['n'], data['e'], data['y']
    with open('gq_parameters/z.json', 'r', encoding='utf-8') as zr:
        data = load(zr)
        z = data['z']
    with open('gq_parameters/a.json', 'r', encoding='utf-8') as ar:
        data = load(ar)
        a = data['a']
    with open('gq_parameters/c.json', 'r', encoding='utf-8') as cr:
        data = load(cr)
        c = data['c']
    print('Подлинность подтверждена' if pow(z, e, n) == (a % n * pow(y, c, n)) % n else 'Подлинность не подтверждена')
    return


def main():
    while True:
        opt = input(
            'Выберите действие:\n0 - Генерация ключей\n1 - Шаг 1\n2 - Шаг 2\n3 - Шаг 3\n4 - Шаг 4\n5 - Выход:\n')
        if opt == '0':
            key_gen()
        elif opt == '1':
            step1()
        elif opt == '2':
            step2()
        elif opt == '3':
            step3()
        elif opt == '4':
            step4()
        elif opt == '5':
            break
        else:
            print('Ошибка, повторите ввод')
    # j = get_attributes_as_j()
    # print(j)
    # n, e, y, x = key_gen()
    # r = randint(2, n-2)
    # a = pow(r, e, n)
    # c = randint(1, e-2)
    # z = (r % n * pow(x, c, n)) % n
    # print(pow(z, e, n) == (a % n * pow(y, c, n)) % n)


if __name__ == '__main__':
    main()
