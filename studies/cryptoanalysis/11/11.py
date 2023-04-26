import math
import random


def primes():
    primes_list = []
    with open("primes_database.txt", "r") as f:
        for line in f:
            number = int(line[:-1])
            primes_list.append(number)

    return primes_list[:-1]


def p_1_pollard():
    print("Введите нечетное n = ", end='')
    n = int(input())
    # print("Введите ограничение по базе с = ", end='')
    # c = int(input())

    # 1 шаг алгоритма
    base = primes()

    # 2 шаг алгоритма
    a = random.randint(2, n - 2)
    d = math.gcd(a, n)
    if d >= 2:
        p = d
        return p
    # 3 шаг
    flag = True

    for i in range(len(base)):
        l = int(math.log(n) / math.log(base[i]))
        a = pow(a, base[i] ** l, n)
        d = math.gcd(a - 1, n)
        if d == 1 or d == n:
            flag = False
        else:
            p = d
            return p

    if not flag:
        print("Делитель не найден")


print(p_1_pollard())
