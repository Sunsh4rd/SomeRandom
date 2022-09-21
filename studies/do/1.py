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


# k = int(input())
# if k == 1 or k % 10 == 1 and k != 11 and k % 100 != 11:
#     print(f'Мне {k} год')
# elif 2 <= k % 10 <= 4 and not 11 <= k <= 14 and not 11 <= k % 100 <= 14:
#     print(f'Мне {k} года')
# else:
#     print(f'Мне {k} лет')

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


a, b = map(int, input().split())
d, d1, d2 = 1, 0, 0
while a < 1000000:
    a *= 3
    d += 1
    if a == b:
        d1 = d
    d2 = d
print(d1, d2)


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
# x = max(m)
