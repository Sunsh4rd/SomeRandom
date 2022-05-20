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

    @staticmethod
    def five_parameters(nc, iv):
        values = []
        n = nc
        p, w = iv[0], iv[1]
        y1p = iv[-1]
        q1, q2, q3 = iv[2], iv[3], iv[4]
        x_init = [int(d) for d in bin(y1p)[2:]]
        x_init = [0] * (p - len(x_init)) + x_init
        x_all = x_init[:]
        for _ in range(n):
            for _ in range(w):
                next_bit = x_all[0] ^ x_all[q1] ^ x_all[q2] ^ x_all[q3]
                x_all.append(next_bit)
                x_all.pop(0)
            values.append(int(''.join(str(x)
                          for x in x_all[-1:-w-1:-1][::-1]), 2))
        return values

    @staticmethod
    def rsa(nc, iv):
        values = []
        c = nc
        n, e, x0, w, l = iv
        x_all = []
        for _ in range(c):
            x0 = pow(x0, e, n)
            xi_b = [int(d) for d in bin(x0)[2:]]
            xi_b = [0] * (w - len(xi_b)) + xi_b
            xi_b = xi_b[::-1][:w][::-1]
            x_all += xi_b
            values.append(int(''.join(str(x) for x in x_all[:l]), 2))
            x_all = x_all[l:]
        return values

    @staticmethod
    def bbs(nc, iv):
        values = []
        c = nc
        n, x0, l = iv
        for _ in range(c):
            x_bin = []
            for _ in range(l):
                x0 = pow(x0, 2, n)
                x_bin.append(x0 % 2)
            values.append(int(''.join(str(x) for x in x_bin), 2))
        return values

    @staticmethod
    def rc4(nc, iv):
        values = []

        n = nc
        w, k = iv[0], iv[1:]
        s = list(range(256))
        j = 0
        for i in range(256):
            j = (j + s[i] + k[i]) % 256
            s[i], s[j] = s[j], s[i]

        i = 0
        j = 0
        bitSequence = ''

        temp = (w * n)//8 + 1
        for u in range(temp):
            i = (i + 1) % 256
            j = (j + s[i]) % 256
            s[i], s[j] = s[j], s[i]
            x = s[(s[i] + s[j]) % 256]

            xBin = format(x, 'b')
            while len(xBin) < 8:
                xBin = '0' + xBin

            bitSequence += xBin

        xBin = ''

        for i in range(0, len(bitSequence)):
            xBin += bitSequence[i]

            if (i + 1) % w == 0:
                values.append(int(xBin, 2))
                xBin = ''

        return values

    @staticmethod
    def nfsr(nc, iv):
        pass

    @staticmethod
    def mersenne_twister(nc, iv):
        pass


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
        case '5p':
            values = Generator.five_parameters(args.n, args.i)
            with open(args.f, 'w') as f:
                f.write(' '.join(str(x) for x in values))
        case 'rsa':
            values = Generator.rsa(args.n, args.i)
            with open(args.f, 'w') as f:
                f.write(' '.join(str(x) for x in values))
        case 'bbs':
            values = Generator.bbs(args.n, args.i)
            with open(args.f, 'w') as f:
                f.write(' '.join(str(x) for x in values))
        case 'rc4':
            values = Generator.rc4(args.n, args.i)
            with open(args.f, 'w') as f:
                f.write(' '.join(str(x) for x in values))
        case 'nfsr':
            values = Generator.nfsr(args.n, args.i)
            with open(args.f, 'w') as f:
                f.write(' '.join(str(x) for x in values))
        case 'mt':
            values = Generator.mersenne_twister(args.n, args.i)
            with open(args.f, 'w') as f:
                f.write(' '.join(str(x) for x in values))


if __name__ == '__main__':
    main()
