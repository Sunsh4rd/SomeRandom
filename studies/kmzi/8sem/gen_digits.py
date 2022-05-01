import random
from bigint import Bigint


def int_to_list_of_digits(x):
    return list(map(int, str(x)))[::-1]


def miller_rabin(n, k):
    n1 = (n - Bigint([1]))[0]
    print(n)
    q = n1
    t = None
    s = 0
    while True:
        q, r = divmod(q, Bigint([2]))
        print(q, r)
        s += 1
        if divmod(q, Bigint([2]))[1] != Bigint([0]):
            t = q
            print(t)
            break

    print('s=', s)
    for _ in range(k):
        a = Bigint(int_to_list_of_digits(random.randint(2, int(str(n))-2)))
        print(a, t, n)
        x = pow(a, t, n)
        print(a, t, x)
        if x == Bigint([1]) or x == n1:
            continue

        for _ in range(s-1):
            x = pow(x, Bigint([2]), n)
            if x == Bigint([1]):
                return False
            if x == n1:
                break

        if x != n1:
            return False

    return True


def main():
    k = int(input())
    halfk = k // 2
    print(miller_rabin(Bigint([1, 2, 1]), k))

    # print(pow(Bigint(int_to_list_of_digits(569)), Bigint(
    # int_to_list_of_digits(513)), Bigint(int_to_list_of_digits(1025))))

    # a = random.randint(0, 1000000)
    # b = random.randint(0, 1000000)

    # biga = Bigint(list(map(int, str(a)))[::-1])
    # bigb = Bigint(list(map(int, str(b)))[::-1])

    # for _ in range(100000000):
    #     if (a == b) != (biga == bigb):
    #         print(a, b, biga, bigb)


if __name__ == '__main__':
    main()
