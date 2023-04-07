import math


def find_all(sub, src):
    start = 0
    while True:
        try:
            start = src.index(sub, start)
        except ValueError:
            break
        yield start
        start += len(sub)


def kasiski():
    with open('params/ciphertext.txt', 'r', encoding='utf-8') as f:
        text = f.read().lower()

    subs_len = int(input('Длина подслова: '))

    subs_pos = {}
    for i in range(len(text)):
        subs = text[i: i + subs_len]
        found = list(find_all(subs, text))
        if len(found) == 1:
            continue
        subs_pos[subs] = found

    print(subs_pos)

    subs_dists = []
    for subs, idx in subs_pos.items():
        for i in range(len(idx)-1):
            subs_dists.append(idx[i+1]-idx[i])

    print(subs_dists)


        # res = text.index(subs, text.index(subs, i) + 1) - text.index(subs, i)
        #     # print(s, res)
        #     l.append(res)
        #     continue
    # print(l)
    # d = {}
    # for i in range(2, 50):
    #     d[i] = sum(map(lambda item: item % i == 0, l))
    # print(d)
    # od = [k for k, v in sorted(d.items(), key=lambda item: item[1])]
    # print("Вероятнее всего длинна ключа равна одному из чисел: ", od[-6:-1] + [od[-1]])
    # return math.gcd(*l)
