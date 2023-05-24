alph = open('alph.txt', 'r', encoding="UTF-8").read()
import itertools

lst = [c for c in alph]
bigrams = list(itertools.product(lst, repeat=2))


def vigenere_encrypt():
    alph = open('alph.txt', 'r', encoding="UTF-8").read()
    key = open('key.txt', 'r', encoding="UTF-8").read()
    with open('keylen.txt', 'w', encoding='utf-8') as kl_w:
        kl_w.write(str(len(key)))
    text = open('text.txt', 'r', encoding="UTF-8").read().lower()
    square = {}
    for i, c in enumerate(alph):
        square[c] = alph[i:] + alph[:i]
    encrypted_text = ""
    j = 0
    for c in text:
        if c not in alph:
            encrypted_text += c
            j += 1
            continue
        key_letter = key[j % len(key)]
        text_letter_idx = alph.index(c)
        encrypted_text += square[key_letter][text_letter_idx]
        j += 1
    open('encrypted_text.txt', 'w', encoding="UTF-8").write(encrypted_text)
    print('Сообщение зашифровано\n')


def vigenere_decrypt(key, encrypted_text, alph, mode):
    square = {}
    for i, c in enumerate(alph):
        square[c] = alph[i:] + alph[:i]
    decrypted_text = ""
    j = 0
    for c in encrypted_text:
        if c not in alph:
            decrypted_text += c
            j += 1
            continue
        key_letter = key[j % len(key)]
        encrypted_text_letter_idx = square[key_letter].index(c)
        decrypted_text += alph[encrypted_text_letter_idx]
        j += 1
    if mode == 1:
        open('decrypted_text.txt', 'w', encoding="UTF-8").write(decrypted_text)
        print('Сообщение расшифровано\n')
    return decrypted_text


def count_frequency_bigrams(text, alph, mode):
    cnts = [[0] * len(alph) for _ in range(len(alph))]
    counter = 0
    for i in range(1, len(text)):
        if text[i - 1] in alph and text[i] in alph:
            cnts[alph.index(text[i - 1])][alph.index(text[i])] += 1
            counter += 1
    cnts = [[element / counter for element in row] for row in cnts]
    if mode == 1:
        with open('E.txt', 'w', encoding="UTF-8") as out:
            for i in range(len(cnts)):
                out.write("\t\t".join("{:.5f}".format(cnts[i][j]) for j in range(len(cnts[i]))) + '\n')
        print('Эталонная матрица частот биграмм составлена\n')
    return cnts


def count_W(key, encrypted_text, alph, mode, E):
    decrypted_text_ki = vigenere_decrypt(key, encrypted_text, alph, mode)
    D = count_frequency_bigrams(decrypted_text_ki, alph, mode)
    res = 0
    for i in range(len(D)):
        for j in range(len(D[i])):
            res += abs(D[i][j] - E[i][j])
    return res


def analysis(k):
    encrypted_text = open('encrypted_text.txt', 'r', encoding="UTF-8").read()
    alph = open('alph.txt', 'r', encoding="UTF-8").read()
    bi = open('E.txt', 'r', encoding="UTF-8").read().rstrip('\n').split('\n')
    E = [[float(c) for c in row.split('\t\t')] for row in bi]
    from random import choice
    key0 = ''.join(choice(alph) for _ in range(k))
    print('\nЭкспериментальный ключ, полученный случайным образом: {}\n'.format(key0))
    open('key0.txt', 'w', encoding="UTF-8").write(key0)
    key = ''
    j = 1
    while key != key0:
        key = key0
        W = count_W(key, encrypted_text, alph, 2, E)
        key0 = key
        for i in range(k):
            W_min = W
            symbol = key0[i]
            for ki in alph:
                new_key = key0[:i] + ki + key0[i + 1:]
                W_ki = count_W(new_key, encrypted_text, alph, 2, E)
                if W_ki <= W_min:
                    W_min = W_ki
                    symbol = ki
            key0 = key0[:i] + symbol + key0[i + 1:]
            W = W_min
        # print('Полученный ключ после {}-го прохода: {}'.format(j, key0))
        j += 1
    open('keys.txt', 'w', encoding="UTF-8").write(key)
    print('\nФинальный ключ: {}\nАнализ ключа проведён\n'.format(key))


def main():
    # k = int(input('Введите длину ключа: '))
    while True:
        cmd = int(input("1 Шифр Виженера\n2 Расшифрование сообщения\n3 Частотный анализ биграмм ОТ\n"
                        "4 Вычисление ключа Виженера\n\nВведите команду: "))
        if cmd == 1:
            vigenere_encrypt()
        elif cmd == 2:
            encrypted_text = open('encrypted_text.txt', 'r', encoding="UTF-8").read()
            key = open('key.txt', 'r', encoding="UTF-8").read()
            alph = open('alph.txt', 'r', encoding="UTF-8").read()
            vigenere_decrypt(key, encrypted_text, alph, 1)
        elif cmd == 3:
            text = open('big_text.txt', 'r', encoding="UTF-8").read().lower()
            alph = open('alph.txt', 'r', encoding="UTF-8").read()
            count_frequency_bigrams(text, alph, 1)
        elif cmd == 4:
            with open('keylen.txt', 'r', encoding='utf-8') as kl_r:
                k = int(kl_r.read())
            analysis(k)


if __name__ == "__main__":
    main()
