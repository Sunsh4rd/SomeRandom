import numpy as np

workers = 7
possible_additional_payment = np.array(range(150, 371))
scores = np.array([21, 32, 33, 33, 37, 55, 57])

diffs = np.diff(scores)
print(diffs)

s,b = scores[0], 150
print(s,b)
for i in scores[1:]:
    nextb = i*b // s
    s,b = i, nextb
    print(s,b)

print('--------------------------------------')

s,b = scores[-1], 370
print(s,b)
for i in scores[:-1][::-1]:
    nextb = i*b // s
    s,b = i, nextb
    print(s,b)


print(np.linspace(150,370,len(list(range(21,58))),dtype=int))
print(np.std(scores))
