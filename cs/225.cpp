#include <iostream>
#include <vector>

using namespace std;

int bin_s(vector<int> a, int x, int l, int r)
{
	while (r - l > 1)
	{
		int mid = (l + r) / 2;
		if (x >= a[mid])
			l = mid + 1;
		else
			r = mid - 1;
	}

	if (a[l] < x)
		return -1;
	else
		return l;
}

int main()
{
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);

	int N, K, max = 0; cin >> N >> K;
	vector<int> a(100000);
	for (int i = 0; i < N; i++)
	{
		int x; cin >> a[i];
		if (x > max)
			max = x;
		for (int j = 0; j < x; j++)
			a[j] += x / (j + 1);
	}

	int k = bin_s(a, K, 0, max);
	cout << ++k << endl;

	return 0;
}

// #include <iostream>
// #include <vector>

// using namespace std;

// int n, k;

// bool f(vector<int>& a, int x) {
// 	int count = 0;
// 	for (int i = 0; i < a.size(); i++)
// 		count += a[i] / x;
// 	return count >= k;
// }

// void bin_search(vector<int>& a, int& l, int& r) {
// 	while (r - l > 1) {
// 		int mid = (l + r) / 2;
// 		if (f(a, mid))
// 			l = mid;
// 		else r = mid;
// 		bin_search(a, l, r);
// 	}
// }

// int main() {
// 	cin >> n >> k;
// 	vector<int> a(n);
// 	for (int i = 0; i < n; i++)
// 		cin >> a[i];
// 	int l = 1, r = *max_element(a.begin(), a.end());
// 	bin_search(a, l, r);
// 	cout << l << endl;

// 	return 0;
// }