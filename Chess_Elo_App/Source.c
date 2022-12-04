#include "Functions.h"


int main()
{
	Player head = { .name = {0}, .rating = 0, .next = NULL };
	PlayerPointer first = &head;

	bool run = true, run_5 = true, run_6 = true;
	char action_number[3] = { 0 };
	int action_number_int = 0;
	char whoWon = " ";
	char white_name[MAX_NAME_SIZE] = { 0 };
	char black_name[MAX_NAME_SIZE] = { 0 };
	PlayerPointer white = NULL, black = NULL;
	char a = " ";

	char filename[MAX_NAME_SIZE] = "Results.txt";

	while (run)
	{
		PrintALine();
		printf("Enter the number of the action you want to do:\n1) Add new player\n2) Play a game between two players\n3) Print all players\n4) Change username\n5) Write to file\n6) Read from file\n7) Remove player\n8) Exit\n");
		PrintALine();

		scanf("%s", action_number);

		action_number_int = atoi(action_number);

		switch (action_number_int)
		{
		case 1:
			CreateNewPlayerForm(first);
			break;

		case 2:
			printf("White:\n\n");
			white = FindPlayerByName(first);
			printf("\n\nBlack\n\n");
			black = FindPlayerByName(first);
			printf("Who won:\nEnter w (white), b (black) or d (draw)\n\nPress any other key to cancel\n\n");
			getchar();
			scanf("%c", &whoWon);

			if (whoWon == 'w' || whoWon == 'b' || whoWon == 'd')
			{
				EloRatingFunction(whoWon, white, black);

				printf("New ratings:\n\n");
				printf("%s  %d\n%s  %d\n\n", white->name, white->rating, black->name, black->rating);
			}

			break;
		case 3:
			PrintAllPlayers(first);
			break;
		case 4:
			ChangeUsername(first);
			break;
		case 5:
			printf("Do you want to SAVE current ratings?\n\n");
			run_5 = true;
			while (run_5)
			{
				printf("(y/n)\n\n");
				getchar();
				scanf("%c", &a);

				if (a == 'y' || a == 'Y')
				{
					WriteToFile(first, filename);
					SaveToFilePrintAnimation();
					run_5 = false;
				}

				else if (a == 'n' || a == 'N')
				{
					printf("OK\n\n");
					run_5 = false;
				}

				else
					printf("Wrong input, please try again.\n\n");
			}
			break;
		case 6:
			printf("Do you want to READ DATA from file?\n\n");
			run_6 = true;
			while (run_6)
			{
				printf("(y/n)\n\n");
				getchar();
				scanf("%c", &a);

				if (a == 'y' || a == 'Y')
				{
					ReadFromFile(first, filename);
					PrintALine();
					PrintAllPlayers(first);
					run_6 = false;
				}

				else if (a == 'n' || a == 'N')
				{
					printf("OK\n\n");
					run_6 = false;
				}

				else
					printf("Wrong input, please try again.\n\n");
			}
			
			break;
		case 7:
			RemovePlayer(first);
			break;
		case 8:
			printf("Do you want to save current ratings?\n\n");
			while (true)
			{
				printf("(y/n)\n\n");
				getchar();
				scanf("%c", &a);

				if(a == 'y' || a == 'Y')
				{
					WriteToFile(first, filename);
					SaveToFilePrintAnimation();
					printf("Shutting down!\n");
					PrintALine();
					return EXIT_SUCCESS;
				}

				else if(a == 'n' || a == 'N')
				{
					printf("Shutting down!\n");
					PrintALine();
					return EXIT_SUCCESS;
				}

				printf("Wrong input, please try again.\n\n");
			}
			
			run = false;
			break;
		default:
			printf("Wrong number, please try again.\n");
			break;
		}

	}

	
	return EXIT_SUCCESS;
}

