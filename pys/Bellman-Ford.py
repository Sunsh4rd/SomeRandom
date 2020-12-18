import json
import math

def Bellman_Ford(gdict, start):
	verts = list(gdict.keys())
	dist = dict.fromkeys(verts, math.inf)
	dist[start] = 0
	for i in range(len(verts) - 1):
		for edge in gdict:
			if gdict[edge]:
				verts = list(gdict[edge].keys())
				for v in verts:
					if dist[edge] + gdict[edge][v] < dist[v]:
						dist[v] = dist[edge] + gdict[edge][v]

	for i in range(len(verts) - 1):
		for edge in gdict:
			if gdict[edge]:
				verts = list(gdict[edge].keys())
				for v in verts:
					if dist[edge] + gdict[edge][v] < dist[v]:
						dist[v] = -math.inf
	return dist

def main():

    with open("graphBF.json", 'r') as f:
        graph_dict = json.load(f)


    print(Bellman_Ford(graph_dict, '0'))


if __name__ == '__main__':
    main()
