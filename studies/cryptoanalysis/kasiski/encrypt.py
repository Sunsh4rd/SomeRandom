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

    if not all([s in allowed_alph for s in message]):
        print('В сообщении присутствуют запрещенные символы')
        exit()

    print(f'{message=}')
    print(f'{key=}')
    permutation_d = {key[i-1]: key[i] for i in range(len(key))}
    # permutation = [permutation_d[i] for i in range(len(key))]
    print(f'{permutation_d=}')
    # print(f'{permutation=}')
    splitted_msg = [message[i: i+block_length]
                    for i in range(0, len(message), block_length)]
    # if len(splitted_msg[-1]) < block_length:
    #     splitted_msg[-1] += ' ' * (block_length - len(splitted_msg[-1]))
    print(f'{splitted_msg=}')
    encrypted_blocks = []
    for block in splitted_msg:
        encrypted_block = [''] * block_length
        print(block)
        # if len(block) == block_length:
        #     for f, t in permutation_d.items():
        #         print(f, t)
        #         encrypted_block[t] = block[f]
        #     encrypted_blocks.append(''.join(encrypted_block))
        # else:
        for f, t in permutation_d.items():
            print(f, t)
            if f < len(block):
                encrypted_block[t] = block[f]
        encrypted_blocks.append(''.join(encrypted_block))
        print(encrypted_block)
        print(encrypted_blocks)

    # encrypted_blocks = [''.join(block[i] for i in permutation) if len(block) == block_length
    #                     else ''.join(block[i] if i < len(block) else '' for i in permutation)
    #                     for block in splitted_msg]
    print(encrypted_blocks)

    with open('params/ciphertext.txt', 'w', encoding='utf-8') as ct_w:
        ct_w.write(''.join(encrypted_blocks))
