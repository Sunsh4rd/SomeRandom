#include <iostream>
#include <string>

int main()
{
	int alph[] = { 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 };
	int n = sizeof(alph) / sizeof(alph[0]);
	int pos = 0 , len = 5;
	int idx[len];
	int password[len];
	int i;
	for (i = 0; i < len; i++)
	{
		idx[i] = 0;
		password[i] = alph[0];
	}

	for (;;)
	{
		for (i = n; (i >= 0) && (idx[i] == n); i--)
		{
			idx[i] = 0;
			password[i] = alph[0];
		}
		
		if (i < 0)
			break;
		
		password[i] = alph[++idx[i]];

		for (int i = 0; i < len; ++i)
			std::cout << password[i];

	}
	
	return 0;
}