import math

from sympy import isprime


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = egcd(b % a, a)
        return g, y - (b // a) * x, x


def mulinv(b, n):
    g, x, _ = egcd(b, n)
    if g == 1:
        return x % n


def check_group(g, b):
    elements = []
    for i in range(1, b):
        elements.append(pow(g, i, b))
    if len(set(elements)) == b - 1:
        return True
    return False


def g_sh_method(g, b, h):
    r = int(math.sqrt(b)) + 1
    ga = [[a, pow(g, a, b)] for a in range(r)]
    ga.sort(key=lambda el: el[1])
    g1 = mulinv(g, b)
    g1 = pow(g1, r, b)
    x = b + 1
    for i in range(r):
        gh = (pow(g1, i, b) * h) % b
        for element in ga:
            if element[1] == gh:
                x = min(x, element[0] + r * i)
            elif element[1] > gh:
                break
    return x


def main():
    g = int(input("Образующий элемент конечной циклической группы G: "))
    b = int(input("Порядок конечной циклической группы G: "))
    h = int(input("Элемент из G: "))
    if not isprime(b):
        print("Введено некорректное значение порядка!")
        exit(0)
    if not check_group(g, b):
        print("Введено некорректное значение образующего элемента!")
        exit(0)
    if not 0 <= h <= b - 1:
        print("Введено некорректное значение элемента группы!")
        exit(0)
    x = g_sh_method(g, b, h)
    print("Значение x = {}".format(x))


if __name__ == '__main__':
    main()
