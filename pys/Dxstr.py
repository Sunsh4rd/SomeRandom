# from priodict import priorityDictionary

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

Dijkstra(g, 'a')