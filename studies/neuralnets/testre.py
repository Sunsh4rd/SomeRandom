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
    print(re.findall(r'\(\s*\w+\s*,\s*\w+\s*,\s*[1-9]{1}\d*\s*\)\s*[,]?',
          '(v1,v3,1)   ,(v1,v2,1),   (v2, v3, a), (v1, v2, 0),(v1, v2,2)'))
    with open('graph.txt', 'r', encoding='utf-8') as g_in:
        print(
            # re.match(r'([\(\w+\s*\,\s*\w+\s*\,\s*\d+\)\s,\s])*\)', g_in.read()))
            # re.match(r'[\(\w+\s*\,\s*\w+\s*\,\s*\d+\)]*', g_in.read()))
            re.fullmatch(r'[\(\w+\, \w+\, \d+\)]*', g_in.read()))


if __name__ == '__main__':
    main()
