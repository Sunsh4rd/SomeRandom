import argparse


class Generator():
    @staticmethod
    def linear_congruential(nc, iv):
        values = []
        n = nc
        a, c, m, x0 = iv
        for _ in range(n):
            xn = (a*x0 + c) % m
            values.append(xn)
            x0 = xn

        return values

    @staticmethod
    def additive(nc, iv):
        values = []
        n = nc
        s = iv[0]
        c, m = iv[-2], iv[-1]
        a_s, xs, = iv[1:s+1], iv[s+1:2*s+1]
        print(a_s, xs)
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
    def lfsr(nc, iv):
        values = []
        n = nc
        p, s, m = iv[0], iv[1], iv[2]
        js = iv[3:m+3]
        y1p = iv[-1]
        x_init = [int(d) for d in bin(y1p)[2:]]
        x_init = [0] * (p - len(x_init)) + x_init
        x_all = []
        for _ in range(n):
            for _ in range(p):
                next_bit = 0
                for jt in js:
                    next_bit ^= x_init[jt-1]
                if len(x_all) == s:
                    values.append(int(''.join(str(x) for x in x_all), 2))
                    x_all.clear()
                if len(values) == n:
                    break
                x_init.append(next_bit)
                x_all.append(next_bit)
                x_init.pop(0)

        return values


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-g', choices=['lc', 'add', '5p', 'lfsr', 'nfsr', 'mt', 'rc4', 'rsa', 'bbs'], required=True)
    parser.add_argument('-f', default='rnd.dat')
    parser.add_argument('-n', type=int, default=10000)
    parser.add_argument('-i', type=int, nargs='+', required=True)
    args = parser.parse_args()
    match args.g:
        case 'lc':
            values = Generator.linear_congruential(args.n, args.i)
            with open(args.f, 'w') as f:
                f.write(' '.join(str(x) for x in values))
        case 'add':
            values = Generator.additive(args.n, args.i)
            with open(args.f, 'w') as f:
                f.write(' '.join(str(x) for x in values))
        case 'lfsr':
            values = Generator.lfsr(args.n, args.i)
            with open(args.f, 'w') as f:
                f.write(' '.join(str(x) for x in values))


if __name__ == '__main__':
    main()
