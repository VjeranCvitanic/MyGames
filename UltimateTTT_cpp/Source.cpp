#define _CRT_SECURE_NO_WARNINGS
#include "Functions.h"



int main()
{
	cout << "Tic tac toe inside a tic tac toe!" << endl << endl; 

	PrintLine();

	bigBoard game;
	player p1, p2;
	bot b1, b2;
	p1.sign = 'x';
	p2.sign = 'o';
	b1.sign = 'x';
	b2.sign = 'o';
	int br = 1;
	int againstBot = 0;

	game.Print();

	if (againstBot == 0)
	{
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
	}
	
	else
	{
		//srand(time(NULL));
		int number = rand() % 9;
		while (game.GameEnd() == '0')
		{
			Sleep(1000);
			PrintLine();
			if (br == 1)
			{
				br = 2;
				number = game.MakeAMoveBot(number, b1.sign);
			}

			else
			{
				br = 1;
				number = game.MakeAMoveBot(number, b2.sign);
			}

			game.Print();
		}
	}

	return 0;
}