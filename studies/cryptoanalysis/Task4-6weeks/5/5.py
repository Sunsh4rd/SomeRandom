def vigenere_encrypt():
    alph = open('alph.txt', 'r', encoding='UTF-8').read().lower()
    key = open('key.txt', 'r', encoding='UTF-8').read().lower()
    text = open('text.txt', 'r', encoding='UTF-8').read().lower()
    flag = True
    for c in key:
        if c not in alph:
            print('Неверно введён ключ, буква ', c)
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
    alph = open('alph.txt', 'r', encoding='UTF-8').read().lower()
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
    sorted_alph = ''
    if file == 'letters_frequency.txt':
        with open(file, 'w', encoding='UTF-8') as out:
            for x in sorted_cnts:
                out.write("{}   {:.5f}\n".format(x[0], x[1] / counter))
    elif file == ' ':
        sorted_cnts = [(sorted_cnts[i][0], "{:.3f}".format((sorted_cnts[i][1] / counter))) for i in
                       range(len(sorted_cnts))]
    for x in sorted_cnts:
        sorted_alph += x[0]
    if alph_file == 'sorted_alph_open.txt':
        open(alph_file, 'w', encoding='UTF-8').write(sorted_alph)
        print('Частотный анализ выполнен\n')
    return sorted_alph, sorted_cnts


def frequency_words():
    letters = 'абвгдежзийклмнопрстуфхцчшщъыьэюяё'

    text = open('big_text.txt', 'r', encoding='UTF-8').read().lower()
    alph = open('alph.txt', 'r', encoding='UTF-8').read()
    word, words, counter = "", {}, 0
    for c in text:
        if c in letters:
            word += c
        else:
            if len(word):
                if word not in words:
                    words[word] = 0
                words[word] += 1
                counter += 1
            word = ""
    if len(word):
        if word not in words:
            words[word] = 0
        words[word] += 1
        counter += 1
    import operator
    sorted_words = sorted(words.items(), key=operator.itemgetter(1))[::-1]
    sorted_word = ''
    with open('frequency_words.txt', 'w', encoding='UTF-8') as out:
        for x in sorted_words:
            out.write("{}   {:.5f}\n".format(x[0], x[1] / counter))
            sorted_word += x[0] + '\n'
    open('sorted_words.txt', 'w', encoding='UTF-8').write(sorted_word)
    print('Частотный анализ слов выполнен\n')


def isotonne(sorted_alph_open, sorted_alph_enc, x):
    sorted_cnt = x.copy()
    alph = open('alph.txt', 'r', encoding='UTF-8').read()
    shifts = {}
    for i in range(len(sorted_alph_enc)):
        x = (alph.index(sorted_alph_enc[i]) - alph.index(sorted_alph_open[i]) + len(alph)) % len(alph)
        if x not in shifts:
            shifts[x] = 0
        shifts[x] += 1
    import operator
    sorted_shifts = sorted(shifts.items(), key=operator.itemgetter(1))[::-1]
    sorted_cnt = [(sorted_cnt[i][0], round(float(sorted_cnt[i][1]), 2)) for i in range(len(sorted_cnt))]
    groups, groups_idx = [], []
    group, group_idx = [], []
    etalon = None
    for i in range(len(sorted_cnt)):
        if etalon is None:
            etalon = sorted_cnt[i][1]
            group, group_idx = [sorted_cnt[i][0]], [i]
        elif sorted_cnt[i][1] == etalon:
            group.append(sorted_cnt[i][0])
            group_idx.append(i)
        else:
            groups.append(group)
            groups_idx.append(group_idx)
            etalon = sorted_cnt[i][1]
            group, group_idx = [sorted_cnt[i][0]], [i]
    groups.append(group)
    groups_idx.append(group_idx)
    info = []
    for shift_tup in sorted_shifts:
        shift = shift_tup[0]
        counter = 0
        for idx in range(len(sorted_alph_open)):
            for j in range(len(groups_idx)):
                if idx in groups_idx[j]:
                    shifted = alph[(alph.index(sorted_alph_open[idx]) + shift) % len(alph)]
                    if shifted in groups[j]:
                        counter += 1
        info.append((shift, counter))
    info.sort(key=lambda x: x[1])
    info = info[::-1]
    predicted_shifts = []
    for shift_tup in info:
        if shift_tup[1] == len(alph):
            predicted_shifts.append(alph[shift_tup[0]])
    for shift_tup in info:
        if len(predicted_shifts) < 3:  # 2 3 4 5  dunno mazafuk
            if shift_tup[0] not in predicted_shifts:
                predicted_shifts.append(alph[shift_tup[0]])
        else:
            break
    return predicted_shifts


def analysis():
    encrypted_text = open("encrypted_text.txt", 'r', encoding='UTF-8').read().lower()
    k = int(input('Введите длину ключа: '))
    sorted_alph_open = open('sorted_alph_open.txt', 'r', encoding='UTF-8').read()
    blocks = {i: '' for i in range(k)}
    for i in range(len(encrypted_text)):
        blocks[i % k] += encrypted_text[i]
    sorted_alph_enc = []
    sorted_cnts = []
    all_symbols = []
    for i in sorted(blocks.keys()):
        sorted_alph_enc, sorted_cnt = count_frequency(blocks[i], ' ', ' ')
        sorted_alph_enc.append(sorted_alph_enc)
        sorted_cnts.append(sorted_cnt)
        symbols = isotonne(sorted_alph_open, sorted_alph_enc, sorted_cnt)
        all_symbols.append(symbols)
    with open('frequency_enc.txt', 'w', encoding='UTF-8') as out_enc:
        for i in range(len(sorted_cnts[0])):
            s = ''
            for sorted_cnt in sorted_cnts:
                s += "{}\t{}\t\t\t".format(sorted_cnt[i][0], sorted_cnt[i][1])
            s += '\n'
            out_enc.write(s)
    import itertools
    keys = list(itertools.product(*all_symbols))
    with open('keys.txt', 'w', encoding='UTF-8') as keys_out:
        for key in keys:
            keys_out.write("".join(c for c in key) + '\n')
    print('Анализ ключа проведён\n')


def analysis_words():
    encrypted_text = open("encrypted_text.txt", 'r', encoding='UTF-8').read().lower()
    k = int(input('Введите длину ключа: '))
    word = input('Введите слово: ')
    alph = open('alph.txt', 'r', encoding='UTF-8').read()
    keys = []
    for shift in range(len(word)):
        shifted = word[shift:] + word[:shift]
        key = ""
        j = 0
        for i in range(len(encrypted_text)):
            if j == len(shifted):
                if key not in keys:
                    keys.append(key)
                key, j = "", 0
            if encrypted_text[i] not in alph:
                key += alph[(alph.index('э') - alph.index(shifted[j]) + len(alph)) % len(
                    alph)]
                j += 1
                continue
            key += alph[(alph.index(encrypted_text[i]) - alph.index(shifted[j]) + len(alph)) % len(alph)]
            j += 1
    for i in range(len(keys)):
        if len(keys[i]) >= k:
            keys[i] = keys[i][:k]
    import itertools
    with open('keys_words.txt', 'w', encoding='UTF-8') as keys_out:
        for key in keys:
            additions = list(itertools.product(alph, repeat=k - len(key)))
            for addition in additions:
                keys_out.write(key + "".join(c for c in addition) + '\n')
    print('Анализ ключа проведён\n')


def brute(input_file, output_file):
    with open('key.txt', 'r', encoding='UTF-8') as key_file:
        key_len = len(key_file.read())

    keys = []

    with open(input_file, 'r', encoding='UTF-8') as out:
        while True:
            cur_sub = out.read(key_len)
            if cur_sub:
                keys.append(cur_sub)
            else:
                break
            out.read(1)

    with open(output_file, 'w', encoding='UTF-8') as brute_file:
        for key in keys:
            decrypted_text = vigenere_decrypt(key, 2)
            brute_file.write("Ключ: {}\nТекст:\n{}\n\n".format(key, decrypted_text))


def main():
    while True:
        cmd = int(input("1 Шифр Виженера\n2 Расшифрование сообщения\n3 Атака по частотному анализу\n"
                        "4 Атака по словарю\n\nВведите команду: "))
        if cmd == 1:
            vigenere_encrypt()
        elif cmd == 2:
            key = open('key.txt', 'r', encoding='UTF-8').read().lower()
            vigenere_decrypt(key, 1)
        if cmd == 3:
            while True:
                cmd = int(input(
                    "1 Частотный анализ символов языка\n2 Вычисление ключа Виженера"
                    "\n3 Перебор ключей\n0 Назад\n\nВведите команду: "))
                if cmd == 1:
                    text = open('big_text.txt', 'r', encoding='UTF-8').read().lower()
                    file = 'letters_frequency.txt'
                    alph_file = 'sorted_alph_open.txt'
                    count_frequency(text, file, alph_file)
                elif cmd == 2:
                    analysis()
                elif cmd == 3:
                    input_file, output_file = 'keys.txt', 'brute.txt'
                    brute(input_file, output_file)
                elif cmd == 0:
                    break
        elif cmd == 4:
            while True:
                cmd = int(input(
                    "1 Частотный анализ слов языка\n2 Вычисление ключа Виженера"
                    "\n3 Перебор ключей\n0 Назад\n\nВведите команду: "))
                if cmd == 1:
                    frequency_words()
                elif cmd == 2:
                    analysis_words()
                elif cmd == 3:
                    input_file, output_file = 'keys_words.txt', 'brute_words.txt'
                    brute(input_file, output_file)
                elif cmd == 0:
                    break


if __name__ == "__main__":
    main()
