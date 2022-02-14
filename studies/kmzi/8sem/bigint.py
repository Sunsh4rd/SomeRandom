import time


class bigint:

    def __init__(self, digits, b=10):
        self.digits = digits
        self.b = b

    def __str__(self):
        return ''.join(str(x) for x in self.digits[::-1])

    def __add__(self, other):
        n = len(self.digits)
        j, k = 0, 0
        digits_sum = []
        while j < n:
            wj = (self.digits[j] + other.digits[j] + k) % self.b
            digits_sum.append(wj)
            k = (self.digits[j] + other.digits[j] + k) // self.b
            j += 1
        wn = k
        digits_sum.append(wn)
        return bigint(digits_sum)


def main():
    a = bigint([9, 1])
    b = bigint([2, 1])
    # a = bigint([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
    # b = bigint([9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9])
    start = time.perf_counter()
    c = a+b
    stop = time.perf_counter()
    print(c, stop-start)

    # start = time.perf_counter()
    # d = 19+12
    # stop = time.perf_counter()
    # print(d, stop-start)

if __name__ == '__main__':
    main()
