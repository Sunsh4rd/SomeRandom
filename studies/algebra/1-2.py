import math


def read_numbers_from_txt_file(file):
    with open(file, 'r') as f:
        numbers = [int(i) for i in f.readlines()]

    return numbers


def phi(n):
    res = n
    for d in range(2, int(math.sqrt(n)) + 1):
        if n % d == 0:
            while n % d == 0:
                n //= d
            res -= res // d
    if n > 1:
        res -= res // n
    return res


def main():
    a, b, m = read_numbers_from_txt_file('studies\\algebra\\numbers.txt')
    d = math.gcd(a, m)
    if b % d != 0:
        print('Не имеет решений')
    else:
        a1, b1, m1 = a // d, b // d, m // d
        if math.gcd(a1, m1) != 1 or b != b1 * d:
            print('Не имеет решений')
        else:
            x0 = (a1 ** (phi(m1) - 1) * b1) % m1
            xn = [(x0 + i * m1) % m for i in range(1, d)]
            print(x0, xn)


if __name__ == '__main__':
    main()
