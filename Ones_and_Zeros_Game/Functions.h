#ifndef FUNCTIONS_H
#define FUNCTIONS_H
#define MATRIX_SIZE 60      //Velièina matrice (MAX = 105, zbog ispisa)

#include <iostream>
#include <random>
#include <time.h>
#include <chrono>
#include <stdlib.h>

using namespace std;


struct _List;                            //Struktura liste, za spremanje puteva kojima se prolazilo
typedef struct _List* Position;
typedef struct _List
{
	int couple[2];
	Position next;
}List;

int RandomMatrix(int** m);             //Generira random matricu nula i jedinica

int PrintMatrix(int** m);				//Ispisuje matricu

int PrintLine();						//Ispisuje "------------------------------------------------------" x2

//int CopyMatrix(int** q, int** m);	
												//Dodatne funkcije za provjeru
//bool CheckIfEqual(int** q, int** m);

//Prvi naèin
int** FindOnes(int** m);               //Pronalazi jedinice koje nisu na rubu i za svaku zove funkciju Remove

int Remove(int** m, int i, int j, Position current);   //Rekurzivna funkcija, briše jedinice koje nisu povezane s rubom

bool CheckIfOnBorder(int** m, int i, int j);          //Vraæa true ako je dana pozicija rubna i ako je njena vrijednost 1

bool CheckList(int i, int j, Position current);      //Vraæa true ako je dani put(i, j) veæ isproban

Position CreateNewCouple(int i, int j);				//Kreira novi int[2] element

int InsertNewCouple(Position first, Position q);	//Stavlja novi element liste u listu

int DeleteList(Position first);						//Briše listu


//Drugi naèin
int** FindOnes2(int** m);							//Pronalazi jedinice na rubovima

int** Replace(int** m, int i, int j);				//Sve jedinice povezane s rubovima mijenja u dvice

int End(int** m);									//Jedinice mijenja u nule, dvice u jedinice
#endif 

