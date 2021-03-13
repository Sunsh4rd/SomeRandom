#ifndef _RATIONAL_H_
#define _RATIONAL_H_

#include <iostream>

class rational
{
private:
	int p;
	int q;
	void normalize()
	{
		int _gcd = gcd(p, q);
		p /= _gcd;
		q /= _gcd;
	}

public:
	rational(int p, int q): p(p), q(q) { normalize(); };
	rational(int p): rational(p, 1) {};

	int get_p() const { return this->p; }
	int get_q() const { return this->q; }

	static int gcd(int a, int b)
	{
		return b == 0 ? a : gcd(b, a%b); 
	}

	rational reverse()
	{
		return rational(this->q, this->p);
	}

	friend std::ostream & operator << (std::ostream &, const rational &);

	const rational operator+(const rational rsh)
	{
		return rational(this->p * rsh.get_q() + rsh.get_p() * this->q, this->q * rsh.get_q());
	}

	const rational operator-(const rational rsh)
	{
		return rational(this->p * rsh.get_q() - rsh.get_p() * this->q, this->q * rsh.get_q());
	}

	const rational operator*(const rational rsh)
	{
		return rational(this->p * rsh.get_p(), this->q * rsh.get_q());
	}

	const rational operator/(const rational rsh)
	{
		return rational(this->p * rsh.get_q(), this->q * rsh.get_p());
	}

	rational operator=(const rational rsh)
	{
		this->p = rsh.get_p();
		this->q = rsh.get_q();
		return (*this);
	}	



	~rational() = default;
	
};


std::ostream & operator << (std::ostream & out, const rational & lsh) 
{
	out << lsh.get_p() << "/" << lsh.get_q();
	return out;
}

#endif