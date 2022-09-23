# (v1, v3, 1), (v2, v3, 2)
import json
from pprint import pprint
import re


class Vertex:

    def __init__(self, name: str) -> None:
        self.name = name

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other) -> bool:
        return self.name == other.name


class Edge:

    def __init__(self, source: Vertex, dest: Vertex, order: int) -> None:
        self.source = source
        self.dest = dest
        self.order = order


class Graph:

    def __init__(self, vertices: list, edges: list):
        self.vertices = vertices
        self.edges = edges

    @staticmethod
    def get_graph_from_file(path):
        with open(path, 'r') as f:
            return map(lambda x: x[1:-1].split(','), re.findall(r'\([^\)]*\)', f.read()))

    def is_acyclic(self) -> bool:
        used = {v: 0 for v in self.vertices}

        def dfs(v):
            used[v] = 1
            adjacent_vertices = (i.dest for i in self.edges if i.source == v)
            # print(adjacent_vertices)
            for to in adjacent_vertices:
                # print(to)
                if used[to] == 0:
                    if dfs(to):
                        return False
                elif used[to] == 1:
                    return False
            used[v] = 2
            return True

        for v in self.vertices:
            if not dfs(v):
                return False

        return True


def main():
    # adasds
    # v1 = Vertex("v1")
    # v2 = Vertex("v1")
    # print(v1 == v2)
    # g = Graph.get_graph_from_file('graph.txt')
    # print(list(g))
    # for s in g:
    # print(s[1:-1].split(','))

    # [(i[0], i[1], int(i[2])) for i in (i[1:-1].split(',')
    #                                    for i in re.findall(rg, '(a,b,1),(d,e,2)'))]

    g = Graph([Vertex('v1'), Vertex('v2'), Vertex('v3')], [
              Edge(Vertex('v1'), Vertex('v3'), 1), Edge(Vertex('v2'), Vertex('v3'), 2)])

    g1 = Graph([Vertex('v1'), Vertex('v2'), Vertex('v3')], [
        Edge(Vertex('v1'), Vertex('v2'), 1), Edge(Vertex('v2'), Vertex('v3'), 1), Edge(Vertex('v3'), Vertex('v1'), 1)])

    print(g.is_acyclic())
    print(g1.is_acyclic())

    for k, v in g.__dict__:
        print(k.__dict__)


if __name__ == '__main__':
    main()
