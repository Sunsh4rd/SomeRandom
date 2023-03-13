def encrypt():
    with open('params/key.txt', 'r', encoding='utf-8') as key_r:
        key = list(map(int, key_r.read().split()))
    block_length = len(key)
    with open('params/message.txt', 'r', encoding='utf-8') as msg_r:
        message = msg_r.read()

    print(message)
    print(key)
    permutation_d = {key[i-1]: key[i] for i in range(len(key))}
    permutation = [int(number) for number in ''.join(
        str(permutation_d[i]) for i in range(len(key)))]
    print(permutation)
    splitted_msg = [message[i:i+block_length]
                    for i in range(0, len(message), block_length)]
    if len(splitted_msg[-1]) < block_length:
        splitted_msg[-1] += ' ' * (block_length - len(splitted_msg[-1]))
    print(splitted_msg)
    encrypted_blocks = [''.join(block[i] for i in permutation)
                        for block in splitted_msg]
    print(encrypted_blocks)

    with open('params/ciphertext.txt', 'w', encoding='utf-8') as ct_w:
        ct_w.write(''.join(encrypted_blocks))
