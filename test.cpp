#include <iostream>

using namespace std;

void fill(int * &a, int n)
{
	for (int i = 0; i < n; ++i)
	{
		int x; cin >> x;
		a[i] = x;
	}
}

void print(int * a, int n)
{
	for (int i = 0; i < n; ++i)
	{
		cout << a[i] << endl;
	}
}

int main()
{
	int n; cin >> n;
	int * a = new int[n];
	fill(a, n);
	print(a, n);
	return 0;
}