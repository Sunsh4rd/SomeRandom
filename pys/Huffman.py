def read_text_from_txt_file(file_name):
    with open(file_name, 'r') as f:
        text = f.read()

    return text


def get_alphabet(text):
    alphabet = list(set(text))
    alphabet.sort()

    return alphabet


def get_symbol_frequencies(alphabet, text):
    frequencies = dict.fromkeys(alphabet, 0)
    for symbol in text:
        frequencies[symbol] += 1

    return frequencies


def main():
    text = read_text_from_txt_file('srcs\\tkisi\\Тест_6.txt')
    print(text)
    alphabet = get_alphabet(text)
    print(alphabet)
    frequencies = get_symbol_frequencies(alphabet, text)
    print(frequencies)


if __name__ == '__main__':
    main()
