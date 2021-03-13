#include <iostream>
#include "polynomial.h"

int main()
{
	rational a(-4, 17);
	rational b(6, 85);
	rational c = a + b;
	rational d = c.reverse();
	rational e = a / rational(1, 2);
	rational f = a - b;
	rational g = b - a;
	std::cout << d << std::endl;
	std::cout << c.reverse() << std::endl;
	std::cout << c << std::endl;
	std::cout << e << std::endl;
	std::cout << f << std::endl;
	std::cout << g << std::endl;
	std::vector<rational> r;
	r.push_back(rational(21));
	r.push_back(rational(3));
	r.push_back(rational(7));
	polynomial p(r);
	p.print();
	return 0;
}