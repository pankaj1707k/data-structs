/* https://www.codechef.com/LRNDSA02/problems/NOTALLFL */

#include <bits/stdc++.h>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t, n, k;
    cin >> t;
    vector<int> v;

    while (t--) {
        cin >> n >> k;
        for (int i = 0; i < n; i++) {
            int tmp;
            cin >> tmp;
            v.push_back(tmp);
        }

        int start = 0, end = 0, d = 0, j = 0;
        vector<int> freq;
        for (int i = 0; i < n; i++)
            freq.push_back(0);
        for (int i = 0; i < n; i++) {
            freq[v[i]]++;
            if (freq[v[i]] == 1)
                d++;
            while (d >= k) {
                freq[v[j]]--;
                if (freq[v[j]] == 0)
                    d--;
                j++;
            }
            if (i-j+1 >= end-start+1) {
                end = i;
                start = j;
            }
        }

        cout << end-start+1 << endl;
        v.clear();
        freq.clear();
    }

    return 0;
}