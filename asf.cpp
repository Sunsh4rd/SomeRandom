#include <iostream>
#include <string>

int fib(int n)
{
	int f = 0, s = 1;
	while(n > 0)
	{
		int tmp = f + s;
		f = s;
		s = tmp;
		n--; 
	}
	return s;
}

int main()
{
	// std::string alph = "0123456789";
	// int n = alph.length() - 1;
	// int pos = 0 , len = 5;
	// int idx[len];
	// std::string password[len];
	// int i;
	// for (i = 0; i < len; i++)
	// {
	// 	idx[i] = 0;
	// 	password[i] = alph[0];
	// }

	// for (;;)
	// {
	// 	for (i = n; (i >= 0) && (idx[i] == n); i--)
	// 	{
	// 		idx[i] = 0;
	// 		password[i] = alph[0];
	// 	}

	// 	if (i < 0)
	// 	{
	// 		break;
	// 	}
	// 	password[i] = alph[++idx[i]];

	// 	std::cout<<password[i];
	// }
	
	int n; std::cin >> n;
	for (int i = 0; i < n; ++i)
	{
		std::cout << fib(i);
	}

	return 0;
}