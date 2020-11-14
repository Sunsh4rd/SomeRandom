def find(passwd, l):
    y = 0
    for x in l:
        if x == passwd:
            return (f'password is {x}, {y} steps')
        else:
            y += 1


def brute():
    charlist = 'abcdefghijklmnopqrstuvwxyz'
    complete = []

    for current in range(4):
        a = [i for i in charlist]
        for x in range(current):
            a = [y + i for i in charlist for y in a]
        complete = complete + a
    return complete


def main():
    a = brute()
    passwd = input()
    print(find(passwd, a))


if __name__ == '__main__':
    main()
