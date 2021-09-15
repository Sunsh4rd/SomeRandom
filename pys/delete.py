a = input().split()
print(a)

a_c = []

a_c = [i for i in a]

for i in a_c:
	a.remove(i)

print(a_c)
print(a)