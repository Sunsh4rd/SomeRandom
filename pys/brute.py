import random

# def find(passwd, l):
#     y = 0
#     for x in l:
#         if x == passwd:
#             return (f'password is {x}, {y} steps')
#         else:
#             y += 1


# def brute():
#     charlist = '0123456789'
#     complete = []

#     for current in range(5):
#         a = [i for i in charlist]
#         for x in range(current):
#             a = [y + i for i in charlist for y in a]
#         complete = complete + a
#     return complete


def main():
    a = [[1,2,3],[4,5,6],[7,8,9]]
    print(random.choice(random.choice(a)))
#     a = brute()
#     print(a[0], a[len(a)-1])
    # passwd = input()
    # print(find(passwd, a))


if __name__ == '__main__':
    main()
