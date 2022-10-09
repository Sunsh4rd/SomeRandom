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
    with open('graph.txt', 'r', encoding='utf-8') as g_in:
        g = g_in.read()
        if re.fullmatch(r'(\(\s*\w+\s*,\s*\w+\s*,\s*[1-9]{1}\d*\s*\)\s*[,]?\s*)*', g):
            print(re.findall(
                r'\(\s*\w+\s*,\s*\w+\s*,\s*[1-9]{1}\d*\s*\)\s*[,]?', g))


if __name__ == '__main__':
    main()
