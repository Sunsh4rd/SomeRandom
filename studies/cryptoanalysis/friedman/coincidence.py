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



def index_of_coincidence_avg():
    mode = input('0 - Для случайных последовательностей\n'
                 '1 - Для последовательностей на английском языке\n'
                 '2 - Для последовательностей на русском языке\n')

    if mode == '0':
        l = int(input('Длина последовательностей: '))
        seq1, seq2 = gen_sequences(l)
    return index_of_coincidence_avg_(seq1, seq2)


def index_of_coincidence_(seq1, seq2):
    return len(list(filter(lambda pair: pair[0] == pair[1], zip(seq1, seq2)))) / min(len(seq1), len(seq2))


def index_of_coincidence_avg_(seq1, seq2):
    alph = string.ascii_lowercase
    return sum((seq1.count(a) / len(seq1)) * (seq2.count(a) / len(seq2)) for a in alph)
