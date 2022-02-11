from functools import reduce
import os
import json


def file_to_blocks(file):
    with open(file, 'r') as f:
        data = f.read() + file
        digits = int.from_bytes(data.encode(), byteorder='big')
        to_split = str(digits)
        blocks = [to_split[i:i+32] for i in range(0, len(to_split), 32)]
        if len(blocks[-1]) != 32:
            blocks[-1] += '0' * (32-len(blocks[-1]))
    return [int(x) for x in blocks]


def hash(blocks):
    return reduce(lambda x, y: x ^ y, blocks)


def main():
    # print(hash(file_to_blocks('studies\\prog_security\\test\\b\\d\\Untitled-2.txt')))
    with open('studies\\prog_security\\last_state.json') as f:
        last_state = json.load(f)
        for root, dirs, files in os.walk('studies\\prog_security\\test'):
            for name in files:
                current_file = os.path.join(root, name)
                current_file_hash = hash(file_to_blocks(current_file))
                if current_file in last_state:
                    if last_state[current_file] == current_file_hash:
                        print('Не изменился')
                    else:
                        print('Изменился')
                else:
                    print('Новый файл')

    with open('studies\\prog_security\\last_state.json', 'w') as f:
        state = {}
        for root, dirs, files in os.walk('studies\\prog_security\\test'):
            for name in files:
                print(os.path.join(root, name))
                print(hash(file_to_blocks(os.path.join(root, name))))
                state[os.path.join(root, name)] = hash(
                    file_to_blocks(os.path.join(root, name)))
        json.dump(state, f, indent=2)


if __name__ == '__main__':
    main()
