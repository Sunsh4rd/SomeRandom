from sympy import *
x = symbols('x')

f = x**5 - x**4 - 2*x**3 - 8*x**2 + 6*x - 1
n = 5


def shift(lst, steps):
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            lst.append(lst.pop(0))
    else:
        for i in range(steps):
            lst.insert(0, lst.pop())


def primes():
    def is_odd_prime(n):
        if n % 3 == 0:
            return False
        i, w = 5, 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True
    n, w = 5, 2
    yield from (2, 3, n)
    while True:
        n += w
        if n < 25 or is_odd_prime(n):
            yield n
        w = 6 - w


def prime_facts(n):
    for p in primes():
        if n < p * p:
            break
        t = n
        while t % p == 0:
            t //= p
            yield p


def facts(n):
    dd, tt = [1], []
    for p in primes():
        if n < p * p:
            break
        t, e = n, 1
        while t % p == 0:
            tt += [d * p ** e for d in dd]
            t //= p
            e += 1
        if e > 1:
            dd += tt
            del tt[:]
    if n != dd[-1]:
        dd += [n // d for d in dd]
    return dd



def Kroneker():
    for i in range(0, int(n/2)+1):
        if f.subs(x, i) == 0:
            g = f - i
            m = 1
            return (g, m)

    U = facts(f.subs(x, 0))
    for i in range(1, int(n/2)+1):
        M = facts(-1 * f.subs(x, i))
        for z in M:
            if M.count(z*(-1)) == 0:
                M.append(z*(-1))
        #print(U, M)
        if i == 1:
            U1 = []
            for k in U:
                for j in M:
                    U1.append([k] + [j])
            U = U1
        else:
            U1 = []
            for k in U:
                for j in M:
                    U1.append(k + [j])
            U = U1

        for u in U1:
            #print(i, u, len(U1))
            shift(u, -1)
            g = '%d ' % (u[0])
            for j in range(1, i+1):
                g += '+ %d * x**%d' % (u[j], j)

            g = simplify(g)
            # print(g)
            q, r = div(f, g, domain='QQ')
            #print(f, '|||', g,'|||', q,'|||', r)
            if r == 0:
                m = i
                return(g)


print(Kroneker())
