def f1():
    alph = open('alphabet.txt', 'r', encoding='UTF-8' ).read()
    sub_alph = list(alph)
    substitution = {c: '' for c in alph}
    from random import choice
    for c in alph:
        sub = choice(sub_alph)
        while sub == c:
            sub = choice(sub_alph)
        substitution[c] = sub
        sub_alph.remove(sub)
    with open('key.txt', 'w', encoding='UTF-8' ) as out_subs:
        out_subs.write("".join(substitution[c] for c in alph))
    print('Ключ сохранен в файл\n')


def f2(shift):
    alph = open('alphabet.txt', 'r', encoding='UTF-8' ).read()
    shifted_alph = alph[(shift % len(alph)):] + alph[:(shift % len(alph))]
    with open('key.txt', 'w', encoding='UTF-8' ) as out_subs:
        out_subs.write("".join(c for c in shifted_alph))
    print('Ключ сохранен в файл\n')


def f3():
    mode = int(input('1) Подстановка\n2) Сдвиг\n\nВведите команду: '))
    if mode == 1:
        f1()
    elif mode == 2:
        shift = int(input('Введите сдвиг: '))
        f2(shift)
    open('mode_key.txt', 'w', encoding='UTF-8' ).write(str(mode))


def f4():
    text = open('text.txt', 'r', encoding='UTF-8' ).read().rstrip().lower()
    alph = open('alphabet.txt', 'r', encoding='UTF-8' ).read().rstrip()
    read_key = open('key.txt', 'r', encoding='UTF-8' ).read().rstrip()

    key = {c: (list(read_key))[i] for i, c in enumerate(alph)}
    encrypted_text = ""
    for c in text:
        if c not in alph:
            encrypted_text += c
            continue
        encrypted_text += key[c]
    open('encrypted_text.txt', 'w', encoding='UTF-8' ).write(encrypted_text)
    print('Сообщение зашифровано\n')


def decrypt(key, alph):
    encrypted_text = open('encrypted_text.txt', 'r', encoding='UTF-8').read().lower()
    decrypted_text = ""

    for c in encrypted_text:
        if c not in alph:
            decrypted_text += c
            continue

        decrypted_text += key[c]
    return decrypted_text


def count_frequency(text, file, alph_file):
    alph = open('alphabet.txt', 'r', encoding='UTF-8').read()
    cnts = {c: 0 for c in alph}
    counter = 0
    for c in text:
        if c in alph:
            cnts[c] += 1
            counter += 1
    import operator
    sorted_cnts = sorted(cnts.items(), key=operator.itemgetter(1))[::-1]
    if file == ' ':
        return sorted_cnts

    sorted_alph = ''
    with open(file, 'w', encoding='UTF-8' ) as out:
        for x in sorted_cnts:
            letter = '/n' if x[0] == '\n' else x[0]
            if file == 'frequencies_from_open_text.txt':
                out.write("{}   {:.10f}\n".format(letter, x[1] / counter))
            else:
                out.write("{}   {:.10f}\n".format(letter, x[1] / counter))
            sorted_alph += x[0]
    open(alph_file, 'w', encoding='UTF-8' ).write(sorted_alph)
    print('Частоты символы сохранены в файл\n')


def transform_key(sorted_key, alph_open):
    alph = open('alphabet.txt', 'r', encoding='UTF-8').read()
    key = ''
    for c in alph:
        key += sorted_key[alph_open.index(c)]
    return key


def is_shifted(transformed_key):
    # return True
    alph = open('alphabet.txt', 'r', encoding='UTF-8').read()
    for i in range(len(alph)):
        shifted_alph = alph[i:] + alph[:i]
        if shifted_alph[:5] == transformed_key[:5]:
            return True
    return False


def dfs(permutations, idx, key, keys, alph_open, mode):
    if idx == 0: #len(permutations) - 1:
        for i in range(len(permutations[idx])):
            add = "".join(c for c in permutations[idx][i])
            # key += add
            key = add + key
            transformed_key = transform_key(key, alph_open)
            if mode == 1:
                open('list_subs.txt', 'a', encoding='UTF-8').write(transformed_key + '\n')
            elif mode == 2 and is_shifted(transformed_key):
                open('list_subs.txt', 'a', encoding='UTF-8').write(transformed_key + '\n')
            key = key[key.find(add) + len(add):]
            # key = key[:key.rfind(add)]
        return keys
    for i in range(len(permutations[idx])):
        add = "".join(c for c in permutations[idx][i])
        # key += add
        key = add + key
        dfs(permutations, idx - 1, key, keys, alph_open, mode)
        key = key[key.find(add) + len(add):]
        # key = key[:key.rfind(add)]
    # return keys


def isotonne(sorted_alph_open, sorted_alph_enc, x):
    sorted_cnt = x.copy()
    alph = open('alphabet.txt', 'r', encoding='UTF-8' ).read()
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
        if len(predicted_shifts) < 5:
            if shift_tup[0] not in predicted_shifts:
                predicted_shifts.append(alph[shift_tup[0]])
        else:
            break
    return predicted_shifts

def mapping(mode):
    # read_key = open('key.txt', 'r').read().split('\n\n')
    # right_key = ''
    # for c in read_key[1].split():
    #     right_key += c

    frequencies_open = {}
    alph_open = ''
    with open('frequencies_from_open_text.txt', 'r',encoding='UTF-8') as frequency_open:
        for line in frequency_open:
            letter, frequency = line.rstrip('\n').split()
            alph_open += letter
            frequencies_open[letter] = float(frequency)

    # print(alph_open)

    frequencies_enc = {}

    accuracy = 3


    with open('frequencies_from_encoded_text.txt', 'r',encoding='UTF-8') as frequency_enc:
        for line in frequency_enc:
            letter, frequency = line.rstrip('\n').split()
            frequencies_enc[letter] = round(float(frequency), accuracy)

    # print(frequencies_open)
    # print()
    # print(frequencies_enc)

    groups = []
    group = []
    etalon = None

    for letter in frequencies_enc:
        if etalon is None:
            etalon = frequencies_enc[letter]
            group = [letter]
        elif frequencies_enc[letter] == etalon:
            group.append(letter)
        else:
            groups.append(group)
            etalon = frequencies_enc[letter]
            group = [letter]
    groups.append(group)

    # Costyle 1 XDDDDDDDDDDDDDD
    if len(groups[7]) > 5:
        groups[7][4], groups[7][2] = groups[7][2], groups[7][4]
        groups[7][1], groups[7][2] = groups[7][2], groups[7][1]

    # print(groups)

    permutations = []
    import itertools
    for group in groups:
        if len(group) == 1:
            permutation = list(tuple(group[0]))
        else:
            permutation = list(itertools.permutations(group))
        permutations.append(permutation)

    # Costyle 2 XDDDDDDDDDD
    if len(permutations[1]) == 2:
        permutations[1] = [permutations[1][1], permutations[1][0]]

    # print(permutations)

    open('keys.txt', 'r+', encoding='UTF-8').truncate(0)
    key = ""
    dfs(permutations, len(permutations) - 1, key, [], alph_open, mode)

    # alph = open('alph.txt', 'r').read()
    # with open('list_subs.txt', 'w') as sub_list:
    #     for sorted_key in keys:
    #         key = ''
    #         for c in alph:
    #             key += sorted_key[alph_open.index(c)]
    #         sub_list.write(key + '\n')
    print('Список изотонных отображений создан\n')
def mapping1(mode):
    encrypted_text = open('encrypted_text.txt', 'r', encoding='UTF-8' ).read().lower()
    frequencies_open = {}
    alph_open = ''
    with open('frequencies_from_open_text.txt', 'r', encoding='UTF-8' ) as frequency_open:
        for line in frequency_open:
            line = line.rstrip('\n')
            letter = ''
            if line[0] == ' ':
                letter, frequency = ' ', line.split()[0]
            else:
                letter, frequency = line.rstrip('\n').split()

            letter = '\n' if letter == '/n' else letter
            alph_open += letter
            frequencies_open[letter] = float(frequency)
    frequencies_enc = {}
    accuracy = 3

    with open('frequencies_from_encoded_text.txt', 'r', encoding='UTF-8' ) as frequency_enc:
        for line in frequency_enc:
            line = line.rstrip('\n')
            if line[0] == ' ':
                letter, frequency = ' ', line.split()[0]
            else:
                letter, frequency = line.rstrip('\n').split()

            letter = '\n' if letter == '/n' else letter
            frequencies_enc[letter] = round(float(frequency), accuracy)
    groups = []
    group = []
    etalon = None
    for letter in frequencies_enc:
        if etalon is None:
            etalon = frequencies_enc[letter]
            group = [letter]
        elif frequencies_enc[letter] == etalon:
            group.append(letter)
        else:
            groups.append(group)
            etalon = frequencies_enc[letter]
            group = [letter]

    groups.append(group)
    permutations = []
    import itertools
    for group in groups:
        if len(group) == 1:
            permutation = list(tuple(group[0]))
        else:
            permutation = list(itertools.permutations(group))
        permutations.append(permutation)

    if mode == 2:
        shifted_alphs = []
        open('keys.txt', 'r+', encoding='UTF-8' ).truncate(0)
        alph = open('alphabet.txt', 'r', encoding='UTF-8' ).read()
        sorted_alph_open = open('sorted_alph_open.txt', 'r', encoding='UTF-8' ).read()
        sorted_alph_enc = open('sorted_alph_enc.txt', 'r', encoding='UTF-8' ).read()
        sorted_cnts = count_frequency(encrypted_text, ' ', ' ')
        symbols = isotonne(sorted_alph_open, sorted_alph_enc, sorted_cnts)
        for symbol in symbols:
            shift = alph.index(symbol)
            shifted_alph = alph[shift:] + alph[:shift]
            open('keys.txt', 'a', encoding='UTF-8').write(shifted_alph + '\n')
            break
    elif mode == 1:
        open('keys.txt', 'r+', encoding='UTF-8').truncate(0)
        key = ""
        keys = []
        dfs(permutations, len(permutations) - 1, key, keys, alph_open)
        with open('keys.txt', 'w', encoding='UTF-8') as out:
            for k in keys:
                out.write(k + "\n")
    print('Список изотонных отображений создан\n')


def brute():
    alph = open('alphabet.txt', 'r', encoding='UTF-8').read()
    len_alph = len(alph)
    subs = []
    with open('keys.txt', 'r', encoding='UTF-8') as out:
        while True:
            cur_sub = out.read(len_alph)
            if cur_sub:
                subs.append(cur_sub)
            else:
                break
            out.read(1)

    with open('brute.txt', 'w', encoding='UTF-8') as brute_file:
        for sub in subs:
            if sub == "":
                continue

            key = {sub[i]: alph[i] for i in range(len(sub))}
            decrypted_text = decrypt(key, alph)
            brute_file.write("Ключ: {}\nТекст:\n{}\n\n".format(sub, decrypted_text))

def make_alph1(text, file):
    al = []
    for i in text:
        if i not in al:
            al.append(i)
            text.replace(i, "")
    with open(file, 'w', encoding='UTF-8') as alph:
        for i in al:
            alph.write(i)

def main():
    while True:
        cmd = int(input("Введите номер команды:\n"
                        "1) Генерация ключа\n"
                        "2) Шифрование\n"
                        "3) Расшифрование\n"
                        "4) Частотный анализ открытого текста\n"
                        "5) Частотный анализ криптограммы\n"
                        "6) Построение изотонных отображений\n"
                        "7) Перебор ключей по изотонным отображениям\n"))
        if cmd == 1:
            f3()
        elif cmd == 2:
            f4()
        elif cmd == 3:
            alph = open('alphabet.txt', 'r', encoding='UTF-8' ).read()
            read_key = open('key.txt', 'r', encoding='UTF-8' ).read().rstrip()
            key = {(list(read_key))[i]: c for i, c in enumerate(alph)}
            decrypted_text = decrypt(key, alph)
            open('decrypted_text.txt', 'w', encoding='UTF-8' ).write(decrypted_text)
            print('Сообщение расшифровано\n')
        elif cmd == 4:
            text = open('big_text.txt', 'r', encoding='UTF-8' ).read().lower()
            file = 'frequencies_from_open_text.txt'
            alph_file = 'sorted_alph_open.txt'
            count_frequency(text, file, alph_file)
        elif cmd == 5:
            text = open('encrypted_text.txt', 'r', encoding='UTF-8' ).read().lower()
            file = 'frequencies_from_encoded_text.txt'
            alph_file = 'sorted_alph_enc.txt'
            count_frequency(text, file, alph_file)
        elif cmd == 6:
            mode = int(open('mode_key.txt', 'r', encoding='UTF-8').read())
            if mode == 1:
                mapping(mode)
            else:
                mapping1(mode)
        elif cmd == 7:
            brute()
        elif cmd == 8:
            text = open('text.txt', 'r', encoding='UTF-8').read().lower()
            text1 = open('big_text.txt', 'r', encoding='UTF-8').read().lower()
            make_alph1(text1, "alph_big_text.txt")
            make_alph1(text, "alph_text.txt")

if __name__ == '__main__':
    main()
