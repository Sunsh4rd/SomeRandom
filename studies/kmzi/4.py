import math

alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alph_d = {i: alph[i] for i in range(len(alph))}
alph_dr = {alph[i]: i for i in range(len(alph))}
n = len(alph)
resid = [i for i in range(n)]
reverse = { i:j for j in range(n) for i in range(n) if (i*j) % n == 1}



def affine(message, a, b):
    if math.gcd(a, n) != 1:
        print('a и n должны быть взаимно просты')
        return

    return ''.join(alph_d[(alph_dr[alph_d[a]]*alph_dr[m]+b) % n] for m in message)


def custom(message, k):
    if k not in resid:
        print('Неверное значение k')
        return

    return ''.join(alph_d[(k - alph_dr[p]) % n] for p in message)


def decrypt_affine(ciphertext, a, b):
    rev_a = reverse[a]
    return ''.join(alph_d[(alph_dr[alph_d[rev_a]]*(alph_dr[c]-b)) % n] for c in ciphertext)


def decrypt_custom(ciphertext, k):
    rev_a = reverse[-1 % n]
    return ''.join(alph_d[(alph_dr[alph_d[rev_a]]*(alph_dr[c]-k)) % n] for c in ciphertext)

def main():
    with open('studies\\kmzi\\msg4.txt', 'r', encoding='utf-8') as f:
        msg = f.read()

    k = int(input('Введите k: '))

    print(custom(msg, k))
    print(affine(msg, n-1, k))
    print(decrypt_affine(affine(msg, n-1, k), n-1, k))
    print(decrypt_custom(custom(msg, k), k))


if __name__ == '__main__':
    main()
