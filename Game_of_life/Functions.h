#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#include <iostream>
#include <Windows.h>
#include <random>
#include <time.h>

#define Y_SIZE 75
#define X_SIZE 25
#define PROBABILITY 5

using namespace std;


class game
{
public:
	char world[X_SIZE][Y_SIZE] = { 0 };
	char copyWorld[X_SIZE][Y_SIZE] = { 0 };
	char liveSign;
	char deadSign;

	game();
	void Set(int x, int y);
	void SetRandom();
	void Live();
	void SaveState();
	int Neighbour(int i, int j);
	void Print();
};



#endif // !FUNCTIONS_H
