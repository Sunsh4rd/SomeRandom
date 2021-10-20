import heapq
from collections import namedtuple
import ast


class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


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
    h = []
    for ch, freq in frequencies.items():
        h.append((freq, len(h), Leaf(ch)))

    heapq.heapify(h)

    count = len(h)
    while len(h) >= 2:
        freq1, _count1, left = heapq.heappop(h)
        freq2, _count2, right = heapq.heappop(h)
        heapq.heappush(h, (freq1 + freq2, count, Node(left, right)))
        count += 1

    code = {}
    if h:
        [(_freq, _count, root)] = h
        root.walk(code, "")
    return code


def huffman_decode(en, code):
    pointer = 0
    encoded_str = ''
    while pointer < len(en):
        for ch in code.keys():
            if en.startswith(code[ch], pointer):
                encoded_str += ch
                pointer += len(code[ch])
    return encoded_str


def main():
    text = read_text_from_txt_file('studies\\tkisi\\Тест_8.txt')
    alphabet = get_alphabet(text)
    code = huffman_encode(alphabet, text)
    encoded = "".join(code[ch] for ch in text)

    for ch in sorted(code):
        print(f'{ch}: {code[ch]}')

    print(len(code))

    with open('studies\\tkisi\\res.bin', 'wb') as f:
        f.write(str(str(len(code)) + ' ' + str(code) + '\n').encode())
        extra_zero = 0 if len(encoded) == 8 else 8 - len(encoded) % 8
        f.write((str(extra_zero) + '\n').encode())
        bts = '0' * extra_zero + encoded
        to_write = bytearray()
        for i in range(0, len(bts), 8):
            to_write.append(int(bts[i: i+8], 2))
        f.write(to_write)

    with open('studies\\tkisi\\res.bin', 'rb') as f:
        # file = f.readlines()
        a = int(f.read(2).decode())
        print(a)
        t = f.read(a).decode()
        print(len(t))
        # tree = ast.literal_eval(file[0].decode())
        # trim = int(file[1].decode())
        # encoded = file[2]
        # for b in encoded:
        #     print(encoded)
        # bitstr = ''
        # byte = f.read(1)
        # while(len(byte) > 0):
            # byte = ord(byte)
            # bits = bin(byte)[2:].rjust(8, '0')
            # bitstr += bits
            # byte = f.read(1)
        # trimmed_bitstr = bitstr[trim:]
        # print(huffman_decode(trimmed_bitstr, tree))




if __name__ == '__main__':
    main()
