import argparse
from functools import reduce
from time import perf_counter_ns
import numpy as np


def euclid(a, b):
    return a if b == 0 else euclid(b, a % b)


def euclid_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = euclid_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def euclid_binary(a, b):
    if a == 0 or a == b:
        return b

    if b == 0:
        return a

    if b % 2 == 1 and a % 2 == 1 and b < a:
        return euclid_binary((a - b) // 2, b)

    if b % 2 == 1 and a % 2 == 1 and b > a:
        return euclid_binary((b - a) // 2, a)

    if b % 2 == 0 and a % 2 == 1:
        return euclid_binary(a, b // 2)

    if b % 2 == 1 and a % 2 == 0:
        return euclid_binary(a // 2, b)

    if b % 2 == 0 and a % 2 == 0:
        return 2 * euclid_binary(a // 2, b // 2)


def modular_multiplicative_inverse(a, m):
    g, x, _ = euclid_extended(a, m)
    if g != 1:
        return None
    else:
        return (x % m + m) % m


def gcrt(us, ms):
    M = reduce(lambda x, y: x * y, ms)
    cs = [M // mi for mi in ms]
    ds = [modular_multiplicative_inverse(ci, mi) for ci, mi in zip(cs, ms)]
    return sum((ci * di * ui for ci, di, ui in zip(cs, ds, us))) % M


def garner(us, ms):
    k = len(us)
    rs = []
    for i in range(k):
        tmp = []
        for j in range(k):
            tmp.append(modular_multiplicative_inverse(ms[i], ms[j]))
        rs.append(tmp)

    xs = [0] * k

    for i in range(k):
        xs[i] = us[i]
        for j in range(i):
            xs[i] = rs[j][i] * (xs[i] - xs[j])
            xs[i] = xs[i] % ms[i]
            if xs[i] < 0:
                xs[i] += ms[i]
    res = 0
    for i in range(len(xs)):
        res += xs[i] * reduce(lambda x, y: x * y, ms[:i], 1)
    return res


def gauss(matrix, m):
    size = len(matrix)
    matrix = [[a % m for a in row] for row in matrix]

    for i in range(size - 1):
        diagonal_element = matrix[i][i]
        inverse = modular_multiplicative_inverse(diagonal_element, m)
        matrix[i] = [(a % m * inverse) % m for a in matrix[i]]
        # print(matrix[i])

        for j in range(i + 1, size):
            subrow = [(a % m * matrix[j][i] % m) % m for a in matrix[i]]
            matrix[j] = [(a - s) % m for a, s in zip(matrix[j], subrow)]

    return matrix


def ext_euclid(num1, num2):
    if num1 == 0:
        return num2, 0, 1
    else:
        div, x, y = Ext_Euclid(num2 % num1, num1)
    return div, y - (num2 // num1) * x, x


def Gauss(A, m):
    for i in range(len(A)):
        g, a_, y = Ext_Euclid(A[i][i], m)
        A[i] = (A[i] % m * a_) % m
        # print(A[i])
        if i != len(A) - 1:
            for j in range(i + 1, len(A)):
                A[j] -= (A[i] % m * A[j][i] % m) % m
                A[j] = A[j] % m
    return A


def main():
    main_parser = argparse.ArgumentParser()
    main_parser.add_argument(
        '--alg', choices=['euclid', 'lcs', 'gauss'], required=True)
    algs_subparsers = main_parser.add_subparsers(title='algorithms')

    euclid_parser = algs_subparsers.add_parser('euclid')
    euclid_parser.add_argument(
        '--type', choices=['common', 'ext', 'bin'], required=True)
    euclid_parser.add_argument('-a', type=int, required=True)
    euclid_parser.add_argument('-b', type=int, required=True)

    gcrt_garner_parser = algs_subparsers.add_parser('lcs')
    gcrt_garner_parser.add_argument(
        '--type', choices=['gcrt', 'garner'], required=True)
    gcrt_garner_parser.add_argument('-u', type=int, nargs='+', required=True)
    gcrt_garner_parser.add_argument('-m', type=int, nargs='+', required=True)

    gauss_parser = algs_subparsers.add_parser('gauss')
    gauss_parser.add_argument('-n', type=int, required=True)
    gauss_parser.add_argument('-v', type=int, required=True)
    gauss_parser.add_argument('-m', type=int, required=True)

    args = main_parser.parse_args()

    match args.alg:
        case 'euclid':
            match args.type:
                case 'common':
                    s = perf_counter_ns()
                    print(euclid(args.a, args.b))
                    f = perf_counter_ns()
                    print(f'Время работы (10^-9 с.) {f - s}')
                case 'ext':
                    s = perf_counter_ns()
                    print(euclid_extended(args.a, args.b))
                    f = perf_counter_ns()
                    print(f'Время работы (10^-9 с.) {f - s}')
                case 'bin':
                    s = perf_counter_ns()
                    print(euclid_binary(args.a, args.b))
                    f = perf_counter_ns()
                    print(f'Время работы (10^-9 с.) {f - s}')

        case 'lcs':
            match args.type:
                case 'gcrt':
                    s = perf_counter_ns()
                    print(gcrt(args.u, args.m))
                    f = perf_counter_ns()
                    print(f'Время работы (10^-9 с.) {f - s}')
                case 'garner':
                    s = perf_counter_ns()
                    print(garner(args.u, args.m))
                    f = perf_counter_ns()
                    print(f'Время работы (10^-9 с.) {f - s}')

        case 'gauss':
            matrix = [list(map(int, input().split())) for _ in range(args.n)]
            s = perf_counter_ns()
            print(*gauss(matrix, args.m), sep='\n')  # чет не так
            print(*Gauss(np.array(matrix), args.m), sep='\n')  # норм
            f = perf_counter_ns()
            print(f'Время работы (10^-9 с.) {f - s}')


if __name__ == '__main__':
    main()
