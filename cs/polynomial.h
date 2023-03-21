#ifndef _POLYNOMIAL_H_
#define _POLYNOMIAL_H_

#include <vector>
#include "rational.h"
#include <algorithm>

class polynomial
{
private:
	std::vector<rational> coefficients;
	void normalize()
	{
		while(coefficients.size() > 1u &&
			  coefficients.back().get_p() == 0)
		{
			coefficients.pop_back();
		}

		if (coefficients.size() <= 1u)
			return;

		rational x = coefficients.back().reverse();
		for (auto & c: coefficients)
			c = c * x;
	}
public:
	polynomial() { coefficients.push_back(rational(0)); }
	polynomial(std::vector<rational> c): coefficients(c) 
	{ 
		if (c.size() == 0) 
			coefficients.push_back(rational(0));
	    normalize(); 
	};

	std::vector<rational> get_coefficients() { return this->coefficients; };

	void print()
	{
		for (auto c: get_coefficients())
			std::cout << c << " ";
		std::cout << std::endl;
	}

	std::pair<polynomial, polynomial> divmod(const polynomial & rsh)
	{
		if (rsh.coefficients.size() > this->coefficients.size())
			return { polynomial(), *this };
		
		auto div = std::vector<rational> (this->coefficients.size() - rsh.coefficients.size());

		auto mod = this->coefficients;
		return { polynomial(div), polynomial(mod) };
	}

	polynomial operator+(const polynomial & rsh) const
	{
		int lsh_size = coefficients.size();
		int rsh_size = rsh.coefficients.size();
		int res_size = std::max(lsh_size, rsh_size);
		int min_size = std::min(lsh_size, rsh_size);
		std::vector<rational> res(res_size);
		int i;
		for (i = 0; i < min_size; i++)
			res[i] = coefficients[i] + rsh.coefficients[i];
		for (; i < lsh_size; i++)
			res[i] = coefficients[i];
		for (; i < rsh_size; i++)
			res[i] = rsh.coefficients[i];

		return polynomial(res);
	}

	polynomial operator-(const polynomial rsh) const
	{
		int lsh_size = coefficients.size();
		int rsh_size = rsh.coefficients.size();
		int res_size = std::max(lsh_size, rsh_size);
		int min_size = std::min(lsh_size, rsh_size);
		std::vector<rational> res(res_size);
		int i;
		for (i = 0; i < min_size; i++)
			res[i] = coefficients[i] - rsh.coefficients[i];
		for (; i < lsh_size; i++)
			res[i] = coefficients[i];
		for (; i < rsh_size; i++)
			res[i] = -rsh.coefficients[i];

		return polynomial(res);
	}

	polynomial operator*(const polynomial rsh) const	
	{
		int ls = coefficients.size();
		int rs = rsh.coefficients.size();
		std::vector<rational> r(ls + rs - 1);
		for (int i = 0; i < ls; i++)
		{
			for (int j = 0; j < rs; j++)
			{
				r[i+j] = r[i+j] + coefficients[i] * rsh.coefficients[j];
			}
		}

		return polynomial(r);
	}

	polynomial operator/(const polynomial rsh) const
	{
		
		return polynomial();
	}

	~polynomial() = default;
	
};


#endif