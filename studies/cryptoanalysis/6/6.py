def vigenere_encrypt():
    alph = open('alph.txt', 'r', encoding='UTF-8').read()
    key = open('key.txt', 'r', encoding='UTF-8').read()
    text = open('text.txt', 'r', encoding='UTF-8').read().lower()
    flag = True
    for c in key:
        if c not in alph:
            print('Неверно введён ключ')
            flag = False
            break
    if not flag:
        return
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
    open('encrypted_text.txt', 'w', encoding='UTF-8').write(encrypted_text)
    print('Сообщение зашифровано\n')


def vigenere_decrypt(key, mode):
    alph = open('alph.txt', 'r', encoding='UTF-8').read()
    encrypted_text = open('encrypted_text.txt', 'r', encoding='UTF-8').read().lower()
    flag = True
    for c in key:
        if c not in alph:
            print('Неверно введён ключ')
            flag = False
            break
    if not flag:
        return
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
        encrypted_text_text_letter_idx = square[key_letter].index(c)
        decrypted_text += alph[encrypted_text_text_letter_idx]
        j += 1
    if mode == 1:
        open('decrypted_text.txt', 'w', encoding='UTF-8').write(decrypted_text)
        print('Сообщение расшифровано\n')
    return decrypted_text


def count_frequency(text, file, alph_file):
    alph = open('alph.txt', 'r', encoding='UTF-8').read()
    cnts = {c: 0 for c in alph}
    counter = 0
    for c in text:
        if c in alph:
            cnts[c] += 1
            counter += 1
    import operator
    sorted_cnts = sorted(cnts.items(), key=operator.itemgetter(1))[::-1]
    sorted_cnts = [(sorted_cnts[i][0], round(sorted_cnts[i][1] / counter, 5)) for i in range(len(sorted_cnts))]
    sorted_alph = ''
    if file == 'frequency_open.txt':
        with open(file, 'w', encoding='UTF-8') as out:
            for x in sorted_cnts:
                out.write("{}   {:.5f}\n".format(x[0], x[1]))
    for x in sorted_cnts:
        sorted_alph += x[0]
    if alph_file == 'sorted_alph_open.txt':
        open(alph_file, 'w', encoding='UTF-8').write(sorted_alph)
        print('Частотный анализ выполнен')
    return sorted_alph, sorted_cnts


def hypothesis0(frequencies):
    alph = open('alph.txt', 'r', encoding='UTF-8').read()
    m = len(alph)
    P = [0 for j in range(m)]
    for i in range(len(frequencies)):
        for k in range(len(frequencies)):
            P[((i - k) + m) % m] += frequencies[i][1] * frequencies[k][1]
    P = [round(P[j], 5) for j in range(m)]
    with open('h0.txt', 'w') as hypothesis:
        for j in range(m):
            hypothesis.write("{}\t{}\n".format(j, P[j]))
    print("Гипотеза H(0) составлена\n")


def hypothesis(d, t, r, y, alph):
    m = len(alph)
    z = []
    for j in range((t - 1) * d + r):
        if y[j] in alph and y[j + d] in alph:
            z.append((alph.index(y[j]) - alph.index(y[j + d]) + m) % m)
    P = [round(z.count(j) / len(z), 5) for j in range(m)]
    return P


def hypotheses(n1, n2):
    alph = open('alph.txt', 'r', encoding='UTF-8').read()
    encrypted_text = open('encrypted_text.txt', 'r', encoding='UTF-8').read().lower()
    P0 = []
    with open('h0.txt', 'r', encoding='UTF-8') as hypot_in:
        for line in hypot_in:
            P0.append(float(line.rstrip('\n').split('\t')[1]))
    N = len(encrypted_text)
    P = []
    values = {}
    for d in range(n1, n2 + 1):
        t, r = N // d, N % d
        p = hypothesis(d, t, r, encrypted_text, alph)
        scalar_mult = 0
        for j in range(min(len(p), len(P0))):
            scalar_mult += pow(p[j] - P0[j], 2)
        P.append(p)
        from math import sqrt
        values[d] = round(sqrt(scalar_mult), 5)
    import operator
    sorted_values = sorted(values.items(), key=operator.itemgetter(1))# [::-1]
    with open('values.txt', 'w', encoding='UTF-8') as values_out:
        for value in sorted_values:
            values_out.write("{}\t\t{:.5f}\n".format(value[0], value[1]))
    with open('hypothesis.txt', 'w', encoding='UTF-8') as hypot_out:
        for i in range(len(P[0])):
            s = ''
            for p in P:
                s += "{:.5f}\t\t".format(p[i])
            hypot_out.write(s + '\n')
    print('Гипотезы H(d) составлены\n')


def main():
    while True:
        cmd = int(input("1) Шифр Виженера;\n2) Расшифрование сообщения;\n3) Частотный анализ и составление гиптотезы;\n"
                        "4) Гипотезы H(d).\n\nВведите команду: "))
        if cmd == 1:
            vigenere_encrypt()
        elif cmd == 2:
            key = open('key.txt', 'r', encoding='UTF-8').read()
            vigenere_decrypt(key, 1)
        elif cmd == 3:
            text = open('big_text.txt', 'r', encoding='UTF-8').read().lower()
            file = 'frequency_open.txt'
            alph_file = 'sorted_alph_open.txt'
            _, sorted_cnts = count_frequency(text, file, alph_file)
            hypothesis0(sorted_cnts)
        elif cmd == 4:
            n1 = int(input('Введите число n1: '))
            n2 = int(input('Введите число n2 (больше, чем {}): '.format(n1)))
            while n2 <= n1:
                n2 = int(input('Введено неправильно значение, введите n2: '))
            hypotheses(n1, n2)


if __name__ == "__main__":
    main()

