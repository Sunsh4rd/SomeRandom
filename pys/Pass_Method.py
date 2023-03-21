variant = 7

def pass_matrix(n):
	res = [[]]
	res[0].append(variant)
	res[0].append(variant / 100.0)
	for i in range(2 ,n):
		res[0].append(0.0)
	for i in range(1, n - 1):
		res.append([])
		for j in range(n):
			if j == i:
				res[i].append(variant + i)
			elif j == i + 1 or j == i - 1:
				res[i].append((variant + i) / 100.0)
			else:
				res[i].append(0.0)
	res.append([])
	for i in range(n - 2):
		res[n - 1].append(0.0)
	res[n - 1].append((variant + n - 1) / 100.0)
	res[n - 1].append(variant + n - 1)
	return res

def straight_pass(d3, d):
	d2 = []
	p = []
	q = []
	p.append(None)
	q.append(None)
	p.append(-d3[0][1] / d3[0][0])
	q.append(d[0] / d3[0][0])
	for i in range(1, len(d3) - 1):
		p.append(d3[i][i + 1] / (-d3[i][i] - d3[i][i-1] * p[i]))
		q.append((d3[i][i-1] * q[i] - d[i]) / (-d3[i][i] - d3[i][i - 1] * p[i]))
	n = len(d3) - 1
	p.append(0.0)
	q.append((d3[n][n - 1] * q[n] - d[n]) / (-d3[n][n] - d3[n][n - 1] * p[n]))
	return p, q
    
def pass_method(d3, d):
	ps = straight_pass(d3, d)
	p = ps[0]
	q = ps[1]
	x = []
	n = len(d3)
	for i in range(n):
		x.append(0.0)
	x[n - 1] = q[n]
	for i in range(n - 2, -1 -1):
		x[i] = p[i + 1] * x[i + 1] + q[i + 1]
	return x

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

def main():
	n = int(input('Введите n:'))
	print('Матрица А:')
	matrix_a = pass_matrix(n)
	for ar in matrix_a:
		print(ar)
	print('X, которые должны получиться')
	st = str_variant(n)
	print(st)
	print('Столбец d')
	d = mult_matr_column(matrix_a, st)
	print(d)
	print('P и Q:')
	p, q = straight_pass(matrix_a, d)
	print(p)
	print(q)
	print('Результаты метода прогонки:')
	print(pass_method(matrix_a, d))

if __name__ == '__main__':
	main()