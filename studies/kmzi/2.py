from os import read
import random
from typing import Counter

alphabet_s = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_d = {alphabet_s[i]: str(i) for i in range(len(alphabet_s))}
alphabet_dr = {str(i): alphabet_s[i] for i in range(len(alphabet_s))}

# sorted_by_freq = ['о','е','а','и','н','т','с','р','в','л',
# 'к','м','д','п','у','я','ы','ь','г','з','б',
# 'ч','й','х','ж','ш','ю','ц','щ','э','ф','ъ','ё']
# sorted_by_freq_cap = [l.upper() for l in sorted_by_freq]
# most_frq_bi = ['СТ', 'НО', 'ЕН', 'ТО', 'НА', 'ОВ', 'НИ', 'РА', 'ВО', 'КО']


def update_map(s, m, k):
    for i in range(len(s) - k + 1):
        if s[i: i + k] in m:
            m[s[i: i + k]] += 1
        else:
            m[s[i: i + k]] = 1


def read_text():
    with open('studies/kmzi/input_4.txt', 'r', encoding='utf-8') as f:
        return f.read()


def get_some_key():
    key = list(alphabet_d.values())
    random.shuffle(key)
    return key


def split_text_by_kgrams(text, k):
    return [text[i: i + k] for i in range(len(text) - k + 1)]


def decrypt(ciphertext, key):
    return ''.join(key[c] for c in ciphertext)

def main():
    text = read_text()
    print(text)
    fr = split_text_by_kgrams(text, 1)
    bigrams = split_text_by_kgrams(text, 2)
    print(bigrams)

    srtfrq = ['Ё', 'Ъ', 'Ф', 'Э', 'Щ', 'Ц', 'Ю', 'Ш', 'Ж', 'Х',
    'Б', 'Ч', 'Й', 'З', 'Г', 'Ы', 'Ь', 'Я', 'У', 'П', 'Л',
    'М', 'К', 'Д', 'Р', 'В', 'С', 'Т', 'Н', 'Е', 'А', 'И', 'О']

    srtfrq_c = sorted(Counter(fr).items(), key=lambda x:x[1])

    print(srtfrq)
    print(srtfrq_c)

    

    # for t in bigrams:
        # print(text.count(t))

    mappd_b = {bi: text.count(bi) for bi in bigrams}

    print(mappd_b)

    sorted_mappd_b = sorted(mappd_b.items(), key=lambda x:x[1], reverse=True)
    print(sorted_mappd_b)

    with open('studies/kmzi/bigr.txt', 'r') as f:
        a = f.readlines()
        newl = []
        for s in a:
            newl.append(s.replace('\n', '').replace(' ', ''))
        # print(newl)
        r_bd = {d[:2]: int(d[2:]) for d in newl}

    # print(r_bd)

    sorted_b = sorted(r_bd.items(), key=lambda x:x[1])
    print(sorted_b)

    iter_crypt = [x[0].lower() for x in sorted_mappd_b]
    print(iter_crypt)

    print(''.join(sorted_b[iter_crypt.index(b.lower())][0] for b in bigrams))

    # with open('studies\\kmzi\\trigrams', 'rb') as f:
    #     print(pickle.load(f))
    # key = get_some_key()
    # key_s = ''.join(alphabet_dr[c] for c in key)
    # print(key, key_s)
    # for i in range(1, 6):
        # s = split_text_by_kgrams(text, i)
        # print(s, len(s))


if __name__ == '__main__':
    main()
