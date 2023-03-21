#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>

using namespace std;
ifstream in("input.txt");
ofstream out("output.txt");

void Sort(vector<int> &v1) {
	for (int i = 1; i < v1.size(); i++)
		for (int j = i; j > 0 && v1[j - 1] > v1[j]; j--)
			swap(v1[j - 1], v1[j]);
}

int main()
{
	int n;
	in >> n;
	int** a = new int*[n];
	for (int i = 0; i < n; i++)
	{
		a[i] = new int[n];
		for (int j = 0; j < n; j++)
			in >> a[i][j];
	}

	for (int k = 1; k <= 2 * n - 2; k++) {
		vector<int> v1;
		for (int i = 0; i < n; i++) {
			if ((k - i < n) && (k - i >= 0))
				v1.push_back(a[i][k - i]);
		}

		Sort(v1);
		int L = 0;

		for (int i = 0; i < n; i++)
		{
			if ((k - i < n) && (k - i >= 0))
			{
				a[i][k - i] = v1[L];
				L++;
			}
		}
		v1.clear();
	}

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
			out << a[i][j] << " ";
		out << '\n';
	}

	in.close();
	out.close();
	return 0;
}