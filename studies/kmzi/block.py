import random


def random_permutation(n):
    L = list(range(n))
    random.shuffle(L)
    return L


def get_opened_text(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.read()


def get_permutation(file):
    with open(file, 'r', encoding='utf-8') as f:
        return [int(s) for s in f.read().split()]


def apply_permutation(s, p):
    return ''.join(s[i] for i in p)


def split_string(s, l):
    res = []
    while s:
        tmp = s[:l]
        res.append((tmp + 'А' * (l-len(tmp)), tmp)[len(tmp) == l])
        s = s[l:]
    return res


def encrypt(splitted, perm):
    permute = [apply_permutation(s, perm) for s in splitted]
    return ''.join(permute)


def split_and_sort_encrypted(encrypted, l):
    res = []
    while encrypted:
        res.append(''.join(sorted(encrypted[:l])))
        encrypted = encrypted[l:]
    return res


def check_correct_permutation(encrypted, perm, l):
    tmp = [i - perm[i] for i in range(len(encrypted))]
    res = []
    while tmp:
        res.append(tmp[:l])
        tmp = tmp[l:]
    return res


def main():

    #  1 0 2 3  5 4  7 6 8 9 11 10
    # -1 1 0 0 -1 1 -1 1 0 0 -1 1
    opened_text = get_opened_text('input.txt')
    # block_length = get_block_length('block.txt')
    perm1 = get_permutation('perm1.txt')
    perm2 = get_permutation('perm2.txt')
    # print(type(perm1))
    # print(perm2)
    # splitted = split_string(opened_text, block_length)
    # encrypted1 = encrypt(splitted, perm1)
    # encrypted2 = encrypt(splitted, perm2)
    encrypted1 = apply_permutation(opened_text, perm1)
    encrypted2 = apply_permutation(opened_text, perm2)

    check_block_length = 2
    while True:
        check_count1 = 0
        check_count2 = 0
        sas_encrypted1 = split_and_sort_encrypted(
            encrypted1, check_block_length)
        check_perm1 = check_correct_permutation(
            encrypted1, perm1, check_block_length)
        sas_encrypted2 = split_and_sort_encrypted(
            encrypted2, check_block_length)
        check_perm2 = check_correct_permutation(
            encrypted2, perm2, check_block_length)
        # if sas_encrypted1 == sas_encrypted2:
        #     print(check_perm1)
        #     print(check_perm2)
        for i in range(len(check_perm1)):
            if check_perm1[0] == check_perm1[i]:
                check_count1 += 1
        for j in range(len(check_perm2)):
            if check_perm2[0] == check_perm2[j]:
                check_count2 += 1
        if check_count1 == check_count2:
            break
        else:
            check_block_length += 1

    print(check_block_length)
    # print('c1 =', encrypted1)
    # print('c2 =', encrypted2)
    # print('Искомая длина блока шифров:', check_block_length)


if __name__ == '__main__':
    main()
