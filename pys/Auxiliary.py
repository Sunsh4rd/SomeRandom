import math

# alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя.,!?:;()'


def read_key():
    with open('../srcs/key_transpose.txt', 'r') as f:
        key = f.read()
    return key


def read_message():
    with open('../srcs/msg.txt', 'r') as f:
        msg = f.read()
    return msg


def unique_sym_count(string):
    return len(set(string.lower()))


def gen_matrix(key):
    m = 1
    n = unique_sym_count(key)
    l = len(read_message())
    if l <= n:
        m = 1
    else:
        m = int(math.ceil(l / n))
    return [[''] * n for i in range(m)]


def print_matrix(m):
    for i in m:
        print(i)
    print()


def write_message_to_matrix(message, matrix):
    n = len(matrix)
    m = len(matrix[0])
    message_c = message
    count = 0
    for i in range(n):
        for j in range(m):
            if message_c:
                matrix[i][j] = message[count]
                count += 1
                message_c = message_c[1:]

