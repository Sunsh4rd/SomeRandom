#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>

using namespace std;

int INF = 1e9;
// ifstream in("7.txt");

int main()
{
	int n;
	cin >> n;
	int m;
	cin >> m;

	int **d = new int *[n];
	for (int i = 0; i < n; i++)
		d[i] = new int[n];

	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			d[i][j] = INF;

	for (int i = 0; i < m; i++)
	{
		int a, b, w;
		cin >> a >> b >> w;
		a--;
		b--;
		// if (w < 0)
		// {
		// 	d[a][b] = w;
		// }
		// else
		// {
			d[a][b] = w;
		// 	d[b][a] = w;
		// }
	}

	for (int i = 0; i < n; i++)
		d[i][i] = min(0, d[i][i]);

	for (int t = 0; t < n; t++)
	{
		for (int u = 0; u < n; u++)
		{
			for (int v = 0; v < n; v++)
			{
				if (d[u][t] < INF && d[t][v] < INF)
					d[u][v] = max(min(d[u][v], d[u][t] + d[t][v]), -INF);
			}
		}

		for (int i = 0; i < n; i++)
		{
			for (int j = 0; j < n; j++)
			{
				if (d[i][j] > 100)
					cout << "inf"
						 << " ";
				else
					cout << d[i][j] << " ";
			}
			cout << endl;
		}
		cout << t << " done" << endl;
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (d[i][j] == INF)
				cout << 0 << " ";
			else
				cout << d[i][j] << " ";
		}
		cout << endl;
	}

	return 0;
}