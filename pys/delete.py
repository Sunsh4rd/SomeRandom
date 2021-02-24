a = input().split()
print(a)

a_c = []

for i in a:
	a_c.append(i)

for i in a_c:
	a.remove(i)

print(a_c)
print(a)