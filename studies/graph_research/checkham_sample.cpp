#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <memory.h>
#include <ctime>
#include <cmath>
#include <string>
#include <sys/times.h>

#define MAXN 16
#define mmax(x, y) (x)>(y)?(x):(y)
struct tms timebuffer;
// #define CPUTIME (times(&timebuffer),\
//               (double)(timebuffer.tms_utime + timebuffer.tms_stime) / CLK_TCK)


int  a[MAXN][MAXN]; // Матрица смежности
int  vec[MAXN]; // Вектор степеней
std::string code; // Код графа в формате graph6
int  n, m;
int  i, j;
int  k, p, el;
int  res;
long long  nTotal, nOre, nDirak;
bool bOre, bDirak;

void printGraph() {
	int i, j;
	std::cout << std::endl;
	for (i = 0; i < n ; i++) {
		for (j = 0; j < n; j++) std::cout << a[i][j] << " ";
		std::cout << std::endl;
	}
	for (i = 0; i < n; i++) std::cout << vec[i] << " ";
		std::cout << std::endl;
}

bool checkOre() {
	int i, j;
	for (i = 0; i <= n - 2; i++)
		for (j = i + 1; j <= n - 1; j++)
			if (a[i][j] == 0)
				if (vec[i] + vec[j] < n) return false;
	return true;
}

bool checkDirak() {
	for (int k = 0; k < n; k++)
		if (2 * vec[k] < n) return false;
	return true;
}

int main() {
	double t1, t2;
	// t1 = CPUTIME;

	while (!feof(stdin)) {
		std::cin >> code; // на вход получаем код графа в формате graph6
		if (feof(stdin)) break;
		n = code[0] - 63; // в первом байте хранится число вершин

		// Разбираем форма graph6

		nTotal++;
		bOre = checkOre();
		bDirak = checkDirak();
		if (bOre) nOre++;
		if (bDirak) nDirak++;
		// if (bOre && !bDirak) printGraph();
		// if (bOre && !bDirak) std::cout << code << std::endl;;
	}
	std::cout << "n:" << n << std::endl;
	std::cout << "Всего:" << nTotal << std::endl;
	std::cout << "Оре:" << nOre << std::endl;
	std::cout << "Дирак:" << nDirak << std::endl;

	// t2 = CPUTIME;
	// std::cout << "Время работы:" << t2 - t1 << "сек." << std::endl;
}