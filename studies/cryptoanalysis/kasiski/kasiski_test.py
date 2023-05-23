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
    print(l)

#     # d = {}
#     # for i in range(2, 50):
#     #     d[i] = sum(map(lambda item: item % i == 0, l))
#     # print(d)
#     # od = [k for k, v in sorted(d.items(), key=lambda item: item[1])]
#     # print("Вероятнее всего длинна ключа равна одному из чисел: ",
#     #       od[-6:-1] + [od[-1]])
#
#     subs_len = int(input('Длина подслова: '))
#
#     subs_pos = {}
#     for i in range(len(text)):
#         subs = text[i: i + subs_len]
#         if len(subs) < subs_len:
#             continue
#         found = list(find_all(subs, text))
#         if len(found) == 1:
#             continue
#         subs_pos[subs] = found
#
#     print(subs_pos)
#
#     subs_dists = []
#     for subs, idx in subs_pos.items():
#         for i in range(len(idx)-1):
#             subs_dists.append(idx[i+1]-idx[i])
#
#     print(subs_dists)
#     print(math.gcd(*subs_dists))
#     #
#     # d = {}
#     # for i in range(2, 24):
#     #     d[i] = sum(map(lambda item: item % i == 0, subs_dists))
#     # print(d)
#     # od = [k for k, v in sorted(d.items(), key=lambda item: item[1])]
#     # print("Вероятнее всего длинна ключа равна одному из чисел: ",
#     #       od[-6:-1] + [od[-1]])
#
#     # print(subs_dists)
#
#     # divisors = []
#     # for dist in subs_dists:
#     #     for d in range(2, int(math.sqrt(dist))+1):
#     #         if dist % d == 0:
#     #             divisors.append(d)
#     # print(divisors)
#
#     # count = Counter(divisors)
#     # print(count)
#     # print(f'Наиболее вероятные длины ключа: {list(count.keys())}')
#     # res = text.index(subs, text.index(subs, i) + 1) - text.index(subs, i)
#     #     # print(s, res)
#     #     l.append(res)
#     #     continue
#     # print(l)
#     # d = {}
#     # for i in range(2, 50):
#     #     d[i] = sum(map(lambda item: item % i == 0, l))
#     # print(d)
#     # od = [k for k, v in sorted(d.items(), key=lambda item: item[1])]
#     # print("Вероятнее всего длинна ключа равна одному из чисел: ", od[-6:-1] + [od[-1]])
#     # return math.gcd(*l)

# from sympy import divisors
#
#
# def kasiski():
#     text = open("params/ciphertext.txt", 'r', encoding='utf-8').read()
#
#     low = int(input('Введите нижнюю границу длины n-грамм: '))
#     while low < 3 or low >= len(text):
#         low = int(input('Неправильная длина!: '))
#     high = int(input('Введите верхнюю границу длины n-грамм: '.format(low)))
#     while high < low or high >= len(text):
#         high = int(input('Неправильная длина: '))
#
#     lens_gcds = {}
#     from math import gcd
#     for l in range(low, high + 1):
#         seqs = {}
#         for i in range(len(text) - l + 1):
#             seq = text[i:(i + l)]
#             if seq not in seqs:
#                 seqs[seq] = []
#             seqs[seq].append(i + 1)
#         # вычисление GCD
#         lens_gcds[l] = {}
#         for seq in seqs.keys():
#             dists = []
#             for i in range(1, len(seqs[seq])):
#                 dists.append(seqs[seq][i] - seqs[seq][i - 1])
#             gcd_dist = 0
#             # считаем НОД от всего списка расстояний между встречами n-граммы seq
#             if len(dists):
#                 gcd_dist = dists[0]
#                 for i in range(1, len(dists)):
#                     gcd_dist = gcd(gcd_dist, dists[i])
#
#             # считаем, сколько раз встретился каждый НОД для n-граммы
#             if gcd_dist != 0:
#                 if gcd_dist not in lens_gcds[l].keys():
#                     lens_gcds[l][gcd_dist] = 0
#                 lens_gcds[l][gcd_dist] += 1
#
#     with open('params/test.txt', 'w', encoding='utf-8') as prob_len:
#         gcd_dividers_dict = {}
#         for l in range(low, high + 1):
#             prob_len.write('Последовательность длины: {}\n\n'.format(str(l)))
#             for gcd_dist in sorted(lens_gcds[l].items(), key=lambda x: (-x[1], x[0])):
#                 if gcd_dist[0] != 1:
#                     gcd_deviders = divisors(gcd_dist[0])
#                     for divider in gcd_deviders:
#                         if divider != 1:
#                             if divider not in gcd_dividers_dict.keys():
#                                 gcd_dividers_dict[divider] = 0
#                             gcd_dividers_dict[divider] += 1
#
#                     prob_len.write('{}:{}\n'.format(gcd_dist[0], gcd_dist[1]))
#             prob_len.write('\n\n')
#
#         prob_len.write('Частота встречаемости делителей всех НОД:\n')
#         for i in sorted(gcd_dividers_dict.items(), key=lambda x: (-x[1], x[0])):
#             prob_len.write('{}:{}\n'.format(i[0], i[1]))
