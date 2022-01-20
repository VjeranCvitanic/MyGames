#ifndef FUNCTIONS_H
#define FUNCTIONS_H
#include <iostream>
#include <random>
#include <math.h>
#include <string>
#define MAX_NUM 9

using namespace std;

//board 3x3 class
class board
{
public:
	char m[3][3];

	board();
	void Print();
	char GameEnd();
	board operator=(board temp);
	bool operator==(board temp);
};		

//board 5x5 class
class board5x5
{
public:
	char m[5][5];

	board5x5();
	void Print();
	char GameEnd();
	board5x5 operator=(board5x5 temp);
	bool operator==(board5x5 temp);
};

//player class
class player
{
public:
	char sign;
	string name;
	int win1v1 = 0;
	int winBot = 0;

	player(); 
	player(char s, string n, int w);

	board MakeAMove(board b);
	board5x5 MakeAMove(board5x5 b);
};

//bot class
class bot
{
public:
	string name;
	char sign;
	int win;
	int tie;

	bot();
	bot(char s, int win);
	board Move(board b);
	board5x5 Move(board5x5 b);
};

//scoreboard -> prints out current result
void Scoreboard(player p1, player p2, int tie);
void Scoreboard(player p1, bot c, int tie);

//The minimax algorithm
int minimax(board b, bool isMax, char sign);
int minimax5x5(board5x5 b, bool isMax, char sign, int alpha, int beta, int depth, int numberOfMoves);

//return x if given o and vice versa
char otherSign(char sign);

//Checks if game can end in one move
int WinInOne(char sign, board b);
int DefendInOne(char sign, board b);

int WinInOne(char sign, board5x5 b, int& i, int& j);
int DefendInOne(char sign, board5x5 b, int& i, int& j);


#endif