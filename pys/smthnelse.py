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

# print(bin(2))

# import numpy as np

# a = np.array([[1,3,2], [4,5,6]])
# print(a)

def mult_matr_column(matrix_a, st):
	b = []
	n = len(matrix_a)
	for i in range(n):
		tmp_sum = 0
		for j in range(n-1):
			tmp_sum += matrix_a[i][j] * st[j]
			b.append(tmp_sum)
	return b

a = [[7, 0.07, 0.0], [7, 0.07, 0.0], [0.0, 0.09, 9, 0.09], [0.0, 0.0, 0.1, 10]]
st = [7, 8, 9, 10]

print(mult_matr_column(a, st))