import random
import sympy as sp
import matplotlib.pyplot as plt


def Legander(a, p):
    res = pow(a, (p-1)//2, p)
    if res == p-1:
        return -1
    if res == 1:
        return 1


def gen_p(n):
    while True:
        p = random.randint(2**(n-1), 2**n)
        if p % 2 != 0 and all(p % x != 0 for x in range(3, int(p**0.5)+1, 2)) and p % 4 == 1:
            break
    return p


def factor(p):
    for i in range(1, int(p**0.5) + 1):
        for j in range(1, int(p**0.5) + 1):
            if i**2 + j**2 == p:
                return i, j


def check_N(p, a, b):
    # N1 = p + 1 - 2*b
    # N2 = p + 1 - 2*a
    # N3 = p + 1 + 2*b
    # N4 = p + 1 + 2*a
    l = [p + 1 - 2*b, p + 1 - 2*a, p + 1 + 2*b, p + 1 + 2*a]
    random.shuffle(l)
    N1, N2, N3, N4 = l[0], l[1], l[2], l[3]
    #print(N1, N2, N3, N4)
    if N1 % 2 == 0:
        if sp.isprime(N1 // 2):
            return N1, N1 // 2, 2
    if N1 % 4 == 0:
        if sp.isprime(N1 // 4):
            return N1, N1 // 4, 4
    if N2 % 2 == 0:
        if sp.isprime(N2 // 2):
            return N2, N2 // 2, 2
    if N2 % 4 == 0:
        if sp.isprime(N2 // 4):
            return N2, N2 // 4, 4
    if N3 % 2 == 0:
        if sp.isprime(N3 // 2):
            return N3, N3 // 2, 2
    if N3 % 4 == 0:
        if sp.isprime(N3 // 4):
            return N3, N3 // 4, 4
    if N4 % 2 == 0:
        if sp.isprime(N4 // 2):
            return N4, N4 // 2, 2
    if N4 % 4 == 0:
        if sp.isprime(N4 // 4):
            return N4, N4 // 4, 4


def check_pr(p, r, m):
    return p != r and all(p**i % r != 1 for i in range(1, m+1))

# def gen_P0 (p, f):
#     # while True:
#     #     x0 = random.randint(1, p-1)
#     #     y0 = random.randint(1, p-1)
#         for x0 in range(1, p-1):
#             for y0 in range(1, p-1):
#                 a = (((pow(y0, 2, p) - pow(x0, 3, p)) % p) * pow(x0, -1, p)) % p
#                 if f == 2:
#                     if Legander(-a, p) == -1 and 2*y0 % p == 0:
#                         return x0, y0, a
#                 if f == 4:
#                     if Legander(-a, p) == 1 and 2*y0 % p == 0:
#                         return x0, y0, a
#         else:
#             print('!!!')
#             return 0,0,0


def gen_P0(p, f):
    if f == 2:
        a = 0
        for i in range(p):
            if Legander(-i, p) == -1:
                a = i
                break
    if f == 4:
        a = 0
        for i in range(p):
            if Legander(-i, p) == 1:
                a = i
                break
    for x0 in range(2, p-1):
        for y0 in range(1, p-1):
            if (((pow(y0, 2, p) - pow(x0, 3, p)) % p) * pow(x0, -1, p)) % p == a:
                return x0, y0, a


def X2(x0, y0, a, p):
    l = (3*x0**3 + a)*pow((2*y0), -1, p) % p
    x1 = (l**2 - 2*x0) % p
    y1 = (l*(x0-x1) - y0) % p
    return x1, y1


def Xpl(x0, y0, x1, y1, a, p):
    l = ((y1 - y0)*pow((x1 - x0), -1, p)) % p
    x2 = (pow(l, 2, p) - x1 - x0) % p
    y2 = (l * (x0-x2) - y0) % p
    return x2, y2


def count_point(Q, N, a, p):
    P = X2(Q[0], Q[1], a, p)

    for i in range(N - 2):
        # print(N, P)
        try:
            P = Xpl(P[0], P[1], Q[0], Q[1], a, p)
        except Exception as e:
            # print(Q, P, N, i)
            return i+2
    return N


def main(n):
    m = 1
    # if n < 7:
    #     print("ERROR!")
    #     return 0, 0, 0, 0
    while True:
        f1 = False
        while not f1:
            p = gen_p(n)
            # p = 61
            if factor(p) != None:
                a, b = factor(p)
            else:
                continue
            N_lst = check_N(p, a, b)
            # print(p,a,b, N_lst)
            if N_lst != None:
                N, r, f = N_lst
                f1 = check_pr(p, r, m)

        #print(a,b, N, r)
        x, y, a = gen_P0(p, f)
        # print(x,y,a)

        if f == 2:
            Q = X2(x, y, a, p)
        if f == 4:
            Q = X2(x, y, a, p)
            Q = Xpl(Q[0], Q[1], x, y, a, p)
            Q = Xpl(Q[0], Q[1], x, y, a, p)
            # Q = X2(Q[0],Q[1], a, p)

        if Q[1] != 0 and count_point(Q, N, a, p) == N:
            print(p, a, Q, r, N)
            return Q, a, p, r


def grafic(Q, a, p, r):
    x = []
    y = []
    q = X2(Q[0], Q[1], a, p)
    x.append(Q[0])
    y.append(Q[1])
    x.append(q[0])
    y.append(q[1])
    while True:
        # if q == (0,0):
        #     break
        try:
            q = Xpl(q[0], q[1], Q[0], Q[1], a, p)
        except Exception as e:
            print(q, Q)
            break

        x.append(q[0])
        y.append(q[1])

    plt.scatter(x, y, s=1)
    plt.show()
