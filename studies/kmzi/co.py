from functools import reduce
from typing import Counter
import string
import random

armenian_capitals = u'\u0531\u0532\u0533\u0534\u0535\u0536\u0537\u0538\u0539\u053a\u053b\u053c\u053d\u053e\u053f\u0540\u0541\u0542\u0543\u0544\u0545\u0546\u0547\u0548\u0549\u054a\u054b\u054c\u054d\u054e\u054f\u0550\u0551\u0552\u0553\u0554\u0555\u0556'
armenian_alphabet = armenian_capitals + armenian_capitals.lower()
english_alphabet = string.ascii_letters
russian_capitals = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
russian_alphabet = russian_capitals + russian_capitals.lower()


def generate_texts():
    with open('studies\\kmzi\\arm.txt', 'a+', encoding='utf-16') as f:
        for _ in range(100000):
            f.write(random.choice(armenian_alphabet))

    with open('studies\\kmzi\\eng.txt', 'a+', encoding='utf-8') as f:
        for _ in range(100000):
            f.write(random.choice(english_alphabet))

    with open('studies\\kmzi\\rus.txt', 'a+', encoding='utf-8') as f:
        for _ in range(100000):
            f.write(random.choice(russian_alphabet))


def cout_ci():
    with open('studies\\kmzi\\arm.txt', 'r', encoding='utf-16') as f:
        armenian_text = f.read()

    with open('studies\\kmzi\\eng.txt', 'r', encoding='utf-8') as f:
        english_text = f.read()

    with open('studies\\kmzi\\rus.txt', 'r', encoding='utf-8') as f:
        russian_text = f.read()

    freq_arm = Counter(armenian_text)
    freq_eng = Counter(english_text)
    freq_rus = Counter(russian_text)

    print(freq_arm, freq_eng, freq_rus)

    ci_arm = reduce(lambda x, y: x + y, map(lambda x: x * x,
                    freq_arm.values())) / (len(armenian_text) ** 2)
    ci_eng = reduce(lambda x, y: x + y, map(lambda x: x * x,
                    freq_eng.values())) / (len(english_text) ** 2)
    ci_rus = reduce(lambda x, y: x + y, map(lambda x: x * x,
                    freq_rus.values())) / (len(russian_text) ** 2)

    return ci_arm, ci_eng, ci_rus


def main():
    generate_texts()
    ci_arm, ci_eng, ci_rus = cout_ci()
    print(ci_arm, ci_eng, ci_rus)

    # l1 = {i: str(i) for i in range(10)}
    # l2 = {i: english_alphabet[i] for i in range(10)}

    # dt1 = ''.join((random.choice(list(l1.values())) for _ in range(10)))
    # dt2 = ''.join((random.choice(list(l2.values())) for _ in range(10)))

    # count_dt1 = Counter(dt1)
    # count_dt2 = Counter(dt2)

    # ci_dt1 = reduce(lambda x, y: x + y, map(lambda x: x * x,
    #                 count_dt1.values())) / (len(dt1) ** 2)
    # ci_dt2 = reduce(lambda x, y: x + y, map(lambda x: x * x,
    #                 count_dt2.values())) / (len(dt2) ** 2)
    
    # print(dt1, dt2, count_dt1, count_dt2, ci_dt1, ci_dt2)


if __name__ == '__main__':
    main()
