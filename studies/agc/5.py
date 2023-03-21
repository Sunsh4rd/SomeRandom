from sympy import legendre_symbol


def pp(x1, y1, x2, y2, a, p):
    if x1 == x2 and -y1 % p == y2:
        return None
    if x1 == x2:
        alpha = ((3*x1*x1 + a) * pow(2*y1, -1, p)) % p
    else:
        alpha = ((y1 - y2) * pow(x1 - x2, -1, p)) % p
    x3 = (pow(alpha, 2, p)-x1-x2) % p
    y3 = (alpha*(x1-x3) - y1) % p
    return x3, y3


def discriminant(a, b, p):
    return (4*a**3+27*b**2) % p


def points(a, b, p):
    print(f'x\ty^2=x^3+{a}x+{b}\ty\t(y^2+{a}x+{b}3 / 11)')
    pts = [0]
    legs = []
    for x in range(11):
        y2np = x**3+a*x+b
        y2 = (x**3+a*x+b) % p
        leg = legendre_symbol(y2, p)
        legs.append(leg)
        if leg != -1:
            ys = []
            for y in range(11):
                if (y*y) % 11 == y2:
                    ys.append(y)
        else:
            ys = ['-']
        for yi in ys:
            if yi != '-':
                pts.append((x, yi))
        print(f'{x}\t{y2np}(mod 11)={y2}\t{ys}\t{leg}')
    return pts, legs


def curve_order(legs, p):
    return p+1+sum(legs)


def sums_table(points, a, m):
    sums = []
    for p in points:
        for q in points:
            sums.append(f'{p} + {q} = {pp(*p,*q,a,m) or 0}')
    return sums


def find_generator(points, a, m, o):
    for g in points:
        gi = g
        gj = g
        for i in range(o):
            try:
                gn = pp(*gj, *gi, a, m)
                gj = (gn[0], gn[1])
            except Exception:
                break
        if i+2 == o:
            return g
    else:
        return None


def main():
    a = int(input('Коэффициент уравнения a = '))
    b = int(input('Коэффициент уравнения b = '))
    m = int(input('Модуль m = '))
    dis = discriminant(a, b, m)
    print(f'Дискриминант равен {dis}')
    if dis != 0:
        print(
            f'Уравнение y^2 = x^3 + {a}x + {b} задает эллиптическую кривую над Z({m})')
        pts, leg = points(a, b, m)
        order = curve_order(leg, m)
        print(f'Порядок кривой = {order}')
        print(f'Точки кривой {pts}')
        print(pts[1:])
        print('Таблица сложения точек:')
        table = sums_table(pts[1:], a, m)
        for t in table:
            print(t)
        gen = find_generator(pts[1:], a, m, order)
        if gen:
            print(f'Группа является циклической.\nПорождающий элемент: {gen}')
        else:
            print('Группа не является циклической')

    else:
        print(
            f'Уравнение y^2 = x^3 + {a}x + {b} не задает эллиптическую кривую над Z({m})')
        exit()


if __name__ == '__main__':
    main()
