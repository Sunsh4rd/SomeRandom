def pp(x1, y1, x2, y2, a, p):
    if x1 == x2 and -y1 % p == y2:
        return None
    if x1 == x2:
        alpha = ((3*x1*x1 + a) * pow(2*y1, -1, p)) % p
    else:
        alpha = ((y1 - y2) * pow(x1 - x2, -1, p)) % p
    print(alpha, end=' ')
    x3 = (pow(alpha, 2, p)-x1-x2) % p
    y3 = (alpha*(x1-x3) - y1) % p
    return x3, y3


def legendre(a, p):
    if a == 0:
        return 0
    res = pow(a, (p-1)//2, p)
    if res == p-1:
        return -1
    if res == 1:
        return 1


def y2slegendre():
    for x in range(11):
        y2 = (x**3+7*x+3) % 11
        leg = legendre(y2, 11)
        if leg != -1:
            print(x, y2, leg)


# y2slegendre()
# print('----------')


def ysfromy2s():
    for y2 in (3, 0, 3, 9, 3):
        for y in range(11):
            if (y*y) % 11 == y2:
                print(y2, y)


def table():
    print('x\ty^2=x^3+7x+3\ty\t(y^2+7x+3 / 11)')
    for x in range(11):
        y2np = x**3+7*x+3
        y2 = (x**3+7*x+3) % 11
        leg = legendre(y2, 11)
        if leg != -1:
            # for y2 in (3, 0, 3, 9, 3):
            ys = []
            for y in range(11):
                if (y*y) % 11 == y2:
                    ys.append(y)
        else:
            ys = ['-']
        print(f'{x}\t{y2np}(mod 11)={y2}\t{ys}\t{leg}')


# ysfromy2s()


def main():
    # table()
    # ps = [(0,5),(0,6),(1,0),(2,5),(2,6),(5,3),(5,8),(9,5),(9,6)]
    pi = (0,5)
    qs = [(0,5),(0,6),(1,0),(2,5),(2,6),(5,3),(5,8),(9,5),(9,6)]
    for q in qs:
        print(f'{pi} + {q} = ',pp(*pi,*q,7,11))


if __name__ == '__main__':
    main()



# p = (9,6)
# a = 7
# m = 11
# print(f'1 p {p}')
# for i in range(11):
#     try:
#         np = pp(*p, 9, 6, a, m)
#         p = (np[0], np[1])
#         print(f'{i+2} p {p}')
#     except Exception as e:
#         print('...')
#         break


# print(pp(4,5,2,3,2,11))
