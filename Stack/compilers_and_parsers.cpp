/* https://www.codechef.com/LRNDSA02/problems/COMPILER */

#include <bits/stdc++.h>
using  namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    while (t--) {
        string s;
        cin >> s;
        vector<int> stk;
        int l = s.length();
        int m = 0;  // length of longest prefix
        for (int i = 0; i < l; i++) {
            if (s[i] == '<')
                stk.push_back(s[i]);
            else if (!stk.empty() && s[i] == '>')
                stk.pop_back();
            else
                break;
            if (stk.empty())
                m = i+1;
        }

        cout << m << endl;
        stk.clear();
    }

    return 0;
}