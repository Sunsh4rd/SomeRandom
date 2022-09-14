def euclid(a, b):
    return a if b == 0 else euclid(b, a % b)


def euclid_extended(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = euclid_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def euclid_binary(a, b):
    pass


def main():
    a, b = map(int, input().split())
    print(euclid(a, b))
    print(euclid_extended(a, b))


if __name__ == '__main__':
    main()
