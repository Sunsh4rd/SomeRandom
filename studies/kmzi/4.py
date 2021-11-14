def gcd_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def get_reverse(a, m):
    d, q, r = gcd_extended(a, m)
    if 1 % d != 0:
        return None
    else:
        x0 = (q * 1 // d) % m
        return x0



alph = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alph_d = { i: alph[i] for i in range(len(alph)) }
alph_dr = { alph[i]: i for i in range(len(alph)) }
n = len(alph)

reverse_mod1 = { i:j for i in range(n) for j in range(n) if (i * j) % n == 1 }
reverse_mod2 = { x: get_reverse(x, n) for x in range(n) }
print(reverse_mod1, reverse_mod2)

resid = [i for i in range(n)]

msg = 'ЭЧПОЧМАК'

a = n - 1

for k in resid:
    aff = ''.join(alph_d[(alph_dr[alph_d[a]]*alph_dr[m]+k)%n] for m in msg)
    ct = ''.join(alph_d[(k - alph_dr[p]) % n] for p in msg)
    # pt = ''.join(alph_d[(get_reverse(alph_dr[c], n)*(k-alph_dr[c])) % n] for c in ct if get_reverse(alph_dr[c], n))
    print(aff, ct)