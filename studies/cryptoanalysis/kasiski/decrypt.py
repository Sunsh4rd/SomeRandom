def decrypt():
    with open('params/key.txt', 'r', encoding='utf-8') as key_r:
        key = list(map(int, key_r.read().split()))
    block_length = len(key)

    with open('params/ciphertext.txt', 'r', encoding='utf-8') as ct_r:
        ciphertext = ct_r.read()

    key_reverse = key[::-1]
    inverse_permutation_d = {
        key_reverse[i-1]: key_reverse[i] for i in range(len(key))}
    inverse_permutation = [int(number) for number in ''.join(
        str(inverse_permutation_d[i]) for i in range(len(key)))]
    print(key)
    print(ciphertext)
    print(inverse_permutation_d)
    splitted_ciphertext = [ciphertext[i:i+block_length]
                           for i in range(0, len(ciphertext), block_length)]
    print(splitted_ciphertext)
    decrypted_blocks = [''.join(block[i] for i in inverse_permutation)
                        for block in splitted_ciphertext]

    with open('params/deciphertext.txt', 'w', encoding='utf-8') as dct_w:
        dct_w.write(''.join(decrypted_blocks))
