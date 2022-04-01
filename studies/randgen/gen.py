import argparse


class Generator():

    @staticmethod
    def linear_congruential(n, a, c, m, x0):
        values = []
        for _ in range(n):
            xn = (a*x0 + c) % m
            values.append(xn)
            x0 = xn

        return values

    @staticmethod
    def additive():
        pass


def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-a', type=int)
    # parser.add_argument('-b', type=int)
    # parser.add_argument('-s', '--some', type=int, default=3)
    # args = parser.parse_args()
    # print(args)
    # print(args.a + args.b + args.some)
    print(Generator.linear_congruential(10, 3, 10, 64, 1))


if __name__ == '__main__':
    main()
