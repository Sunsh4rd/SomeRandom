#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

void inFile(int** a, int n)
{
	for (int i = 0; i < n; i++)
		for (int j = 0; j < n; j++)
			in >> a[i][j];
}

void print(int** a, int n)
{
	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
			out << a[i][j] << " ";
		out << endl;
	}
}

void sort(vector<int> & x)
{
	int k = 10;
	vector<vector<int> > b(100);
	for (int i = 0; i < k; i++)
	{
		for (int j = 0; j < x.size(); j++)
		{
			int idx = x[j] / int(pow(10, i)) % 10;
			b[idx].push_back(x[j]);
		}
		x.clear();
		for (int j = 9; j >= 0; j--)
			x.insert(x.end(), b[j].begin(), b[j].end());
		for (int j = 0; j < 10; j++)
			b[j].clear();
	}
}

void x_sort(int** a, int n)
{
	int L;
	for (int j = 0; j < n; j++)
	{
		vector <int> x;
		for (int i = 0; i < n; i++)
			x.push_back(a[i][j]);
		sort(x);
		L = 0;
		for (int i = 0; i < n; i++)
		{
			a[i][j] = x[L];
			L++;
		}
		x.clear();
	}
}

int main()
{
	int n;
	in >> n;
	int** a = new int*[n];
	for (int i = 0; i < n; i++)
		a[i] = new int[n];
	inFile(a, n);
	x_sort(a, n);
	print(a, n);
	return 0;
}