s = copy = input()
l = s.split()
l1 = copy.lower().split()
print(l)

sym = input()

for i in range(len(l1)):
	if sym in l1[i]:
		print(l[i], end=' ')