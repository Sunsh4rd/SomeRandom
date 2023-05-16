from random import choice
from math import factorial, gcd
from sympy import divisors

def gen_monocycle_permutation(n):
    numbers = [i for i in range(n)]
    permutation = {i: -1 for i in range(n)}
    j = 0
    while len(numbers):
        num = choice(numbers)
        while len(numbers) > 1 and (num == j or permutation[num] != -1):
            num = choice(numbers)
        permutation[j] = num
        j = num
        numbers.remove(num)
    key = [permutation[i] + 1 for i in permutation.keys()]
    return key


def gen_key():
    n = int(input("Введите длину ключа (n>2): "))
    while n < 2:
        n = int(input("Введите длину ключа (n>2): "))
    open("key_length.txt", "w", encoding='utf-8').write(str(n))
    key = gen_monocycle_permutation(n)
    open("key.txt", "w", encoding='utf-8').write(" ".join(str(x) for x in key))
    print("Ключ был успешно сгенерирован: ", key)


def crypt():
    text = open("text.txt", "r", encoding='utf-8').read()
    key = list(map(int, open("key.txt", "r", encoding='utf-8').read().split()))
    if len(text) % len(key) != 0:
        text += " " * (len(key) - (len(text) % len(key)))
    i = 0
    encrypted_text = ""
    while i < len(text):
        tmp = ""
        part_of_text = text[i:i + len(key)+1]
        for j in range(len(key)):
            tmp += part_of_text[key[j] - 1]
        encrypted_text += tmp
        i += len(key)
    open("encrypt.txt", "w", encoding='utf-8').write(encrypted_text)
    print("Сообщение было зашифровано.\n")


def decrypt(key=None):
    if key is None:
        key = [i - 1 for i in list(map(int, open("key.txt", "r", encoding='utf-8').read().split()))]
    else:
        key = [number - 1 for number in key]
    encrypted_text = open("encrypt.txt", 'r', encoding='utf-8').read()
    if len(encrypted_text) % len(key) != 0:
        encrypted_text += " " * (len(key) - (len(encrypted_text) % len(key)))
    i = 0
    decrypted_text = ""
    while i < len(encrypted_text):
        tmp = [""] * len(key)
        part_of_text = encrypted_text[i:i + len(key)]
        for j in range(len(key)):
            tmp[key[j]] = part_of_text[j]
        decrypted_text += "".join(x for x in tmp)
        i += len(key)
    return decrypted_text


def kasiski():
    text = open("encrypt.txt", "r", encoding='utf-8').read()
    l_limit = int(input('Введите нижнюю границу длины n-грамм: '))
    h_limit = int(input('Введите верхнюю границу длины n-грамм: '))

    gcds_of_lengths = {}
    for length in range(l_limit, h_limit + 1):
        sequences = {}
        for i in range(len(text) - length + 1):
            sequence = text[i:i + length]
            if sequence not in sequences:
                sequences[sequence] = []
            sequences[sequence].append(i + 1)

        gcds_of_lengths[length] = {}
        for sequence in sequences.keys():
            distances = []
            for i in range(1, len(sequences[sequence])):
                distances.append(sequences[sequence][i] - sequences[sequence][i - 1])
            gcd_of_distance = 0
            if len(distances):
                gcd_of_distance = distances[0]
                for i in range(1, len(distances)):
                    gcd_of_distance = gcd(gcd_of_distance, distances[i])
            if gcd_of_distance != 0:
                if gcd_of_distance not in gcds_of_lengths[length].keys():
                    gcds_of_lengths[length][gcd_of_distance] = 0
                gcds_of_lengths[length][gcd_of_distance] += 1
    with open("kasiski_result.txt", "w", encoding='utf-8') as res:
        gcd_dividers_dict = {}
        for l in range(l_limit, h_limit + 1):
            #res.write('Последовательность длины: {}\n\n'.format(str(l)))
            for gcd_dist in sorted(gcds_of_lengths[l].items(), key=lambda x: (-x[1], x[0])):
                if gcd_dist[0] != 1:
                    gcd_deviders = divisors(gcd_dist[0])
                    for divider in gcd_deviders:
                        if divider != 1:
                            if divider not in gcd_dividers_dict.keys():
                                gcd_dividers_dict[divider] = 0
                            gcd_dividers_dict[divider] += 1

                    #res.write('{} - {}\n'.format(gcd_dist[0], gcd_dist[1]))
            #res.write('\n\n')

        res.write('Частота встречаемости НОД:\n')
        for i in sorted(gcd_dividers_dict.items(), key=lambda x: (-x[1], x[0])):
            res.write('{} - {}\n'.format(i[0], i[1]))
def brute():
    l = int(input("Введите длину ключа: "))
    with open("result_of_brute.txt", "w", encoding='utf-8') as result:
        result.write("Длина ключа = {};\n".format(l))
        cnt_of_all_permutation = factorial(l - 1)
        all_keys = {}
        while len(all_keys) < cnt_of_all_permutation:
            current_key = gen_monocycle_permutation(l)
            while ", ".join(str(s) for s in current_key) in all_keys.keys():
                current_key = gen_monocycle_permutation(l)
            all_keys[", ".join(str(s) for s in current_key)] = decrypt(current_key)
            current_key = ", ".join(str(s) for s in current_key)
            result.write("Дешифровка на ключе: {}; дает следующий результат: {}\n".format(current_key,
                                                                                          all_keys[current_key]))
    print("Перебор ключей завершен.\n")


def main():
    print("Выберите шаг: \n"
          "1. Генерация ключа; \n"
          "2. Шифрование; \n"
          "3. Расшифрование; \n"
          "4. Метод Касиски; \n"
          "5. Перебор ключей. \n")
    while True:
        print("Выберите шаг: ")
        cmd = int(input())
        if cmd == 1:
            gen_key()
        elif cmd == 2:
            crypt()
        elif cmd == 3:
            open("decrypt.txt", "w", encoding='utf-8').write(decrypt())
            print("Сообщение было расшифровано.\n")
        elif cmd == 4:
            kasiski()
        elif cmd == 5:
            brute()
        else:
            exit(0)


if __name__ == '__main__':
    main()
