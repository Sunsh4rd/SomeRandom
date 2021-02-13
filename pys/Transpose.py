from Auxiliary import *

k = read_key()
# print(k)
# m = gen_matrix(k)
# print_matrix(m)
# msg = read_message()
# write_message_to_matrix(msg, m)
# print_matrix(m)

a = [['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и'],
	 ['й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т'],
	 ['у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь'],
	 ['э', 'ю', 'я', '.', ',', '!', '?', ':', ';', '('],
	 [')', '', '', '', '', '', '', '', '', '']]

b = [(k[j], [a[i][j] for i in range(len(a))]) for j in range(len(a[0]))]
print_matrix(b)


b.sort()
print_matrix(b)


en = ''
for i in b:
	en += ''.join(i[1])

print(en)