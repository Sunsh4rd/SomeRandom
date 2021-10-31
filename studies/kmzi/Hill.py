def setup():
    cypher_text = open('studies\kmzi\cyphertext_hill.txt',
                       'r', encoding='utf-8').read()
    alphabet_s = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    alphabet_d = {i: alphabet_s[i] for i in range(len(alphabet_s))}
    alphabet_d_r = {alphabet_s[i]: i for i in range(len(alphabet_s))}
    return cypher_text, alphabet_s, alphabet_d, alphabet_d_r


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
        print('Не имеет решений')
    else:
        x0 = (q * 1 // d) % m
        return x0


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
    split_text = []
    for i in range(0, len(cryptogramm), n):
        slc = cryptogramm[i:i + n]
        split_text.append(slc)

    split_text_n = []
    for part in split_text:
        split_text_n.append([[alphabet_d_r[c] for c in part]])

    matrix_a_r = [[20, 32, 12],[25, 32, 30],[32, 12, 31]]
    vector_a = [[11, 12, 13]]

    decrypted_text_l = []
    for y in split_text_n:
        decrypted_text_l.append(multiply_matrix(
            subtract_matrix(y, vector_a, m), matrix_a_r, m))

    decrypted_text = ''
    for el in decrypted_text_l:
        decrypted_text += ''.join(map(lambda x: alphabet_d[x], *el))

    return decrypted_text



def main():
    cryptogramm, alphabet_s, alphabet_d, alphabet_d_r = setup()
    m = len(alphabet_s)


    cypher_text = encrypt_by_hill(
        'ТЕКСТ', 3, alphabet_d, alphabet_d_r, m)
    #[[1, 2, 3], [4, 1, 6], [7, 5, 1]]
    #[[20, 32, 12],[25, 32, 30],[32, 12, 31]]
    print(cypher_text)

    decrypted = decrypt(cypher_text, 3, alphabet_d, alphabet_d_r, m)
    print(decrypted)


if __name__ == '__main__':
    main()



