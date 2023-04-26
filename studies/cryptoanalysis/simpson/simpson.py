import random


def index_of_coincidence(sequence1, sequence2, alphabet):
    # вычисляем индекс совпадения (индексацию начинаем с 1)

    matches = 0
    for i in range(100):
        if sequence1[i] == sequence2[i]:
            matches += 1

    index_of_coincidence = matches / 100

    frequency1 = {char: 0 for char in alphabet}
    for char in sequence1:
        frequency1[char] += 1

    frequency2 = {char: 0 for char in alphabet}
    for char in sequence2:
        frequency2[char] += 1

    middle_index = 0
    for i in alphabet:
        index_char = frequency1[i] / 100 * frequency2[i] / 100
        middle_index += index_char

    return index_of_coincidence, middle_index


def main():
    # Считываем английский алфавит из файла
    with open('english_alphabet.txt', 'r') as f:
        english_alphabet = f.read().strip()

    # Считываем ключ из файла
    with open('key.txt', 'r') as f:
        key = f.read().strip()

    # Считываем открытый текст
    with open('text.txt', 'r') as f:
        text = f.read().strip().lower()

    print(text)

    # Генерируем случайную строку из 100 английских букв
    # plaintext = ''.join(random.choices(english_alphabet, k=100))

    plaintext = text

    # Шифруем строку с помощью шифра Виженера
    ciphertext = ''
    for i in range(len(plaintext)):
        pi = english_alphabet.index(plaintext[i])
        ki = english_alphabet.index(key[i % len(key)])
        ci = (pi + ki) % len(english_alphabet)
        ciphertext += english_alphabet[ci]

    # Сохраняем сдвиги в файл
    with open('chiper_text.txt', 'w') as f:
        f.write(ciphertext)

    with open('key.txt', 'r') as f:
        period_key = len(f.read())

    print(period_key)

    sequence = ['' for i in range(period_key)]
    print(ciphertext)
    print(sequence)
    for i in range(len(ciphertext)):
        sequence[i % period_key] = sequence[i % period_key] + ciphertext[i]

    # Создание словаря английского алфавита
    english_alphabet_dict = {}
    count = 0
    for i in english_alphabet:
        english_alphabet_dict[i] = count
        count += 1

    print(english_alphabet_dict)

    delta_spis = []

    # Находим как говорится нашу дельту
    for k in range(1, period_key):
        delta = 0
        delta_letter = 0
        for i in range(1, len(english_alphabet)):
            new_sequence = ''
            for j in sequence[k]:
                new_sequence += english_alphabet[(english_alphabet_dict[j] - i) % len(english_alphabet)]
            index, midle_index = index_of_coincidence(sequence[0], new_sequence, english_alphabet)
            if midle_index > delta:
                delta = midle_index
                delta_letter = i
        delta_spis.append(delta_letter)
        # print(f'Дельта = {delta}')
        # print(f'Дельта = {delta_letter}')

    print(f"Выводим дельта список {delta_spis}")

    # Вычисляем частотный анализ

    chast_dict = {}

    for i in english_alphabet:
        chast_dict[i] = 0

    for i in ciphertext:
        chast_dict[i] += 1
    len_ciper = len(ciphertext)

    for i in english_alphabet:
        chast_dict[i] /= len_ciper
        chast_dict[i] *= 100

    max_symbol = ''
    chast_max = 0
    for i in english_alphabet:
        if chast_dict[i] > chast_max:
            max_symbol = i
            chast_max = chast_dict[i]
    print(chast_dict)

    with open('output.txt', 'w') as f:
        for i in range(len(english_alphabet)):
            line = english_alphabet[i]
            for j in range(len(delta_spis)):
                line += english_alphabet[(i + delta_spis[j]) % len(english_alphabet)]
            # print(line)
            f.write(line + '\n')

    with open('output_1.txt', 'w') as f:
        line = max_symbol
        for i in range(len(english_alphabet)):
            if english_alphabet[i] == max_symbol:
                i_help = i

        for j in range(len(delta_spis)):
            line += english_alphabet[(i_help + delta_spis[j]) % len(english_alphabet)]
        print(line)
        f.write(line + '\n')


if __name__ == '__main__':
    main()
