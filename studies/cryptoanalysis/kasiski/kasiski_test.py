import math


def kasiski():
    with open('params/ciphertext.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    l = []
    for j in range(2, 10):
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
    for i in range(2, 50):
        d[i] = sum(map(lambda item: item % i == 0, l))
    print(d)
    od = [k for k, v in sorted(d.items(), key=lambda item: item[1])]
    print("Вероятнее всего длинна ключа равна одному из чисел: ", od[-6:-1] + [od[-1]])
    return math.gcd(*l)
