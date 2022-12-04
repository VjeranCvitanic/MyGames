#include "Functions.h"

PlayerPointer CreateNewPlayer(char name[])
{
	PlayerPointer q = NULL;
	q = (PlayerPointer)malloc(sizeof(Player));
	if (!q)
		return NULL;

	strcpy(q->name, name);
	q->rating = START_RATING;
	q->next = NULL;

	return q;
}

int EloRatingFunction(char whoWon, PlayerPointer player_white, PlayerPointer player_black)
{
	float whiteWin = 0;
	float blackWin = 0;
	float probability_of_winning_white = 1.0 / (1 + pow(10, ((player_white->rating - player_black->rating) / 400)));
	float probability_of_winning_black = 1.0 / (1 + pow(10, ((player_black->rating - player_white->rating) / 400)));

	if (whoWon == 'w')
		whiteWin = 1;
	else if (whoWon == 'b')
		blackWin = 1;
	else if (whoWon == 'd')
	{
		whiteWin = 0.5;
		blackWin = 0.5;
	}

	player_white->rating = player_white->rating + (int)K * (whiteWin - probability_of_winning_white);
	player_black->rating = player_black->rating + (int)K * (blackWin - probability_of_winning_black);

	return EXIT_SUCCESS;
}

int InsertAfter(PlayerPointer prev, PlayerPointer q)
{
	if (!q || !prev)
		return EXIT_FAILURE;

	q->next = prev->next;
	prev->next = q;

	return EXIT_SUCCESS;
}

int InsertSorted(PlayerPointer first, PlayerPointer q)
{
	PlayerPointer temp = first;
	
	while (temp->next && strcmp(temp->next->name, q->name) < 0)
		temp = temp->next;

	if (temp->next && strcmp(temp->next->name, q->name) == 0)
	{
		printf("UserName already taken, please try another one\n");
		return EXIT_FAILURE;
	}

	
	InsertAfter(temp, q);
	

	return EXIT_FAILURE;
}

int CreateNewPlayerForm(PlayerPointer first)
{
	PlayerPointer q = NULL;
	char username[MAX_NAME_SIZE] = { 0 };

	printf("\nEnter new player username:\n");

	scanf("%s", username);

	q = CreateNewPlayer(username);

	if (q)
	{
		InsertSorted(first, q);
	}

	return EXIT_SUCCESS;
}

int PrintAllPlayers(PlayerPointer first)
{
	PlayerPointer temp = first->next;

	PrintALine();

	printf("Username | ELO rating\n\n");

	while (temp)
	{	
		printf("%s  %d\n", temp->name, temp->rating);
		temp = temp->next;
	}

	PrintALine();

	return EXIT_SUCCESS;
}

int ReadFromFile(PlayerPointer first, char fileName[])
{
	FILE* fp = NULL;
	char buffer[100] = { 0 };
	char username[MAX_NAME_SIZE] = { 0 };
	int rating = 0;
	fp = fopen(fileName, "r");
	PlayerPointer q = NULL;

	if (!fp)
		return EXIT_FAILURE;

	while (!feof(fp))
	{
		fgets(buffer, MAX_LINE, fp);
		
		sscanf(buffer, "%s  %d\n", username, &rating);

		q = CreatePlayerWithRating(username, rating);

		InsertSorted(first, q);
	}

	fclose(fp);

	return EXIT_SUCCESS;
}

void PrintALine()
{
	printf("\n\n");
	printf("----------------------------------------------------------------------------------");
	printf("\n\n");
}

PlayerPointer FindPlayer(PlayerPointer first, char username[])
{
	PlayerPointer temp = first->next;

	while (temp && strcmp(temp->name, username) < 0)
		temp = temp->next;

	if (!temp || strcmp(temp->name, username) > 0)
	{
		return NULL;
	}

	return temp;
}

PlayerPointer FindPlayerByName(PlayerPointer first)
{
	bool run = true;
	char name[MAX_NAME_SIZE] = { 0 };
	PlayerPointer q = NULL;

	while (run)
	{
		printf("Enter the name of the player:\n");
		scanf("%s", name);

		q = FindPlayer(first, name);

		if (q)
			run = false;
		else
			printf("There is no player with that username.\n");
	}

	return q;
}

int DeleteAll(PlayerPointer first)
{
	while (first->next)
		DeleteAfter(first);

	return EXIT_SUCCESS;
}

int DeleteAfter(PlayerPointer temp)
{
	PlayerPointer q = NULL;
	if (!temp || !temp->next)
		return EXIT_SUCCESS;

	else
	{
		q = temp->next;
		temp->next = q->next;
		free(q);
	}

	return EXIT_SUCCESS;
}

int WriteToFile(PlayerPointer first, char fileName[])
{
	FILE* fp = fopen(fileName, "w");
	if (!fp)
		return EXIT_FAILURE;

	PlayerPointer temp = first->next;

	while (temp)
	{
		fprintf(fp, "%s  %d", temp->name, temp->rating);
		temp = temp->next;
		if (temp)
			fprintf(fp, "\n");
	}

	fclose(fp);

	return EXIT_SUCCESS;
}

PlayerPointer CreatePlayerWithRating(char username[], int rating)
{
	PlayerPointer q = (PlayerPointer)malloc(sizeof(Player));
	if (!q)
		return NULL;

	strcpy(q->name, username);
	q->rating = rating;
	q->next = NULL;

	return q;
}

PlayerPointer FindPrevious(PlayerPointer first, PlayerPointer q)
{
	PlayerPointer temp = first;

	while (temp->next && temp->next != q)
		temp = temp->next;

	if (temp->next)
		return temp;

	return NULL;
}

int ChangeUsername(PlayerPointer first)
{
	PlayerPointer q = FindPlayerByName(first);
	PlayerPointer prev = FindPrevious(first, q);
	char newUsername[MAX_NAME_SIZE] = { 0 };

	while (true)
	{
		printf("Enter new username:\n");
		scanf("%s", newUsername);

		if (FindPlayer(first, newUsername) == NULL)
		{
			strcpy(q->name, newUsername);
			prev->next = prev->next->next;
			InsertSorted(first, q);
			return EXIT_SUCCESS;
		}

		else
		{
			printf("Username already taken, please try another one:\n\n");
		}
	}

	return EXIT_SUCCESS;
}

int RemovePlayer(PlayerPointer first)
{
	PlayerPointer q = FindPlayerByName(first);
	char a = " ";

	printf("Are you sure you want to remove player %s, rating: %d\n\n", q->name, q->rating);

	while (true)
	{
		printf("(y/n)\n");
		getchar();
		scanf("%c", &a);

		if (a == 'y' || a == 'Y')
		{
			PlayerPointer prev = FindPrevious(first, q);
			prev->next = prev->next->next;
			free(q);
			return EXIT_SUCCESS;
		}

		else if (a == 'n' || a == 'N')
		{
			return EXIT_SUCCESS;
		}

		printf("Wrong input, please try again:\n\n");
	}
	
	return EXIT_SUCCESS;
}

void SaveToFilePrintAnimation()
{
	PrintALine();
	printf("..........Saving current data to a file..........\n\n");
	printf("\t\tProgress saved!\n");
	PrintALine();
}

