from Auxiliary import *

k = read_key()
print(k)
print(key_unique_unordered())
m = gen_matrix('original_message')
print_matrix(m)
msg = read_message('original_message')
print(msg)
write_message_to_matrix(msg, m)
print_matrix(m)

am = assign_key_symbols_to_matrix(m)
print_matrix(am)
en = encrypt(am)
print(en)

with open('../srcs/encrypted_message.txt', 'w') as f:
	f.write(en)

# m1 = gen_matrix('encrypted_message')
# msg1 = read_message('encrypted_message')
# write_message_to_matrix(msg1, m1)
# print_matrix(m1)
# print(sort_key())

