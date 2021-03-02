from Auxiliary import *

k = read_key()
print(k)
print(key_unique_unordered())
m = gen_matrix('original_message')
print_matrix(m)
msg_a = read_message('original_message') 
msg = msg_a.lower()
print(msg)
write_message_to_matrix(msg, m)
print_matrix(m)

am = assign_key_symbols_to_matrix(m)
print_matrix(am)
en = encrypt(am)



with open('../srcs/encrypted_message.txt', 'w', encoding='utf-8') as f:
    f.write(en)
