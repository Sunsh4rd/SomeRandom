import random
import pickle

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
    with open('studies\kmzi\input_4.txt', 'r', encoding='utf-8') as f:
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
    trigrams = split_text_by_kgrams(text, 3)

    # for t in trigrams:
        # print(text.count(t))

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
