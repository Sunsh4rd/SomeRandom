#ifndef _POLYNOMIAL_H_
#define _POLYNOMIAL_H_

#include <vector>
#include "rational.h"

class polynomial
{
private:
	std::vector<rational> coefficients;
	void normalize()
	{
		rational x = coefficients[0].reverse();
		for (auto & c: coefficients)
			c = c * x;
	}
public:
	polynomial() { coefficients.push_back(0); };
	polynomial(std::vector<rational> c): coefficients(c) { normalize(); };

	std::vector<rational> get_coefficients() { return this->coefficients; };

	void print()
	{
		for (auto c: get_coefficients())
			std::cout << c << " ";
		std::cout << std::endl;
	}

	const polynomial operator+(polynomial rsh)
	{
		int lsh_size = this->coefficients.size();
		int rsh_size = rsh.get_coefficients().size();
		int res_size = lsh_size > rsh_size ? lsh_size : rsh_size;
		std::vector<rational> res = lsh_size > rsh_size ? this->coefficients : rsh.get_coefficients();
		std::vector<rational> less = lsh_size < rsh_size ? this->coefficients : rsh.get_coefficients();
		for (int i = 0; i < res_size; i++)
			res[i] = res[i] + less[i];

		return polynomial(res);
	}

	// const polynomial operator-(const polynomial rsh)
	// {
	// 	return polynomial(this->p * rsh.get_q() - rsh.get_p() * this->q, this->q * rsh.get_q());
	// }

	// const polynomial operator*(const polynomial rsh)	
	// {
	// 	return polynomial(this->p * rsh.get_p(), this->q * rsh.get_q());
	// }

	// const polynomial operator/(const polynomial rsh)
	// {
	// 	return polynomial(this->p * rsh.get_q(), this->q * rsh.get_p());
	// }

	~polynomial() = default;
	
};


#endif