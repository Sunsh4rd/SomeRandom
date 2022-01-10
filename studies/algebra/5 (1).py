from sympy.polys.galoistools import gf_monic
from sympy.polys.galoistools import gf_degree
from sympy.polys.galoistools import gf_diff
from sympy.polys.galoistools import gf_gcd
from sympy.polys.galoistools import gf_quo
from sympy.polys.domains import ZZ

def gf_sqf_list(f, p, K, all=False):

    n, sqf, factors, r = 1, False, [], int(p)

    lc, f = gf_monic(f, p, K)

    if gf_degree(f) < 1:
        return lc, []

    while True:
        F = gf_diff(f, p, K)

        if F != []:
            g = gf_gcd(f, F, p, K) 
            h = gf_quo(f, g, p, K)#находим целу часть от деления

            i = 1

            while h != [K.one]:
                G = gf_gcd(g, h, p, K)
                H = gf_quo(h, G, p, K)

                if gf_degree(H) > 0:
                    factors.append((H, i*n))

                g, h, i = gf_quo(g, G, p, K), G, i + 1

            if g == [K.one]:
                sqf = True
            else:
                f = g

        if not sqf:
            d = gf_degree(f) // r

            for i in range(0, d + 1):
                f[i] = f[i*r]

            f, n = f[:d + 1], n*r
        else:
            break

    if all:
        raise ValueError("'all=True' is not supported yet")

    return lc, factors

#f = [1, -1, -2, 2, 1, -1]
f = [1, 5, 8, 4]
#f = [1, 3]
print(gf_sqf_list(f, 3, ZZ))