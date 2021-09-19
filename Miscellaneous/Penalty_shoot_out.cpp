/* https://www.codechef.com/LRNDSA02/problems/PSHOT */

#include <bits/stdc++.h>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t, n, scoreA, scoreB, shotsLeftA, shotsLeftB;
    cin >> t;
    string s;

    while (t--) {
        cin >> n;
        cin >> s;
        shotsLeftA = shotsLeftB = n;
        scoreA = scoreB = 0;
        for (int i = 0; i < 2*n; i++) {
            if (i%2 == 0) {
                if (s[i] == '1')
                    scoreA++;
                shotsLeftA--;
            } else {
                if (s[i] == '1')
                    scoreB++;
                shotsLeftB--;
            }

            if (((scoreA > scoreB) && ((scoreA - scoreB) > shotsLeftB)) || ((scoreB > scoreA) && ((scoreB - scoreA) > shotsLeftA))) {
                cout << i+1 << endl;
                break;
            }

            if (shotsLeftA == 0 || shotsLeftB == 0) {
                cout << 2*n << endl;
                break;
            }
        }
    }

    return 0;
}