import json

INF = float('inf')
def printmatrix(m):
    r,c = len(m),len(m[0])
    for i in range(r):
        for j in range(c):
            print(m[i][j],end=" ")
        print()

with open("../srcs/graph.json", 'r') as f:
    graph_dict = json.load(f)
    
verts = list(graph_dict.keys())
v = len(verts)
m = [[None] * v for i in range(v)]
for i in range(v):
    for j in range(v):
        if i == j:
            m[i][j] = 0
        else:
            m[i][j] = INF

e = 0
for v in graph_dict:
    if graph_dict[v]:
        e += len(graph_dict[v])

l = list(graph_dict.items())

for i in l:
    if i[1]:
        a = i[1]
        a1 = list(map(int, a.keys()))
        val = list(a.values())
        idx = [int(i[0])] * len(a1)
    for i in range(len(idx)):
        m[idx[i]][a1[i]] = val[i]


printmatrix(m)
print("-------------------")
# apply our algo
# T.C = O(v^3)
for k in range(len(verts)):
    for i in range(len(verts)):
        for j in range(len(verts)):
            # cost of tmp path is less
            # update
            if m[i][k]+m[k][j] < m[i][j]:
                m[i][j] = m[i][k] + m[k][j]

printmatrix(m)


N = 10
vertex = []
for i in range(len(m)):
    ap = []
    k = 0
    for j in range(len(m)):
        if m[i][j] == INF:
            k += 1
            continue
        if k == len(verts) - 1:
            break
        if m[i][j] < N and m[i][j] != 0:
            ap.append(i)
        if len(ap) == len(verts) - 1 - k:
            vertex.append(i)
                
print(vertex)