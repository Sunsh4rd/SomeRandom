en = 'abcdefghijklmnopqrstuvwxyz'
ru = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
other = ' .,/\\!?[]()0123456789{}\'\":;|@#$%^&*_=+-'
allowed_alph = en + en.upper() + ru + ru.upper() + other


def decrypt():

    def find_original_block(block, permutation):
        previous_block = block[:]
        while True:
            encrypted_block = ''.join((previous_block[i] if i < len(
                previous_block) else '' for i in permutation))
            # print(previous_block, encrypted_block)
            if encrypted_block == block:
                break
            previous_block = encrypted_block[:]

        return ''.join(previous_block)

    with open('params/key.txt', 'r', encoding='utf-8') as key_r:
        key = list(map(int, key_r.read().split()))
    block_length = len(key)

    with open('params/ciphertext.txt', 'r', encoding='utf-8') as ct_r:
        ciphertext = ct_r.read()

    if not all([s in allowed_alph for s in ciphertext]):
        print('В криптограмме присутствуют запрещенные символы')
        exit()

    key_reverse = key[::-1]
    permutation_d = {key[i-1]: key[i] for i in range(len(key))}
    permutation = [int(number) for number in (
        str(permutation_d[i]) for i in range(len(key)))]
    inverse_permutation_d = {
        key_reverse[i-1]: key_reverse[i] for i in range(len(key))}
    inverse_permutation = [inverse_permutation_d[i] for i in range(len(key))]
    print(f'{key=}')
    print(f'{key_reverse=}')
    print(f'{ciphertext=}')
    print(f'{permutation_d=}')
    print(f'{permutation=}')
    print(f'{inverse_permutation_d=}')
    print(f'{inverse_permutation=}')
    splitted_ciphertext = [ciphertext[i:i+block_length]
                           for i in range(0, len(ciphertext), block_length)]
    print(f'{splitted_ciphertext=}')
    decrypted_blocks = [''.join(block[i] for i in inverse_permutation) if len(block) == block_length
                        else find_original_block(block, permutation)
                        for block in splitted_ciphertext]

    with open('params/deciphertext.txt', 'w', encoding='utf-8') as dct_w:
        dct_w.write(''.join(decrypted_blocks))
