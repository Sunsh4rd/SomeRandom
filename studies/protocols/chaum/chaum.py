from json import dump, load
from math import gcd
from random import getrandbits
from sympy import isprime


def generator(p):
    fact = []
    phi = p-1
    n = phi
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            fact.append(i)
            while n % i == 0:
                n //= i

    if n > 1:
        fact.append(n)

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
    l = int(input('length of prime: '))
    p = getrandbits(l)
    while True:
        if isprime(p):
            break
        p = getrandbits(l)
    g = generator(p)
    with open('chaum_parameters/p.json', 'w', encoding='utf-8') as pw:
        dump({'p': p}, pw, indent=4)
    with open('chaum_parameters/g.json', 'w', encoding='utf-8') as gw:
        dump({'g': g}, gw, indent=4)


def gen_private_params():
    l = int(input('length of x: '))
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
    with open('chaum_parameters/public_key.json', 'w', encoding='utf-8') as pubw:
        dump({'p': p, 'g': g, 'y': y}, pubw, indent=4)
    with open('chaum_parameters/private_key.json', 'w', encoding='utf-8') as privw:
        dump({'x': x}, privw, indent=4)


def sign():
    me = 'message'
    m = hash(me)
    with open('chaum_parameters/p.json', 'r', encoding='utf-8') as pr:
        p = load(pr)['p']
    with open('chaum_parameters/private_key.json', 'r', encoding='utf-8') as privr:
        x = load(privr)['x']
    sign = pow(m, x, p)
    with open('chaum_parameters/signed.json', 'w', encoding='utf-8') as signedw:
        dump({'message': m, 'signature': sign}, signedw, indent=4)


def verify():
    la = int(input('length of a: '))
    lb = int(input('length of b: '))
    a = getrandbits(la)
    b = getrandbits(lb)
    print('a', a)
    print('b', b)
    with open('chaum_parameters/signed.json', 'r', encoding='utf-8') as signedr:
        data = load(signedr)
        m, z = data['message'], data['signature']
    with open('chaum_parameters/public_key.json', 'r', encoding='utf-8') as pubr:
        data = load(pubr)
        p, g, y = data['p'], data['g'], data['y']
    c = (pow(z, a, p) * pow(y, b, p)) % p
    with open('chaum_parameters/private_key.json', 'r', encoding='utf-8') as privr:
        x = load(privr)['x']
    t = pow(x, -1, p-1)
    d = pow(c, t, p)
    print('verified' if d % p == (pow(m, a, p)*pow(g, b, p)) %
          p else 'not verified')


def main():
    gen_shared_params()
    gen_private_params()
    sign()
    verify()


if __name__ == '__main__':
    main()
