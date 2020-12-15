import math
from heapq import *
import json

class Graph():

    def __init__(self, gdict = None):
        self.gdict = gdict

with open("graph.json") as f:
  graph_dict = json.load(f)
  g = Graph(graph_dict)



# with open("test_dijkstra.txt") as file: #Читаем файл
#   onstring = file.read().splitlines()
# dict = {}
# dict2 = {}


# for item in onstring:
#     key = item.split(" ")[0]
#     l = item.split(" ")[1:]
#     n = item.split(" ")[1:]
#     while len(l) != 0:
#       key2 = l.pop(0)
#       weith = l.pop(0)
#       dict2[key2] = weith
#       dict[key]= dict2
#     dict2 = {}
# print(dict)
# file.close()
#Создаем граф
# g = Graph(dict)

def dijkstra(gdict, start):
  verts = list(gdict.keys())
  visited = dict.fromkeys(verts, False)
  dist = dict.fromkeys(verts, math.inf)
  dist[start] = 0
  queue = []
  heappush(queue, (start, 0))
  while queue:
    idx, min_value = heappop(queue)
    visited[idx] = True
    if dist[idx] < min_value:
      continue
    if gdict[idx]:
      next_verts = list(gdict[idx].keys())
      for v in next_verts:
        if visited[v]:
          continue
        new_dist = dist[idx] + int(gdict[idx][v])
        if new_dist < dist[v]:
          dist[v] = new_dist
          heappush(queue, (v, new_dist))

  return dist

def dijkstra_wrapper(g, v):
  return dijkstra(g.gdict, v)


print(dijkstra_wrapper(g, '0'))
