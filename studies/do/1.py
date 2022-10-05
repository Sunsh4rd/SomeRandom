# a = int(input())
# b = int(input())
# print(a + b)


# a = int(input())
# s, m = 0, 1
# while a > 0:
#     s += a % 10
#     m *= a % 10
#     a //= 10

# print(f'{s}\n{m}')


# a = int(input())
# print(f'{a%10}{a//10%10}{a//100}')


# a = int(input())
# print(f'{a//10%10}{a//100}{a%10}')


# print(2 ** (int(input()) // 3))


# y = int(input())
# if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
#     print(29)
# else:
#     print(28)

# my, v = [], []
# for k in range(121):
#     if k == 1 or k % 10 == 1 and k != 11 and k % 100 != 11:
#         my.append(f'Мне {k} год')
#     elif 2 <= k % 10 <= 4 and not 11 <= k <= 14 and not 11 <= k % 100 <= 14:
#         my.append(f'Мне {k} года')
#     else:
#         my.append(f'Мне {k} лет')

# for i in range(121):
#     k = str(i)
#     if k[-1] == '1' and (len(k) == 1 or 11 < int(k) < 111):
#         v.append(f'Мне {k} год')
#     elif k[-1] in ['2', '3', '4'] and (len(k) == 1 or 14 < int(k) < 105):
#         v.append(f'Мне {k} года')
#     else:
#         v.append(f'Мне {k} лет')

# print(my == v)

# m = 1
# while True:
#     a = float(input())
#     if a < 0:
#         break
#     m *= a
# print(f'{m:.6f}')


# n = int(input())
# m = 0
# nm = 0
# for i in range(n):
#     a = int(input())
#     if abs(a) >= m:
#         m = abs(a)
#         nm = i
# print(nm + 1)


# a, b = map(int, input().split())
# leaves, k = a, 1
# while leaves < b:
#     leaves *= 3
#     k += 1
# n = 1
# leaves = a
# s = a
# while s < 10 ** 6:
#     leaves *= 3
#     s += leaves
#     n += 1

# print(k, n)


# n = int(input())
# for i in range(2, int(n**0.5)+1):
# if n % i == 0:
# print('No')
# break
# else:
# print('Yes')


# w = input()
# print(f"{'*'*len(w)}{w}{'*'*len(w)}")


# print(sum(map(int, (x for x in input() if x.isdigit()))))


# print(input()[1::2][::-1])


# print(' '.join(input().split()))

# n = int(input())
# m = [int(input()) for _ in range(n)]
# k = int(input())
# print(*map(lambda x: x*k, m))

# n = int(input())
# m = list(map(int, input().split()))
# m[m.index(max(m))] = -m[m.index(max(m))]
# print(*m)


# n, m, k = map(int, input().split())
# print(sum(filter(lambda x: abs(x) % 10 == k and abs(x) %
#       m != 0, map(int, input().split()))))

# from math import pi
# d = input()
# p, s = d[0], d[2:]
# if p == 'k':
#     r = float(s)
#     print(f'{2 * pi * r:.4f} {pi * r * r:.4f}')
# if p == 'p':
#     a, b = map(float, s.split())
#     print(f'{2 * (a + b):.4f} {a * b:.4f}')
# if p == 't':
#     a, b, c = map(float, s.split())
#     halfp = (a + b + c) / 2
#     print(f'{2*halfp:.4f} {(halfp*(halfp-a)*(halfp-b)*(halfp-c))**0.5:.4f}')

# print(len(set(input().lower())))


# if len(set(input())) == 4:
#     print('NO')
# else:
#     print('YES')


# s1 = input()
# s2 = input()
# print(not set(s2)-set(s1))


# n = int(input())
# l = list(map(int, input().split()))
# print(*list(filter(lambda x: len(str(abs(x))) != len(set(str(abs(x)))), l)))


# roman_numbers = {
#     'I': 1,
#     'V': 5,
#     'X': 10,
#     'L': 50,
#     'C': 100,
#     'D': 500,
#     'M': 1000
# }

# print(roman_numbers.get(input(), 0))

# suits = ['spades', 'clubs', 'diamonds', 'hearts']
# suitsd = {i+1: suits[i] for i in range(4)}

# ranks = ['six', 'seven', 'eight', 'nine',
#          'ten', 'jack', 'queen', 'king', 'ace']
# ranksd = {i+6: ranks[i] for i in range(len(ranks))}

# s, r = map(int, input().split())
# print(f'the {ranksd[r]} of {suitsd[s]}')


# from collections import Counter, defaultdict


# c1 = Counter(input())
# c2 = Counter(input())

# for k, v in c2.items():
#     print(k, v)
#     if v > c1[k]:
#         print(False)
#         break
# else:
#     print(True)

# afasfasssdds

# from typing import Counter
# print(''.join(sorted(k for k, _ in filter(
#     lambda x: x[1] == 1, Counter(input()).items()))))


# a = Counter('anjafa')
# b = {'b': 1}

# print(a['b'])
# print(b['a'])

# d = defaultdict(int)
# print(d)


# def is_power_of_five(n):
#     while n > 1:
#         if n % 5 != 0:
#             return False
#         n //= 5
#     return True


# n = int(input())
# l = map(int, input().split())

# print(len(list(filter(lambda x: is_power_of_five(x), l))))


# def is_prime(n):
#     if n == 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True


# n = int(input())
# # for n in filter(lambda x: not x % 2, range(4, 1001)):
# #     print(f'{n}:')
# for i in range(1, n):
#     if is_prime(i) and is_prime(n-i):
#         print(i, n-i)
#         break


# print(*(filter(lambda x: is_prime(x), range(4, 1000))))


# def swap_min_last(l):
#     l[l.index(min(l))], l[-1] = l[-1], l[l.index(min(l))]


# n, m = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(n)]
# matrix = [[matrix[i][j] for i in range(n)] for j in range(m)]

# for col in matrix:
#     swap_min_last(col)

# matrix = [[matrix[i][j] for i in range(m)] for j in range(n)]

# for row in matrix:
#     print(*row)

# def swap(m):
#     for i in range(len(m)):
#         for j in range(len(m[i])):
#             if not m[i][j] % 2:
#                 m[i][j] = 0


# n, m = map(int, input().split())
# matrix1 = [list(map(int, input().split())) for _ in range(n)]
# matrix2 = [list(map(int, input().split())) for _ in range(n)]

# swap(matrix1)
# swap(matrix2)

# if matrix1 == matrix2:
#     print('YES')
# else:
#     print('NO')


# def transpose(matrix):
#     n, m = len(matrix), len(matrix[0])
#     matrix = [[matrix[j][i] for i in range(m)] for j in range(n)]

# def transpose(m):
#     return list(zip(*m))


# n, m = map(int, input().split())
# matrix = [list(map(int, input().split())) for _ in range(n)]

# for row in transpose(matrix):
#     print(*row)
# matrix = [[matrix[i][j] for i in range(n)] for j in range(m)]


# def mult(a, b):
#     return [[sum(x * y for x, y in zip(a_row, b_col)) for b_col in zip(*b)] for a_row in a]


# n = int(input())
# matrix = [list(map(float, input().split())) for _ in range(n)]

# orig_m = [[e for e in row] for row in matrix]
# for i in range(n-1):
#     matrix = mult(matrix, orig_m)

# for row in matrix:
#     print(''.join(f'{e:.3f} ' for e in row))


# def del_par(s):
#     while '(' in s:
#         s = s.replace(s[s.index('('):s.index(')')+1], '')
#     return s


# n = int(input())
# l = [input() for _ in range(n)]
# print(*map(del_par, l), sep='\n')


def fib(n):
    f, s = 0, 1
    for _ in range(n):
        f, s = s, f+s
    return f


print(fib(int(input())))
