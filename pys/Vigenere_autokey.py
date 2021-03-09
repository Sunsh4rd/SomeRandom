import random


def encrypt(message):

    with open('../srcs/key_vigenere.txt', 'r', encoding='utf-8') as f:
        key = f.read()

    ciphertext = ''
    print(key)
    for i in range(len(message)):
        tmp_k = key[i]
        tmp_m = message[i]
        idx = (alph[tmp_k] + alph[tmp_m]) % n
        key += alph_s[idx]
        ciphertext += alph_s[idx]
    print(key)
    return ciphertext


def decrypt(message):

    with open('../srcs/key_vigenere.txt', 'r', encoding='utf-8') as f:
        key = f.read()

    decrypted = ''
    tmp_k = key + message[:len(message)-1:1]
    print(tmp_k)
    for i in range(len(message)):
        tmp_m = message[i]
        idx = (alph[tmp_m] - alph[tmp_k[i]]) % n
        key += alph_s[idx]
        decrypted += alph_s[idx]
    return decrypted


if __name__ == '__main__':
	
    alph_s = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя #.,!?:;0123456789'
    letters = alph_s[:33]
    print(letters)
    alph = {alph_s[i]: i for i in range(len(alph_s))}
    n = len(alph)
    print(alph)
    opt = 0

    while True:
        opt = int(input('0 - Зашифровать сообщение, 1 - Расшифровать сообщение, 2 - Остановить работу:\n'))
        if opt == 0:
            with open('../srcs/key_vigenere.txt', 'w', encoding='utf-8') as f:
            	f.write(random.choice(letters))

            with open('../srcs/vigenere_original_message.txt', 'r', encoding='utf-8') as f:
                msg = f.read()
            print(msg)

            msg_w = msg.lower()
            encrypted = encrypt(msg_w)

            with open('../srcs/vigenere_encrypted_message.txt', 'w', encoding='utf-8') as f:
                f.write(encrypted)
        elif opt == 1:
            with open('../srcs/vigenere_encrypted_message.txt', 'r', encoding='utf-8') as f:
                msg = f.read()
            print(msg)

            msg_w = msg.lower()
            decrypted = decrypt(msg_w)

            with open('../srcs/vigenere_decrypted_message.txt', 'w', encoding='utf-8') as f:
                f.write(decrypted)
        elif opt == 2:
        	break
        else:
            print('Повторите попытку...')
