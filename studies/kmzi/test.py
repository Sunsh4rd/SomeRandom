# t1 = 'aaabcbcead'
# t2 = 'bcaaaadebc'

# t1 = 'aaabcbcead'
# t2 = 'bcaaabcead'

# t1 = 'бавгедёжизйк'
# t2 = 'багведжёизкй'

# t1 = 'абвгдеёжзийк'
t1 = 'бавгедёжизйк'
t2 = 'авбедгёзжкйй'

# t1 = 'вбаедгзжёкйи'
# t2 = 'вбагёеджйизк'

# t1 = 'aabcdeegfigk'
# t2 = 'baaceedggifk'


ps = []


def check(t1, t2, p):
    for o in range(0, len(t1), len(p)):
        for i in range(len(p)):
            if t1[o + i] != t2[o + p[i]]:
                return False
    return True


def get_permutations(x, y, p, i):
    if i == len(p):
        if check(t1, t2, p):
            ps.append(p[:])
        return
    for j in range(len(x)):
        if x[i] == y[j] and j not in p:
            p[i] = j
            get_permutations(x, y, p, i+1)
    p[i] = None


def check_block(b1, b2):
    get_permutations(b1, b2, [None] * len(b1), 0)


if sorted(t1) != sorted(t2):
    print('Невозможно получить одну перестановку из другой')
    exit(0)

for x in range(1, len(t1)+1):
    split_text1 = [t1[i:i + x] for i in range(0, len(t1), x)]
    split_text2 = [t2[i:i + x] for i in range(0, len(t2), x)]

    if len(split_text1[0]) == len(split_text1[-1]):
        blocks_to_check = list(zip(split_text1, split_text2))

        for b1, b2 in blocks_to_check:
            if sorted(b1) != sorted(b2):
                break
            try:
                check_block(b1, b2)
            except Exception:
                print('pass')

if ps:
    if len(ps[0]) < len(t1):
        print(f'Перестановки имеют длины блока { len(ps[0]) }')
    else:
        print(f'Перестановки имеют длины блока { len(t1) }')
else:
    print('Перестановки имеют разные длины блока')
