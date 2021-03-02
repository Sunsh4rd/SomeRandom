from Auxiliary import *


dec = decrypt()

with open('../srcs/decrypted_message.txt', 'w', encoding='utf-8') as f:
    f.write(dec)
