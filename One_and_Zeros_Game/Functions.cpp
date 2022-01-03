#include "Functions.h"

int RandomMatrix(int** m)
{
	srand(time(0));
	for(int i = 0; i< MATRIX_SIZE; i++)
		for (int j = 0; j < MATRIX_SIZE; j++)
		{
			*(*(m + i) + j) = rand() % 2;
		}

	return EXIT_SUCCESS;
}

int PrintMatrix(int** m)
{
	for(int i = 0; i < MATRIX_SIZE; i++)
	{
		cout << endl;
		for (int j = 0; j < MATRIX_SIZE; j++)
		{
			cout << *(*(m + i) + j) << " ";
		}
	}

	cout << endl;

	return EXIT_SUCCESS;
}

int PrintLine()
{
	cout << endl << "-------------------------------------------------------------------------------------------" << endl;
	cout << "-------------------------------------------------------------------------------------------" << endl << endl;

	return EXIT_SUCCESS;
}


//Prvi naèin
int** FindOnes(int** m)
{
	int temp = 0;
	
	List head = { 0 };
	head.couple[0] = -1;
	head.couple[1] = -1;
	head.next = NULL;

	Position first = &head;
	

	for(int i = 1; i < MATRIX_SIZE - 1; i++)
		for (int j = 1; j < MATRIX_SIZE - 1; j++)
		{
			if (*(*(m + i) + j) == 1)
			{
				Position q = CreateNewCouple(i, j);
				InsertNewCouple(first, q);
				temp = Remove(m, i, j, first->next);
				if (temp == 0)(*(*(m + i) + j) = 0);

				DeleteList(first);
				first->next = NULL;
			}
		}



	return m;
}

int Remove(int** m, int i, int j, Position first)
{
	int temp = 0;
	int temp1 = 0, temp2 = 0, temp3 = 0, temp4 = 0;
	if (CheckIfOnBorder(m,i,j))return 1;

	
	if(!CheckList(i,j + 1,first))
		if (*(*(m + i) + j + 1) == 1)
		{
			Position q = CreateNewCouple(i, j + 1);
			InsertNewCouple(first, q);
			temp1 = Remove(m, i, j + 1, first); 
		}
	
	if (temp1 != 1)
	{
		if (!CheckList(i + 1, j, first))if (*(*(m + i + 1) + j) == 1)
		{
			Position q = CreateNewCouple(i + 1, j);
			InsertNewCouple(first, q);
			temp2 = Remove(m, i + 1, j, first);
		}
	}

	if (temp2 != 1)
	{
		if (!CheckList(i, j - 1, first))if (*(*(m + i) + j - 1) == 1)
		{
			Position q = CreateNewCouple(i, j - 1);
			InsertNewCouple(first, q);
			temp3 = Remove(m, i, j - 1, first);
		}
	}

	if (temp3 != 1)
	{
		if (!CheckList(i - 1, j, first))if (*(*(m + i - 1) + j) == 1)
		{
			Position q = CreateNewCouple(i - 1, j);
			InsertNewCouple(first, q);
			temp4 = Remove(m, i - 1, j, first);
		}
	}
	
	

	temp = temp1 + temp2 + temp3 + temp4;

	return temp;
}

bool CheckIfOnBorder(int** m, int i, int j)
{
	if (i == MATRIX_SIZE - 1 || j == MATRIX_SIZE - 1 || i == 0 || j == 0)
		if (*(*(m + i) + j) == 1)
			return true;

	return false;
}

bool CheckList(int i, int j, Position current)
{
	Position temp = current;
	while (temp)
	{
		if (temp->couple[0] == i && temp->couple[1] == j)return true;
		else temp = temp->next;
	}

	return false;
}

Position CreateNewCouple(int i, int j)
{
	Position q = (Position)malloc(MAX_SIZE * sizeof(List));

	if (!q)
		return NULL;
	
	q->couple[0] = i;
	q->couple[1] = j;
	q->next = NULL;

	return q;
}

int InsertNewCouple(Position first, Position q)
{
	q->next = first->next;
	first->next = q;

	return EXIT_SUCCESS;
}

int DeleteList(Position first)
{
	Position temp = first->next;

	if (!temp)return EXIT_SUCCESS;

	while (temp)
	{
		Position q = temp;
		temp = temp->next;
		free(q);
	}

	return EXIT_SUCCESS;
}


//Drugi naèin
int** FindOnes2(int** m)
{
	for(int i = 0; i < MATRIX_SIZE; i++)
		for (int j = 0; j < MATRIX_SIZE; j++)
		{
			if (CheckIfOnBorder(m, i ,j) && *(*(m + i) + j) == 1)
			{
				m = Replace(m, i, j);
			}
		}

	return m;
}

int** Replace(int** m, int i, int j)
{
	*(*(m + i) + j) = 2;
	if ( i >= 0 && j + 1 >= 0 && i < MATRIX_SIZE && j + 1 < MATRIX_SIZE && *(*(m + i) + j + 1) == 1)Replace(m, i, j + 1);
	if ( i + 1 >= 0 && j >= 0 && i + 1 < MATRIX_SIZE && j < MATRIX_SIZE && *(*(m + i + 1) + j) == 1)Replace(m, i + 1, j);
	if ( i >= 0 && j - 1 >= 0 && i < MATRIX_SIZE && j - 1 < MATRIX_SIZE && *(*(m + i) + j - 1) == 1)Replace(m, i, j - 1);
	if ( i - 1 >= 0 && j >= 0 && i - 1 < MATRIX_SIZE && j < MATRIX_SIZE && *(*(m + i - 1) + j) == 1)Replace(m, i - 1, j);

	return m;
}

int End(int** m)
{
	for(int i = 0; i < MATRIX_SIZE; i++)
		for (int j = 0; j < MATRIX_SIZE; j++)
		{
			if (*(*(m + i) + j) == 1)
			{
				*(*(m + i) + j) = 0;
			}

			if (*(*(m + i) + j) == 2)
			{
				*(*(m + i) + j) = 1;
			}
		}

	return EXIT_SUCCESS;
}