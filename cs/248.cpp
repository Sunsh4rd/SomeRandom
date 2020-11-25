#include <iostream>
#include <vector>

using namespace std;

struct Point
{
	int n, x, y;
};

pair<int, int> partition_x(vector<Point> &a, int l, int r, Point p)
{
	int i = l, j = r;
	while (i <= j)
	{
		while (i <= r && a[i].x < p.x) i++;
		while (j >= l && a[j].x > p.x) j--;
		if (i <= j)
		{
			swap(a[i], a[j]);
			i++; j--;
		}
	}
	return make_pair(i, j);
}

void qsort_x(vector<Point> &a, int l, int r)
{
	Point p = a[(l + r) / 2];
	pair<int, int> ij = partition_x(a, l, r, p);
	int i = ij.first, j = ij.second;
	if (l < j) qsort_x(a, l, j);
	if (i < r) qsort_x(a, i, r);
}

pair<int, int> partition_y(vector<Point> &a, int l, int r, Point p)
{
	int i = l, j = r;
	while (i <= j)
	{
		while (i <= r && a[i].y < p.y) i++;
		while (j >= l && a[j].y > p.y) j--;
		if (i <= j)
		{
			swap(a[i], a[j]);
			i++; j--;
		}
	}
	return make_pair(i, j);
}

void qsort_y(vector<Point> &a, int l, int r)
{
	Point p = a[(l + r) / 2];
	pair<int, int> ij = partition_y(a, l, r, p);
	int i = ij.first, j = ij.second;
	if (l < j) qsort_y(a, l, j);
	if (i < r) qsort_y(a, i, r);
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int N; cin >> N;
	vector<Point> p;

	for (int i = 0; i < N; ++i)
	{	
		Point a;
		a.n = i + 1;
		cin >> a.x >> a.y;
		p.push_back(a);
	}

	qsort_x(p, 0, N-1);
	qsort_y(p, 0, N-1);

	for (int i = 0; i < N; ++i)
		cout << p[i].n << " ";

	cout << endl;

	return 0;
}