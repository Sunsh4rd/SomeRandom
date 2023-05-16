def gen_permutation(n):
    numbers = [i for i in range(n)]
    permutation = {i: -1 for i in range(n)}
    j = 0
    while len(numbers):
        from random import choice
        num = choice(numbers)
        while len(numbers) > 1 and (num == j or permutation[num] != -1):
            num = choice(numbers)
        permutation[j] = num
        j = num
        numbers.remove(num)
    key = [permutation[i] + 1 for i in permutation.keys()]
    return key


def gen_key():
    k = int(input('Введите длину ключа: '))
    while k < 2:
        k = int(input('Неправильное значение. Введите другое: '))
    permutation = gen_permutation(k)
    open('key.txt', 'w', encoding='utf-8').write(" ".join(str(num) for num in permutation))
    print('Ключ сгенерирован\n')


def encrypt():
    text = open('text.txt', 'r', encoding='UTF-8').read().lower()

    key = [int(num) - 1 for num in open('key.txt', 'r', encoding='utf-8').read().split()]
    i = 0
    encrypted_text = ""
    while i < len(text):
        print(len(text))
        subs_text = [""] * len(key)
        if i + len(key) < len(text):
            text_part = text[i:i + len(key)]
        else:
            text_part = text[i:len(text)] + "." * (i + len(key) - len(text))
        for j in range(len(key)):
            subs_text[key[j]] = text_part[j]
        encrypted_text += "".join(x for x in subs_text)
        i += len(key)
    open("encrypted_text.txt", 'w', encoding='utf-8').write(encrypted_text)


def decrypt(key, mode):
    encrypted_text = open("encrypted_text.txt", 'r', encoding='utf-8').read().lower()
    if mode == 'file':
        key = [int(num) - 1 for num in open('key.txt', 'r', encoding='utf-8').read().split()]
    i = 0
    decrypted_text = ""
    while i < len(encrypted_text):
        subs_text = ""
        if i + len(key) < len(encrypted_text):
            text_part = encrypted_text[i:i + len(key)]
        else:
            text_part = encrypted_text[i:len(encrypted_text)] + "." * (i + len(key) - len(encrypted_text))
        for j in range(len(key)):
            subs_text += text_part[key[j]]
        decrypted_text += subs_text
        i += len(key)
    open("decrypted_text.txt", 'w', encoding='utf-8').write(decrypted_text)
    if mode == 'file':
        print('Сообщение расшифровано\n')
    return decrypted_text


def compute_forbidden_bigrams():
    text = open('big_text.txt', 'r', encoding='UTF-8').read().lower()

    alph = open('alph.txt', 'r', encoding='UTF-8').read()

    import itertools
    lst = [c for c in alph]
    bigrams = list(itertools.product(lst, repeat=2))

    for i in range(1, len(text)):
        if text[i - 1] in alph and text[i] in alph:
            if (text[i - 1], text[i]) in bigrams:
                bigrams.remove((text[i - 1], text[i]))

    with open('forbidden_bigrams.txt', 'w', encoding='utf-8') as out:
        for tup in bigrams:
            out.write("{}\n".format("".join(c for c in tup)))
    print('Список запретных биграмм сформирован\n')


def create_table():
    encrypted_text = open("encrypted_text.txt", 'r', encoding='utf-8').read().lower()
    k = int(input('Введите длину периода: '))
    table = [[' ' for i in range(k)] for j in range(k)]

    blocks = {i: [] for i in range(k)}

    for i in range(len(encrypted_text)):
        blocks[i % k].append(encrypted_text[i])

    forbidden_bigrams = []
    with open('forbidden_bigrams.txt', 'r', encoding='utf-8') as bigrams:
        for line in bigrams:
            forbidden_bigrams.append("{}".format(line.rstrip('\n')))

    for i in range(k):
        for j in range(k):
            if i == j:
                table[i][j] = 'X'
                continue
            flag = True
            for idx in range(len(blocks[i])):
                first = blocks[i][idx]
                second = blocks[j][idx]

                bigram = first + second

                if bigram in forbidden_bigrams:
                    if i == 3 and j == 8:
                        print(bigram)
                    flag = False
                    break
            if not flag:
                table[i][j] = 'X'
    with open('table.txt', 'w', encoding='utf-8') as out_table:
        out_table.write(" \t{}\n".format("\t".join(str(i) for i in range(1, k + 1))))
        for i in range(len(table)):
            out_table.write("{}\t{}\n".format(str(i + 1), "\t".join(c for c in table[i])))



def dfs(table, row, k, depth, visited: set):
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
            sub = dfs(table, col, k, depth + 1, visited)
            visited.remove(col)
            res[col + 1] = sub
    return res


def build_forest():
    table = []
    with open('table.txt', 'r', encoding='utf-8') as table_file:
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
        tree[start + 1] = dfs(table, start, k, 1, {start})
    tree = {key: value for (key, value) in tree.items() if value}
    tree['Length of key'] = k
    import json
    with open('keys.txt', 'w', encoding='utf-8') as out_keys:
        json.dump(tree, out_keys, indent=4)

    keys = json.load(open('keys.txt', 'r', encoding='UTF-8'))
    k = keys['Length of key']
    keys.pop('Length of key')
    keys = parse_keys(keys, k)

    with open("keys1.txt", 'w', encoding='UTF-8') as out:
        for key in keys:
            print(" ".join(x for x in key), file=out, sep='\n')


def dfs_keys(v, keys, depth, k, key, all_keys):
    key.append(v)
    for u in keys[v]:
        all_keys, key = dfs_keys(u, keys[v], depth + 1, k, key, all_keys)
    if depth == k:
        all_keys.append(key)
    key = key[:len(key) - 1]
    return all_keys, key


def parse_keys(keys, k):
    key, all_keys = [], []
    for v in keys:
        key = []
        all_keys, _ = dfs_keys(v, keys, 1, k, key, all_keys)
    return all_keys


def brute_keys():
    import json
    keys = json.load(open('keys.txt', 'r', encoding='utf-8'))
    k = keys['Length of key']
    keys.pop('Length of key')
    keys = parse_keys(keys, k)
    with open("brute.txt", 'w', encoding='utf-8') as out:
        for key in keys:
            out.write("Ключ: {}\n\n".format(" ".join(x for x in key)))
            key = [int(x) - 1 for x in key]
            out.write("Текст:\n{}\n\n".format(decrypt(key, 'not file')))
    print('Перебор ключей закончен\n')


def main():
    while True:
        cmd = int(input("1) Генерация ключа;\n2) Шифрование;\n3) Расшифрование;\n4) Запретные биграммы;\n5) Вспомогательная "
                        "таблица;\n6) Построение ориентированного леса;\n7) Перебор ключей.\n\nВведите команду: "))
        if cmd == 1:
            gen_key()
        elif cmd == 2:
            encrypt()
        elif cmd == 3:
            decrypt([], 'file')
        elif cmd == 4:
            compute_forbidden_bigrams()
        elif cmd == 5:
            create_table()
        elif cmd == 6:
            build_forest()
        elif cmd == 7:
            brute_keys()


if __name__ == "__main__":
    main()