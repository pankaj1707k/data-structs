/*
    Implement a simple text editor. The editor contains an empty string S. 
    Perform Q operations of the following 4 types:
    1. append(W) - Append string W to the end of S
    2. delete(k) - Delete the last k characters from S
    3. print(k) - Print the k_th character of S (follow 1-based index)
    4. undo() - Undo the last (not previously undone) operation of the type 1 or 2, reverting S to the state it was in prior to that operation
*/

#include <bits/stdc++.h>

using namespace std;


int main() {
    int num_of_ops;
    cin >> num_of_ops;

    string s = "";
    string op;
    stack<string> stk;
    stk.push(s);
    int op_code;

    for (int i = 0; i < num_of_ops; i++) {
        cin >> op_code;
        s = stk.top();
        if (op_code == 1) {
            string temp_str;
            cin >> temp_str;
            s += temp_str;
            stk.push(s);
        } else if (op_code == 2) {
            int k;
            cin >> k;
            s = stk.top();
            s.erase(s.begin()+s.length()-k, s.end());
            stk.push(s);
        } else if (op_code == 3) {
            int pos;
            cin >> pos;
            s = stk.top();
            cout << s[pos-1] << endl;
        } else {
            stk.pop();
        }
    }

    return 0;
}