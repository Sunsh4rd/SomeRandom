import math


def read_key():
    with open('../srcs/key_transpose.txt', 'r') as f:
        key = f.read()
    return key.lower()


def read_message(name):
    with open(f'../srcs/{name}.txt', 'r', encoding='utf-8') as f:
        msg = f.read()
    return msg


def unique_sym_count(string):
    return len(set(string.lower()))


def key_unique_unordered():
    k = read_key()
    char_seen = []
    for i in k:
        if i not in char_seen:
            char_seen.append(i)
    return ''.join(char_seen)


def gen_matrix(message):
    key = read_key()
    n = unique_sym_count(key)
    l = len(read_message(message))
    m = (l + n - 1) // n
    res = [[''] * n for i in range(m)]
    return res


def print_matrix(m):
    for i in m:
        print(i)
    print()


def write_message_to_matrix(message, matrix):
    n = len(matrix)
    message_c = message
    count = 0
    for i in range(n):
        for j in range(len(matrix[i])):
            if message_c:
                matrix[i][j] = message[count]
                count += 1
                message_c = message_c[1:]


def assign_key_symbols_to_matrix(matrix):
    key = key_unique_unordered()
    assigned = [(key[j], j, [matrix[i][j] for i in range(len(matrix))])
                for j in range(len(matrix[0]))]
    return assigned


def encrypt(matrix):
    matrix.sort()
    print_matrix(matrix)
    back = [[matrix[i][2][j]
             for i in range(len(matrix))] for j in range(len(matrix[0][2]))]
    print_matrix(back)
    en = ''
    for i in back:
        en += ''.join(i)
    return en


def decrypt():
    message = read_message('encrypted_message')
    print(message)
    matrix = gen_matrix('encrypted_message')
    print_matrix(matrix)
    write_message_to_matrix(message, matrix)
    print_matrix(matrix)
    key_s = key_unique_unordered()
    print(key_s)
    key = list(key_s)
    idx = list(range(len(key)))
    order = list(map(lambda x, y: (x, y, []), key, idx))
    order.sort()
    print_matrix(order)
    k = 0
    for k in range(0, len(message), len(order)):
        m = len(message) - k
        t = 0
        for j in range(len(order)):
            if order[j][1] < m:
                order[j][2].append(message[k + t])
                t += 1
            else:
                order[j][2].append('')
    print_matrix(order)
    order.sort(key=lambda x: x[1])
    print_matrix(order)
    back = [[order[i][2][j]
             for i in range(len(order))] for j in range(len(order[0][2]))]
    print_matrix(back)
    dec = ''
    for i in back:
        dec += ''.join(i)
    return dec


# def sort_key():
#     key = key_unique_unordered()
#     key1 = list(key)
#     idx = list(range(len(key)))
#     order = list(map(lambda x, y: (x, y), key1, idx))
#     order.sort(key=lambda x: x[0])
#     order.sort(key=lambda x: x[1])
#     print(key)
#     print(key1)
#     print(idx)
#     print(order)
#     key1.sort()
#     return ''.join(key1)
