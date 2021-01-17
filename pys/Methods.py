import math

variant = 7
h = 1.0

def f(x, y):
	return 2 * variant * x + variant * x * x - y

def get_y_eaxct(x0, n):
	y = []
	y.append(variant * x0 * x0)
	xk = x0
	for i in range(2, n + 1):
		xk += h
		y.append(variant * xk * xk)
	return y

def euler_method(x0, y0, n):
	y = []
	y.append(y0)
	xk = x0
	for i in range(1, n):
		yk = y[i - 1]
		y.append(yk + h * f(xk, yk))
		xk += h
	return y

def euler_method_improved(x0, y0, n):
	y = []
	y.append(y0)
	xk = x0
	for i in range(1, n):
		yk = y[i - 1]
		y.append(yk + h * f(xk + h / 2.0, yk + h / 2.0 * f(xk, yk)))
		xk += h
	return y

def predictor_corrector_method(x0, y0, n):
	y = []
	y.append(y0)
	xk = x0
	for i in range(1, n):
		yk = y[i - 1]
		y.append(yk + h / 2.0 * (f(xk, yk) + f(xk + h, yk + h * f(xk, yk))))
		xk += h
	return y

def get_x_with_h(x0, n, h):
	x = []
	xk = x0
	for i in range(1, n + 1):
		x.append(xk)
		xk += h
	return x

def get_e(yt, y):
	e = []
	for i in range(len(yt)):
		e.append(abs(yt[i] - y[i]))
	return e


def table_out(x, yt, y):
	print('x:\t', end=' ')
	for xs in x:
		print('%10.5f' % xs, end=' ')
	print()

	print('y мет:\t', end=' ')
	for ys in y:
		print('%10.5f' % ys, end=' ')
	print()

	print('y точн:\t', end=' ')
	for yts in yt:
		print('%10.5f' % yts, end=' ')
	print()

	print('e:\t', end=' ')
	e = get_e(yt, y)
	for es in e:
		print('%10.5f' % es, end=' ')

	print()

def main():
	x_with_h = get_x_with_h(1.0, 10, h)
	y_exact = get_y_eaxct(1.0, 10)
	euler_method_t = euler_method(1.0, 4.0, 10)
	euler_method_improved_t = euler_method_improved(1.0, 4.0, 10)
	predictor_corrector_method_t = predictor_corrector_method(1.0, 4.0, 10)
	print('Классический метод Эйлера:')
	table_out(x_with_h, y_exact, euler_method_t)
	print('Улучшенный метод Эйлера:')
	table_out(x_with_h, y_exact, euler_method_improved_t)
	print('Метод предиктора-корректора:')
	table_out(x_with_h, y_exact, predictor_corrector_method_t)

if __name__ == '__main__':
	main()