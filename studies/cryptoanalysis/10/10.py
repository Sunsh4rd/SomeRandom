import math


def p_pollard():
    print("Введите нечетное n = ", end='')
    n = int(input())
    print("Введите начальное значение с = ", end='')
    c = int(input())

    # Функция Полларда

    # Алгоритм
    # 1 шаг
    a = c
    b = c

    while True:
        # 2 шаг
        a = (a ** 2 + 1) % n
        b = (b ** 2 + 1) % n
        b = (b ** 2 + 1) % n

        # 3 шаг
        d = math.gcd(a - b, n)
        if 1 < d < n:
            p = d
            print(f'{p=}')
            break
        elif d == n:
            print("Делитель не найден")
            break


p_pollard()
