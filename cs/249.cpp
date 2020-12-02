#include <iostream>
#include <vector>

using namespace std;

pair<int, int> partition(vector<int> &a, int l, int r, int p)
{
	int i = l, j = r;
	while (i <= j)
	{
		while (i <= r && a[i] < p) i++;
		while (j >= l && a[j] > p) j--;
		if (i <= j)
		{
			swap(a[i], a[j]);
			i++; j--;
		}
	}
	return make_pair(i, j);
}

void qsort(vector<int> &a, int l, int r)
{
	int p = a[(l + r) / 2];
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
	vector<int> A;
	for (int i = 0; i < N; ++i)
	{
		int x; cin >> x;
		A.push_back(x);
	}

	int M; cin >> M;
	vector<int> B;
	for (int i = 0; i < M; ++i)
	{
		int x; cin >> x;
		B.push_back(x);
	}

	int K; cin >> K;
	vector<int> C;
	for (int i = 0; i < K; ++i)
	{
		int x; cin >> x;
		C.push_back(x);
	}

	qsort(A, 0, N - 1);
	qsort(B, 0, M - 1);

	for (int l = 0; l < K; ++l)
	{
		bool OK = false;
		int i = 0, j = M - 1;
		while (i < N && j >= 0)
		{
			if (A[i] + B[j] == C[l])
			{
				OK = true;
				cout << "YES" << endl;
				break;
			}
			if (A[i] + B[j] < C[l])
				i++;
			else
				j--;
		}
		if (!OK)
			cout << "NO" << endl;
	}

	return 0;
}