import time


class bigint:

    def __init__(self, digits, b=10):
        if digits[-1] == 0 and len(digits) >= 2:
            digits.pop()
        self.digits = digits
        self.b = b

    def __str__(self):
        return ''.join(str(x) for x in self.digits[::-1])

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
        # 10020 -> [02001]
        #  9287 -> [7829 ]
        #          [337  ]
        n = max(len(self.digits), len(other.digits))
        m = min(len(self.digits), len(other.digits))

        if len(self.digits) == n:
            more_digits, less_digits = self.digits[:], other.digits[:]
        else:
            more_digits, less_digits = other.digits[:], self.digits[:]

        j, k = 0, 0
        digits_sub = []

        while j < m:
            if more_digits[j] >= less_digits[j]:
                wj = (more_digits[j] - less_digits[j]) % self.b
                digits_sub.append(wj)
            j += 1
            else:
                print()

        while j < n:
            wj = (more_digits[j] + k) % self.b
            digits_sum.append(wj)
            k = (more_digits[j] + k) // self.b
            j += 1

        wn = k
        digits_sum.append(wn)

        return bigint(digits_sum)


def main():

    try:
        ina = list(map(int, input('a = ')))[::-1]
        inb = list(map(int, input('b = ')))[::-1]
    except Exception:
        print('Ошибка ввода')
        exit(0)

    checka = ina[::-1]
    checkb = inb[::-1]
    countza = 0
    countzb = 0
    trail = False
    for x in checka:
        if countza >= 2:
            trail = True
            break
        if x == 0:
            countza += 1
        else:
            break

    for x in checkb:
        if countzb >= 2:
            trail = True
            break
        if x == 0:
            countzb += 1
        else:
            break

    if trail:
        print('Ошибка ввода')
        exit(0)

    a = bigint(ina)
    b = bigint(inb)

    start = time.perf_counter_ns()
    c = a + b
    stop = time.perf_counter_ns()

    print(c, stop - start)

    d = int(str(a))
    e = int(str(b))

    start = time.perf_counter_ns()
    f = d + e
    stop = time.perf_counter_ns()
    print(f, stop - start)


if __name__ == '__main__':
    main()
