import heapq
from collections import namedtuple

Node = namedtuple('Node', ['left', 'right'])
Leaf = namedtuple('Leaf', ['char'])

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


def huffman_encode(alphabet, text):
    frequencies = get_symbol_frequencies(alphabet, text)
    h = [(freq, ch) for ch, freq in frequencies.items()]
    heapq.heapify(h)

    while len(h) >= 2:
        freq1, ch1 = heapq.heappop(h)
        freq2, ch2 = heapq.heappop(h)
        heapq.heappush(freq1 + freq2, ch1 + ch2)

def main():
    # text = read_text_from_txt_file('D:\\SomeRandom\\srcs\\tkisi\\Тест_6.txt')
    text = input()
    print(text)
    alphabet = get_alphabet(text)
    print(alphabet)
    frequencies = get_symbol_frequencies(alphabet, text)
    print(frequencies)
    encoded = "".join()


if __name__ == '__main__':
    main()
