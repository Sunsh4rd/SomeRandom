from Auxiliary import *

k = read_key()
print(k)
m = gen_matrix(k)
print_matrix(m)
msg = read_message()
# write_message_to_matrix(msg, m)
# print_matrix(m)
print(mm(msg))