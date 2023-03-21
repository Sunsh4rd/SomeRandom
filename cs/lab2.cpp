#include <iostream>
#include <vector>
#include <ctime>
#include <math.h>

const int N = 10000; // Число выборок
double A = 0.0, B = 1.0;
double C = 1.0 / (1 - 2 * exp(-1));
double fx = 1 / (B - A);
double M = C * exp(-1);
double D = M / fx;

double fr(double x)
{
	if (x < 0) 
		return 0;
	if (x > 1)
		return 1;
	return C + (-C * x - C) * exp(-x);
}

int main()
{
	int m = 1 + (log(10) / log(2)) * log10(N); //Формула Стерджесса
	std::vector<double> p_inter(m);
	std::vector<std::pair <double, double>> interval(m);//отрезки
	std::vector<int> pop(m);
	double step = (B - A) / m;
	double start = A, end = start + step;
	for (int i = 0; i < m; i++)
	{
		pop[i] = 0;
		interval[i].first = start;
		interval[i].second = end;
		p_inter[i] = fr(end) - fr(start);
		start = end;
		end += step;
	}
	srand(time(0));
	double practicMathExp = 0;
	std::vector<double> sample(N);
	for (int i = 0; i < N;)
	{
		double x = (rand() * 1.0 / RAND_MAX) * (B - A) + A;
		double y = (rand() * 1.0 / RAND_MAX) * D * fx;
		if (y < (C * x / exp(x)))
		{
			sample[i] = x;
			for (int r = 0; r < m; r++)
			{
				if (x > interval[r].first && x < interval[r].second)
				{
					pop[r]++;
					break;
				}
			}
			practicMathExp += sample[i];
			i++;
		}
	}

	practicMathExp = practicMathExp / N;
	double teorMathExp = C * (2 - 5 * exp(-1));
	double practicDisp = 0;
	for (int i = 0; i < N; i++)
	{
		double x = sample[i] - practicMathExp;
		practicDisp += x * x;
	}
	practicDisp = practicDisp / N;
	double teorDisp = C * (6 - 16 * exp(-1)) - teorMathExp * teorMathExp;
	double hiSquared = 0;
	for (int i = 0; i < m; i++)
	{
		if (pop[i] == 0) 
			continue;
		double x = pop[i] - N * p_inter[i];
		hiSquared += x * x / (N * p_inter[i]);
	}
	
	std::cout << "Math exp:\n Teor math exp = " << teorMathExp << ", " << "Pract math exp = " << practicMathExp << std::endl;
	std::cout << "Disp:\n Teor disp = " << teorDisp << " , " << "Pract disp = " << practicDisp << std::endl;

	std::cout << m << " - Hi squared = " << hiSquared << std::endl;
	
	return 0;
}