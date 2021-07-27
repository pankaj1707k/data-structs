/* https://www.codechef.com/LRNDSA02/problems/STFOOD */

#include <bits/stdc++.h>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t, n, s, p, v, profit, max_profit = INT_MIN;
    cin >> t;

    while (t--) {
        cin >> n;
        while (n--) {
            cin >> s >> p >> v;
            s++;
            profit = (p/s)*v;
            max_profit = (profit > max_profit) ? profit : max_profit;
        }
        cout << max_profit << endl;
        max_profit = INT_MIN;
    }

    return 0;
}