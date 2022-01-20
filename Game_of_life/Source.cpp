#include "Functions.h"


int main()
{
	game a;
	int x = 0, y = 0;
	/*cout << "Enter starting state (i.e. (34,67), (57, 89),...)" << endl;
	while (cin >> x >> y)
		a.Set(x, y);*/

	a.SetRandom();

	/*a.Set(1, 1);
	a.Set(1, 2);
	a.Set(1, 3);
	*/

	a.Print();

	while (true)
	{
		Sleep(1000);
		a.SaveState();
		a.Live();
		a.Print();
	}

	return 0;
}