# # (v1, v3, 1), (v2, v3, 2)
import json
import re
import math


class Vertex:

    def __init__(self, name: str) -> None:
        self.name = name
        self.result = 0

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

    def __init__(self, vertices: list, edges: list, stock: list):
        self.vertices = vertices
        self.edges = edges
        self.stock = stock
    @staticmethod
    def get_graph_from_file(path: str):
        with open(path, 'r') as f:
            graph_edges = [[e[0], e[1][1:], int(e[2])] for e in map(
                lambda x: x[1:-1].split(','), re.findall(r'\([^\)]*\)', f.read()))]
            vertices_list, edges_list, input_list, output_list, stock_list, used = [], [], [], [], [], []
            for source, dest, order in graph_edges:
                s, d = Vertex(source), Vertex(dest)
                if s not in vertices_list:
                    vertices_list.append(s)
                    input_list.append(s)
                if d not in vertices_list:
                    vertices_list.append(d)
                    output_list.append(d)
                edges_list.append(Edge(s, d, order))

            vertices_list.sort()
            input_list.sort()
            output_list.sort()

            if len(vertices_list) == len(input_list):
                print("Стока нет")
            else:
                for i in range(len(vertices_list)):
                    if (vertices_list[i] not in input_list) and (vertices_list[i] in output_list):
                        stock_list.append(vertices_list[i])


            edges_list.sort(key=lambda x: x.order)
            return vertices_list, edges_list, stock_list

    def two_exercise(self):

        visited = []
        str_1 = []

        def dfs(v):
            str_1.append(str(v))
            visited.append(v)
            Flag = False
            chet = 0
            for i in self.edges:
                if i.dest == v and i.source not in visited:
                    chet += 1
                    Flag = True
                    if chet == 1:
                        str_1.append('(')
                    if chet >= 2:
                        str_1.append(',')
                    dfs(i.source)
            if Flag and chet <= 1:
                str_1.append(')')
            elif Flag and chet >= 2:
                str_1.append(')')



        for i in range(len(self.stock)):
            str_1 = []
            visited = []
            dfs(self.stock[i])
            path_str = ""
            for i in range(len(str_1)):
                path_str += str(str_1[i])
            print("Выводим постфиксный путь ", end ="")
            print(path_str)
        #2 задание


    def three_exercise(self):
        edges_list = self.edges
        visited = []
        vert_dict = {
            'E': '+',
            'D': 'exp',
            'B': 'exp',
            'A': '5',
            'C': '6',
            'F': '7',
        }
        result = 0
        print("3 задание")
        def dfs_result(v, result):
            visited.append(v)
            v.result = vert_dict[str(v)]
            #print(f'Обновленные вершины {v.result}')
            if v.result.isdigit():
                v.result = int(v.result)
            Flag = False
            chet = 0
            vert_son = []
            for i in edges_list:
                if i.dest == v and i.source not in visited:
                    chet += 1
                    vert_son.append(i.source)
                    Flag = True
                    dfs_result(i.source, 0)
            if v.result == '+':
                v.result = 0
                for i in vert_son:
                    v.result += int(i.result)
            if v.result == 'exp':
                v.result = round(math.exp(int(vert_son[0].result)))
            if v.result == '*':
                v.result = 1
                for i in vert_son:
                    v.result *= int(i.result)
            print(f'Вершина', v.name)
            print(f'Результат', v.result)

        for i in range(len(self.stock)):
            str_1 = []
            visited = []
            dfs_result(self.stock[i], 0)


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

    def get_function_by_graph(self):
        if not self.is_acyclic():
            return None

    def get_result(path : str):
        with open(path, 'r') as f:

            graph_edges = [[e[0], e[1][1:], int(e[2])] for e in map(
                lambda x: x[1:-1].split(','), re.findall(r'\([^\)]*\)', f.read()))]

def main():

    rg = Graph(*Graph.get_graph_from_file('graph.txt'))
    print(*rg.vertices)
    print(*rg.edges)
    rg.save_graph_as_json('test.json')
    rg.two_exercise()
    rg.three_exercise()

    


if __name__ == '__main__':
    main()
