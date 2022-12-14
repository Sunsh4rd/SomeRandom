from itertools import product


g_matrix = [
    [0, 0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0],
    [1, 0, 1, 0, 0, 0, 0],
]


def nonadjacent_vertices(v, m):
    nonadjacent = [i for i in range(len(m[v])) if m[v][i] == 0]
    # for i in range(len(g_matrix[v])):
    #     if g_matrix[v][i] == 0:
    #         nonadjacent.append(i)

    return nonadjacent


def adjacent_vertices(v, m):
    adjacent = [i for i in range(len(m[v])) if m[v][i] == 1]
    # for i in range(len(g_matrix[v])):
    #     if g_matrix[v][i] == 0:
    #         nonadjacent.append(i)

    return adjacent


# for v in range(len(g_matrix)):


def maximal_independent_sets(v, s, ind):
    # if v == 7:
    #     return s
    print(v, ind, s)
    for row in ind:
        if sum(row) != 0:
            print('not yet')
            break
    else:
        print('found', s)
        return
    # if v not in s:
    s.append(v)
    print(s)
    n = [v] + adjacent_vertices(v, ind)
    # print(n)
    induced = [[i for i in row]for row in ind]
    # print(induced)
    for i in n:
        induced[v][i] = 0
        induced[i][v] = 0
    # print(induced)
    print(s)
    maximal_independent_sets(v+1, s, induced)
    # non = nonadjacent_vertices(v)
    # print(non)


print(maximal_independent_sets(0, [], g_matrix))

'''
[0,1,2]
[0,1,3]
...
[0,1,5]
[0,2,3]
'''
