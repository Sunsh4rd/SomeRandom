from collections import Counter
from functools import reduce
from math import gcd


def create_db():
    t = int(input('Число простых сомножителей: '))
    with open('primes.txt', 'r', encoding='utf-8') as pr_r:
        primes = list(map(int, pr_r.read().split('\n')))

    mults = {reduce(lambda x, y: x * y, primes[i: i + t]): primes[i: i + t] for i in range(len(primes) - t + 1)}

    with open('db.txt', 'w', encoding='utf-8') as db_w:
        db_w.write('\n'.join(f"{k} {' '.join(str(i) for i in v)}" for k, v in mults.items()))


def trial_division(n):
    with open('primes.txt', 'r', encoding='utf-8') as pr_r:
        primes = list(map(int, pr_r.read().split('\n')))

    with open('db.txt', 'r', encoding='utf-8') as db_r:
        db = {}
        for line in db_r.read().split('\n'):
            prod = list(map(int, line.split()))
            db[prod[0]] = prod[1:]
    # print(db)
    while True:
        d = list(filter(lambda x: gcd(n, x) != 1, db.keys()))[0]
        # print(d)
        for div in db[d]:
            if n % div == 0:
                yield div
                n //= div
        if n in primes:
            yield n
            break


def main():
    opt = input('1 - Создать базу данных простых чисел\n'
                '2 - Метод пробного деления\n')
    if opt == '1':
        create_db()
    elif opt == '2':
        print(Counter(list(trial_division(int(input('n = '))))))


if __name__ == '__main__':
    main()
