import json


def main():

    with open('pys\\12.json', 'r') as f:
        setup = json.load(f)
        n, g = setup['n'], setup['M']

    print(n, g)

    # for (int i=0; i<n; ++i)
    # 	for (int j=0; j<n; ++j)
    # 		deg[i] += g[i][j];

    deg = [sum(g[i]) for i in range(n)]
    print(deg)

    # int first = 0;
    # while (!deg[first])  ++first;

    first = 0
    while not deg[first]:
        first += 1

        # int v1 = -1,  v2 = -1;
    v1, v2 = -1, -1
    # bool bad = false;
    bad = False
    # for (int i=0; i<n; ++i)
    # 	if (deg[i] & 1)
    # 		if (v1 == -1)
    # 			v1 = i;
    # 		else if (v2 == -1)
    # 			v2 = i;
    # 		else
    # 			bad = true;
    for i in range(n):
        if deg[i] & 1:
            if v1 == -1:
                v1 = i
            elif v2 == -1:
                v2 = i
            else:
                bad = True

        # if (v1 != -1)
        # 	++g[v1][v2],  ++g[v2][v1];

    if v1 != -1:
        g[v1][v2] += 1
        g[v2][v1] += 1

        # stack<int> st;
        # st.push (first);
        # vector<int> res;
    st = []
    st.append(first)
    res = []
    while st:
        v = st.pop()
        for i in range(n):
            if g[v][i]:
                break

        if i == n:
            res.append(v)
            st.pop()
        else:
            g[v][i] -= 1
            g[i][v] -= 1
            st.append(i)
        # while (!st.empty())
        # {
        # 	int v = st.top();
        # 	int i;
        # 	for (i=0; i<n; ++i)
        # 		if (g[v][i])
        # 			break;
        # 	if (i == n)
        # 	{
        # 		res.push_back (v);
        # 		st.pop();
        # 	}
        # 	else
        # 	{
        # 		--g[v][i];
        # 		--g[i][v];
        # 		st.push (i);
        # 	}
        # }

    if v1 != -1:
        for i in range(len(res) - 1):
            if res[i] == v1 and res[i+1] == v2 or res[i] == v2 and res[i+1] == v1:
                res2 = []
                for j in range(i+1, len(res)):
                    res2.append(res[j])
                for j in range(1, i+1):
                    res2.append(res[j])
                res = res2[:]
                break
        # if (v1 != -1)
        # 	for (size_t i=0; i+1<res.size(); ++i)
        # 		if (res[i] == v1 && res[i+1] == v2 || res[i] == v2 && res[i+1] == v1)
        # 		{
        # 			vector<int> res2;
        # 			for (size_t j=i+1; j<res.size(); ++j)
        # 				res2.push_back (res[j]);
        # 			for (size_t j=1; j<=i; ++j)
        # 				res2.push_back (res[j]);
        # 			res = res2;
        # 			break;
        # 		}
    for i in range(n):
        for j in range(n):
            if g[i][j]:
                bad = True
        # for (int i=0; i<n; ++i)
        # 	for (int j=0; j<n; ++j)
        # 		if (g[i][j])
        # 			bad = true;
    if bad:
        print(-1)
    else:
        print(res)
        # if (bad)
        # 	puts ("-1");
        # else
        # 	for (size_t i=0; i<res.size(); ++i)
        # 		printf ("%d ", res[i]+1);


if __name__ == '__main__':
    main()
