import math


def read_key():
    with open('../srcs/key_transpose.txt', 'r') as f:
        key = f.read()
    return key.lower()


def str_key():
    key = read_key()
    a = list(set(key))
    a.sort()
    return ''.join(a)


def key_unique_unordered():
    k = read_key()
    char_seen = []
    for i in k:
        if i not in char_seen:
            char_seen.append(i)
    return ''.join(char_seen)


def read_message():
    with open('../srcs/msg.txt', 'r') as f:
        msg = f.read()
    return msg


def unique_sym_count(string):
    return len(set(string.lower()))


def gen_matrix():
    key = read_key()
    m = 1
    n = unique_sym_count(key)
    l = len(read_message())
    if l <= n:
        m = 1
    else:
        m = int(math.ceil(l / n))
    return [[''] * n for i in range(m)]

def gen_en_matrix():
    key = read_key()
    m = 1
    n = unique_sym_count(key)
    l = len(read_encrypted_message())
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


def assign_key_symbols_to_matrix(matrix):
	key = key_unique_unordered()
	assigned = [(key[j], j, [matrix[i][j] for i in range(len(matrix))]) for j in range(len(matrix[0]))]
	return assigned


def encrypt(matrix):
	matrix.sort()
	print_matrix(matrix)
	back = [[matrix[i][2][j] for i in range(len(matrix))] for j in range(len(matrix[0][2]))]
	print_matrix(back)
	en = ''
	for i in back:
		en += ''.join(i)
	return en


def read_encrypted_message():
    with open('../srcs/encrypted.txt', 'r') as f:
        msg = f.read()
    return msg


def decrypt():
	message = read_encrypted_message()
	print(message)
	matrix = gen_en_matrix()
	print_matrix(matrix)
	write_message_to_matrix(message, matrix)
	print_matrix(matrix)
	key = list(key_unique_unordered())
	idx = list(range(len(key)))
	order = list(map(lambda x,y:(x,y), key, idx))
	order.sort(key=lambda x:x[0])
	assigned = [(order[j][0], order[j][1], [matrix[i][j] for i in range(len(matrix))]) for j in range(len(matrix[0]))]
	assigned.sort(key=lambda x:x[1])
	print(key)
	print(idx)
	print(order)
	print_matrix(matrix)
	print_matrix(assigned)
	# am = assign_key_symbols_to_matrix(matrix)
	# print_matrix(am)
	# am.sort(key=lambda x:x[1])
	# print_matrix(am)
	back = [[assigned[i][2][j] for i in range(len(assigned))] for j in range(len(assigned[0][2]))]
	print_matrix(back)
	en = ''
	for i in back:
		en += ''.join(i)
	return en


def sort_key():
	key = key_unique_unordered()
	key1 = list(key)
	idx = list(range(len(key)))
	order = list(map(lambda x,y:(x,y), key1, idx))
	order.sort(key=lambda x:x[0])
	order.sort(key=lambda x:x[1])
	print(key)
	print(key1)
	print(idx)
	print(order)
	key1.sort()
	return ''.join(key1)