def fact(n):
    acc = 1
    for i in range(1, n + 1):
        acc *= i
    return acc


def main():
    p = int(input())
    with open('studies\\algebra\\fact.txt', 'w') as f:
        f.write(str((fact(p-1) + 1) % p == 0))


if __name__ == '__main__':
    main()
