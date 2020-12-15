import math

class Graph():

    def __init__(self, gdict = None):
        self.gdict = gdict


with open("NotOrqWithW.txt") as file: #Читаем файл
  onstring = file.read().splitlines()
dict = {}
dict2 = {}


for item in onstring:
    key = item.split(" ")[0]
    l = item.split(" ")[1:]
    n = item.split(" ")[1:]
    while len(l) != 0:
      key2 = l.pop(0)
      weith = l.pop(0)
      dict2[key2] = weith
      dict[key]= dict2
    dict2 = {}
print(dict)
file.close()
#Создаем граф
g = Graph(dict)


# def dijkstra(G, start, end = None):

#     D = {}  # dictionary of final distances
#     P = {}  # dictionary of predecessors
#     Q = {}  # estimated distances of non-final vertices
#     Q[start] = 0

#     for v in Q:
#         D[v] = Q[v]
#         if v == end:
#             break

#         for w in G[v]:
#             vwLength = D[v] + int(G[v][w])
#             if w in D:
#                 if vwLength < D[w]:
#                     raise ValueError("Dijkstra: found better path to already-final vertex")
#             elif w not in Q or vwLength < Q[w]:
#                 Q[w] = vwLength
#                 P[w] = v

#     return (D, P)

# def dijkstra(w, start):
#   INF = 10 ** 10
#   dist = [INF] * n
#   dist[start] = 0
#   used = [False] * n
#   min_dist = 0
#   min_vertex = start
#   while min_dist < INF:
#       i = min_vertex 
#       used[i] = True 
#       for j in range(n): 
#           if dist[i] + w[i][j] < dist[j]: 
#               dist[j] = dist[i] + w[i][j] 
#       min_dist = INF
#       for j in range(n):
#           if not used[j] and dist[j] < min_dist:
#               min_dist = dist[j]
#               min_vertex = j
#   return dist
  
# dijkstra(g.gdict, 'a')

# from heapq import *

# graph = {'A': [(2, 'M'), (3, 'P')],
#          'M': [(2, 'A'), (2, 'N')],
#          'N': [(2, 'M'), (2, 'B')],
#          'P': [(3, 'A'), (4, 'B')],
#          'B': [(4, 'P'), (2, 'N')]}

# def dijkstra(start, goal, g):
#     queue = []
#     heappush(queue, (0, start))
#     print(queue)
#     cost_visited = {start: 0}
#     print(cost_visited)
#     visited = {start: None}

#     while queue:
#         cur_cost, cur_node = heappop(queue)
#         if cur_node == goal:
#             break

#         next_nodes = graph[cur_node]
#         print(next_nodes)
#         for next_node in next_nodes:
#             neigh_cost, neigh_node = next_node
#             new_cost = cost_visited[cur_node] + neigh_cost

#             if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
#                 heappush(queue, (new_cost, neigh_node))
#                 cost_visited[neigh_node] = new_cost
#                 visited[neigh_node] = cur_node
#     return visited

# start = 'A'
# goal = 'B'
# visited = dijkstra(start, goal, graph)

# cur_node = goal
# print(f'\npath from {goal} to {start}: \n {goal} ', end='')
# while cur_node != start:
#     cur_node = visited[cur_node]
#     print(f'---> {cur_node} ', end='')

