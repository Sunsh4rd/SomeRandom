def read_numbers_from_txt_file(file):
    with open(file, 'r') as f:
        numbers = [int(i) for i in f.readlines()]

    return numbers


def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def main():
    a, b, m = read_numbers_from_txt_file('numbers.txt')
    d, q, r = gcd_extended(a, m)
    print(d, q, r)
    if b % d != 0:
        print('Не имеет решений')
    else:
        x0 = (q * b // d) % m
        print(x0, m)
        m1 = m // d
        print(m, d)
        print(list(range(1,d)))
        xn = [(x0 + i * m1) % m for i in range(1, d)]
        print(x0, xn)
        



if __name__ == '__main__':
    main()
