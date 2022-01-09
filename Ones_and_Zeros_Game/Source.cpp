#include <iostream>
#include "Functions.h"

using namespace std;

										//Objašnjenja funkcija su u header file-u

int main()
{
	int flag = 0;
	int flag1 = 0;
	int flag2 = 0;
	while (flag == 0)
	{
		int** matrix = NULL;
		matrix = (int**)malloc(MATRIX_SIZE * sizeof(int*));
		char c = ' ';
		int br = 0;

		for (int i = 0; i < MATRIX_SIZE; i++)
		{
			*(matrix + i) = (int*)malloc(MATRIX_SIZE * sizeof(int));
		}

		RandomMatrix(matrix);

		PrintLine();
		cout << "Randomly generated matrix(" << MATRIX_SIZE << "x" << MATRIX_SIZE << "):" << endl;

		PrintMatrix(matrix);
		PrintLine();

		cout << endl;

		while (br == 0)
		{
			cout << "Select: 1st way(Enter '1') or 2nd way(Enter '2')." << endl << "If you want information about two ways(Enter 'i' or 'I')." << endl;

			cin >> c;

			if (c == '1')
			{
				br = 1;
				matrix = FindOnes(matrix);			//Prvi naèin -> Pronalazi jedinice koje nisu povezane s rubovima i briše ih
				PrintLine();
				cout << endl << "First method: " << endl;
				PrintMatrix(matrix);
				PrintLine();
			}

			else if (c == '2')
			{
				br = 1;
				matrix = FindOnes2(matrix);				//Drugi naèin -> Sve jedinice povezane s rubovima mijenja u dvice, ostale jedinice mijenja u nule, zatim dvice vraæa u jedinice
				End(matrix);
				PrintLine();
				cout << endl << "Second method: " << endl;
				PrintMatrix(matrix);
				PrintLine();
			}

			else if (toupper(c) == 'I')
			{
				PrintLine();
				cout << endl << "First method finds all ones(1) disconnected from edges and replaces them with zeroes(0) directly." << endl << endl << "Second method finds all ones(1) connected with edges, replaces them with twos(2)," << endl << "then replaces remaining ones(1) with zeroes(0), finally switches twos(2) back to ones(1)." << endl;
				PrintLine();
			}

			else 
			{
				cout << "Wrong input, please try again. " << endl;
				PrintLine();
			}

		}

		flag1 = 0;
		while (flag1 == 0)
		{
			cout << "If you want to try again with another random matrix(Enter -> 'a' or 'A')." << endl << "Else(Enter -> 'e' or 'E')" << endl;

			cin >> c;

			if (toupper(c) == 'A')
			{
				br = 0;
				flag1 = 1;
			}

			else if (toupper(c) == 'E')
			{
				flag2 = 1;
				flag1 = 1;
			}

			else
			{
				cout << "Wrong input, please try again. " << endl << endl;
				PrintLine();
			}
		}

		if (flag2 == 1)break;
	}
	
	PrintLine();
	
	return EXIT_SUCCESS;
}