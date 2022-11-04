# # (v1, v3, 1), (v2, v3, 2)
import json
import re


class Vertex:

    def __init__(self, name: str) -> None:
        self.name = name

    def __hash__(self) -> int:
        return hash(self.name)

    def __eq__(self, other) -> bool:
        return self.name == other.name

    def __str__(self) -> str:
        return self.name

    def __lt__(self, other) -> bool:
        return self.name < other.name


class Edge:

    def __init__(self, source: Vertex, dest: Vertex, order: int) -> None:
        self.source = source
        self.dest = dest
        self.order = order

    def __str__(self) -> str:
        return f'({self.source}, {self.dest}, {self.order})'


class Graph:

    def __init__(self, vertices: list[Vertex], edges: list[Edge]) -> None:
        self.vertices = vertices
        self.edges = edges

    @staticmethod
    def get_graph_from_file(path: str) -> tuple[list[Vertex], list[Edge]]:
        with open(path, 'r') as f:
            graph_edges = [[e[0], e[1][1:], int(e[2])] for e in map(
                lambda x: x[1:-1].split(','), re.findall(r'\([^\)]*\)', f.read()))]
            vertices_list, edges_list = [], []
            for source, dest, order in graph_edges:
                s, d = Vertex(source), Vertex(dest)
                if s not in vertices_list:
                    vertices_list.append(s)
                if d not in vertices_list:
                    vertices_list.append(d)
                edges_list.append(Edge(s, d, order))

            vertices_list.sort()
            edges_list.sort(key=lambda x: x.order)

            return vertices_list, edges_list

    def save_graph_as_json(self, path: str):
        with open(path, 'w') as f:
            json.dump(
                {
                    'vertices': [str(v) for v in self.vertices],
                    'edges': [
                        {'source': str(edge.source),
                         'dest': str(edge.dest),
                         'order': edge.order
                         } for edge in self.edges
                    ]
                }, f, indent=4)

    def is_acyclic(self) -> bool:
        used = {v: 0 for v in self.vertices}

        def dfs(v: Vertex) -> bool:
            used[v] = 1
            adjacent_vertices = (i.dest for i in self.edges if i.source == v)
            for to in adjacent_vertices:
                if used[to] == 0:
                    if dfs(to):
                        return True
                elif used[to] == 1:
                    return True
            used[v] = 2
            return False

        for v in self.vertices:
            if dfs(v):
                return False

        return True

    def get_children_of_vertex(self, vertex: Vertex) -> list[Vertex] | Vertex:
        return [e.dest for e in self.edges if e.source == vertex] or vertex

    def get_function_by_graph(self, current_vertex: Vertex = Vertex('E')) -> str | None:
        if not self.is_acyclic():
            return None
        start = current_vertex
        acc = f'{start.name}('
        print(start)
        children = self.get_children_of_vertex(start)
        print('before if', children)
        if isinstance(children, list):
            for v in children:
                acc += v.name
                print(acc)
                self.get_function_by_graph(v)
        else:
            print('else', children)
            acc += children.name
            print(acc)

        return acc
        # print(fun)
        # fun += ')'
        # fun += ')'


def main():
    # adasds
    # v1 = Vertex("v1")
    # v2 = Vertex("v1")
    # print(v1 == v2)
    g = Graph(*Graph.get_graph_from_file('graph.txt'))
    # print(list(g))
    # for s in g:
    # print(s[1:-1].split(','))

    # [(i[0], i[1], int(i[2])) for i in (i[1:-1].split(',')
    #                                    for i in re.findall(rg, '(a,b,1),(d,e,2)'))]

    # g = Graph([Vertex('v1'), Vertex('v2'), Vertex('v3')], [
    #           Edge(Vertex('v1'), Vertex('v3'), 1), Edge(Vertex('v2'), Vertex('v3'), 2)])

    g1 = Graph([Vertex('v1'), Vertex('v2'), Vertex('v3')], [
        Edge(Vertex('v1'), Vertex('v2'), 1), Edge(Vertex('v2'), Vertex('v3'), 1), Edge(Vertex('v3'), Vertex('v1'), 1)])

    g2 = Graph([Vertex('v1'), Vertex('v2'), Vertex('v3'), Vertex('v4')], [Edge(Vertex('v1'), Vertex('v2'), 1), Edge(
        Vertex('v2'), Vertex('v3'), 1), Edge(Vertex('v3'), Vertex('v4'), 1), Edge(Vertex('v4'), Vertex('v1'), 1)])

    g3 = Graph([Vertex('v1'), Vertex('v2'), Vertex('v3'), Vertex('v4')], [Edge(Vertex('v1'), Vertex('v2'), 1), Edge(
        Vertex('v2'), Vertex('v3'), 1), Edge(Vertex('v3'), Vertex('v4'), 1), Edge(Vertex('v1'), Vertex('v4'), 2)])

    print(g.is_acyclic())
    print(g1.is_acyclic())
    print(g2.is_acyclic())
    print(g3.is_acyclic())

    rg = Graph(*Graph.get_graph_from_file('graph.txt'))
    print(*rg.vertices)
    print(*rg.edges)
    rg.save_graph_as_json('test.json')

    v_names = 'ABCDEF'
    g2 = Graph(list(map(Vertex, v_names)), [Edge(Vertex('E'), Vertex('D'), 1), Edge(Vertex('D'), Vertex('A'), 1), Edge(
        Vertex('E'), Vertex('B'), 1), Edge(Vertex('B'), Vertex('C'), 1), Edge(Vertex('E'), Vertex('F'), 1)])
    print(g2.is_acyclic())
    print(g2.get_function_by_graph())

    # print(type(rg[0]), type(rg[1]))
    # for verts in Graph.get_graph_from_file('graph.txt'):
    #     for v in verts:
    #         print(v)
    # for e in ed:
    #     print(e)

    # for k, v in g.__dict__:
    #     print(k.__dict__)


if __name__ == '__main__':
    main()
