def multiply(a, b):
    res = []
    for row in a:
        for cols in b:
            for col in cols:
                res.append((row, col))
    return res

    # return list(zip(((row, col) for row in a) for col in cols) for cols in b)


def main():
    a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    b = [
        [1],
        [9], 
        [2]
    ]

    print(multiply(a, b))


if __name__ == '__main__':
    main()
