#include <iostream>

int main()
{
	int a = 4;
	double b = 1.5;
	std::cout << a - int(a) << " " << b - int(b) << std::endl;
	return 0;
}