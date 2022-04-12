import argparse


class Generator():

    @staticmethod
    def linear_congruential(**iv):
        values = []
        n, a, c, m, x0 = iv.values()
        for _ in range(n):
            xn = (a*x0 + c) % m
            values.append(xn)
            x0 = xn

        return values

    @staticmethod
    def additive(**iv):
        values = []
        n, s, a_s, xs, c, m = iv.values()
        for i in range(n):
            xi = 0
            for j in range(s):
                xi += a_s[j] * xs[i+j]
            xi += c
            xi %= m
            xs.append(xi)
            values.append(xi)
        return values

    @staticmethod
    def lfsr(**iv):
        values = []
        n, p, s, m, js, y1p = iv.values()
        x_init = [int(d) for d in bin(y1p)[2:]]
        a_s = [1 if i+1 in js else 0 for i in range(p)]
        xs = []
        for i in range(5):
            pass
        return a_s, x_init


def main():
    # parser = argparse.ArgumentParser()
    # parser.add_argument('-a', type=int)
    # parser.add_argument('-b', type=int)
    # parser.add_argument('-s', '--some', type=int, default=3)
    # args = parser.parse_args()
    # print(args)
    # print(args.a + args.b + args.some)
    print(Generator.linear_congruential(n=10, a=3, c=10, m=64, x0=1))
    print(Generator.additive(n=10, s=3, a_s=[
          1, 3, 5], xs=[2, 4, 6], c=7, m=93))
    print(Generator.lfsr(n=None, p=5, s=None, m=None, js=[1, 5], y1p=12))


if __name__ == '__main__':
    main()
