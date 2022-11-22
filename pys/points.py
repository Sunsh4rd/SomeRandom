def pp(x1, y1, x2, y2, a, p):
    if x1 == x2:
        alpha = ((3*x1*x1 + a) * pow(2*y1, -1, p)) % p
    else:
        alpha = ((y1 - y2) * pow(x1 - x2, -1, p)) % p
    print(alpha, end=' ')
    x3 = (pow(alpha, 2, p)-x1-x2) % p
    y3 = (alpha*(x1-x3) - y1) % p
    return x3, y3

def legendre(a, p):
    res = pow(a, (p-1)//2, p)
    if res == p-1:
        return -1
    if res == 1:
        return 1 

def y2slegendre():
    for x in range(11):
        y2 = (x**3+2*x+1)%11
        leg = legendre(y2,11)
        if leg != -1:
            print(x, y2, leg)

# y2slegendre()
print('----------')
def ysfromy2s():
    for y2 in (1,4,1,4,9,1,0,9):
        for y in range(11):
            if (y*y) % 11 == y2:
                print(y2, y)

# ysfromy2s()

# print(pp(10,3,1,5,7,11))


p = (64032, 10)
b = 101
m = 64033
for i in range(2):
    try:
        np = pp(*p, 64032, 10, b, m)
        p = (np[0], np[1])
        print(p)
    except Exception as e:
        print('...')
        break


# print(pp(4,5,2,3,2,11))