from functools import reduce


def create_db():
    t = int(input('Число простых сомножителей: '))
    with open('primes.txt', 'r', encoding='utf-8') as pr_r:
        primes = list(map(int, pr_r.read().split('\n')))

    mults = {reduce(lambda x, y: x * y, primes[i: i+t]): primes[i: i+t] for i in range(len(primes) - t + 1)}

    with open('db.txt', 'w', encoding='utf-8') as db_w:
        db_w.write('\n'.join(f'{k}: {v}' for k, v in mults.items()))




def main():
    create_db()


if __name__ == '__main__':
    main()