#include <iostream>
//g++  -I/usr/local/include statements.cpp -o statements

int main()
{
	// Example of a single statement
	std::cout << "Hi there!\n";

	std::cout << "Hi there!\n"; std::cout << "Strange things are afoot...\n";


	// Example of a compound statement
	{
		int a = 10;
		int b = 20;
		int result = a + b;
	}
	// std::cout << result;

	int a = 10;
	int b = 20;
	if ( a > 5 )  { b=a; a++; }


	if (a > 5) {
		// This is K&R style
		std::cout << "Hi there!\n";
	}

	if (a > 5) 
	{
		// This is ANSI C++ style
		std::cout << "Hi there!\n";
	}

	if (a > 5) 
	{
		// This is GNU style
		std::cout << "Hi there!\n";
	}

	return 0;
}

