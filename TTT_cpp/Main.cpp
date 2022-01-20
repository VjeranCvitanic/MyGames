#include <iostream>
#include <random>
#include <math.h>
#include <string>
#include <time.h>
#include <windows.h>
#include "Functions.h"
using namespace std;

int main()
{
	int tie = 0;
	int flag1 = 0;
	string a;
	int br = 0;
	int numOfMoves = 0;

	player p1('x', "Player one", 0);
	player p2('o', "Player two", 0);
	bot c('o', 0);

	while (1)
	{
		br = rand() % 2 + 1;
		board b;
		board5x5 b5;
		char temp = '0';
		Scoreboard(p1, p2, tie);
		Scoreboard(p1, c, tie);

		cout << "------------------------------------------------------" << endl << "------------------------------------------------------" << endl << endl;

		cout << "Do you want to play: " << endl << endl << "1v1 -> Enter 'yes'" << endl << "Against bot -> Enter 'bot'" << endl << "1v1 on 5x5 board -> Enter '5'" << endl << "Against bot on 5x5 board -> Enter 'bot5'" << endl << "Exit -> Enter 'no'" << endl << endl;
		cout << "Your input: ";
		cin >> a;
		cout << endl;
		if (a == "no")
		{
			cout << "Game over!" << endl << endl;
			cout << endl << "Final scoreboard: " << endl << endl;
			Scoreboard(p1, p2, tie);
			Scoreboard(p1, c, tie);
			break;
		}

		else if (a == "yes")
		{
			if (br == 1)
			{
				p1.sign = 'x';
				p2.sign = 'o';
			}

			else
			{
				p1.sign = 'o';
				p2.sign = 'x';
			}

			cout << "Game of tic-tac-toe is starting!" << endl << endl;
			while (temp == '0')
			{
				if (br == 1)
				{
					cout << p1.name << "'s move: (" << p1.sign << ")" << endl;
					b = p1.MakeAMove(b);
					br = 2;
				}
				else if (br == 2)
				{
					cout << p2.name << "'s move: (" << p2.sign << ")" << endl;
					b = p2.MakeAMove(b);
					br = 1;
				}

				b.Print();
				temp = b.GameEnd();
			}

			if (temp == 't')
			{
				cout << "Tie game." << endl;
				tie += 1;
			}

			else if (temp == p1.sign)
			{
				cout << "The winner is " << p1.name << "(" << p1.sign << ")!" << endl;
				p1.win1v1 += 1;
			}

			else if(temp == p2.sign)
			{
				cout << "The winner is " << p2.name << "(" << p2.sign << ")!" << endl;
				p2.win1v1 += 1;
			}
		}

		else if (a == "bot")
		{

			if (br == 1)
			{
				p1.sign = 'x';
				c.sign = 'o';
			}

			else
			{
				p1.sign = 'o';
				c.sign = 'x';
			}
			cout << "Game of tic-tac-toe vs bot is starting!" << endl << endl;
			while (temp == '0')
			{
				if (br == 1)
				{
					cout << p1.name << "'s move: (" << p1.sign << ")" << endl;
					b = p1.MakeAMove(b);
					br = 2;
				}
				else if (br == 2)
				{
					cout << c.name << "'s move: (" << c.sign << ")" << endl;
					if (WinInOne(c.sign, b) || DefendInOne(c.sign, b))
					{
						b = c.Move(b);
					}
					else 
					{
						Sleep(700);
						b = c.Move(b);
					}

					br = 1;
				}

				b.Print();
				temp = b.GameEnd();
			}

			if (temp == 't')
			{
				cout << "Tie game." << endl;
				c.tie += 1;
			}

			else if (temp == p1.sign)
			{
				cout << "The winner is " << p1.name << "(" << p1.sign << ")!" << endl;
				p1.winBot += 1;
			}

			else if (temp == c.sign)
			{
				cout << "The winner is " << c.name << "(" << c.sign << ")!" << endl;
				c.win += 1;
			}

		}

		else if (a == "5")
		{
		if (br == 1)
		{
			p1.sign = 'x';
			p2.sign = 'o';
		}

		else
		{
			p1.sign = 'o';
			p2.sign = 'x';
		}

		cout << "Game of tic-tac-toe on 5x5 board is starting!" << endl << endl << "The goal is to connect three!" << endl << endl;
		while (temp == '0')
		{
			if (br == 1)
			{
				cout << p1.name << "'s move: (" << p1.sign << ")" << endl;
				b5 = p1.MakeAMove(b5);
				br = 2;
			}
			else if (br == 2)
			{
				cout << p2.name << "'s move: (" << p2.sign << ")" << endl;
				b5 = p2.MakeAMove(b5);
				br = 1;
			}

			b5.Print();
			temp = b5.GameEnd();
		}

		if (temp == 't')
		{
			cout << "Tie game." << endl;
			tie += 1;
		}

		else if (temp == p1.sign)
		{
			cout << "The winner is " << p1.name << "(" << p1.sign << ")!" << endl;
			p1.win1v1 += 1;
		}

		else if (temp == p2.sign)
		{
			cout << "The winner is " << p2.name << "(" << p2.sign << ")!" << endl;
			p2.win1v1 += 1;
		}
		}

		//unfinished
		else if (a == "bot5")
		{
		if (br == 1)
		{
			p1.sign = 'x';
			c.sign = 'o';
		}

		else
		{
			p1.sign = 'o';
			c.sign = 'x';
		}
		cout << "Game of tic-tac-toe vs bot on 5x5 board is starting!" << endl << endl;
		while (temp == '0')
		{
			if (br == 1)
			{
				cout << p1.name << "'s move: (" << p1.sign << ")" << endl;
				b5 = p1.MakeAMove(b5);
				br = 2;
			}
			else if (br == 2)
			{
				//Sleep(700);
				b5 = c.Move(b5);
				br = 1;
			}

			b5.Print();
			temp = b5.GameEnd();
		}

		if (temp == 't')
		{
			cout << "Tie game." << endl;
			c.tie += 1;
		}

		else if (temp == p1.sign)
		{
			cout << "The winner is " << p1.name << "(" << p1.sign << ")!" << endl;
			p1.winBot += 1;
		}

		else if (temp == c.sign)
		{
			cout << "The winner is " << c.name << "(" << c.sign << ")!" << endl;
			c.win += 1;
		}
		}
		

		else
		{
			cout << "Wrong input, please try again:" << endl;
		}
	}

	return 0;
}