#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#include <iostream>
#include <stdio.h>  
#include <stdlib.h>   
#include <time.h> 
#include <Windows.h>

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
	int MakeAMoveBot(int number, char sign);
	char GameEnd();
};

class bot
{
public:
	char sign;
	bot();
	int Move();
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
};

class bigBoard
{
public:
	smallBoard boards[9];
	bigBoard();
	void Print();
	char GameEnd();
	int MakeAMove(int number, char sign);
	int MakeAMoveBot(int number, char sign);
};

void PrintLine();

#endif 

