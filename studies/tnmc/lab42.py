import math
import random
import time


class ChainFractionSqrt:
    def getLastAndGenerateNext(self):
        ans = [self.P[-1], self.Q[-1]]
        self.v_i = (self.n - self.u_i ** 2) // self.v_i
        q = (int(math.sqrt(self.n)) + self.u_i) // self.v_i
        self.P.append(q * self.P[-1] + self.P[-2])
        self.Q.append(q * self.Q[-1] + self.Q[-2])
        self.u_i = q * self.v_i - self.u_i
        del self.P[0]
        del self.Q[0]
        return ans

    def __init__(self, n):
        self.P = [0, 1]
        self.Q = [1, 0]
        self.n = n
        self.P.append(int(math.sqrt(self.n)) * self.P[-1] + self.P[-2])
        self.Q.append(int(math.sqrt(self.n)) * self.Q[-1] + self.Q[-2])
        del self.P[0]
        del self.Q[0]
        self.v_i = 1
        self.u_i = int(math.sqrt(n))
        self.getLastAndGenerateNext()


p_arr = []
d = [None, None]
s = ''


def isPrimeNumber(num):
    if num == 3:
        return True
    count_of_rounds = 10
    for i in range(count_of_rounds):
        s = 0
        r = num - 1
        while r % 2 == 0:
            r //= 2
            s += 1
        a = random.randint(2, num - 2)
        y = pow(a, r, num)
        if (y != 1) and (y != num - 1):
            j = 1
            while (j <= s - 1) and (y != num - 1):
                y = pow(y, 2, num)
                if y == 1:
                    return False
                j += 1
            if y != num - 1:
                return False
    return True


def jacobi(a, n):
    if gcdClassic(a, n) != 1:
        return 0
    return jacobiHelp(a, n)


def jacobiHelp(a, n):
    if a < 0:
        return int(jacobi(-a, n) * math.pow(-1, int((n - 1) / 2)))
    if a % 2 == 0:
        return int(jacobi(a / 2, n) * math.pow(-1, int((n * n - 1) / 8)))
    if a == 1:
        return 1
    if a < n:
        return int(jacobi(n, a) * math.pow(-1, int(((a - 1) / 2) * ((n - 1) / 2))))
    return jacobi(a % n, n)


def nextPrimeNumber(p):
    if p % 2 == 0:
        p += 1
    else:
        p += 2
    while True:
        if isPrimeNumber(p) == True:
            return p
        p += 2


def gcdClassic(first, second):
    first = abs(first)
    second = abs(second)
    while first != 0 and second != 0:
        if first >= second:
            first %= second
        else:
            second %= first
    return first + second


def genFactorBase(num, a):
    global k, p_arr, s
    s += 'p: ''\t''-1 ''\t'''
    p_arr.append(-1)
    L = math.pow(
        math.exp(math.pow(math.log(num) * math.log(math.log(num)), 0.5)), a)
    p = 2
    while p <= L:
        t = jacobi(num, p)
        if t != -1:
            p_arr.append(p)
            s += str(p) + '\t'
        p = nextPrimeNumber(p)
    k = len(p_arr)


def factorBase(Qmi, vStep):
    global p_arr
    vi = []
    c = Qmi
    if c < 0:
        vi.append(1)
        vStep.append(1)
        c = -c
    else:
        vi.append(0)
        vStep.append(0)
    existNotNull = False
    for i in range(1, len(p_arr)):
        a = 0
        while c % p_arr[i] == 0:
            a += 1
            c /= p_arr[i]
        if a % 2 != 0:
            existNotNull = True
        vStep.append(a)
        a %= 2
        vi.append(a)
    if (not existNotNull) or c != 1:
        return None
    return vi


def findSolution(v, x=None):
    if x == None:
        x = [0 for i in range(len(v) - 1)]
        x.append(1)
    else:
        l = len(x) - 1
        while l >= 0 and x[l] == 1:
            x[l] = 0
            l -= 1
        if l == -1:
            return []
        x[l] = 1
    while True:
        j = 0
        for j in range(len(v[0])):
            res = 0
            for i in range(len(v)):
                res += v[i][j] * x[i]
                res %= 2
            if res != 0:
                break
        if j + 1 == len(v[0]):
            break
        l = len(x) - 1
        while l >= 0 and x[l] == 1:
            x[l] = 0
            l -= 1
        if l == -1:
            return []
        x[l] = 1
    return x


def morrison(num, a):
    global k, d, s
    genFactorBase(num, a)
    ch = ChainFractionSqrt(num)
    while True:
        v = []
        vStep = []
        P = []
        Qm = []
        while len(v) != k + 1:
            PQ = ch.getLastAndGenerateNext()
            Qmi = PQ[0] ** 2 - (num * PQ[1] ** 2)
            viStep = []
            vi = factorBase(Qmi, viStep)
            if vi == None:
                continue
            Qm.append(Qmi)
            P.append(PQ[0])
            v.append(vi)
            vStep.append(viStep)
        x = findSolution(v)
        if len(x) == 0:
            continue
        while True:
            x = findSolution(v, x)
            if len(x) == 0:
                break
            X = 1
            Y = 1
            for i in range(k + 1):
                X = X * (P[i] ** x[i]) % num
            for j in range(k):
                step = 0
                for i in range(len(x)):
                    step += x[i] * vStep[i][j]
                step /= 2
                Y = Y * (p_arr[j] ** step) % num
            if pow(int(X), 2, num) != pow(int(Y), 2, num):
                continue
            prov = [X + Y, X - Y]
            for i in range(len(prov)):
                gcd = gcdClassic(prov[i], num)
                if gcd > 1 and gcd < num:
                    d[0] = gcd
                    d[1] = num // gcd
                    s += '\n'
                    for j in range(len(v)):
                        s += str(Qm[j]) + ': ''\t'' '
                        for l in range(len(v[j])):
                            s += str(v[j][l]) + '\t'
                        s += '\n'
                    s += 'x: '
                    for j in x:
                        s += str(j) + ' '
                    return


print("Введите составное число n = ")
num = int(input())
while isPrimeNumber(num):
    print("Неправильный ввод!")
    num = int(input())
root = math.sqrt(num)
if int(root + 0.5) ** 2 == num:
    print(num, "это квадрат")
    print(str(num) + ' = ' + str(root) + ' * ' + str(root))
else:
    print("Введите \"a\": 0 < a < 1 ")
    a = float(input())
    morrison(num, a)
    print(s)
    if d[0] == 'none':
        print('Нельзя провести факторизацию')
    else:
        print(str(num) + ' = ' + str(d[0]) + ' * ' + str(d[1]))
