def chain(a_1, a_2):
    q = []
    while (a_1 % a_2 != 0):
        q.append(a_1//a_2)
        a_1 %= a_2
        a_1, a_2 = a_2, a_1
    q.append(a_1 // a_2)
    return q


def main():
    a = chain(10,3)
    print(a)


if __name__ == '__main__':
    main()
