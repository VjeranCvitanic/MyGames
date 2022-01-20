#include "Functions.h"

//small board functions

smallBoard::smallBoard()
{
    int i = 0, j = 0;
    for (i = 0; i < 3; i++)
        for (j = 0; j < 3; j++)
            m[i][j] = ' ';

    flag = '0';
}

void smallBoard::Print()
{
    cout << endl;
    cout << "    1   2   3" << endl;
    cout << "  -------------" << endl;
    cout << "A | " << m[0][0] << " | " << m[0][1] << " | " << m[0][2] << " |" << endl;
    cout << "  -------------" << endl;
    cout << "B | " << m[1][0] << " | " << m[1][1] << " | " << m[1][2] << " |" << endl;
    cout << "  -------------" << endl;
    cout << "C | " << m[2][0] << " | " << m[2][1] << " | " << m[2][2] << " |" << endl;
    cout << "  -------------" << endl;
    cout << endl << "////////////////////////////////////////////////////////" << endl;
    cout << "////////////////////////////////////////////////////////" << endl;
}

void smallBoard::Fill()
{
    int i = 0, j = 0;
    for (i = 0; i < 3; i++)
        for (j = 0; j < 3; j++)
            m[i][j] = flag;
}

char smallBoard::GameEnd()
{
    int a = 0, b = 0;

    while (a < 3)
    {
        if (m[a][b] == m[a][b + 1] and m[a][b] == m[a][b + 2] && m[a][b + 2] != ' ')
        {
            flag = m[a][b];
            Fill();
            return m[a][b];
        }

        a = a + 1;
    }

    a = 0;

    while (b < 3)
    {
        if (m[a][b] == m[a + 1][b] and m[a][b] == m[a + 2][b] && m[a][b] != ' ')
        {
            flag = m[a][b];
            Fill();
            return m[a][b];
        }

        b = b + 1;
    }

    b = 0;

    if (m[0][0] == m[1][1] and m[0][0] == m[2][2] and m[1][1] != ' ')
    {
        flag = m[1][1];
        Fill();
        return m[1][1];
    }

    else if (m[0][2] == m[1][1] and m[0][2] == m[2][0] and m[1][1] != ' ')
    {
        flag = m[1][1];
        Fill();
        return m[1][1];
    }

    else if (m[0][0] != ' ' and m[0][1] != ' ' and m[0][2] != ' ' and m[1][0] != ' ' and m[1][1] != ' ' and m[1][2] != ' ' and m[2][0] != ' ' and m[2][1] != ' ' and m[2][2] != ' ')
    {
        flag = 't';
        Fill();
        return 't';
    }

    else
    {
        flag = '0';
        return '0';
    }
}

int smallBoard::MakeAMove(int number, char sign)
{
    int br = 0;
    cout << "Enter a number from 1-9 which represents the square where you want to play:" << endl << endl;
    cin >> br;
    if (br < 1 || br > 9)return MakeAMove(number, sign);
    br = br - 1;

    int a = br / 3;
    int b = br % 3;

    if (m[a][b] == ' ')
    {
        m[a][b] = sign;
        GameEnd();
        return br;
    }

    else return MakeAMove(number, sign);
}

int smallBoard::MakeAMoveBot(int number, char sign)
{
    //srand(time(NULL));
    int i = rand() % 9;

    int a = i / 3;
    int b = i % 3;

    if (m[a][b] == ' ')
    {
        m[a][b] = sign;
        GameEnd();
        return i;
    }

    else MakeAMoveBot(number, sign);

    return number;
}

//player class functions

player::player()
{
    sign = ' ';
    name = { 0 };
    win1v1 = 0;
    winBot = 0;
}

player::player(char s, string n, int w)
{
    sign = s;
    name = n;
    win1v1 = w;
}


//Big board class functions

bigBoard::bigBoard()
{
    for (int i = 0; i < 9; i++)
    {
        boards[i];
    }
}

void bigBoard::Print()
{
    for (int i = 0; i < 3; i++)
    {
        //cout << 3*i + 1;
        for (int a = 0; a < 3;a++)
        {
            cout << "--------------------------------------------------" << endl;
            cout << " | " << boards[3 * i].m[a][0] << " | " << boards[3 * i].m[a][1] << " | " << boards[3 * i].m[a][2] << " |  -  | " << boards[3 * i + 1].m[a][0] << " | " << boards[3 * i + 1].m[a][1] << " | " << boards[3 * i + 1].m[a][2] << " |  -  | " << boards[3 * i + 2].m[a][0] << " | " << boards[3 * i + 2].m[a][1] << " | " << boards[3 * i + 2].m[a][2] << " | " << endl;
        }
        cout << "--------------------------------------------------" << endl;
    }


}

char bigBoard::GameEnd()
{
    int signal = 0;

    for (int i = 0; i < 3; i++)
    {
        if (boards[i].flag == boards[i + 1].flag && boards[i].flag == boards[i + 2].flag && boards[i].flag != '0')
            return boards[i].flag;
    }

    for (int i = 0; i < 3; i++)
    {
        if (boards[i].flag == boards[i + 3].flag && boards[i].flag == boards[i + 6].flag && boards[i].flag != '0')
            return boards[i].flag;
    }

    if (boards[0].flag == boards[4].flag and boards[0].flag == boards[8].flag and boards[0].flag != '0')
    {
        return boards[0].flag;
    }

    if (boards[2].flag == boards[4].flag and boards[2].flag == boards[6].flag and boards[2].flag != '0')
    {
        return boards[2].flag;
    }

    for(int i = 0; i < 9; i++)
    {
        if (boards[i].flag == '0')signal = 1;
    }
    if (signal == 0)return 't';

    return '0';
}

int bigBoard::MakeAMove(int number, char sign)
{
    if (boards[number].flag == '0')
    {
        number = boards[number].MakeAMove(number, sign);
        return number;
    }
    else return MakeAMove(number + 1, sign);
}

int bigBoard::MakeAMoveBot(int number, char sign)
{
    if (boards[number].flag == '0')
    {
        number = boards[number].MakeAMoveBot(number, sign);
        return number;
    }
    else return MakeAMoveBot(number + 1, sign);
}

//bot class functions

bot::bot()
{
    sign = ' ';
}

/*int bot::Move()
{
    srand(time(NULL));
    int i = rand() % 9;

    return i;
}*/



//other functions

void PrintLine()
{
    cout << endl << "----------------------------------------------------------------------------------------------------------------------" << endl;
    cout << "----------------------------------------------------------------------------------------------------------------------" << endl << endl << endl;
}