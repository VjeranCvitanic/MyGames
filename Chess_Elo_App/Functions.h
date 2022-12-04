#define _CRT_SECURE_NO_WARNINGS
#ifndef FUNCTIONS_H
#define FUNCTIONS_H

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <math.h>

#define MAX_NAME_SIZE 20
#define START_RATING 1500
#define MAX_LINE 1024
#define K 15

//1 for white
//2 for black
//0 for draw

struct _Player;
typedef struct _Player* PlayerPointer;
typedef struct _Player
{
	char name[MAX_NAME_SIZE];
	int rating;
	PlayerPointer next;
}Player;

PlayerPointer CreateNewPlayer(char name[]);

int CreateNewPlayerForm();

int InsertAfter(PlayerPointer prev, PlayerPointer q);

int InsertSorted(PlayerPointer first, PlayerPointer q);

int EloRatingFunction(char whoWon, PlayerPointer player_white, PlayerPointer player_black);

int PrintAllPlayers(PlayerPointer first);

int ReadFromFile(PlayerPointer first, char fileName[]);

void PrintALine();

PlayerPointer FindPlayer(PlayerPointer first, char username[]);

PlayerPointer FindPlayerByName(PlayerPointer first);

int DeleteAll(PlayerPointer first);

int DeleteAfter(PlayerPointer temp);

int WriteToFile(PlayerPointer first, char fileName[]);

PlayerPointer CreatePlayerWithRating(char username[], int rating);

int ChangeUsername(PlayerPointer first);

PlayerPointer FindPrevious(PlayerPointer first, PlayerPointer q);

int RemovePlayer(PlayerPointer first);

void SaveToFilePrintAnimation();

// TO DO
//void PrintLeaderboard(PlayerPointer first);


#endif
