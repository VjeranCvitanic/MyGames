#include "Functions.h"

game::game()
{
	liveSign = 'O';
	deadSign = '.';
	for (int i = 0; i < X_SIZE; i++)
		for(int j = 0; j < Y_SIZE; j++)
		{
			world[i][j] = deadSign;
			copyWorld[i][j] = deadSign;
		}
}

void game::Set(int x, int y)
{
	world[x][y] = liveSign;
}

void game::SetRandom()
{
	srand(time(NULL));
	for(int i = 0; i < X_SIZE; i++)
		for (int j = 0; j < Y_SIZE; j++)
		{
			int br = rand() % PROBABILITY;
			if (br == 1)
				world[i][j] = liveSign;
		}
}

void game::Live()
{
	
	for (int i = 0; i < X_SIZE; i++)
		for (int j = 0; j < Y_SIZE; j++)
		{
			int temp = Neighbour(i, j);

			if (copyWorld[i][j] == deadSign)
			{
				/*if (temp == 3)
				{
					copyWorld[i][j] == liveSign;
				}*/
				copyWorld[i][j] = liveSign;
			}

			else
			{
				if (temp < 2 || temp > 3)
				{
					world[i][j] = deadSign;
				}
			}
		}
}

int game::Neighbour(int i, int j)
{
	int temp = 0;

	for(int a = -1; a < 2; a++)
		for (int b = -1; b < 2; b++)
		{
			if ((a != 0 || b != 0) && (i + a >= 0 && j + b >= 0 && i + a < X_SIZE && j + b < Y_SIZE))
			{
				if (copyWorld[i + a][j + b] == liveSign)temp++;
			}
		}

	return temp;
}

void game::Print()
{
	cout << "--------------------------------------------------------------------------------";
	for (int i = 0; i < X_SIZE; i++)
	{
		cout << endl;
		cout << "| ";
		for (int j = 0; j < Y_SIZE; j++)
		{
			cout << world[i][j];
		}
		cout << " |";
	}
	cout << endl << "--------------------------------------------------------------------------------" << endl;
}

void game::SaveState()
{
	for (int i = 0; i < X_SIZE; i++)
		for (int j = 0; j < Y_SIZE; j++)
		{
			copyWorld[i][j] = world[i][j];
		}
}