import random


def gen_key(k):
    l = [x for x in range(k)]
    random.shuffle(l)
    return l


def replace(text, k, key, f):
    d = {}
    if f:
        d[0] = key[0]
        d[key[-1]] = 0
        for i in range(len(key) - 1):
            d[key[i]] = key[i + 1]
    else:
        d[key[0]] = 0
        d[0] = key[-1]
        for i in range(len(key) - 1):
            d[key[i + 1]] = key[i]

    bloks = [text[x:x + k] for x in range(0, len(text), k)]

    crypt_bloks = []
    for bl in bloks:
        cr_bl = ''
        if len(bl) == k:
            for i in range(k):
                cr_bl += bl[d[i]]
        else:
            if f:
                for i in range(k):
                    if d[i] >= len(bl):
                        continue
                    cr_bl += bl[d[i]]
            else:

                cr_bl = [bl]
                for i in range(k - 1):
                    if [replace(cr_bl[0], k, key, True)] != [bl]:
                        cr_bl = [replace(cr_bl[0], k, key, True)]
                    else:
                        break
                cr_bl = cr_bl[0]

        crypt_bloks.append(cr_bl)

    return ''.join(crypt_bloks)


def brute():
    l = int(input('Введите длину ключа для перебора: '))

    f = open('params/ciphertext.txt', 'r', encoding="utf-8")
    cryptogram = f.read()
    f.close()
    print('yay')
    with open("params/brute.txt", 'w', encoding='utf-8') as out:
        out.write("Длина ключа: " + str(l) + "\n\n")
        all_keys = {}
        from math import factorial
        n = factorial(l - 1)
        while len(all_keys) < n:
            key = gen_key(l)
            while ", ".join(str(x) for x in key) in all_keys.keys():
                key = gen_key(l)
            all_keys[", ".join(str(x) for x in key)] = replace(cryptogram, l, key, False)
            key = ", ".join(str(x) for x in key)
            out.write("Ключ: " + key + "\n")
            out.write("Текст:\n" + all_keys[key] + "\n\n")
