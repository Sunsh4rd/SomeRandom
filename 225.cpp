#include <iostream>

using namespace std;

int bin_s(int * a, int el, int l, int r)
{
	while (l <= r)
	{
		int m = (l + r) / 2;
		int p = a[m];
		if (p == el)
			return m;
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
	
	int N, K, max = 0;
	cin >> N >> K;

	int * A = new int[N];
	for (int i = 0; i < N; ++i)
	{
		cin >> A[i];
		if (A[i] > max)
			max = A[i];
	}

	cout << bin_s(A, max, 0, N-1) << endl;

	return 0;
}