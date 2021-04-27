import json


def print_m(m):
    for row in m:
        print(row)
    print('---------')


def transpose_m(m):
    return [[m[i][j] for i in range(len(m))] for j in range(len(m))]


def sum_m(a, b):
    return [[(a[j][i] + b[j][i]) % 2 for i in range(len(a))] for j in range(len(a))]


def mult_m(a, b):
    rm = [[0 for col in range(len(b[0]))] for row in range(len(a))]
    for i in range(len(a)):
        for j in range(len(b[0])):
            for k in range(len(b)):
                rm[i][j] += a[i][k] * b[k][j]
            rm[i][j] %= 2
    return rm


def commutability_s(F):
    r = 0
    for a in F:
        for b in F:
            if sum_m(a, b) == sum_m(b, a):
                r += 1
    return r == len(F) ** 2


def associativity_s(F):
    r = 0
    for a in F:
        for b in F:
            for c in F:
                if sum_m(sum_m(a, b), c) == sum_m(a, sum_m(b, c)):
                    r += 1
    return r == len(F) ** 3


def find_zero(F):
    zero = []
    for a in F:
        c = 0
        for b in F:
            if sum_m(a, b) == b:
                c += 1
        if c == len(F):
            zero = a
    return zero


def find_opposite(F):
    zero = find_zero(F)
    r = 0
    for a in F:
        for b in F:
            if sum_m(a, b) == zero:
                r += 1
                break
    return r == len(F)


def commutability_m(F):
    r = 0
    for a in F:
        for b in F:
            if mult_m(a, b) == mult_m(b, a):
                r += 1
    return r == len(F) ** 2


def associativity_m(F):
    r = 0
    for a in F:
        for b in F:
            for c in F:
                if mult_m(mult_m(a, b), c) == mult_m(a, mult_m(b, c)):
                    r += 1
    return r == len(F) ** 3


def find_e(F):
    zero = find_zero(F)
    e = []
    for a in F:
        c = 0
        for b in F:
            if zero:
                if mult_m(a, b) == b and a != zero and b != zero:
                    c += 1
            else:
                if mult_m(a, b) == b:
                    c += 1
        if zero and c == len(F) - 1:
            e = a
        if not zero and c == len(F):
            e = a
    return e


def find_reverse(F):
    e = find_e(F)
    z = find_zero(F)
    r = 0
    for a in F:
        for b in F:
            if z:
                if mult_m(a, b) == e and a != z and b != z:
                    r += 1
                    break
            if not z:
            	if mult_m(a, b) == e:
                    r += 1
                    break
    return r


def distributiveness(F):
    r = []
    for a in F:
        for b in F:
            for c in F:
                if mult_m(sum_m(a, b), c) == sum_m(mult_m(a, b), mult_m(b, c)):
                    if c not in r:
                        r.append(c)
    return r == F


if __name__ == '__main__':

    with open('set.json', 'r') as f:
        st = json.load(f)

    F = st['f']
    N = st['n']
    ax = 0

    print('Коммутативность сложения:')
    if commutability_s(F):
        print('Выполняется')
        ax += 1
    else:
        print('Не выполняется')

    print('Ассоциативность сложения:')
    if associativity_s(F):
        print('Выполняется')
        ax += 1
    else:
        print('Не выполняется')

    print('Нулевой элемент:')
    if find_zero(F):
        print('Существует')
        ax += 1
        print_m(find_zero(F))
    else:
        print('Не существует')

    print('Противоположные элементы:')
    if not find_zero(F):
        print('Нулевой элемент отсутствует, невозможно найти противоположные')
    else:
        if find_opposite(F):
            print('Существуют для всех')
            ax += 1
        else:
            print('Существуют не для всех')

    print('Коммутативность умножения:')
    if commutability_m(F):
        print('Выполняется')
        ax += 1
    else:
        print('Не Выполняется')

    print('Ассоциативность умножения:')
    if associativity_m(F):
        print('Выполняется')
        ax += 1
    else:
        print('Не Выполняется')

    print('Единичный элемент:')
    if find_e(F):
        print('Существует')
        ax += 1
        print_m(find_e(F))
    else:
        print('Не существует')

    print('Обратные элементы для ненулевых элементов:')
    if not find_e(F):
        print('Единичный элемент отсутствует, невозможно найти обратные')
    if find_reverse(F) == len(F) - 1:
        print('Существуют для всех')
        ax += 1
    elif find_reverse(F) == 0:
        print('Не существуют ни для одного элемента')
    else:
        print('Существуют не для всех')

    print('Дистрибутивность умножения относительно сложения:')
    if distributiveness(F):
        print('Выполняется')
        ax += 1
    else:
        print('Не Выполняется')

    if ax == 9:
        ch = 1
        e = find_e(F)
        z = find_zero(F)
        acc = find_e(F)
        while True:
            if acc == z:
                break
            else:
                acc = sum_m(acc, e)
                ch += 1
        if ch == N:
        	print(f'Множетсво F является полем характеристики {ch}')
        else:
        	print(f'Множетсво F не является полем характеристики {N}')
    else:
        print('Множетсво F не является полем')
