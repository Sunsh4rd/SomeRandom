# # (v1, v3, 1), (v2, v3, 2)
from dataclasses import dataclass
import json
import re


@dataclass(frozen=True, order=True, repr=True)
class Vertex:
    name: str

    def __str__(self) -> str:
        return self.name


@dataclass(frozen=True)
class Edge:
    source: Vertex
    dest: Vertex
    order: int


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

    def save_graph_as_json(self, path: str) -> None:
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

    def get_function_by_graph(self) -> str | None:

        used = []
        fun = []
        def get_function_as_string(sink: Vertex) -> None:
            fun.append(str(sink))
            used.append(sink)
            flag = False
            ansectors = 0
            for e in self.edges:
                if e.dest == sink and e.source not in used:
                    ansectors += 1
                    flag = True
                    if ansectors == 1:
                        fun.append('(')
                    if ansectors >= 2:
                        fun.append(',')
                    get_function_as_string(e.source)
            if flag and ansectors <= 1:
                fun.append(')')
            elif flag and ansectors >= 2:
                fun.append(')')

        if not self.is_acyclic():
            return None
        
        vertices_from, vertices_to = [],[]
        for e in self.edges:
            if e.source not in vertices_from:
                vertices_from.append(e.source)
            if e.dest not in vertices_to:
                vertices_to.append(e.dest)
            
        vertices_from.sort()
        vertices_to.sort()

        if len(self.vertices) == len(vertices_from):
            print('no sinks')
            return None
        
        sinks = [v for v in self.vertices if v not in vertices_from and v in vertices_to]
        print(sinks)

        for s in sinks:
            get_function_as_string(s)
            print(''.join(fun))
            fun = []
            used = []

    # def get_children_of_vertex(self, vertex: Vertex) -> list[Vertex] | Vertex:
    #     return [e.dest for e in self.edges if e.source == vertex] or vertex

    # def get_function_by_graph(self, current_vertex: Vertex = Vertex('E')) -> str | None:
    #     if not self.is_acyclic():
    #         return None
    #     start = current_vertex
    #     acc = f'{start.name}('
    #     print(start)
    #     children = self.get_children_of_vertex(start)
    #     print('before if', children)
    #     if isinstance(children, list):
    #         for v in children:
    #             acc += v.name
    #             print(acc)
    #             self.get_function_by_graph(v)
    #     else:
    #         print('else', children)
    #         acc += children.name
    #         print(acc)

    #     return acc
        # print(fun)
        # fun += ')'
        # fun += ')'


def main():
    
    g = Graph(*Graph.get_graph_from_file('graph.txt'))
    

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
    # print(*rg.vertices)
    # print(*rg.edges)
    # rg.save_graph_as_json('test.json')
    print(rg.is_acyclic())
    rg.get_function_by_graph()


    # v_names = 'ABCDEF'
    # g2 = Graph(list(map(Vertex, v_names)), [Edge(Vertex('E'), Vertex('D'), 1), Edge(Vertex('D'), Vertex('A'), 1), Edge(
    #     Vertex('E'), Vertex('B'), 1), Edge(Vertex('B'), Vertex('C'), 1), Edge(Vertex('E'), Vertex('F'), 1)])
    # print(g2.is_acyclic())
    # print(g2.get_function_by_graph())

    




if __name__ == '__main__':
    main()
