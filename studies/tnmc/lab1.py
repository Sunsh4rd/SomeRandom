from functools import reduce
from time import perf_counter_ns


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

    # print(rs)
    xs = [0] * k
    # print(xs)
    for i in range(k):
        xs[i] = us[i]
        for j in range(i):
            xs[i] = rs[j][i] * (xs[i]-xs[j])
            xs[i] = xs[i] % ms[i]
            if xs[i] < 0:
                xs[i] += ms[i]
    # print(xs, ms)
    res = 0
    for i in range(len(xs)):
        res += xs[i] * reduce(lambda x, y: x * y, ms[:i], 1)
    return res  # xs[0]+xs[1]*ms[0]+xs[2]*ms[0]*ms[1]


def gauss(matrix, m):
    size = len(matrix)

    # for i in range(size):  # если числа в матрице не приведены по модулю
    #     for j in range(len(matrix[i])):
    #         matrix[i][j] %= m

    matrix = [[a % m for a in row] for row in matrix]
    print(matrix)

    # print(matrix, '\n', mod_matrix)

    for i in range(size - 1):
        diagonal_element = matrix[i][i]
        print(matrix[i])
        inverse = modular_multiplicative_inverse(diagonal_element, m)
        print(diagonal_element, inverse)
        # matrix[i] *= inverseToDiagonalElement
        matrix[i] = [(a * inverse) % m for a in matrix[i]]
        # print(matrix[i])
        # matrix[i] = [x % m for x in matrix[i]]

        for j in range(i + 1, size):
            subrow = [(a * matrix[j][i]) % m for a in matrix[i]]
            matrix[j] = [(a - s) % m for a, s in zip(matrix[j], subrow)]
            # matrix[j] -= (matrix[i] * matrix[j][i]) % m
            # matrix[j] %= m

    return matrix


# def main():
#     count = int(input("Введите число уравнений системы: "))
#     m = int(input("Введите количество переменных в уравнениях: "))
#     p = int(input("Введите модуль: "))

#     print("Введите матрицу, составленную из коэффициентов a и b:")
#     matrix = []
#     for i in range(count):
#         row = []
#         for s in input().split():
#             row.append(int(s))
#         matrix.append(row)

#     resMatrix = gaussAlgorithm(np.array(matrix), p)

#     print("Согласно алгоритму Гаусса система уравнений приведена к виду:")
#     result = ""
#     for row in resMatrix:
#         rowSize = len(row)
#         tempRes = ""
#         for i in range(rowSize):
#             rowEl = row[i]
#             if rowEl != 0:
#                 if not tempRes:
#                     tempRes += f'{rowEl} * x{i + 1}'
#                 else:
#                     if i != rowSize - 1:
#                         tempRes += f' + {rowEl} * x{i + 1}'
#                     else:
#                         tempRes += f' = {rowEl}\n'
#         result += tempRes
#     print(result)


def main():
    # a, b = map(int, input().split())
    # print(euclid(a, b))
    # print(euclid_extended(a, b))
    # print(euclid_binary(a, b))
    # print(modular_multiplicative_inverse(14, 5))
    print(gcrt([5, 3, 10], [7, 11, 13]))
    print(gcrt([5, 7, 9], [9, 2, 1]))
    print(gcrt([5, 17, 23], [11, 2, 13]))
    print(gcrt([11, 16, 27, 41, 65], [19, 34, 55, 71, 79]))
    print(gcrt([10, 5, 8], [3, 7, 17]))
    print(garner([5, 3, 10], [7, 11, 13]))
    print(garner([5, 7, 9], [9, 2, 1]))
    print(garner([5, 17, 23], [11, 2, 13]))
    print(garner([11, 16, 27, 41, 65], [19, 34, 55, 71, 79]))
    print(garner([10, 5, 8], [3, 7, 17]))

    resMatrix = gauss(
        [[3, 2, -5, -1], [2, -1, 3, 13], [1, 2, -1, 9]], 5)

    print("Согласно алгоритму Гаусса система уравнений приведена к виду:")
    result = ""
    for row in resMatrix:
        rowSize = len(row)
        tempRes = ""
        for i in range(rowSize):
            rowEl = row[i]
            if rowEl != 0:
                if not tempRes:
                    tempRes += f'{rowEl} * x{i + 1}'
                else:
                    if i != rowSize - 1:
                        tempRes += f' + {rowEl} * x{i + 1}'
                    else:
                        tempRes += f' = {rowEl}\n'
        result += tempRes
    print(result)


if __name__ == '__main__':
    main()
