from random import shuffle


def gen_key(n):
    r = list(range(n))
    shuffle(r)
    with open('params/key.txt', 'w', encoding='utf-8') as key_w:
        key_w.write(' '.join(str(i) for i in r))
