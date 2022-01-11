#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#include <iostream>

using namespace std;

class smallBoard
{
public:
	char m[3][3];
	char flag;

	smallBoard();
	void Print();
	void Fill();
	int MakeAMove(int number, char sign);
	char GameEnd();
	smallBoard operator=(smallBoard temp);
	bool operator==(smallBoard temp);
};

class player
{
public:
	char sign;
	string name;
	int win1v1 = 0;
	int winBot = 0;

	player();
	player(char s, string n, int w);

	//smallBoard MakeAMove(smallBoard b);
};

class bigBoard
{
public:
	smallBoard boards[9];
	bigBoard();
	void Print();
	char GameEnd();
	int MakeAMove(int number, char sign);
	bigBoard operator=(bigBoard temp);
	bool operator==(bigBoard temp);
};

void PrintLine();

#endif 

