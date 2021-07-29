/* https://www.codechef.com/LRNDSA02/problems/INPSTFIX */

#include <bits/stdc++.h>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t, n;
    cin >> t;
    stack<char> stk;
    string infix;

    unordered_map<char,int> operator_precedence;
    operator_precedence['^'] = 3;
    operator_precedence['/'] = operator_precedence['*'] = 2;
    operator_precedence['+'] = operator_precedence['-'] = 1;

    while (t--) {
        cin >> n;
        cin >> infix;

        string postfix = "";

        for (int i = 0; i < n; i++) {
            if (infix[i] == '(')
                stk.push(infix[i]);
            else if (infix[i] == ')') {
                while (stk.top()!='(') {
                    postfix += stk.top();
                    stk.pop();
                }
                stk.pop();
            } else if (infix[i] >= 'A' && infix[i] <= 'Z')
                postfix += infix[i];
            else {
                while (!stk.empty() && operator_precedence[infix[i]] <= operator_precedence[stk.top()] && stk.top()!='(') {
                    postfix += stk.top();
                    stk.pop();
                }
                stk.push(infix[i]);
            }
        }

        while (!stk.empty()) {
            postfix += stk.top();
            stk.pop();
        }

        cout << postfix << endl;
    }

    return 0;
}