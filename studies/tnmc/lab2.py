from random import randint


def chain(a_1, a_2):
    q = []
    while (a_1 % a_2 != 0):
        q.append(a_1//a_2)
        a_1 %= a_2
        a_1, a_2 = a_2, a_1
    q.append(a_1 // a_2)
    return q


def euclid_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = euclid_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def modular_multiplicative_inverse(a, m):
    g, x, _ = euclid_extended(a, m)
    if g != 1:
        return None
    else:
        return (x % m + m) % m


def diophantus(a, b, c):
    gcd, x, y = euclid_extended(a, b)
    p, q = [0, 1], [1, 0]
    q_chain = chain(a, b)

    for i in range(len(q_chain)):
        p.append(q_chain[i] * p[i + 1] + p[i])
        q.append(q_chain[i] * q[i + 1] + q[i])
    p = p[2:]
    q = q[2:]
    if c % gcd == 0:
        k = len(p)
        a //= gcd
        b //= gcd
        c //= gcd
        x = (-1) ** k * q[-2] * c + b
        y = -1 * ((-1) ** k * p[-2] * c + a)
    return x, y


def linear_comparison(a, b, m):
    x, y = diophantus(a, m, b)
    x %= m
    return x


def legendre(a, p):
    if a == 1:
        return 1
    b = a % p
    if b > p // 2:
        b -= p
    if b > 0:
        t = 2
    else:
        t = 1
        b = -b
    k = 0
    while b % 2 == 0:
        b //= 2
        k += 1
    c = b
    t_1 = 1
    if t % 2 == 1:
        t_1 = pow(-1, (p - 1) // 2)
    k_1 = 1
    if k % 2 == 1:
        k_1 = pow(-1, (p * p - 1) // 8)
    if c == 1:
        return t_1 * k_1
    return t_1 * k_1 * pow(-1, ((c - 1) // 2) * ((p - 1) // 2)) * legendre(p, c)


def jacobi(a, p):
    if euclid_extended(a, p)[0] != 1:
        return 0
    r = 0
    t = 1
    a = a % p
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if p % 8 == 3 or p % 8 == 5:
                t = -t
        r = p
        p = a
        a = r
        if a % 4 == 3 and p % 4 == 3:
            t = -t
        a = a % p
    if p == 1:
        return t


def min_k(a, p, q):
    k = 0
    while (a ** (2 ** k * q)) % p != 1:
        k += 1
    return k


def sqrt(a, p):
    q = p - 1
    m = 0
    while q % 2 == 0:
        q //= 2
        m += 1
    b = randint(1, p)
    while legendre(b, p) != -1:
        b = randint(1, p)
    _as = []
    ks = []
    _as.append(a)
    k = min_k(a, p, q)
    ks.append(k)
    while k != 0:
        a = (a * b ** (2 ** (m - k))) % p
        k = min_k(a, p, q)
        _as.append(a)
        ks.append(k)
    rs = []
    r = (_as[len(_as) - 1] ** ((q + 1) // 2)) % p
    rs.append(r)
    for i in range(0, len(_as) - 1):
        bc = b ** (2 ** (m - ks[len(ks) - i - 2] - 1))
        r = (rs[i] * modular_multiplicative_inverse(bc, p)) % p
        rs.append(r)
    return rs[0]


def main():
    opt = input("0 - разложение в цепную дробь\n1 - решения диофантова уравнения \n2 - вычисление обратного элемента в кольце\n3 - решение линейного сравнения\n4 - вычисление символов Лежандра и Якоби\n5 - извлечение квадратных корней в кольце вычетов\n6 - выход\n")
    if opt == '0':
        m, n = int(input('Числитель дроби = ')), int(
            input('Знаменатель дроби = '))
        print('Разложение в цепную дробь =', chain(m, n))

    if opt == '1':
        m, n, c = int(input('Число a = ')), int(
            input('Число b = ')), int(input('Число c = '))
        print('Решение диафантова уравнения =', (diophantus(m, n, c)))

    if opt == '2':
        a, m = int(input('Число a = ')), int(
            input('Модуль m = '))
        print('Обратный элемент по заданному модулю =',
              modular_multiplicative_inverse(a, m))

    if opt == '3':
        m, n, c = int(input('Число a = ')), int(
            input('Число b = ')), int(input('Модуль m = '))
        print('Решение линейного сравнения =', diophantus(m, c, n)[0] % c)

    if opt == '4':
        a, n = int(input('Число а = ')), int(input('Число p = '))
        print('Символ Лежандра = ', legendre(a, n))
        print('Символ Якоби = ', jacobi(a, n))

    if opt == '5':
        a, p = int(input('Число a = ')), int(input('Модуль p = '))
        print('Квадратный корень a по модулю p =', sqrt(a, p))

    if opt == '6':
        exit()


if __name__ == '__main__':
    main()
