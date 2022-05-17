import math
import random
from bigint import Bigint
from gen_digits import gen_digits
from gen_digits import int_to_list_of_digits
from gen_digits import miller_rabin
import json

alph_s = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя.!, '
alph_d = {alph_s[i]: i+10 for i in range(len(alph_s))}
alph_dr = {v: k for (k, v) in alph_d.items()}


def gcd_extended(a, b):
    if a == Bigint([0]):
        return b, Bigint([0]), Bigint([1])
    gcd, x1, y1 = gcd_extended(divmod(b, a)[1], a)
    x, s = y1 - divmod(b, a)[0] * x1
    y = x1

    return gcd, x, y


def inverse(a, n):
    t, newt, r, newr = Bigint([0]), Bigint([1]), n, a
    newt, newr = newt - Bigint([0]), newr - Bigint([0])
    while newr[0] != Bigint([0]):
        while newt[1] == True:
            newt = n - newt[0]
        while newr[1] == True:
            newr = n - newr[0]
        q = divmod(r, newr[0])[0]
        t, newt = newt[0], t - q * newt[0]
        r, newr = newr[0], r - q * newr[0]

    if t == a:
        t = t + n

    return t


def keygen(p, q):
    # p, q = gen_digits(l), gen_digits(l)
    n = p * q
    euler = (p-Bigint([1]))[0] * (q-Bigint([1]))[0]
    e = Bigint(int_to_list_of_digits(random.randint(2, int(str(euler))-1)))
    while True:
        if gcd_extended(euler, e)[0] == Bigint([1]):
            break
        e = Bigint(int_to_list_of_digits(
            random.randint(2, int(str(euler))-1)))
    d = inverse(e, euler)
    # print(divmod(e*d, euler)[1])
    return e, d, n


def encrypt(plain_text_file, e, n):
    with open(plain_text_file, 'r', encoding='utf-8') as f:
        text = f.read()
        for c in text:
            if c not in alph_s:
                print('В тексте есть недопустимые символы')
                exit(0)
        cipher_text = ' '.join(
            str(pow(Bigint(int_to_list_of_digits(alph_d[c])), e, n)) for c in text)
        return cipher_text


def decrypt(cipher_text_file, d, n):
    with open(cipher_text_file, 'r', encoding='utf-8') as f:
        text = list(map(int, f.read().split()))
        decipher_text = ''.join(
            str(alph_dr[int(str(pow(Bigint(int_to_list_of_digits((c))), d, n)))]) for c in text)
        return decipher_text


def main():
    e, d, n = None, None, None
    try:
        with open('public.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            e, n = Bigint(int_to_list_of_digits(data['e'])), Bigint(
                int_to_list_of_digits(data['n']))

        with open('private.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
            d, n = Bigint(int_to_list_of_digits(data['d'])), Bigint(
                int_to_list_of_digits(data['n']))

        print(f'Есть доступные ключи: e = {e}, d = {d}, n = {n}')
    except Exception:
        print('Нет доступных ключей, необходимо сгенерировать новые ключи')

    opt = input(
        '0 - Генерация ключей, 1 - Зашифровать текст, 2 - Расшифровать текст: ')
    if opt == '0':
        p = Bigint(int_to_list_of_digits(int(input('p = '))))
        q = Bigint(int_to_list_of_digits(int(input('q = '))))
        while True:
            if miller_rabin(p, int(math.log2(int(str(p))))) and miller_rabin(q, int(math.log2(int(str(q))))):
                e, d, n = keygen(p, q)
                break
            print('p и q должны быть простыми')

        print(f'e = {e}, d = {d}, n = {n}')
        with open('public.json', 'w', encoding='utf-8') as f:
            json.dump({'e': int(str(e)), 'n': int(str(n))}, f)
        with open('private.json', 'w', encoding='utf-8') as f:
            json.dump({'d': int(str(d)), 'n': int(str(n))}, f)
        print('Ключи сгенерированы')

    elif opt == '1':
        if e is None:
            print('Ключи не найдены, необходимо сгенерировать новые ключи')
            exit(0)
        with open('cipher_text.txt', 'w', encoding='utf-8') as f:
            f.write(encrypt('plain_text.txt', e, n))

    elif opt == '2':
        if d is None:
            print('Ключи не найдены, необходимо сгенерировать новые ключи')
            exit(0)
        with open('decipher_text.txt', 'w', encoding='utf-8') as f:
            f.write(decrypt('cipher_text.txt', d, n))


if __name__ == '__main__':
    main()
