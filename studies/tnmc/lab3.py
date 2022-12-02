from random import randint


def euclid_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = euclid_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def jacobi(a, n):
    if (euclid_extended(a, n)[0] != 1):
        return 0
    if (a < 0):
        return jacobi(-a, n) * -1 ** ((n - 1) // 2)
    if a % 2 == 0:
        return jacobi(a // 2, n) * (-1) ** ((n ** 2 - 1) // 8)
    if a == 1:
        return 1
    if (a < n):
        return jacobi(n, a) * (-1) ** ((a - 1) * ((n - 1) // 4))
    return jacobi(a % n, n)


def fermat(n):
    a = randint(2, n - 2)
    r = pow(a, (n-1), n)
    if r == 1:
        return 'Вероятно простое'
    else:
        return 'Составное'


def solovay_strassen(n):
    a = randint(2, n - 2)
    r = pow(a, (n-1) // 2, n)
    if r != 1 and r != n-1:
        return 'Составное'
    s = jacobi(a, n)
    if r % n == s % n:
        return 'Вероятно простое'
    else:
        return 'Составное'


def miller_rabin(n):
    s = 0
    n_test = n - 1
    while(n_test % 2 == 0):
        s += 1
        n_test //= 2
    r = n_test
    a = randint(2, n - 2)
    y = pow(a, r, n)
    j = 1
    if y != 1 and y != n - 1:
        while j <= s - 1 and y != n - 1:
            y = pow(y, 2, n)
            if y == 1:
                return 'Составное'
            j += 1
    if y != n - 1:
        return 'Составное'
    return 'Веротяно простое'


def main():
    opt = input(
        '0 - Провека тестом Ферма\n1 - Проверка тестом Соловея-Штрассена\n2 - Проверка тестом Миллера-Рабина\n')
    n = int(input('Число для проверки = '))
    if opt == '0':
        print(f'Результат проверки тестом Ферма: {fermat(n)}')
    elif opt == '1':
        print(
            f'Результат проверки тестом Соловея-Штрассена: {fermat(n)}')
    elif opt == '2':
        print(f'Результат проверки тестом Миллера-Рабина: {fermat(n)}')


if __name__ == '__main__':
    main()
