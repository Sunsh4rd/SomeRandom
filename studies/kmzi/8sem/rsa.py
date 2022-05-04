from gen_digits import gen_digits


def main():
    p, q = gen_digits(32), gen_digits(32)
    n = p * q
    print(p, q, n)


if __name__ == '__main__':
    main()
