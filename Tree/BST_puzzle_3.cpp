#include <bits/stdc++.h>
using namespace std;


int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t, n, m;
    cin >> t;

    while (t) {
        set<long> s;
        long val;
        cin >> n >> m;
        
        while (n) {
            cin >> val;
            s.insert(val);
            n--;
        }

        while (m) {
            cin >> val;
            if (s.find(val) != s.end())
                cout << "YES" << endl;
            else {
                cout << "NO" << endl;
                s.insert(val);
            }
            m--;
        }

        s.clear();
        t--;
    }
}