#include <iostream>
#include <vector>

using namespace std;

int bin_s(vector<int> a, int el, int l, int r)
{
	while (l < r)
	{
		int m = (l + r) / 2;
		int p = a[m];
		if (el > p)
			r = m - 1;
		else
			l = m + 1;
	}
	if (a[l] < el)
		return -1;
	else
		return l;
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	vector<int> a;
	int N, K, max = 0; cin >> N >> K;
	a.resize(100000);
	for (int i = 0; i < N; i++)
	{
		int x; cin >> x;
		a.push_back(x);
		if (x > max)
			max = x;
		for (int j = 0; j < x; j++)
			a[j] += x / (j + 1);
	}

	int k = bin_s(a, K, 0, max - 1);
	cout << ++k << endl;

	return 0;
}