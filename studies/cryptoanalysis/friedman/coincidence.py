import string

from gen_sequence import gen_sequences


def index_of_coincidence():
    mode = input('0 - Для случайных последовательностей\n'
                 '1 - Для последовательностей на английском языке\n'
                 '2 - Для последовательностей на русском языке\n')

    if mode == '0':
        l = int(input('Длина последовательностей: '))
        seq1, seq2 = gen_sequences(l)
        print(f'{index_of_coincidence_(seq1, seq2):.3f}')
    if mode == '1':
        for i in range(1, 5):
            with open(f'params/eng{i}1.txt', 'r', encoding='utf-8') as et1_r, \
                    open(f'params/eng{i}2.txt', 'r', encoding='utf-8') as et2_r:
                et1, et2 = et1_r.read(), et2_r.read()
                print(et1)
                print(et2)
            print(f'Пример {i}: {index_of_coincidence_(et1, et2):.3f}')
    if mode == '2':
        for i in range(1, 5):
            with open(f'params/rus{i}1.txt', 'r', encoding='utf-8') as rt1_r, \
                    open(f'params/rus{i}2.txt', 'r', encoding='utf-8') as rt2_r:
                rt1, rt2 = rt1_r.read(), rt2_r.read()
                print(rt1)
                print(rt2)
            print(f'Пример {i}: {index_of_coincidence_(rt1, rt2):.3f}')


def index_of_coincidence_avg():
    mode = input('0 - Для случайных последовательностей\n'
                 '1 - Для последовательностей на английском языке\n'
                 '2 - Для последовательностей на русском языке\n')

    if mode == '0':
        l = int(input('Длина последовательностей: '))
        seq1, seq2 = gen_sequences(l)
        with open('params/alph.txt', 'r', encoding='utf-8') as alph_r:
            alph = alph_r.read()
        print(f'{index_of_coincidence_avg_(seq1, seq2, alph):.3f}')
    if mode == '1':
        for i in range(1, 5):
            with open(f'params/eng{i}1.txt', 'r', encoding='utf-8') as et1_r, \
                    open(f'params/eng{i}2.txt', 'r', encoding='utf-8') as et2_r, \
                    open('params/alph.txt', 'r', encoding='utf-8') as alph_r:
                alph = alph_r.read()
                et1, et2 = et1_r.read(), et2_r.read()
                print(et1)
                print(et2)
            print(f'Пример {i}: {index_of_coincidence_avg_(et1, et2, alph):.3f}')
    if mode == '2':
        for i in range(1, 5):
            with open(f'params/rus{i}1.txt', 'r', encoding='utf-8') as rt1_r, \
                    open(f'params/rus{i}2.txt', 'r', encoding='utf-8') as rt2_r, \
                    open('params/alph1.txt', 'r', encoding='utf-8') as alph_r:
                alph = alph_r.read()
                rt1, rt2 = rt1_r.read(), rt2_r.read()
                print(rt1)
                print(rt2)
            print(f'Пример {i}: {index_of_coincidence_avg_(rt1, rt2, alph):.3f}')


def index_of_coincidence_(seq1, seq2):
    return len(list(filter(lambda pair: pair[0] == pair[1], zip(seq1, seq2)))) / min(len(seq1), len(seq2))


def index_of_coincidence_avg_(seq1, seq2, alph):
    return sum((seq1.count(a) / len(seq1)) * (seq2.count(a) / len(seq2)) for a in alph)
