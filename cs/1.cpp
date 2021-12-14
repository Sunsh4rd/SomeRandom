#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

int INF = 1e9;
// ifstream in("7.txt");

int main()
{
	int n, m;
	cin >> n >> m;

	vector<vector<pair<int, int>>> g(n);

	for (int i = 0; i < m; i++)
	{
		int x, y, l;
		cin >> x >> y >> l;
		x--;
		y--;
		if (l < 0)
			g[x].push_back({y, l});
		else
		{
			g[x].push_back({y, l});
			g[y].push_back({x, l});
		}
	}

	int *d = new int[n];
	for (int i = 0; i < n; i++)
	{
		d[i] = INF;
	}
	d[0] = 0;

	for (int it = 0; it < n - 1; it++)
	{
		bool F = false;
		for (int v = 0; v < n; v++)
			for (auto to : g[v])
				if (d[v] != INF)
				{
					d[to.first] = min(d[to.first], d[v] + to.second);
					F = true;
				}
		for (int i = 0; i < n; i++)
			cout << d[i] << " ";

		cout << endl;

		if (!F)
			break;
	}

	for (int i = 1; i < n; i++)
		cout << d[i] << endl;

	return 0;
}