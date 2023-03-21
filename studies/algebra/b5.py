import warnings
from sympy.polys.galoistools import gf_monic
from sympy.polys.galoistools import gf_div
from sympy.polys.galoistools import gf_sub_mul
from sympy.polys.galoistools import gf_mul_ground
from sympy.polys.domains import ZZ
import numpy.core.numeric as NX
from numpy.lib.twodim_base import diag
from numpy.linalg import eigvals
from numpy.core import (hstack)
import numpy as np


def normalize(poly):
    while poly and poly[-1] == 0:
        poly.pop()
    if poly == []:
        poly.append(0)


def poly_divmod(num, den):
    # Create normalized copies of the args
    num = num[:]
    normalize(num)
    den = den[:]
    normalize(den)

    if len(num) >= len(den):
        # Shift den towards right so it's the same degree as num
        shiftlen = len(num) - len(den)
        den = [0] * shiftlen + den
    else:
        return [0], num

    quot = []
    divisor = float(den[-1])
    for i in range(shiftlen + 1):
        # Get the next coefficient of the quotient.
        mult = num[-1] / divisor
        quot = [mult] + quot

        # Subtract mult * den from num, but don't bother if mult == 0
        # Note that when i==0, mult!=0; so quot is automatically normalized.
        if mult != 0:
            d = [mult * u for u in den]
            num = [u - v for u, v in zip(num, d)]

        num.pop()
        den.pop(0)

    normalize(num)
    return quot, num


def test(num, den):
    print("%s / %s ->" % (num, den))
    q, r = poly_divmod(num, den)
    print("quot: %s, rem: %s\n" % (q, r))
    return q, r


def degree(f):
    try:
        return len(f)-1
    except:
        return 0


def convert_int(x):
    return [x]


def polynomial_subtraction(f, g):
    # subtracting g from f
    new_poly = []
    if type(f) == int:
        f = convert_int(f)
    if type(g) == int:
        g = convert_int(g)
    if len(f) > len(g):
        for i in range(len(g)):
            new_poly.append(f[i] - g[i])
        for j in range(len(g), len(f)):
            new_poly.append(f[j])
    elif len(f) == len(g):
        for i in range(len(f)):
            new_poly.append(f[i] - g[i])
    else:
        for i in range(len(f)):
            new_poly.append(f[i] - g[i])
        for j in range(len(f), len(g)):
            new_poly.append(-g[j])
    return new_poly


def copy_list(f):
    new_poly = []
    for i in range(len(f)):
        new_poly.append(f[i])
    return new_poly


def check(f):
    new_poly = copy_list(f)
    if len(new_poly) == 0:
        return 0
    elif new_poly[len(new_poly)-1] == 0:
        new_poly.pop()
        return check(new_poly)
    else:
        return f


def lead(f):
    try:
        return f[len(f) - 1]
    except:
        return 0


def multiply_polynomials(f, g):
    new_poly = []
    for i in range(len(f) * len(g)):
        new_poly.append(0)
    for i in range(len(f)):
        for j in range(len(g)):
            index = i+j
            new_poly[index] += f[i] * g[j]
    new_poly = check(new_poly)
    return new_poly


def divide_polynomials(f, g):
    if degree(g) == 0 and g[0] == 0:
        warnings.warn("g cannot be the 0 polynomial")
    q = [0]
    r = f
    while r != 0 and degree(r) >= degree(g):
        ti = []
        t = float(lead(r)) / float(lead(g))
        x = degree(r) - degree(g)
        while degree(q) < x:
            q.append(0)
        while degree(ti) < x:
            ti.append(0)
        if x == 0:
            q.append(0)
            ti.append(0)
        q[x] = t
        ti[x] = t
        r = polynomial_subtraction(r, multiply_polynomials(ti, g))

        r = check(r)
    return (q, r)


def convert_to_monic(polynomial):
    if lead(polynomial) != 1:
        new_poly = []
        for i in range(len(polynomial)):
            new_poly.append(polynomial[i]/lead(polynomial))
        return new_poly
    else:
        return polynomial


def gcd(f, g):
    if degree(g) == 0 and g[0] == 0:
        warnings.warn("g cannot be the 0 polynomial")
    if degree(f) >= degree(g):
        ma = f
        mi = g
    else:
        ma = g
        mi = f
    q, r = divide_polynomials(ma, mi)
    if r == 0:
        return mi
    else:
        r1 = convert_to_monic(r)
        return gcd(mi, r1)


def gcdex(f, g, p, K):

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


def berlekamp():
    from numpy.polynomial import Polynomial as P
    import numpy as np

    from numpy.linalg import matrix_rank
    import fractions

    p = np.array([1, 0, 1, 1, 1])

    p1 = np.array([1])
    p2 = np.array([1, 0, 0])
    p3 = np.array([1, 0, 0, 0, 0])
    p4 = np.array([1, 0, 0, 0, 0, 0, 0])

    a1 = np.absolute(np.polydiv(p1, p)[1])[::-1].tolist()
    a2 = np.absolute(np.polydiv(p2, p)[1])[::-1].tolist()
    a3 = np.absolute(np.polydiv(p3, p)[1])[::-1].tolist()
    a4 = np.absolute(np.polydiv(p4, p)[1])[::-1].tolist()

    for i in range(len(a4)-len(a1)):
        a1.append(0)

    for i in range(len(a4)-len(a2)):
        a2.append(0)

    for i in range(len(a4)-len(a3)):
        a3.append(0)

    for i in range(len(a4)-len(a4)):
        a4.append(0)

    x = np.array([a1, a2, a3, a4])

    y = np.absolute(
        x-np.array([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]))
    print(y)

    r = matrix_rank(y)

    print(r)


def roots(p):
    p = np.array(p)
    # find non-zero array entries
    non_zero = NX.nonzero(NX.ravel(p))[0]

    # Return an empty array if polynomial is all zeros
    if len(non_zero) == 0:
        return NX.array([])

    # find the number of trailing zeros -- this is the number of roots at 0.
    trailing_zeros = len(p) - non_zero[-1] - 1

    # strip leading and trailing zeros
    p = p[int(non_zero[0]):int(non_zero[-1])+1]

    
    if not issubclass(p.dtype.type, (NX.floating, NX.complexfloating)):
        p = p.astype(float)

    N = len(p)
    if N > 1:
        # наш полином будет являться характеристическим многочленом сопровождающей матрицы
        # Строим сопровождающую матрицу и находим ее собсвтенные значения (корни)
        A = diag(NX.ones((N-2,), p.dtype), -1)
        A[0, :] = -p[1:] / p[0]
        # находим решения характеристического уравнения матрицы
        roots = eigvals(A)
        # которые равны собственным значениям матрицы, то есть найдем корни полинома
    else:
        roots = NX.array([])

    roots = hstack((roots, NX.zeros(trailing_zeros, roots.dtype)))
    return roots


def poly_horner(A, x):
    p = A[-1]
    i = len(A) - 2
    while i >= 0:
        p = p * x + A[i]
        i -= 1
    return p


def main():
    num = [1, 5, 10, 10, 5, 1]
    den = [1, 2, 1]
    print('div', test(num, den))

    num = [5, 16, 10, 22, 7, 11, 1, 3]
    den = [1, 2, 1, 3]

    q, r = test(num, den)
    print('div', q, r)

    print('div', test([1, 0, -1], [1, -1]))
    print('div', test([1, -2, 1], [1, -1]))

    print('gcd', gcd([1, -2, 1], [1, -1]))
    f = [1, 7, 6, 6]
    g = [1, 1, 2]
    print('gcdex', gcdex(f, g, 3, ZZ))

    polynom = [1, -2, 1]
    rootsPol = roots(polynom)
    rootsInt = []
    for i in rootsPol:
        rootsInt.append(float(i))
    n = len(rootsPol)
    print(rootsInt)

    values = []
    for i in rootsPol:
        values.append(poly_horner(polynom, i))

    print(values)

    print()
    berlekamp()


if __name__ == '__main__':
    main()
