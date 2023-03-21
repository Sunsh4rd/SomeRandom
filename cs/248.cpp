#include <iostream>
#include <vector>

using namespace std;

pair<int, int> partition(vector<pair<int, pair<int, int>>> &a, int l, int r, pair<int, pair<int, int>> p)
{
	int i = l, j = r;
	while (i <= j)
	{
		while (i <= r && a[i].second < p.second) i++;
		while (j >= l && a[j].second > p.second) j--;
		if (i <= j)
		{
			swap(a[i], a[j]);
			i++; j--;
		}
	}
	return make_pair(i, j);
}

void qsort(vector<pair<int, pair<int, int>>> &a, int l, int r)
{
	pair<int, pair<int, int>> p = a[(l + r) / 2];
	pair<int, int> ij = partition(a, l, r, p);
	int i = ij.first, j = ij.second;
	if (l < j) qsort(a, l, j);
	if (i < r) qsort(a, i, r);
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int N; cin >> N;
	vector<pair<int, pair<int, int>>> p;

	for (int i = 0; i < N; ++i)
	{	
		pair<int, pair<int, int>> a;
		a.first = i + 1;
		cin >> a.second.first >> a.second.second;
		p.push_back(a);
	}

	qsort(p, 0, N-1);

	for (int i = 0; i < N; ++i)
		cout << p[i].first << " ";

	cout << endl;

	return 0;
}