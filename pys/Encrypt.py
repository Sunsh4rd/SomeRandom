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
print(encrypt(am))
 
print(sort_key())

