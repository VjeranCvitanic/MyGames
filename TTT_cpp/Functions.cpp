#include <iostream>
#include <random>
#include <math.h>
#include <tuple>
#include "Functions.h"
using namespace std;

//board class functions
void board::Print()
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
board::board()
{
    int i = 0, j = 0;
    for (i = 0; i < 3; i++)
        for (j = 0; j < 3; j++)
            m[i][j] = ' ';
}
char board::GameEnd()
{
    int a = 0, b = 0;

    while (a < 3)
    {
        if (m[a][b] == m[a][b + 1] and m[a][b] == m[a][b + 2] && m[a][b + 2] != ' ')
        {
            return m[a][b];
        }

        a = a + 1;
    }

    a = 0;

    while (b < 3)
    {
        if (m[a][b] == m[a + 1][b] and m[a][b] == m[a + 2][b] && m[a][b] != ' ')
        {
            return m[a][b];
        }

        b = b + 1;
    }

    b = 0;

    if (m[0][0] == m[1][1] and m[0][0] == m[2][2] and m[1][1] != ' ')
    {
        return m[1][1];
    }

    else if (m[0][2] == m[1][1] and m[0][2] == m[2][0] and m[1][1] != ' ')
    {
        return m[1][1];
    }

    else if (m[0][0] != ' ' and m[0][1] != ' ' and m[0][2] != ' ' and m[1][0] != ' ' and m[1][1] != ' ' and m[1][2] != ' ' and m[2][0] != ' ' and m[2][1] != ' ' and m[2][2] != ' ')
    {
        return 't';
    }

    else return '0';
}
board board::operator=(board temp)
{
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            m[i][j] = temp.m[i][j];

    return temp;
}
bool board::operator==(board temp)
{
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (m[i][j] != temp.m[i][j])
                return false;

    return true;
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
board player::MakeAMove(board b)
{
    string a = " ";
    while (1)
    {
        cout << "Pick a square:" << endl;
        cin >> a;

        if(a == "a1")
        {
            if (b.m[0][0] == ' ')
            {
                b.m[0][0] = sign;
                return b;
            }
        }

        else if (a == "a2")
        {
            if (b.m[0][1] == ' ')
            {
                b.m[0][1] = sign;
                return b;
            }
        }

        else if (a == "a3")
        {
            if (b.m[0][2] == ' ')
            {
                b.m[0][2] = sign;
                return b;
            }
        }


        else if (a == "b1")
        {
            if (b.m[1][0] == ' ')
            {
                b.m[1][0] = sign;
                return b;
            }
        }

        else if (a == "b2")
        {
            if (b.m[1][1] == ' ')
            {
                b.m[1][1] = sign;
                return b;
            }
        }

        else if (a == "b3")
        {
            if (b.m[1][2] == ' ')
            {
                b.m[1][2] = sign;
                return b;
            }
        }


        else if (a == "c1")
        {
            if (b.m[2][0] == ' ')
            {
                b.m[2][0] = sign;
                return b;
            }
        }

        else if (a == "c2")
        {
            if (b.m[2][1] == ' ')
            {
                b.m[2][1] = sign;
                return b;
            }
        }

        else if (a == "c3")
        {
            if (b.m[2][2] == ' ')
            {
                b.m[2][2] = sign;
                return b;
            }
        }

        else
        {
        cout << "Wrong input! Please try again:" << endl;
        }
    }
}
board5x5 player::MakeAMove(board5x5 b)
{
    string a = " ";
    while (1)
    {
        cout << "Pick a square:" << endl;
        cin >> a;

        if (a == "a1")
        {
            if (b.m[0][0] == ' ')
            {
                b.m[0][0] = sign;
                return b;
            }
        }

        else if (a == "a2")
        {
            if (b.m[0][1] == ' ')
            {
                b.m[0][1] = sign;
                return b;
            }
        }

        else if (a == "a3")
        {
            if (b.m[0][2] == ' ')
            {
                b.m[0][2] = sign;
                return b;
            }
        }

        else if (a == "a4")
        {
            if (b.m[0][3] == ' ')
            {
                b.m[0][3] = sign;
                return b;
            }
        }

        else if (a == "a5")
        {
            if (b.m[0][4] == ' ')
            {
                b.m[0][4] = sign;
                return b;
            }
        }

        else if (a == "b1")
        {
            if (b.m[1][0] == ' ')
            {
                b.m[1][0] = sign;
                return b;
            }
        }

        else if (a == "b2")
        {
            if (b.m[1][1] == ' ')
            {
                b.m[1][1] = sign;
                return b;
            }
        }

        else if (a == "b3")
        {
            if (b.m[1][2] == ' ')
            {
                b.m[1][2] = sign;
                return b;
            }
        }

        else if (a == "b4")
        {
            if (b.m[1][3] == ' ')
            {
                b.m[1][3] = sign;
                return b;
            }
        }

        else if (a == "b5")
        {
            if (b.m[1][4] == ' ')
            {
                b.m[1][4] = sign;
                return b;
            }
        }

        else if (a == "c1")
        {
            if (b.m[2][0] == ' ')
            {
                b.m[2][0] = sign;
                return b;
            }
        }

        else if (a == "c2")
        {
            if (b.m[2][1] == ' ')
            {
                b.m[2][1] = sign;
                return b;
            }
        }

        else if (a == "c3")
        {
            if (b.m[2][2] == ' ')
            {
                b.m[2][2] = sign;
                return b;
            }
        }

        else if (a == "c4")
        {
            if (b.m[2][3] == ' ')
            {
                b.m[2][3] = sign;
                return b;
            }
        }

        else if (a == "c5")
        {
            if (b.m[2][4] == ' ')
            {
                b.m[2][4] = sign;
                return b;
            }
        }

        else if (a == "d1")
        {
            if (b.m[3][0] == ' ')
            {
                b.m[3][0] = sign;
                return b;
            }
        }

        else if (a == "d2")
        {
            if (b.m[3][1] == ' ')
            {
                b.m[3][1] = sign;
                return b;
            }
        }

        else if (a == "d3")
        {
            if (b.m[3][2] == ' ')
            {
                b.m[3][2] = sign;
                return b;
            }
        }

        else if (a == "d4")
        {
            if (b.m[3][3] == ' ')
            {
                b.m[3][3] = sign;
                return b;
            }
        }
          
        else if (a == "d5")
        {
            if (b.m[3][4] == ' ')
            {
                b.m[3][4] = sign;
                return b;
            }
        }


        else if (a == "e1")
        {
            if (b.m[4][0] == ' ')
            {
                b.m[4][0] = sign;
                return b;
            }
        }

        else if (a == "e2")
        {
            if (b.m[4][1] == ' ')
            {
                b.m[4][1] = sign;
                return b;
            }
        }

        else if (a == "e3")
        {
            if (b.m[4][2] == ' ')
            {
                b.m[4][2] = sign;
                return b;
            }
        }

        else if (a == "e4")
        {
            if (b.m[4][3] == ' ')
            {
                b.m[4][3] = sign;
                return b;
            }
        }

        else if (a == "e5")
        {
            if (b.m[4][4] == ' ')
            {
                b.m[4][4] = sign;
                return b;
            }
        }

        else
        {
            cout << "Wrong input! Please try again:" << endl;
        }
    }
}

//bot class functions
bot::bot()
{
    name = "Bot";
    sign = ' ';
    win = 0;
    tie = 0;
}
bot::bot(char s, int w)
{
    name = "Bot";
    sign = s;
    win = w;
    tie = 0;
}
board bot::Move(board b)
{
    int bestMove[2] = { 0 };
    board btemp = b;
    int score = 0;
    int bestScore = -5;

    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
            if (btemp.m[i][j] == ' ')
            {
                btemp.m[i][j] = sign;
                score = minimax(btemp, false, sign);
                btemp.m[i][j] = ' ';
                if (score > bestScore)
                {
                    bestScore = score;
                    bestMove[0] = i;
                    bestMove[1] = j;
                }
            }

    b.m[bestMove[0]][bestMove[1]] = sign;
    return b;
}
board5x5 bot::Move(board5x5 b)
{
    int depth = 0;
    static int numOfMoves = 0;
    int i = 0, j = 0;
    numOfMoves++;
    int bestMove[2] = { 0 };
    board5x5 btemp = b;
    int score = 0;
    int bestScore = -5;
    srand(time(NULL));

    if (numOfMoves <= 2)
    {
        while (true)
        {
            
            int a = rand() % 2 + 1;
            int r = rand() % 2 + 1;
            if (b.m[a][r] == ' ') 
            {
                bestMove[0] = a;
                bestMove[1] = r;
                break;
            }
            
        }
    }



    else if (WinInOne(sign, b, i, j)) { bestMove[0] = i; bestMove[1] = j; }
    else if (DefendInOne(sign, b, i, j)) { bestMove[0] = i; bestMove[1] = j; }

    else 
        for (int i = 0; i < 5; i++)
            for (int j = 0; j < 5; j++)
                if (btemp.m[i][j] == ' ')
                {
                    int alpha = -5, beta = 5;
                    btemp.m[i][j] = sign;
                    score = minimax5x5(btemp, false, sign, alpha, beta, depth, numOfMoves);
                    btemp.m[i][j] = ' ';
                    if (score > bestScore)
                    {
                        bestScore = score;
                        bestMove[0] = i;
                        bestMove[1] = j;
                    }
                }

    b.m[bestMove[0]][bestMove[1]] = sign;
    return b;
}


//boardNxN class functions
board5x5::board5x5()
{
    for(int i = 0;i < 5; i++)
        for (int j = 0; j < 5; j++)
        {
            m[i][j] = ' ';
        }
}
void board5x5::Print()
{
    cout << endl;
    cout << "    1   2   3   4   5" << endl;
    cout << "  ---------------------" << endl;
    cout << "A | " << m[0][0] << " | " << m[0][1] << " | " << m[0][2] << " | " << m[0][3] << " | " << m[0][4] << " | " << endl;
    cout << "  ---------------------" << endl;
    cout << "B | " << m[1][0] << " | " << m[1][1] << " | " << m[1][2] << " | " << m[1][3] << " | " << m[1][4] << " | " << endl;
    cout << "  ---------------------" << endl;
    cout << "C | " << m[2][0] << " | " << m[2][1] << " | " << m[2][2] << " | " << m[2][3] << " | " << m[2][4] << " | " << endl;
    cout << "  ---------------------" << endl;
    cout << "D | " << m[3][0] << " | " << m[3][1] << " | " << m[3][2] << " | " << m[3][3] << " | " << m[3][4] << " | " << endl;
    cout << "  ---------------------" << endl;
    cout << "E | " << m[4][0] << " | " << m[4][1] << " | " << m[4][2] << " | " << m[4][3] << " | " << m[4][4] << " | " << endl;
    cout << "  ---------------------" << endl;
    cout << endl << "////////////////////////////////////////////////////////" << endl;
    cout << "////////////////////////////////////////////////////////" << endl;
}
char board5x5::GameEnd()
{
    int a = 0, b = 0;
    int flag = 0;

    //checks rows
    for (a = 0; a < 5; a++)
    {
        for (b = 0; b < 2; b++)
        {
            if (m[a][b] == m[a][b + 1] && m[a][b] == m[a][b + 2] && m[a][b] == m[a][b + 3] && m[a][b] != ' ')
            {
                return m[a][b];
            }
        }
    }

    //checks collumns
    for (b = 0; b < 5; b++)
    {
        for (a = 0; a < 2; a++)
        {
            if (m[a][b] == m[a + 1][b] && m[a][b] == m[a + 2][b] && m[a][b] == m[a + 3][b] && m[a][b] != ' ')
            {
                return m[a][b];
            }
        }
    }


    //checks the main diagonal
    for (a = 0; a < 2; a++)
    {
        if (m[a][a] == m[a + 1][a + 1] && m[a][a] == m[a + 2][a + 2] && m[a][a] == m[a + 3][a + 3] && m[a][a] != ' ')
        {
            return m[a][a];
        }

    }

    //checks the other diagonal
    for (a = 0; a < 2; a++)
    {
        if (m[a][4 - a] == m[a + 1][3 - a] && m[a][4 - a] == m[a + 2][2 - a] && m[a][4 - a] == m[a + 3][1 - a] && m[a][4 - a] != ' ')
        {
            return m[a][4 - a];
        }

    }


    if (m[1][0] == m[2][1] && m[1][0] == m[3][2] && m[1][0] == m[4][3] && m[1][0] != ' ')
        return m[1][0];

    if (m[0][1] == m[1][2] && m[0][1] == m[2][3] && m[0][1] == m[3][4] && m[0][1] != ' ')
        return m[0][1];

    if (m[0][3] == m[1][2] && m[0][3] == m[2][1] && m[0][3] == m[3][0] && m[0][3] != ' ')
        return m[0][3];

    if (m[1][4] == m[2][3] && m[1][4] == m[3][2] && m[1][4] == m[4][1] && m[1][4] != ' ')
        return m[1][4];


    //checks if the matrix is full -> (tie game)
    for (a = 0; a < 5; a++)
        for (b = 0; b < 5; b++)
        {
            if (m[a][b] == ' ')flag = 1;
        }

    if (flag == 0)return 't';

    else return '0';

}
board5x5 board5x5:: operator=(board5x5 temp)
{
    for (int i = 0; i < 5; i++)
        for (int j = 0; j < 5; j++)
            m[i][j] = temp.m[i][j];

    return temp;
}
bool board5x5::operator==(board5x5 temp)
{
    for (int i = 0; i < 5; i++)
        for (int j = 0; j < 5; j++)
            if (m[i][j] != temp.m[i][j])
                return false;

    return true;
}



//non class functions
char otherSign(char sign)
{
    if (sign == 'x')return 'o';
    else return 'x';
}
void Scoreboard(player p1, player p2, int tie)
{
    cout << "Result: " << p1.name << " :::: tie :::: " << p2.name << endl;
    cout << "             " << p1.win1v1 << "           " << tie << "            " << p2.win1v1 << endl;
}
void Scoreboard(player p1, bot c, int tie)
{
    cout << "Result: " << p1.name << " :::: tie :::: " << c.name << endl;
    cout << "             " << p1.winBot << "           " << c.tie << "        " << c.win << endl;
}
int WinInOne(char sign, board b)
{
    board btemp;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
        {
            btemp = b;
            if (b.m[i][j] == ' ')
            {
                btemp.m[i][j] = sign;
                if (btemp.GameEnd() == sign)
                    return 1;
            }
        }

    return 0;
}
int DefendInOne(char sign, board b)
{
    char stemp = ' ';
    stemp = otherSign(sign);

    board btemp;
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++)
        {
            btemp = b;
            if (b.m[i][j] == ' ')
            {
                btemp.m[i][j] = stemp;
                if (btemp.GameEnd() == stemp)
                {
                    btemp = b;
                    btemp.m[i][j] = sign;

                    return 1;
                }

            }
        }

    return 0;
}

int WinInOne(char sign, board5x5 b, int& n, int& m)
{
    for (int i = 0; i < 5; i++)
        for (int j = 0; j < 5; j++)
        {
            if (b.m[i][j] == ' ')
            {
                b.m[i][j] = sign;
                if (b.GameEnd() == sign)
                {
                    b.m[i][j] = ' ';
                    n = i;
                    m = j;
                    return 1;
                }

                b.m[i][j] = ' ';
            }
        }

    return 0;
}
int DefendInOne(char sign, board5x5 b, int& n, int& m)
{
    char stemp = ' ';
    stemp = otherSign(sign);

    for (int i = 0; i < 5; i++)
        for (int j = 0; j < 5; j++)
        {
            if (b.m[i][j] == ' ')
            {
                b.m[i][j] = stemp;
                if (b.GameEnd() == stemp)
                {
                    b.m[i][j] = ' ';
                    n = i;
                    m = j;
                    return 1;
                };

                b.m[i][j] = ' ';
            }
        }

    return 0;
}


//minimax algorithm  
int minimax(board b, bool isMax, char sign)
{
    int score = 0;
    int bestMove[2] = { 0 };
    if (b.GameEnd() == sign)return 1;
    else if (b.GameEnd() == 't')return 0;
    else if (b.GameEnd() == otherSign(sign))return -1;

    if (isMax)
    {
        int bestScore = -5;
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (b.m[i][j] == ' ')
                {
                    b.m[i][j] = sign;
                    score = minimax(b, false, sign);
                    b.m[i][j] = ' ';
                    if (score > bestScore)
                    {
                        bestScore = score;
                    }
                }
        return bestScore;
    }

    else
    {
        int bestScore = 5;
        for (int i = 0; i < 3; i++)
            for (int j = 0; j < 3; j++)
                if (b.m[i][j] == ' ')
                {
                    b.m[i][j] = otherSign(sign);
                    score = minimax(b, true, sign);
                    b.m[i][j] = ' ';
                    if (score < bestScore)
                    {
                        bestScore = score;
                    }
                }
        return bestScore;
    }
}


int minimax5x5(board5x5 b, bool isMax, char sign, int alpha, int beta, int depth, int numberOfMoves)
{
    depth++;
    if (numberOfMoves < 4 && depth > 7)return 0;
    if (numberOfMoves < 8 && depth > 9)return 0;
    else if (depth > 15)return 0;

    int score = 0;
    if (b.GameEnd() == sign)return 1;
    else if (b.GameEnd() == 't')return 0;
    else if (b.GameEnd() == otherSign(sign))return -1;

    if (isMax)
    {
        int bestScore = -5;
        for (int i = 0; i < 5; i++)
            for (int j = 0; j < 5; j++)
                if (b.m[i][j] == ' ')
                {
                    b.m[i][j] = sign;
                    score = minimax5x5(b, false, sign, alpha, beta, depth, numberOfMoves);
                    b.m[i][j] = ' ';
                    if (alpha < score)alpha = score;
                    if (beta <= alpha)
                    {
                        break;
                    }
                    if (score > bestScore)
                    {
                        bestScore = score;
                    }
                }
                
        return bestScore;
    }

    else
    {
        int bestScore = 5;
        for (int i = 0; i < 5; i++)
            for (int j = 0; j < 5; j++)
                if (b.m[i][j] == ' ')
                {
                    b.m[i][j] = otherSign(sign);
                    score = minimax5x5(b, true, sign, alpha, beta, depth, numberOfMoves);
                    b.m[i][j] = ' ';
                    if (score < beta)beta = score;
                    if (beta <= alpha)
                    {
                        break;
                    }
                    if (score < bestScore)
                    {
                        bestScore = score;
                    }
                }
                
            
            
        return bestScore;
    }
}




