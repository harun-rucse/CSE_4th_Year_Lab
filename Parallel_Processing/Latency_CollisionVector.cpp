#include <bits/stdc++.h>
using namespace std;

int reservation_table[10][10];

int main()
{
    int row, col;

    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> row >> col;
    int store[col+1] = {0};

    for (int i=0; i < row; i++)
    {
        for (int j=0; j < col; j++)
        {
            cin >> reservation_table[i][j];
        }
    }

    for (int i=0; i < row; i++)
    {
        for (int j=0; j < col; j++)
        {
            if (reservation_table[i][j] == 1 && j != 0)
            {
                for (int k = j-1; k >= 0; k--)
                {
                    if ((reservation_table[i][j] - reservation_table[i][k]) == 0)
                    {
                        store[j-k] = 1;
                    }
                }
            }
        }
    }

    int max_forbidden_lattency = 0;
    cout << "Output of Forbidden latency: ";

    for (int i = 1; i <= col; i++)
    {
        if (store[i] == 1)
        {
            cout << i << " ";
            max_forbidden_lattency = i;
        }
    }
    cout << endl;
    cout << "Output of Permissible latency: ";

    for (int i = 1; i <= col; i++)
    {
        if (store[i] == 0)
        {
            cout << i << " ";
        }
    }
    cout << endl;
    cout << "Output of Collision Vector: ";
    for (int i = max_forbidden_lattency; i >= 1; i--)
    {
        cout << store[i] << " ";
    }
    cout << endl;

    return 0;
}