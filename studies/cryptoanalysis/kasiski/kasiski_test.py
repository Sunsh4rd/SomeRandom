import math
from collections import Counter


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
    start, end = map(int, input('Длина подслова(от-до): ').split())
    l = []
    for j in range(start, end + 1):
        for i in range(len(text) - 1):
            s = text[i:i + j]
            try:
                res = text.index(s, text.index(s, i) + 1) - text.index(s, i)
                # print(s, res)
                l.append(res)
            except ValueError:
                continue
    # print(l)
    d = {}
    for i in range(2, 24):
        d[i] = sum(map(lambda item: item % i == 0, l))
    print(d)
    od = [k for k, v in sorted(d.items(), key=lambda item: item[1])]
    print("Вероятнее всего длинна ключа равна одному из чисел: ",
          od[-6:-1] + [od[-1]])

    # subs_len = int(input('Длина подслова: '))
    #
    # subs_pos = {}
    # for i in range(len(text)):
    #     subs = text[i: i + subs_len]
    #     if len(subs) < subs_len:
    #         continue
    #     found = list(find_all(subs, text))
    #     if len(found) == 1:
    #         continue
    #     subs_pos[subs] = found
    #
    # print(subs_pos)
    #
    # subs_dists = []
    # for subs, idx in subs_pos.items():
    #     for i in range(len(idx)-1):
    #         subs_dists.append(idx[i+1]-idx[i])
    #
    # d = {}
    # for i in range(2, 24):
    #     d[i] = sum(map(lambda item: item % i == 0, subs_dists))
    # print(d)
    # od = [k for k, v in sorted(d.items(), key=lambda item: item[1])]
    # print("Вероятнее всего длинна ключа равна одному из чисел: ",
    #       od[-6:-1] + [od[-1]])

    # print(subs_dists)

    # divisors = []
    # for dist in subs_dists:
    #     for d in range(2, int(math.sqrt(dist))+1):
    #         if dist % d == 0:
    #             divisors.append(d)
    # print(divisors)

    # count = Counter(divisors)
    # print(count)
    # print(f'Наиболее вероятные длины ключа: {list(count.keys())}')
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
