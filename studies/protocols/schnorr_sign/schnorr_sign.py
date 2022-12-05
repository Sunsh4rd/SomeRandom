from hashlib import sha256
import random
from sympy import isprime


def get_random_prime(n):
    while True:
        number = random.getrandbits(n)
        if isprime(number):
            return number


def check_element_is_primitive(element, p, q):
    return not pow(element, (p - 1) // q, p) == 1 and not pow(element, (p - 1) // 2, p) == 1


def get_g(p, q):
    g = random.randint(1, p - 1)
    while not check_element_is_primitive(g, p, q):
        g = random.randint(1, p - 1)
    return g


def gen_shared_parameters(n):
    q = get_random_prime(n)
    k = 0
    p = (2**k) * q + 1
    while True:
        if isprime(p):
            break
        k += 1
        p = (2**k) * q + 1

    a = pow(get_g(p, q), (2**k), p)

    return p, q, a


def main():
    while True:
        opt = input('0 - Генерация общих параметров\n1 - Генерация индивидуальных параметров\n2 - Генерация подписи (шаг 1)\n3 - Генерация подписи (шаг 2-3)\n4 - Проверка подписи\n')
        if opt == '0':
            l = int(input('Длина числа p: '))
            p, q, a = gen_shared_parameters(l)
            print(f'p = {p}, q = {q}, a = {a}')
            print(pow(a, q, p))
            with open('parameters/shared.txt', 'w', encoding='utf-8') as spw:
                spw.write(' '.join(str(x) for x in [p, q, a]))
        elif opt == '1':
            with open('parameters/shared.txt', 'r', encoding='utf-8') as spr:
                p, q, a = map(int, spr.read().split())
            s = random.randint(1, q-1)
            v = pow(a, -s, p)
            print(f's = {s}, v = {v}')
            with open('parameters/private_key.txt', 'w', encoding='utf-8') as privkw:
                privkw.write(str(s))
            with open('parameters/public_key.txt', 'w', encoding='utf-8') as pubkw:
                pubkw.write(str(v))
        elif opt == '2':
            with open('parameters/shared.txt', 'r', encoding='utf-8') as spr:
                p, q, a = map(int, spr.read().split())
            r = random.randint(1, q-1)
            x = pow(a, r, p)
            with open('parameters/r.txt', 'w', encoding='utf-8') as rw:
                rw.write(str(r))
            with open('parameters/x.txt', 'w', encoding='utf-8') as xw:
                xw.write(str(x))
            print(f'r = {r}, x = {x}')
        elif opt == '3':
            with open('parameters/message.txt', 'r', encoding='utf-8') as mr:
                m = mr.read()
            with open('parameters/x.txt', 'r', encoding='utf-8') as xr:
                x = int(xr.read())
            e = sha256((m+str(x)).encode()).hexdigest()
            print(f'e = {e}')
            with open('parameters/e.txt', 'w', encoding='utf-8') as ew:
                ew.write(str(e))
        # elif opt == '4':
            with open('parameters/shared.txt', 'r', encoding='utf-8') as spr:
                p, q, a = map(int, spr.read().split())
            with open('parameters/r.txt', 'r', encoding='utf-8') as rr:
                r = int(rr.read())
            with open('parameters/private_key.txt', 'r', encoding='utf-8') as privkr:
                s = int(privkr.read())
            with open('parameters/e.txt', 'r', encoding='utf-8') as er:
                e = int(er.read(), base=16)
            y = (r + s*e) % q
            print(f'y = {y}')
            with open('parameters/y.txt', 'w', encoding='utf-8') as yw:
                yw.write(str(y))
        elif opt == '4':
            with open('parameters/shared.txt', 'r', encoding='utf-8') as spr:
                p, q, a = map(int, spr.read().split())
            with open('parameters/y.txt', 'r', encoding='utf-8') as yr:
                y = int(yr.read())
            with open('parameters/e.txt', 'r', encoding='utf-8') as er:
                e = int(er.read(), base=16)
            with open('parameters/public_key.txt', 'r', encoding='utf-8') as pubkr:
                v = int(pubkr.read())
            x_b = (pow(a, y, p)*pow(v, e, p)) % p
            with open('parameters/message.txt', 'r', encoding='utf-8') as mr:
                m = mr.read()
            chck = int(sha256((m+str(x_b)).encode()).hexdigest(), base=16)
            if e == chck:
                print('Подпись подлинная')
            else:
                print('Подпись не подлинная')


if __name__ == '__main__':
    main()
