import itertools
import random


def setup():
    cypher_text = open('studies\kmzi\cyphertext_hill.txt',
                       'r', encoding='utf-8').read()
    alphabet_s = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    alphabet_d = {i: alphabet_s[i] for i in range(len(alphabet_s))}
    alphabet_d_r = {alphabet_s[i]: i for i in range(len(alphabet_s))}
    return cypher_text, alphabet_s, alphabet_d, alphabet_d_r


def transpose_matrix(m):
    return [[m[i][j] for i in range(len(m))] for j in range(len(m))]


def multiply_matrix(a, b, m):
    return [[sum(x * y for x, y in zip(a_row, b_col)) % m for b_col in zip(*b)] for a_row in a]


def add_matrix(a, b, m):
    return [[(a[j][i] + b[j][i]) % m for i in range(len(a[j]))] for j in range(len(a))]


def subtract_matrix(a, b, m):
    return [[(a[j][i] - b[j][i]) % m for i in range(len(a[j]))] for j in range(len(a))]


def print_matrix(m):
    for row in m:
        print(*row)


def get_matrix_minor(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]


def get_matrix_determinant(m):
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1) ** c) * \
            m[0][c] * get_matrix_determinant(get_matrix_minor(m, 0, c))
    return determinant


def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def get_reverse(a, m):
    d, q, r = gcd_extended(a, m)
    if 1 % d != 0:
        return None
    else:
        x0 = (q * 1 // d) % m
        return x0


def get_reverse_matrix(a, m):
    det = get_matrix_determinant(a)
    det_r = get_reverse(det, m)
    if not det_r:
        return None
    else:
        adjugate_matrix = [[0 for i in range(len(a))] for j in range(len(a))]
        for i in range(len(a)):
            for j in range(len(a[i])):
                adjugate_matrix[i][j] = ((-1) ** (i + j)) * \
                    get_matrix_determinant(get_matrix_minor(a, i, j)) * det_r

        reversed_matrix = [[adjugate_matrix[i][j] % m for i in range(
            len(adjugate_matrix))] for j in range(len(adjugate_matrix))]
    return reversed_matrix


def encrypt_by_hill(text, n, alphabet_d, alphabet_d_r, m):
    split_text = []
    for i in range(0, len(text), n):
        slc = text[i:i + n]
        split_text.append(slc if len(slc) == n else slc + 'А' * (n - len(slc)))

    split_text_n = []
    for part in split_text:
        split_text_n.append([[alphabet_d_r[c] for c in part]])

    matrix_a = [[1, 2, 3], [4, 1, 6], [7, 5, 1]]
    vector_a = [[11, 12, 13]]

    cypher_text_l = []
    for x in split_text_n:
        cypher_text_l.append(add_matrix(
            multiply_matrix(x, matrix_a, m), vector_a, m))

    cypher_text = ''
    for el in cypher_text_l:
        cypher_text += ''.join(map(lambda x: alphabet_d[x], *el))

    return cypher_text


def decrypt(cryptogramm, n, alphabet_d, alphabet_d_r, m):
    while True:
        matrix_a_r = [[random.randint(0, 32)
                       for i in range(n)] for j in range(n)]
        if not get_reverse_matrix(matrix_a_r, m):
            print_matrix(matrix_a_r)
            print('Irreversable, skipping')
            continue
        else:
            vectors = [[list(vec)] for vec in itertools.product(
                list(range(33)), repeat=3)]
            for vector_a in vectors:
                split_text = []
                for i in range(0, len(cryptogramm), n):
                    slc = cryptogramm[i:i + n]
                    split_text.append(slc)

                split_text_n = []
                for part in split_text:
                    split_text_n.append([[alphabet_d_r[c] for c in part]])

                decrypted_text_l = []
                for y in split_text_n:
                    decrypted_text_l.append(multiply_matrix(
                        subtract_matrix(y, vector_a, m), matrix_a_r, m))

                decrypted_text = ''
                for el in decrypted_text_l:
                    decrypted_text += ''.join(
                        map(lambda x: alphabet_d[x], *el))

                with open('studies\kmzi\hill_decrypt.txt', 'a+', encoding='utf-8') as f:
                    f.write(f'{decrypted_text}\n')


def main():
    cryptogramm, alphabet_s, alphabet_d, alphabet_d_r = setup()
    m = len(alphabet_s)

    #[[1, 2, 3], [4, 1, 6], [7, 5, 1]]
    #[[20, 32, 12],[25, 32, 30],[32, 12, 31]]

    # print_matrix(get_reverse_matrix([[20, 32, 12],[25, 32, 30],[32, 12, 29]], m))

    # decrypted =
    decrypt(cryptogramm, 3, alphabet_d, alphabet_d_r, m)
    # print(decrypted)


if __name__ == '__main__':
    main()
