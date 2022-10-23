from dataclasses import dataclass
import re


@dataclass(frozen=True)
class Vertex:
    name: str


@dataclass(frozen=True)
class Edge:
    source: Vertex
    dest: Vertex
    order: int


def main():
    item = r'\(\s*\w+\s*,\s*\w+\s*,\s*[1-9]{1}\d*\s*\)'
    seq = f'\s*{item}\s*(,\s*{item}\s*)*'
    with open('graph.txt', 'r', encoding='utf-8') as g_in:
        g = g_in.read()
        # if re.fullmatch(r'(\(\s*\w+\s*,\s*\w+\s*,\s*[1-9]{1}\d*\s*\)\s*[,]?\s*)*', g):
        # find = [re.findall(r'\w+', i) for i in re.findall(
        # r'\(\s*\w+\s*,\s*\w+\s*,\s*[1-9]{1}\d*\s*\)', g)]
        # print(find)

        if re.fullmatch(seq, g):
            find = [re.findall(r'\w+', i) for i in re.findall(item, g)]
            print(find)


if __name__ == '__main__':
    main()
