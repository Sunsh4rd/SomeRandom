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

    def __eq__(self, other):
        if len(self.digits) != len(other.digits):
            return False

        for (s, o) in zip(self.digits[::-1], other.digits[::-1]):
            if s != o:
                return False
            else:
                continue

        return True

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

    def sub_negative(f, s):
        n = max(len(f.digits), len(s.digits))
        m = min(len(f.digits), len(s.digits))
        if len(f.digits) == n:
            more_digits, less_digits = f.digits[:], s.digits[:]
        else:
            more_digits, less_digits = s.digits[:], f.digits[:]

        j, k = 0, 0
        digits_sub = []

        while j < m:
            if more_digits[j] + k >= less_digits[j]:
                wj = (more_digits[j] - less_digits[j] + k) % f.b
                digits_sub.append(wj)
                j += 1
                k = 0
            else:
                wj = (more_digits[j] - less_digits[j] + k) % f.b
                digits_sub.append(wj)
                j += 1
                k = -1

        while j < n:
            if more_digits[j] + k >= 0:
                wj = (more_digits[j] + k) % f.b
                digits_sub.append(wj)
                j += 1
                k = 0
            else:
                wj = (more_digits[j] + k) % f.b
                digits_sub.append(wj)
                j += 1
                k = -1

        return Bigint(digits_sub), True

    def __sub__(self, other):
        this = Bigint(self.digits)
        n = max(len(self.digits), len(other.digits))
        m = min(len(self.digits), len(other.digits))
        minus_sign = self < other

        if minus_sign:
            return Bigint.sub_negative(other, this)

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
        other_s = Bigint(other.digits)
        q, r = [], []

        if len(other.digits) == 1 and other.digits[0] == 0:
            raise ZeroDivisionError

        if len(this.digits) == 1 and this.digits[0] == 0:
            return Bigint([0]), Bigint([0])

        n = len(other.digits)
        m = len(this.digits) - n

        if m < 0:
            return Bigint([0]), this

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
            qt = (this.digits[j+n] * this.b +
                  this.digits[j+n-1]) // other.digits[n-1]
            rt = (this.digits[j+n] * this.b +
                  this.digits[j+n-1]) % other.digits[n-1]

            while rt < this.b:
                if qt == this.b or qt*other.digits[n-2] > this.b*rt + this.digits[j+n-2]:
                    qt -= 1
                    rt += other.digits[n-1]
                    if rt < this.b:
                        if qt == this.b or qt*other.digits[n-2] > this.b*rt + this.digits[j+n-2]:
                            qt -= 1
                            rt += other.digits[n-1]
                else:
                    break

            bigqt = Bigint([qt])
            mult = bigqt * other
            divisible = Bigint(this.digits[j:j+n+1])
            sub_dm, minus = divisible - mult
            flag = False
            if minus:
                qt -= 1
                flag = True

                bb = Bigint([self.b])
                for _ in range(n):
                    bb = bb * Bigint([self.b])

                bb, sign = bb - sub_dm
            else:
                bb = sub_dm

            q.append(qt)

            while len(bb.digits) < n+1:
                bb.digits.append(0)

            for i in range(len(bb.digits)):
                this.digits[j+i] = bb.digits[i]

            if flag:
                bb = bb + other
                bb.digits.pop()
                for i in range(len(bb.digits)):
                    this.digits[j+i] = bb.digits[i]

            j -= 1

        r = this.digit_divide(d)
        quo = Bigint(q[::-1])
        if int(str(r)) >= int(str(other_s)):
            div, mod = int(str(r)) // int(str(other_s)
                                          ), int(str(r)) % int(str(other_s))
            quo = quo + Bigint([div])
            r = Bigint([mod])

        return quo, r

    def __pow__(self, d, m):
        if len(self.digits) == 1 and self.digits[0] == 0:
            return 0
        z = divmod(Bigint(self.digits), m)[1]
        n = d
        y = Bigint([1])
        while True:
            n, mod_n = divmod(n, Bigint([2]))
            if mod_n.digits[-1] != 0:
                y = divmod(y*z, m)[1]
            if n.digits[-1] == 0:
                return y
            z = divmod(z*z, m)[1]


def main():

    while True:

        try:
            ina = list(map(int, input('a = ')))[::-1]
            inb = list(map(int, input('b = ')))[::-1]
        except Exception:
            print('Ошибка ввода')
            exit(0)

        a = Bigint(ina)
        b = Bigint(inb)

        start = time.perf_counter_ns()
        c = a * b
        stop = time.perf_counter_ns()
        print(c, stop - start)
        start = time.perf_counter_ns()
        c1 = int(str(a)) * int(str(b))
        stop = time.perf_counter_ns()
        print(c1, stop - start)


if __name__ == '__main__':
    main()
