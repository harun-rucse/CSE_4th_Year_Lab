#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;

    freopen("input2.txt", "r", stdin);

    cout << "Number of process: ";
    cin >> n;
    cout << n << endl;

    string instruction;
    string input_set[n][10];
    string output_set[n];
    int input_len[n];

    string dependency[15];

    for (int i = 0; i < n; i++)
    {
        cout << "Program order: ";
        cin >> instruction;
        cout << instruction << endl;

        // separate input set
        int indx = 0;
        for (int j = 5; j < instruction.size(); j = j + 2)
        {
            input_set[i][indx] = instruction[j];
            indx++;
        }
        input_len[i] = indx;

        // separate output set
        output_set[i] = instruction[3];
    }

    // check bernstein condition for parallism
    int iteration = 0;
    for (int i=0; i < n; i++)
    {
        for (int j=i+1; j < n; j++)
        {
            bool condition = true;

            // check Output1 n Output2
            if (output_set[i] == output_set[j]) {
                condition = false;

                dependency[iteration] = "P" + to_string(i+1) + " Output Dependent on P" + to_string(j+1);
                iteration++;
            }
                
            for (int k=0; k < input_len[i]; k++)
            {
                // check Input1 n Output2
                if (input_set[i][k] == output_set[j]) {
                    condition = false;
                    
                    dependency[iteration] = "P" + to_string(i+1) + " Anti Dependent on P" + to_string(j+1);
                    iteration++;
                }

                // check Output1 n Input2
                if (output_set[i] == input_set[j][k]) {
                    condition = false;
                    
                    dependency[iteration] = "P" + to_string(i+1) + " Flow Dependent on P" + to_string(j+1);
                    iteration++;
                } 
            }

            if (condition)
            {
                cout << "P" << i+1 << "||" << "P" << j+1 << endl;
            }
        }
    }

    cout << endl << "Dependency Graph" << endl;
    for(int i=0; i<iteration; i++) {
        cout << dependency[i] << endl;
    }

    return 0;
}
