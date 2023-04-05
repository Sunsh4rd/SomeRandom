from random import choice


def preprocessing(mode):
    if mode == 1:
        case = int(
            input("1 Для случайной последовательности\n2 Для английского языка\n3 Для русского языка\n4 Сравнить индексы для последовательностей\n0 Назад\n\n"
                  "Введите команду: "))
    elif mode == 2:
        case = int(
            input("1 Для случайной последовательности\n2 Для английского языка\n3 Для русского языка\n4 Сравнить индексы для последовательностей\n0 Назад\n\n"
                  "Введите команду: "))
    if case == 1:
        with open('alph.txt', 'r', encoding="utf-8") as lang_file:
            alph = lang_file.read().rstrip().lower()

        N = int(input('Введите длину для рандомных последовательностей: '))
        y, z = "", ""

        for i in range(N):
            y += choice(alph)
            z += choice(alph)

        open('random_first_text.txt', 'w', encoding="utf-8").write(y)
        open('random_second_text.txt', 'w', encoding="utf-8").write(z)
        print('Последовательности сгенерированы\n')
        return y, z, alph

    elif case == 0:
        return None, None, None
    elif case == 2:
        with open('alph_eng.txt', 'r', encoding="utf-8") as lang_file:
            lang = lang_file.read().rstrip().lower()

        with open('eng_text_1.txt', 'r', encoding="utf-8") as lang_file:
            y = lang_file.read().rstrip().lower()

        with open('eng_text_2.txt', 'r', encoding="utf-8") as lang_file:
            z = lang_file.read().rstrip().lower()

        open('first_text.txt', 'w', encoding="utf-8").write(y)
        open('second_text.txt', 'w', encoding="utf-8").write(z)
        print('Последовательности сгенерированы\n')
        return y, z, lang

    elif case == 3:
        with open('alph_rus.txt', 'r', encoding="utf-8") as lang_file:
            lang = lang_file.read().rstrip().lower()

        with open('rus_text_1.txt', 'r', encoding="utf-8") as lang_file:
            y = lang_file.read().rstrip().lower()

        with open('rus_text_2.txt', 'r', encoding="utf-8") as lang_file:
            z = lang_file.read().rstrip().lower()

        open('first_text.txt', 'w', encoding="utf-8").write(y)
        open('second_text.txt', 'w', encoding="utf-8").write(z)
        print('Последовательности сгенерированы\n')
        return y, z, lang

    elif case == 4:
        N = int(input('Введите длину последовательностей: '))
        for num in range(1, 5):



            with open('alph.txt', 'r', encoding="utf-8") as lang_file:
                rand_alph = lang_file.read().rstrip().lower()

            with open('alph_eng.txt', 'r', encoding="utf-8") as lang_file:
                eng_lang = lang_file.read().rstrip().lower()

            with open('alph_rus.txt', 'r', encoding="utf-8") as lang_file:
                rus_lang = lang_file.read().rstrip().lower()

            with open(f'rus_text_1_{num}.txt', 'r', encoding="utf-8") as lang_file:
                rus_text_1 = lang_file.read().rstrip().lower()

            with open(f'rus_text_2_{num}.txt', 'r', encoding="utf-8") as lang_file:
                rus_text_2 = lang_file.read().rstrip().lower()

            with open(f'eng_text_1_{num}.txt', 'r', encoding="utf-8") as lang_file:
                eng_text_1 = lang_file.read().rstrip().lower()

            with open(f'eng_text_2_{num}.txt', 'r', encoding="utf-8") as lang_file:
                eng_text_2 = lang_file.read().rstrip().lower()

            rand_1, rand_2 = "", ""

            for i in range(N):
                rand_1 += choice(rand_alph)
                rand_2 += choice(rand_alph)

            if mode == 1:
                N_1, I_1 = match_idx(rand_1, rand_2)
                print('Индекс совпадения для случайных последовательностей: {:.03f}\n'.format(I_1 / N_1))

                N_5, I_5 = match_idx(eng_text_1, eng_text_2)
                print('Индекс совпадения для английских последовательностей: {:.03f}\n'.format(I_5 / N_5))

                N_7, I_7 = match_idx(rus_text_1, rus_text_2)
                print('Индекс совпадения для русских последовательностей: {:.03f}\n'.format(I_7 / N_7))
                #return None, None, None

            if mode == 2:
                I_1 = match_idx_average(rand_1, rand_2, rand_alph)
                print('Средний индекс совпадения для случайных последовательностей: y и z = {:.03f}\n'.format(I_1))

                I_5 = match_idx_average(eng_text_1, eng_text_2, eng_lang)
                print('Средний индекс совпадения для английских последовательностей: y и z = {:.03f}\n'.format(I_5))

                I_7 = match_idx_average(rus_text_1, rus_text_2, rus_lang)
                print('Средний индекс совпадения для русских последовательностей: y и z = {:.03f}\n'.format(I_7))
                #return None, None, None
        return None, None, None
    else:
        print('Неправильный ввод')
        return None, None, None


def match_idx(y, z):
    N, I = min(len(y), len(z)), 0
    for i in range(N):
        I += int(y[i] == z[i])

    return N, I


def match_idx_average(y, z, dict):
    I_average = 0

    N1, N2 = 0, 0
    for i in y:
        if i in dict:
            N1 += 1

    for i in z:
        if i in dict:
            N2 += 1

    for x in dict:
        I_average += (y.count(x) / N1) * (z.count(x) / N2)

    return I_average


def crypt(key, text):
    with open('alphv.txt', 'r', encoding="utf-8") as lang_file:
        alph = lang_file.read().rstrip().lower()

    flag = True
    for c in key:
        if c not in alph:
            print('Неверный ключ')
            flag = False
            break
    if not flag:
        return None

    square = {}
    for i, c in enumerate(alph):
        square[c] = alph[i:] + alph[:i]

    encrypted_text = ""
    j = 0
    for c in text:
        if c not in alph:
            print(f'В тексте встретился неверный символ {c}')
            return None

        key_letter = key[j % len(key)]
        text_letter_idx = alph.index(c)
        encrypted_text += square[key_letter][text_letter_idx]
        j += 1

    return encrypted_text


def vigenere_encrypt():
    with open('key.txt', 'r', encoding="utf-8") as key_file:
        key = key_file.read().rstrip().lower()

    text = open('text.txt', 'r', encoding="utf-8").read().lower()

    en_text = crypt(key, text)

    if en_text:
        open('encrypted_text.txt', 'w', encoding="utf-8").write(en_text)
        print('Успешно зашифровано\n')


def vigenere_decrypt():
    with open('alphv.txt', 'r', encoding="utf-8") as lang_file:
        alph = lang_file.read().rstrip().lower()

    with open('key.txt', 'r', encoding="utf-8") as key_file:
        key = key_file.read().rstrip().lower()

    encrypted_text = open('encrypted_text.txt', 'r', encoding="utf-8").read().lower()

    flag = True
    for c in key:
        if c not in alph:
            print('Ключ неверный')
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
            print('В тексте встретился неверный символ')
            return

        key_letter = key[j % len(key)]
        encrypted_text_text_letter_idx = square[key_letter].index(c)
        decrypted_text += alph[encrypted_text_text_letter_idx]
        j += 1
    open('decrypted_text.txt', 'w', encoding="utf-8").write(decrypted_text)
    print('Успешно расшифровано\n')


def shift():
    # mode = int(input("1 генерация ключей и шифрование\n2 сдвиг и нахождение индекса  \n0 Назад\n\nВведите команду: "))
    # if mode == 0:
    #     return
    #
    # if mode == 1:
    #     k_5, k_7 = "", ""
    #
    #     with open('alph.txt', 'r') as lang_file:
    #         alph = lang_file.read().rstrip().lower()
    #
    #     with open('text.txt', 'r') as text_file:
    #         text = text_file.read().rstrip().lower()
    #
    #     for i in range(5):
    #         k_5 += choice(alph)
    #
    #     for i in range(7):
    #         k_7 += choice(alph)
    #
    #     with open('key_5.txt', 'w') as key_1_file:
    #         key_1_file.write(k_5)
    #
    #     with open('key_7.txt', 'w') as key_2_file:
    #         key_2_file.write(k_7)
    #
    #     with open('encrypted_5.txt', 'w') as key_1_file:
    #         key_1_file.write(crypt(k_5, text))
    #
    #     with open('encrypted_7.txt', 'w') as key_2_file:
    #         key_2_file.write(crypt(k_7, text))
    #
    #     print('Ключи длины 5 и 7 сгенерированы')
    #
    # if mode == 2:
    #     l = int(input('Введите l (сдвиг): '))
    #
    #     with open('text.txt', 'r') as text_file:
    #         text = text_file.read().rstrip().lower()
    #
    #     with open('encrypted_5.txt', 'r') as en_text_5_file:
    #         en_5_text = en_text_5_file.read().rstrip().lower()
    #
    #     with open('encrypted_7.txt', 'r') as en_text_7_file:
    #         en_7_text = en_text_7_file.read().rstrip().lower()
    #
    #     new_text = text[l:] + text[:l]
    #     N_1, I_1 = match_idx(text, new_text)
    #     print('Индекс совпадения для открытого текста: {:.03f}\n'.format(I_1 / N_1))
    #
    #     new_en_5_text = en_5_text[l:] + en_5_text[:l]
    #     N_5, I_5 = match_idx(en_5_text, new_en_5_text)
    #     print('Индекс совпадения при k = 5: {:.03f}\n'.format(I_5 / N_5))
    #
    #     new_en_7_text = en_7_text[l:] + en_7_text[:l]
    #     N_7, I_7 = match_idx(en_7_text, new_en_7_text)
    #     print('Индекс совпадения при k = 7: {:.03f}\n'.format(I_7 / N_7))
    l = int(input('Введите l (сдвиг): '))

    for l in range(1,16):
        with open('encrypted_text.txt', 'r', encoding="utf-8") as en_text_file:
            en_text = en_text_file.read().rstrip().lower()

        new_text = en_text[l:] + en_text[:l]

        N_1, I_1 = match_idx(en_text, new_text)
        print('Индекс совпадения: {:.03f}\n'.format(I_1 / N_1))


def main():
    while True:
        cmd = int(input("1 Индекс совпадения\n2 Средний индекс совпадения\n3 Шифр Виженера\n4 Расшифрование сообщения\n5 Индекс совпадения со сдвигом l\n\nВведите команду: "))
        if cmd == 1 or cmd == 2:
            y, z, dict = preprocessing(cmd)
            if y is None:
                continue
            if cmd == 1:
                N, I = match_idx(y, z)
                print('Индекс совпадения y и z = {:.03f}\n'.format(I / N))
            else:
                I_average = match_idx_average(y, z, dict)
                print('Средний индекс совпадения y и z = {:.03f}\n'.format(I_average))
        elif cmd == 3:
            vigenere_encrypt()
        elif cmd == 4:
            vigenere_decrypt()
        elif cmd == 5:
            shift()


if __name__ == "__main__":
    main()
