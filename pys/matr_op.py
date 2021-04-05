def print_m(m):
	for row in m:
		for col in row:
			print(col, end=' ')
		print()

a = [[1,1,1],
	 [1,1,1],
	 [1,1,1]]

b = [[1,2,3],
	 [4,5,6],
	 [7,8,9]]

rs = [[a[j][i] + b[j][i] for i in range(len(a))] for j in range(len(a))]

rt = [[b[i][j] for i in range(len(b))] for j in range(len(b))]

print_m(rs)
print_m(rt)