#include <iostream>

using namespace std;

// pair<int, int> partition(vector<int> &a, int l, int r, int p)
// {
// 	int i = l, j = r;
// 	while (i <= j)
// 	{
// 		while (i <= r && a[i] < p) i++;
// 		while (j >= l && a[j] > p) j--;
// 		if (i <= j)
// 		{
// 			swap(a[i], a[j]);
// 			i++; j--;
// 		}
// 	}
// 	return make_pair(i, j);
// }

// void qsort(vector<int> &a, int l, int r)
// {
// 	int p = a[(l + r) / 2];
// 	pair<int, int> ij = partition(a, l, r, p);
// 	int i = ij.first, j = ij.second;
// 	if (l < j) qsort(a, l, j);
// 	if (i < r) qsort(a, i, r);
// }

void print(int * a, int n)
{
	for (int i = 0; i < n; i++)
		cout << a[i] << " ";
	cout << endl;
}

int bin_s(int * a, int el, int l, int r)
{
	while (l <= r)
	{
		int m = (l + r) / 2;
		int p = a[m];
		if (p == el)
		{
			return m;
		}
		if (el < p)
			r = m - 1;
		else
			l = m + 1;
	}
	return -1;
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	int N, K;
	cin >> N >> K;
	int * A = new int[N];
	for (int i = 0; i < N; ++i)
		cin >> A[i];

	return 0;
}