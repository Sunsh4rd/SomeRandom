from functools import reduce
import random

def fact(n):
    acc = 1
    for i in range(1, n + 1):
        acc *= i
    return acc


def wielson(p):
    return (fact(p-1) + 1) % p == 0


def fermat(n):
    a = range(1, n)
    test = [pow(ai, n-1) % n == 1 % n for ai in a]
    return reduce(lambda x, y: x & y, test)

def main():
    # print(wielson(200000))
    print(fermat(127))

    

if __name__ == '__main__':
    main()
