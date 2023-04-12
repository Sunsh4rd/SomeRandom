import random
import math


def gen_key(k):
    l = [x for x in range(1, k)]
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


def kaziski(text):
    l = []
    for j in range(3, 6):
        for i in range(len(text) - 1):
            s = text[i:i+j]
            try:
                res = text.index(s, text.index(s, i) + 1) - text.index(s, i)
                #print(s, res)
                l.append(res)
            except ValueError:
                continue
    # print(l)
    d = {}
    for i in range(2, 24):
        d[i] = sum(map(lambda item: item % i == 0, l))
    print(d)
    od = [k for k, v in sorted(d.items(), key=lambda item: item[1])]
    print("Вероятнее всего длинна ключа равна одному из чисел: ",
          od[-6:-1] + [od[-1]])
    return math.gcd(*l)


def brute():
    l = int(input('Введите длину ключа для перебора: '))

    f = open('cryptogram.txt', 'r', encoding="utf-8")
    cryptogram = f.read()
    f.close()

    with open("brute.txt", 'w', encoding='utf-8') as out:
        out.write("Длина ключа: " + str(l) + "\n\n")
        all_keys = {}
        from math import factorial
        n = factorial(l - 1)
        while len(all_keys) < n:
            key = gen_key(l)
            while ", ".join(str(x) for x in key) in all_keys.keys():
                key = gen_key(l)
            all_keys[", ".join(str(x) for x in key)] = replace(
                cryptogram, l, key, False)
            key = ", ".join(str(x) for x in key)
            out.write("Ключ: " + key + "\n")
            out.write("Текст:\n" + all_keys[key] + "\n\n")


def main():
    while True:
        a = input(
            '''Что вы хотите сделать?
    1. Генерировать ключ моноциклической перестановки
    2. Зашифровать открытый текст
    3. Расшифровать криптограмму
    4. Тест Казиски по вычислению длины ключа
    5. Перебор ключей по известной длинне ключа\n'''
        )

        if a == '1':
            k = int(input('Введите длинну ключа моноциклической перестановки:\n'))
            f = open('len_key.txt', 'w', encoding="utf-8")
            f.write(str(k))
            f.close()
            f = open('key.txt', 'w', encoding="utf-8")
            f.write(' '.join(map(str, gen_key(k))))
            f.close()
        elif a == '2':
            f = open('open_text.txt', 'r', encoding="utf-8")
            open_text = f.read()
            f.close()
            f = open('len_key.txt', 'r', encoding="utf-8")
            k = int(f.read())
            f.close()
            f = open('key.txt', 'r', encoding="utf-8")
            key = list(map(int, f.read().split()))
            f.close()

            cryptogram = replace(open_text, k, key, True)
            f = open('cryptogram.txt', 'w', encoding="utf-8")
            f.write(cryptogram)
            f.close()

        elif a == '3':
            f = open('cryptogram.txt', 'r', encoding="utf-8")
            cryptogram = f.read()
            f.close()
            f = open('len_key.txt', 'r', encoding="utf-8")
            k = int(f.read())
            f.close()
            f = open('key.txt', 'r', encoding="utf-8")
            key = list(map(int, f.read().split()))
            f.close()

            decrypt = replace(cryptogram, k, key, False)
            f = open('decryp.txt', 'w', encoding="utf-8")
            f.write(decrypt)
            f.close()
        elif a == '4':
            f = open('cryptogram.txt', 'r', encoding="utf-8")
            cryptogram = f.read()
            f.close()
            print('Длинна ключа по тесту Казиски (НОД расстояний) = ',
                  kaziski(cryptogram))
        elif a == '5':
            brute()
        else:
            print('Вы ввели некорректное значение, программа завершается!')
            break


main()
