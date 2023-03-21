from sympy.polys.galoistools import gf_monic
from sympy.polys.galoistools import gf_div
from sympy.polys.galoistools import gf_sub_mul
from sympy.polys.galoistools import gf_mul_ground
from sympy.polys.domains import ZZ
from sympy import rem
from sympy import poly
from sympy.abc import x
import numpy as np
from sympy import *
x = symbols('x')


def without_zero(h):  # Функция удаляющая члены с 0-ми коэффициентами
    ind = 0  # при старших степенях,
    for b in h:  # чтобы не было 0x^3 + 0x^2 + 3x +1
        if b == 0:
            ind += 1
        else:
            break
    h = h[ind:]
    return h


def gf_gcdex(f, g, p, K):  # Функция нахождения НОД многочленов
    # над полем Галуа (расширенный Евклид)
    if not (f or g):
        return [K.one], [], []
    p0, r0 = gf_monic(f, p, K)
    p1, r1 = gf_monic(g, p, K)
    if not f:
        return [], [K.invert(p1, p)], r1
    if not g:
        return [K.invert(p0, p)], [], r0
    s0, s1 = [K.invert(p0, p)], []
    t0, t1 = [], [K.invert(p1, p)]
    while True:
        Q, R = gf_div(r0, r1, p, K)
        if not R:
            break
        (lc, r1), r0 = gf_monic(R, p, K), r1
        inv = K.invert(lc, p)
        s = gf_sub_mul(s0, s1, Q, p, K)
        t = gf_sub_mul(t0, t1, Q, p, K)
        s1, s0 = gf_mul_ground(s, inv, p, K), s1
        t1, t0 = gf_mul_ground(t, inv, p, K), t1
    return s1, t1, r1


def to_list(r):  # полином переводим в список коэффициентов
    a = []
    for j in range(0, n+1):
        a.append(r.coeff(x, j))
    return a


def from_list(l):  # список коэффициентов переводим в полином
    var = x - x
    i = 0
    for a in l:
        var += a * x**i
        i += 1
    return var


def obr(x, p):  # ищем обратный элемент в поле
    for b in range(0, p):  # (нужно будет заменить деление умножением)
        if (x * b) % p == 1:
            return b


p = 13  # Дано
f = x**4 + 4*x**3 + x**2 + 2*x + 8
n = 4

I = np.zeros((n, n), dtype=np.int32)  # Единичная матрица
for i in range(0, n):
    I[i][i] = 1

# Формируем матрицу элементов конечного поля
# Здесь нужно делить одночлен вида x^ip на f для всех i от 0 до n
# При таком делении будем получать многочлен в остатке
# Коэффициенты этого многочлена и составляют матрицу
Q = []
for i in range(0, n):
    q, r = div(x**(i*p), f, domain='QQ')
    a = []
    for j in range(0, n):
        a.append(r.coeff(x, j) % p)
    Q.append(a)
Q = np.asarray(Q)
Q = (Q-I) % p


# Далее находим нуль-базис матрицы Q-I
V = []
r = 0
c = [-1] * (n)

for k in range(0, n):
    j = 0

    t = False
    # В k-й строке будем искать ненулевой элемент и запоминать в каком он столбце
    for z in range(0, n):
        if Q[k][z] != 0 and c[z] < 0:
            j = z
            t = True
            break
    # Если такой элемент вообще нашелся
    if t:
        # То j-й столбец умножим на -1/этот_элемент
        Q[:, j] = (Q[:, j] * -1*obr(Q[k][j], p)) % p
        # Затем к каждому i-му столбцу кроме j-го будем прибавлять j-й столбец
        # умноженный на i-й элемент k-й строки
        for i in list(range(0, j)) + list(range(j+1, n)):
            q = (Q[:, j]*Q[k][i]) % p
            Q[:, i] = (Q[:, i] + q) % p
        # В с отмечаем столбцы которые уже брали
        c[j] = k
    # Если такого элемента нет
    else:
        # То ранг увеличиваем на единицу и добавляем в список векторов нуль-базиса
        # элементы k-й строки матрицы которрые соответствуют уже рассмотренным столбцам
        r += 1
        V.append([0] * (n))
        for s in range(0, n):
            j = c[s]
            if j >= 0:
                V[-1][j] = Q[k][s]
        V[-1][k] = 1
V = np.asarray(V)


# Основной цикл
t = 0
m = 0
U = []
# Добавляем в список множителей сам полином f
U.append(f)

for m in range(0, r):
    if t < r:
        for j in range(1, r):
            if t < r:
                for s in range(0, p):
                    if t < r:
                        # Будем искать НОД полиномов уже хранящихся в U и полиномов
                        # построенных на основе векторов нуль-базиса
                        u = to_list(U[m])
                        v = V[j].copy()
                        v[0] = v[0] - s
                        v = list(v)
                        u.reverse()
                        v.reverse()
                        u = without_zero(u)
                        v = without_zero(v)
                        h = gf_gcdex(u, v, p, ZZ)[2]
                        h.reverse()
                        if from_list(h) != 1:
                            if h == U[m]:
                                break
                            else:
                                # Если такой НОД найден и полиномы не оказались взаимнопростыми
                                # и этот НОД не совпадает с тем что уже есть в U
                                # то добавляем его в список U
                                t += 1
                                U.append(from_list(h))
                                h.reverse()
                                Um = gf_div(u, h, p, ZZ)[0]
                                Um.reverse()
                                U[m] = from_list(Um)


print(U)
