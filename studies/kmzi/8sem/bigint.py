import time


class bigint:

    def __init__(self, digits, b=10):
        while digits[-1] == 0 and len(digits) >= 2:
            digits.pop()
        self.digits = digits
        self.b = b

    def __str__(self):
        return ''.join(str(x) for x in self.digits[::-1])

    def __lt__(self, other):
        if len(self.digits) == len(other.digits):
            for (s, o) in zip(self.digits[::-1], other.digits[::-1]):
                print(s, o)
                if s == o:
                    continue
                else:
                    return s < o

        return len(self.digits) < len(other.digits)

    def __add__(self, other):
        n = max(len(self.digits), len(other.digits))
        m = min(len(self.digits), len(other.digits))

        if len(self.digits) == n:
            more_digits, less_digits = self.digits[:], other.digits[:]
        else:
            more_digits, less_digits = other.digits[:], self.digits[:]

        j, k = 0, 0
        digits_sum = []

        while j < m:
            wj = (more_digits[j] + less_digits[j] + k) % self.b
            digits_sum.append(wj)
            k = (more_digits[j] + less_digits[j] + k) // self.b
            j += 1

        while j < n:
            wj = (more_digits[j] + k) % self.b
            digits_sum.append(wj)
            k = (more_digits[j] + k) // self.b
            j += 1

        wn = k
        digits_sum.append(wn)

        return bigint(digits_sum)

    def __sub__(self, other):
        n = max(len(self.digits), len(other.digits))
        m = min(len(self.digits), len(other.digits))
        minus_sign = self < other

        if len(self.digits) == n:
            more_digits, less_digits = self.digits[:], other.digits[:]
        else:
            more_digits, less_digits = other.digits[:], self.digits[:]

        j, k = 0, 0
        digits_sub = []

        while j < m:
            if more_digits[j] + k >= less_digits[j]:
                wj = (more_digits[j] - less_digits[j] + k) % self.b
                digits_sub.append(wj)
                j += 1
                k = 0
            else:
                wj = (more_digits[j] - less_digits[j] + k) % self.b
                digits_sub.append(wj)
                j += 1
                k = -1

        while j < n:
            if more_digits[j] + k >= 0:
                wj = (more_digits[j] + k) % self.b
                digits_sub.append(wj)
                j += 1
                k = 0
            else:
                wj = (more_digits[j] + k) % self.b
                digits_sub.append(wj)
                j += 1
                k = -1

        return bigint(digits_sub), minus_sign

    def __mul__(self, other):
        m, n = len(self.digits), len(other.digits)
        digits_mul = [0] * (m + n)
        j = 0

        while j < n:
            if other.digits[j] == 0:
                digits_mul[j+m] = 0
                j += 1
            else:
                i, k = 0, 0
                while i < m:
                    t = self.digits[i] * other.digits[j] + digits_mul[i+j] + k
                    digits_mul[i+j] = t % self.b
                    k = t // self.b
                    i += 1
                digits_mul[j+m] = k
                j += 1

        return bigint(digits_mul)

    def __divmod__(self, other):
        q, r = [], []
        if len(self.digits) == 1 and self.digits[0] == 0:
            return bigint([0]), bigint([0])

        n = len(other.digits)
        m = len(self.digits) - n

        if m < 0:
            return bigint([0]), self

        if n <= 1:
            other.digits.append(0)
            n += 1

        d = self.b // (other.digits[n-1] + 1)
        bigd = bigint([d])

        if d == 1:
            self.digits.append(0)
        else:
            self = self * bigd
            self.digits.append(0)
            other = other * bigd

        j = m
        qt, rt = None, None

        while j >= 0:
            qt = (self.digits[j+n] * self.b +
                  self.digits[j+n-1]) // other.digits[n-1]
            rt = (self.digits[j+n] * self.b +
                  self.digits[j+n-1]) % other.digits[n-1]

            dig = 2
            while rt < self.b:
                u = None
                if j + n - dig < 0:
                    u = 0
                else:
                    u = self.digits[j+n-dig]

                v = None
                if n - dig < 0:
                    v = 0
                else:
                    v = other.digits[n-dig]

                if qt == self.b or qt*v > self.b*rt + u:
                    qt -= 1
                    rt += other.digits[n-1]
                else:
                    if j+n-dig < len(self.digits) and j+n-dig > -1 and n-dig < len(other.digits) and n-dig > -1 and v == 0 and u == 0:
                        dig += 1
                    else:
                        break

            bigqt = bigint([qt])
            mult = bigqt * other
            divisable = bigint([self.digits[x] for x in range(j, j+n+1)])
            before = divisable.digits[:]
            sub_dm, minus = divisable - mult
            after = sub_dm.digits[:]

            if minus:
                bb = bigint([self.b])
                for _ in range(n+1):
                    bb = bb * bigint([self.b])

                divisable = divisable + bb
                q.append(qt)
                qt -= 1
                other.digits.inset(0, 0)
                divisable = divisable + other
                divisable.digits.pop(0)
            else:
                divisable = sub_dm
                q.append(qt)

            count_zeroes = 0
            if len(after) < len(before):
                sub_dm.digits.extend([0]*(len(before)-len(after)))
                # divisable.digits.extend([0]*(len(before)-len(after)))

            if len(sub_dm.digits) == 1 and sub_dm.digits[0] == 0:
                for x in range(j, j+n+1):
                    self.digits[x] = 0
            else:
                for x in range(j, j+n+1):
                    self.digits[x] = sub_dm.digits[count_zeroes]
                    count_zeroes += 1

            j -= 1

        if rt == 0:
            r = bigint([0])
        else:
            while self.digits[-1] == 0 and len(self.digits) >= 2:
                self.digits.pop()
            while bigd.digits[-1] == 0 and len(bigd.digits) >= 2:
                bigd.digits.pop()
            self.digits = self.digits[::-1]
            q, r = divmod(self, bigd)

        return bigint(q), bigint(r)


def main():

    try:
        ina = list(map(int, input('a = ')))[::-1]
        inb = list(map(int, input('b = ')))[::-1]
    except Exception:
        print('Ошибка ввода')
        exit(0)

    # checka = ina[::-1]
    # checkb = inb[::-1]
    # countza = 0
    # countzb = 0
    # trail = False
    # for x in checka:
    #     if countza >= 2:
    #         trail = True
    #         break
    #     if x == 0:
    #         countza += 1
    #     else:
    #         break

    # for x in checkb:
    #     if countzb >= 2:
    #         trail = True
    #         break
    #     if x == 0:
    #         countzb += 1
    #     else:
    #         break

    # if trail:
    #     print('Ошибка ввода')
    #     exit(0)

    # a = bigint(ina)
    # b = bigint(inb)

    # start = time.perf_counter_ns()
    # c = a + b
    # stop = time.perf_counter_ns()

    # print(c, stop - start)

    # d = int(str(a))
    # e = int(str(b))

    # start = time.perf_counter_ns()
    # f = d + e
    # stop = time.perf_counter_ns()
    # print(f, stop - start)

    # r1 = bigint(ina)
    # r2 = bigint(inb)

    # r3 = int(str(r1))
    # r4 = int(str(r2))

    # start = time.perf_counter_ns()
    # r = r1 - r2
    # stop = time.perf_counter_ns()
    # print(*r)  # stop - start)

    # start = time.perf_counter_ns()
    # rr = r3 - r4
    # stop = time.perf_counter_ns()
    # print(rr, stop - start)

    # m1 = bigint(ina)
    # m2 = bigint(inb)

    # m3 = int(str(m1))
    # m4 = int(str(m2))

    # start = time.perf_counter_ns()
    # m = m1 * m2
    # stop = time.perf_counter_ns()
    # print(m, stop-start)

    # start = time.perf_counter_ns()
    # mm = m3 * m4
    # stop = time.perf_counter_ns()
    # print(mm, stop-start)

    d1 = bigint(ina)
    d2 = bigint(inb)

    d = divmod(d1, d2)
    print(*d)


if __name__ == '__main__':
    main()
