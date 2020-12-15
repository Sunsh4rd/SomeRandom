# import time
# from threading import Thread


# def sleepnprint():
#     i = 0
#     while True:
#         time.sleep(1)
#         print(i)
#         i += 1


# t1 = Thread(target=sleepnprint)
# t2 = Thread(target=sleepnprint)

# t1.start()
# t2.start()
# t1.join()
# t2.join()


# def fib(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n - 1) + fib(n - 2)


# def fib1(n):
#     f, s = 0, 1
#     while n > 0:
#         f, s = s, f + s
#         n -= 1
#     return s


# for i in range(30):
#     print(fib1(i), end=' ')

# import random

# l = list('JavaScript')

# for i in range(100):
# 	random.shuffle(l)
# 	print(''.join(l))

print(bin(2))