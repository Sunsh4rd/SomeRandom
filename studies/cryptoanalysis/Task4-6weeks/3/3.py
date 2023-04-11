def f1(n):
    num_ = [i for i in range(n)]
    per_ = {i: -1 for i in range(n)}
    j = 0
    while len(num_):
        from random import choice
        num = choice(num_)
        while len(num_) > 1 and (num == j or per_[num] != -1):
            num = choice(num_)
        per_[j] = num
        j = num
        num_.remove(num)
    key = [per_[i] + 1 for i in per_.keys()]
    return key


def f2():
    k = int(input('Введите длину ключа: '))
    while k < 2:
        k = int(input('Неправильное значение. Введите другое: '))
    per_ = f1(k)
    open('key.txt', 'w', encoding='UTF-8').write(" ".join(str(num) for num in per_))
    print('Ключ сохранен в файл\n')


def f3():
    t_ = open('open_text.txt', 'r', encoding='UTF-8').read().lower()

    t_alph = list(set(t_))
    with open('alphabet.txt', 'r', encoding='UTF-8') as alph_file:
        big_text_alph = alph_file.read().rstrip()

    for c in t_alph:
        if c not in big_text_alph:
            print('Обнаружен символ не из алфавита: ', c)
            return

    key = [int(num) - 1 for num in open('key.txt', 'r', encoding='UTF-8').read().split()]
    i = 0
    encrypted_text = ""
    while i < len(t_):
        subs_text = [""] * len(key)
        if i + len(key) < len(t_):
            text_part = t_[i:i + len(key)]
        else:
            text_part = t_[i:len(t_)] + "\1" * (i + len(key) - len(t_))
        for j in range(len(key)):
            subs_text[key[j]] = text_part[j]
        encrypted_text += "".join(x for x in subs_text)
        i += len(key)
    open("encrypted_text.txt", 'w', encoding='UTF-8').write(encrypted_text)
    print('Шифртекст сохранен в файл\n')


def f4(key, mode):
    encrypted_text = open("encrypted_text.txt", 'r', encoding='UTF-8').read().lower()
    if mode == 'file':
        key = [int(num) - 1 for num in open('key.txt', 'r', encoding='UTF-8').read().split()]
    i = 0
    decrypted_text = ""
    while i < len(encrypted_text):
        subs_text = ""
        if i + len(key) < len(encrypted_text):
            text_part = encrypted_text[i:i + len(key)]
        else:
            text_part = encrypted_text[i:len(encrypted_text)] + "\1" * (i + len(key) - len(encrypted_text))
        for j in range(len(key)):
            subs_text += text_part[key[j]]
        decrypted_text += subs_text
        i += len(key)
    open("decrypted_text.txt", 'w', encoding='UTF-8').write(decrypted_text)
    if mode == 'file':
        print('Расшифрованный текст сохранен в файл\n')
    return decrypted_text


def f5():
    text = open('big_text.txt', 'r', encoding='UTF-8').read().lower()
    alphabet = sorted(list(set(text)))
    import itertools
    lst = [c for c in alphabet]
    bigrams = list(itertools.product(lst, repeat=2))

    for i in range(1, len(text)):
        if (text[i - 1], text[i]) in bigrams:
            bigrams.remove((text[i - 1], text[i]))

    with open('forbidden_bigrams.txt', 'w', encoding='UTF-8') as out:
        for tup in bigrams:
            out.write("{}".format("".join(c for c in tup)))

    with open('alphabet.txt', 'w', encoding='UTF-8') as out:
        out.write("".join(alphabet))

    print('Алфавит: ', alphabet)
    print('Список запретных биграмм сформирован\n')


def f6():
    encrypted_text = open("encrypted_text.txt", 'r', encoding='UTF-8').read().lower()
    k = int(input('Введите длину периода: '))
    table = [[' ' for i in range(k)] for j in range(k)]
    blocks = {i: [] for i in range(k)}
    while len(encrypted_text) % k != 0:
        encrypted_text += ' '
    for i in range(len(encrypted_text)):
        blocks[i % k].append(encrypted_text[i])
    forbidden_bigrams = []
    with open('forbidden_bigrams.txt', 'r', encoding='UTF-8') as bigrams:
        while True:
            bigram = bigrams.read(2)
            if not bigram:
                break
            forbidden_bigrams.append(bigram)

    for i in range(k):
        for j in range(k):
            if i == j:
                table[i][j] = '*'
                continue
            flag = True
            for idx in range(len(blocks[i])):
                first = blocks[i][idx]
                second = blocks[j][idx]

                bigram = first + second

                if bigram in forbidden_bigrams:
                    if i == 3 and j == 8:
                        print('запретка ', bigram)
                    flag = False
                    break
            if not flag:
                table[i][j] = '*'
    with open('table.txt', 'w', encoding='UTF-8') as out_table:
        out_table.write(" \t{}\n".format("\t".join(str(i) for i in range(1, k + 1))))
        for i in range(len(table)):
            out_table.write("{}\t{}\n".format(str(i + 1), "\t".join(c for c in table[i])))
    print('Вспомогательная таблица сохранена в файл\n')


def f7(table, row, k, depth, visited: set):
    if depth == k:
        return {}
    if depth == k - 1:
        res = {}
        for col in range(k):
            if table[row][col] == ' ' and col not in visited:
                res[col + 1] = {}
        return res
    res = {}
    for col in range(k):
        if table[row][col] == ' ' and col not in visited:
            visited.add(col)
            sub = f7(table, col, k, depth + 1, visited)
            visited.remove(col)
            res[col + 1] = sub
    return res


def f8():
    table = []
    with open('table.txt', 'r') as table_file:
        for i, line in enumerate(table_file):
            if i == 0:
                continue
            table.append(line.rstrip('\n').split('\t')[1:])
    k = len(table)
    col_spaces = [[table[row][col] for row in range(k)].count(' ') for col in range(k)]
    mins = []
    for i in range(len(col_spaces)):
        if col_spaces[i] == 0:
            mins.append(i)

    if len(mins) == 0:
        mins = [idx for idx in range(k)]

    tree = {}
    for start in mins:
        tree[start + 1] = f7(table, start, k, 1, {start})
    tree = {key: value for (key, value) in tree.items() if value}
    tree['Length of key'] = k
    import json
    with open('keys_tree.txt', 'w') as out_keys:
        json.dump(tree, out_keys, indent=4)

    keys = json.load(open('keys_tree.txt', 'r', encoding='UTF-8'))
    k = keys['Length of key']
    keys.pop('Length of key')
    keys = f10(keys, k)

    with open("keys_tree.txt", 'w', encoding='UTF-8') as out:
        for key in keys:
            print(" ".join(x for x in key), file=out, sep='\n')
    print('Лес сохранен в файл\n')


def f9(v, keys, depth, k, key, all_keys):
    key.append(v)
    for u in keys[v]:
        all_keys, key = f9(u, keys[v], depth + 1, k, key, all_keys)
    if depth == k:
        all_keys.append(key)
    key = key[:len(key) - 1]
    return all_keys, key


def f10(keys, k):
    key, all_keys = [], []
    for v in keys:
        key = []
        all_keys, _ = f9(v, keys, 1, k, key, all_keys)
    return all_keys


def get_paths(source):
    paths = []
    if isinstance(source, dict):
        for k, v in source.items():
            paths.append([k])
            paths += [[k] + x for x in get_paths(v)]
    return paths


def f11():
    keys = []
    with open('keys_tree.txt', 'r', encoding='UTF-8') as keys_file:
        while True:
            key = keys_file.readline().rstrip()
            if not key:
                break

            keys.append(key)

    with open("bruteforce.txt", 'w', encoding='UTF-8') as out:
        for key in keys:
            out.write("Ключ: {}\n\n".format(key))
            key = [int(x) - 1 for x in key.split()]
            out.write("Текст:\n{}\n\n".format(f4(key, 'not file')))
    print('Перебор ключей завершен и результаты сохранены в файл\n')


def main():
    while True:
        c = int(input("Введите номер команды:\n"
                      "1) Генерация ключа\n"
                      "2) Шифрование\n"
                      "3) Расшифрование\n"
                      "4) Создание списка запретных биграмм и алфавита по большому тексту\n"
                      "5) Построение вспомогательной таблицы\n"
                      "6) Построение ориентированного леса\n"
                      "7) Перебор ключей по лесу\n"))
        if c == 1:
            f2()
        elif c == 2:
            f3()
        elif c == 3:
            f4([], 'file')
        elif c == 4:
            f5()
        elif c == 5:
            f6()
        elif c == 6:
            f8()
        elif c == 7:
            f11()


if __name__ == "__main__":
    main()

