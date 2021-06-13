/*
    A sequence of brackets is said to be balanced if:
        1. it contains no unmatched brackets
        2. the subset of brackets enclosed within the confines of a matched pair of brackets is also a matched pair of brackets
    
    Given a string of brackets, determine whether it is balanced or not.
*/

#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
    The function is expected to return a STRING.
    The function accepts STRING s as parameter.
 */

string isBalanced(string s) {
    bool balanced = true;
    stack<char> stk;
    int counts[2][3] = {0};
    /*
        [0][0] -> ( , [0][1] -> [ , [0][2] -> {
        [1][0] -> ) , [1][1] -> ] , [1][2] -> }
    */

    for (int i=0; i < s.length(); i++) {
        if (s[i]=='(')
            counts[0][0]++;
        else if (s[i]=='[')
            counts[0][1]++;
        else if (s[i]=='{')
            counts[0][2]++;
        else if (s[i]==')')
            counts[1][0]++;
        else if (s[i]==']')
            counts[1][1]++;
        else if (s[i]=='}')
            counts[1][2]++;
    }

    if ( // number of opening brackets equal to number of closing brackets for each type of bracket
        (counts[0][0] == counts[1][0]) && 
        (counts[0][1] == counts[1][1]) && 
        (counts[0][2] == counts[1][2])
    ) {

        string s_grpd = "";

        for (int i=0; i < s.length(); i++) {
            if (s[i]=='(' || s[i]=='[' || s[i]=='{')    // push opening brackets to stack
                stk.push(s[i]);
            else if (s[i]==')' || s[i]==']' || s[i]=='}') {  // pop from stack top if closing bracket is encountered
                s_grpd += stk.top();
                stk.pop();
                s_grpd += s[i];
            }
        }

        for (int i=0; i < s_grpd.length(); i+=2) {
            if ( // check whether correct pairs are formed
                (s_grpd[i] == '(' && s_grpd[i+1] == ')') || 
                (s_grpd[i] == '[' && s_grpd[i+1] == ']') || 
                (s_grpd[i] == '{' && s_grpd[i+1] == '}')
            ) {
                continue;
            }
            else {
                balanced = false;
                break;
            }
        }

    }
    else {
        balanced = false;
    }

    if (balanced)
        return "YES";
    
    return "NO";
}

int main()
{
    string t_temp;
    getline(cin, t_temp);

    int t = stoi(ltrim(rtrim(t_temp)));

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string s;
        getline(cin, s);

        string result = isBalanced(s);

        cout << result << "\n";
    }

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
