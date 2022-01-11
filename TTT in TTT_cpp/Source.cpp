#define _CRT_SECURE_NO_WARNINGS
#include "Functions.h"



int main()
{
	cout << "Tic tac toe inside a tic tac toe!" << endl << endl; 

	PrintLine();

	bigBoard game;
	player p1, p2;
	p1.sign = 'x';
	p2.sign = 'o';
	int br = 1;

	game.Print();

	int number = 0;
	cout << "Enter a number from 1-9 which represents the matrix where you want to play:" << endl << endl;
	cin >> number;
	if (number < 1 || number > 9)return -1;
	number = number - 1;

	while (game.GameEnd() == '0')
	{
		if (br == 1)
		{
			br = 2;
			number = game.MakeAMove(number, p1.sign);
		}

		else
		{
			br = 1;
			number = game.MakeAMove(number, p2.sign);
		}

		game.Print();
	}

	return 0;
}