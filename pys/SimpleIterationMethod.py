eps = 0.0001
variant = 7

def matrix_variant(n):
	res = []
	var = variant
	for i in range(n):
		res.append([])
		for j in range(n):
			if i == j:
				res[i].append(var)
			else:
				res[i].append(var / 100.0)
		var += 1
	return res

def check_condition(xk, xk1):
	for i in range(len(xk)):
		if abs(xk[i] - xk1[i]) >= eps:
			return False
	return True

def str_variant(n):
	st = []
	var = variant
	for i in range(n):
		st.append(var)
		var += 1
	return st

def mult_matr_column(matrix_a, st):
	b = []
	n = len(matrix_a)
	for i in range(n):
		tmp_sum = 0
		for j in range(n):
			tmp_sum += matrix_a[i][j] * st[j]
		b.append(tmp_sum)
	return b

def simple_iteration_method(a, b):
	x = [1.0] * len(a)
	xk = []
	flag = True
	iteration_count = 0
	while flag:
		for i in range(len(a)):
			tmp_from_1_to_i = 0.0
			tmp_from_i1_to_n = 0.0
			for j in range(i):
				tmp_from_1_to_i += a[i][j] * x [j]
			for j in range(i + 1, len(a)):
				tmp_from_i1_to_n += a[i][j] * x[j]
			xk.append(1.0 / a[i][i] * (-tmp_from_1_to_i - tmp_from_i1_to_n + b[i]))
		flag = not check_condition(x, xk)
		x, xk = xk, []
		iteration_count += 1
	return x, iteration_count

def main():
	n = int(input('Введите n: '))
	print('Матрица А:')
	matrix_a = matrix_variant(n)
	for ar in matrix_a:
		print(ar)
	print('X, которые должны получиться: ')
	st = str_variant(n)
	print(st)
	print('Столбец b:')
	b = mult_matr_column(matrix_a, st)
	print(b)
	print('Найденные методом простых итераций x и количество итераций:')
	x, it = simple_iteration_method(matrix_a, b)
	print(x, it)
	print('Погрешность: ' + str(eps))

if __name__ == '__main__':
	main()