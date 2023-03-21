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
	r.push_back(rational(1));
	r.push_back(rational(1));
	r.push_back(rational(1));
	r.push_back(rational(1));
	r.push_back(rational(1));
	polynomial p(r);
	p.print();
	std::vector<rational> r1;
	r1.push_back(rational(1));
	r1.push_back(rational(1));
	r1.push_back(rational(1));
	r1.push_back(rational(1));
	r1.push_back(rational(1));
	polynomial q(r1);
	q.print();
	polynomial bb = p*q;
	p.print();
	q.print();
	bb.print();
	return 0;
}