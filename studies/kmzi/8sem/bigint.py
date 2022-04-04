import random
import time


class Bigint:

    def __init__(self, digits, b=10):
        while digits[-1] == 0 and len(digits) >= 2:
            digits.pop()
        self.digits = list(digits)
        self.b = b

    def __str__(self):
        return ''.join(str(x) for x in self.digits[::-1])

    def __lt__(self, other):
        if len(self.digits) == len(other.digits):
            for (s, o) in zip(self.digits[::-1], other.digits[::-1]):
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

        return Bigint(digits_sum)

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

        return Bigint(digits_sub), minus_sign

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

        return Bigint(digits_mul)

    def digit_divide(self, digit):
        this = Bigint(self.digits)
        r = 0
        for i in range(len(this.digits)-1, -1, -1):
            r = r * this.b + this.digits[i]
            this.digits[i] = r // digit
            r = r % digit
        return Bigint(this.digits)

    def __divmod__(self, other):
        this = Bigint(self.digits)
        other = Bigint(other.digits)
        q, r = [], []

        if len(other.digits) == 1 and other.digits[0] == 0:
            raise ZeroDivisionError

        if len(this.digits) == 1 and this.digits[0] == 0:
            return Bigint([0]), Bigint([0])

        n = len(other.digits)
        m = len(this.digits) - n

        if m < 0:
            return Bigint([0]), this

        # if n <= 1:
            # other.digits.append(0)
            # n += 1

        d = this.b // (other.digits[n-1] + 1)
        bigd = Bigint([d])

        if d == 1:
            this.digits.append(0)
        else:
            this = this * bigd
            if len(self.digits) == len(this.digits):
                this.digits.append(0)
            other = other * bigd

        j = m
        qt, rt = None, None

        while j >= 0:
            # print(other.digits)
            qt = (this.digits[j+n] * this.b +
                  this.digits[j+n-1]) // other.digits[n-1]
            rt = (this.digits[j+n] * this.b +
                  this.digits[j+n-1]) % other.digits[n-1]

            # dig = 2
            while rt < this.b:
                # u = 0 if j + n - dig < 0 else this.digits[j+n-dig]

                # v = 0 if n - dig < 0 else other.digits[n-dig]

                if qt == this.b or qt*other.digits[n-2] > this.b*rt + this.digits[j+n-2]:
                    qt -= 1
                    rt += other.digits[n-1]
                else:
                    break
                    # if j+n-dig < len(this.digits) and j+n-dig > -1 and n-dig < len(other.digits) and n-dig > -1 and v == 0 and u == 0:
                    # dig += 1
                    # else:
                    # break
            while True:
                bigqt = Bigint([qt])
                mult = bigqt * other
                divisible = Bigint(this.digits[j:j+n+1])
                # before = divisible.digits[:]
                # print(divisible, mult)
                sub_dm, minus = divisible - mult
                # after = sub_dm.digits[:]
                # print(
                # f'q={bigqt}, mlt={mult}, div={divisible}, sub={sub_dm}, min={minus}')
                if minus:
                    qt -= 1
                else:
                    break

                # bb = Bigint([this.b])
                # for _ in range(n):
                    # bb = bb * Bigint([this.b])

                # qt -= 1

                # other.digits.insert(0, 0)
                # divisible = bb + other - sub_dm
                # divisible.digits.pop(0)
            q.append(qt)
            divisible = sub_dm

            # count_zeroes = 0
            # if len(after) < len(before):
            # sub_dm.digits.extend([0]*(len(before)-len(after)))
            # divisible.digits.extend([0]*(len(before)-len(after)))

            # if len(sub_dm.digits) == 1 and sub_dm.digits[0] == 0:
            # for x in range(j, j+n+1):
            # this.digits[x] = 0
            # else:
            for x in range(j, j+n+1):
                this.digits[x] = sub_dm.digits[x -
                                               j] if x-j < len(sub_dm.digits) else 0
                # count_zeroes += 1
            # print(this, sub_dm)

            j -= 1

        # if rt == 0:
        #     r = Bigint([0])
        # else:
        #     while this.digits[-1] == 0 and len(this.digits) >= 2:
        #         this.digits.pop()
        #     while bigd.digits[-1] == 0 and len(bigd.digits) >= 2:
        #         bigd.digits.pop()

        #     q, r = divmod(this, bigd)

        r = this.digit_divide(d)

        return Bigint(q[::-1]), r


def main():

    # try:
    #     ina = list(map(int, input('a = ')))[::-1]
    #     inb = list(map(int, input('b = ')))[::-1]
    # except Exception:
    #     print('Ошибка ввода')
    #     exit(0)

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

    # a = Bigint(ina)
    # b = Bigint(inb)

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

    # r1 = Bigint(ina)
    # r2 = Bigint(inb)

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

    # m1 = Bigint(ina)
    # m2 = Bigint(inb)

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

    # d1 = Bigint(ina)
    # d2 = Bigint(inb)
    #
    # d = divmod(d1, d2)
    # print(*d)

    for _ in range(10000):
        a = random.randint(0, 10000000000)
        b = random.randint(10, 5000)

        biga = Bigint(list(map(int, str(a)[::-1])))
        bigb = Bigint(list(map(int, str(b)[::-1])))

        if list(map(str, divmod(a, b))) != list(map(str, divmod(biga, bigb))):
            print(a, b, biga, bigb, list(map(str, divmod(a, b))),
                  list(map(str, divmod(biga, bigb))))

        # assert(map(str, divmod(a, b)) == map(str, divmod(biga, bigb)))


if __name__ == '__main__':
    main()
