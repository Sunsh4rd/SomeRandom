en = 'abcdefghijklmnopqrstuvwxyz'
ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
other = ' .,/\\!?[]()0123456789{}\'\":;|@#$%^&*_=+-'
allowed_alph = en + en.upper() + ru + ru.upper() + other


def encrypt():
    with open('params/key.txt', 'r', encoding='utf-8') as key_r:
        key = list(map(int, key_r.read().split()))
    block_length = len(key)
    with open('params/message.txt', 'r', encoding='utf-8') as msg_r:
        message = msg_r.read()

    permutation_d = {key[i - 1]: key[i] for i in range(len(key))}
    splitted_msg = [message[i: i + block_length]
                    for i in range(0, len(message), block_length)]
    encrypted_blocks = []
    for block in splitted_msg:
        encrypted_block = [''] * block_length
        for f, t in permutation_d.items():
            if f < len(block):
                encrypted_block[t] = block[f]
        encrypted_blocks.append(''.join(encrypted_block))

    with open('params/ciphertext.txt', 'w', encoding='utf-8') as ct_w:
        ct_w.write(''.join(encrypted_blocks))
