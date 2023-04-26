from itertools import cycle

from coincidence import index_of_coincidence_

with open('params/alph.txt', 'r', encoding='utf-8') as alph_r, \
        open('params/key.txt', 'r', encoding='utf-8') as key_r:
    alph = alph_r.read()
    key = key_r.read()


def encrypt():
    with open('params/message.txt', 'r', encoding='utf-8') as text_r, \
            open('params/ciphertext.txt', 'w', encoding='utf-8') as ct_w:
        text = text_r.read()
        print(*filter(lambda x: x not in alph, text))
        ciphertext = ''.join(alph[(alph.index(s) + alph.index(k)) % len(alph)] for s, k in zip(text, cycle(key)))
        ct_w.write(ciphertext)
    return ciphertext


def decrypt():
    with open('params/ciphertext.txt', 'r', encoding='utf-8') as ct_r, \
            open('params/deciphertext.txt', 'w', encoding='utf-8') as dct_w:
        ciphertext = ct_r.read()
        deciphertext = ''.join(
            alph[(alph.index(s) - alph.index(k)) % len(alph)] for s, k in zip(ciphertext, cycle(key)))
        dct_w.write(deciphertext)
    return deciphertext


def shift():
    with open('params/message.txt', 'r', encoding='utf-8') as msg_r, \
            open('params/ciphertext.txt', 'r', encoding='utf-8') as ct_r:
        text = msg_r.read()
        ciphertext = ct_r.read()
        for i in range(1, 16):
            shifted_t = text[i:] + text[:i]
            shifted_c = ciphertext[i:] + ciphertext[:i]
            print(text)
            print(shifted_t)
            print(f'Для сдвига {i}, открытый текст: {index_of_coincidence_(text, shifted_t):.3f}')
            print(f'Для сдвига {i}, криптограмма: {index_of_coincidence_(ciphertext, shifted_c):.3f}')
