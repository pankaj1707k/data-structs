/* https://www.codechef.com/LRNDSA02/problems/ZCO12001 */

#include <bits/stdc++.h>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, depth = 0, depth_pos, longest_seq = 0, longest_seq_pos;
    cin >> n;
    vector<int> stk;

    for (int i = 1; i <= n; i++) {
        int bracket, temp;
        cin >> bracket;

        if (stk.empty())
            temp = i;

        if (bracket == 1)
            stk.push_back(bracket);
        else if (bracket == 2 && !stk.empty())
            stk.pop_back();
        
        if (stk.size() > depth) {
            depth = stk.size();
            depth_pos = i;
        }

        if (stk.empty() && (i-temp+1) > longest_seq) {
            longest_seq = i-temp+1;
            longest_seq_pos = temp;
        }
    }

    cout << depth << " " << depth_pos << " " << longest_seq << " " << longest_seq_pos << endl;

    return 0;
}