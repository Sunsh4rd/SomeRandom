import math
from collections import deque
import json


class Graph():

    def __init__(self, gdict=None):
        self.gdict = gdict


def dijkstra(gdict, start):
    verts = list(gdict.keys())
    visited = dict.fromkeys(verts, False)
    dist = dict.fromkeys(verts, math.inf)
    dist[start] = 0
    queue = deque()
    queue.appendleft((start, 0))
    while queue:
        idx, min_value = queue.popleft()
        visited[idx] = True
        if dist[idx] < min_value:
            continue
        if gdict[idx]:
            next_verts = list(gdict[idx].keys())
            for v in next_verts:
                new_dist = dist[idx] + int(gdict[idx][v])
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    queue.appendleft((v, new_dist))

    return dist


def dijkstra_wrapper(g, v):
    return dijkstra(g.gdict, v)


def main():

    with open("graph.json", 'r') as f:
        graph_dict = json.load(f)
        print(graph_dict)
        g = Graph(graph_dict)

    with open("gr_copy.json", 'w') as f:
        f.write(json.dumps(graph_dict))

    print(dijkstra_wrapper(g, '0'))


if __name__ == '__main__':
    main()
