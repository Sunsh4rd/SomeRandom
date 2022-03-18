import argparse


def linear_congruential(a, c, x0, m, n):
    values = []
    for i in range(1, n):
        xn = (a*x0 + c) % m
        values.append(xn)
        x0 = xn

    return values


def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-a', type=int)
    # parser.add_argument('-b', type=int)
    # parser.add_argument('-s', '--some', type=int, default=3)
    # args = parser.parse_args()
    # print(args)
    # print(args.a + args.b + args.some)
    print(linear_congruential(3,5,7,10,100))


if __name__ == '__main__':
    main()
