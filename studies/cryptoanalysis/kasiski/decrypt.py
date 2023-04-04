en = 'abcdefghijklmnopqrstuvwxyz'
ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
other = ' .,/\\!?[]()0123456789{}\'\":;|@#$%^&*_=+-'
allowed_alph = en + en.upper() + ru + ru.upper() + other


def decrypt():
    with open('params/key.txt', 'r', encoding='utf-8') as key_r:
        key = list(map(int, key_r.read().split()))
    block_length = len(key)

    def find_original_block(block, permutation):
        previous_block = block[:]
        while True:
            encrypted_block = [''] * block_length
            for f, t in permutation.items():
                if f < len(block):
                    encrypted_block[t] = previous_block[f]
            if ''.join(encrypted_block) == block:
                break
            previous_block = ''.join(encrypted_block)

        return ''.join(previous_block)

    with open('params/ciphertext.txt', 'r', encoding='utf-8') as ct_r:
        ciphertext = ct_r.read()

    key_reverse = key[::-1]
    permutation_d = {key[i - 1]: key[i] for i in range(len(key))}
    # permutation = [permutation_d[i] for i in range(len(key))]
    inverse_permutation_d = {
        key_reverse[i - 1]: key_reverse[i] for i in range(len(key))}
    # inverse_permutation = [inverse_permutation_d[i] for i in range(len(key))]
    splitted_ciphertext = [ciphertext[i:i + block_length]
                           for i in range(0, len(ciphertext), block_length)]
    decrypted_blocks = []
    for block in splitted_ciphertext:
        decrypted_block = [''] * block_length
        if len(block) < block_length:
            decrypted_blocks.append(find_original_block(block, permutation_d))
        else:
            for f, t in inverse_permutation_d.items():
                if f < len(block):
                    decrypted_block[t] = block[f]
            decrypted_blocks.append(''.join(decrypted_block))

    with open('params/deciphertext.txt', 'w', encoding='utf-8') as dct_w:
        dct_w.write(''.join(decrypted_blocks))
