/* https://www.codechef.com/LRNDSA02/problems/STUPMACH */

#include <bits/stdc++.h>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t, n, l;
    cin >> t;
    vector<int> v;  // capacities of boxes
    long long max_tokens, min_cap;

    while (t--) {
        cin >> n;
        for (int i = 0; i < n; i++) {
            int temp;
            cin >> temp;
            v.push_back(temp);
        }

        min_cap = max_tokens = v[0];
        for (int i = 1; i < n; i++) {
            if (v[i] < min_cap)
                min_cap = v[i];
            max_tokens += min_cap;
        }
        
        cout << max_tokens << endl;
        v.clear();
    }

    return 0;
}