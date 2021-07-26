#include <bits/stdc++.h>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t, n, m;
    cin >> t;
    unordered_set<long> s;

    while (t--) {
        cin >> n >> m;
        while (n--) {
            int temp;
            cin >> temp;
            s.insert(temp);
        }

        while (m--) {
            int temp;
            cin >> temp;
            if (s.find(temp) != s.end())
                cout << "YES" << endl;
            else
                cout << "NO" << endl;
        }

        s.clear();
    }

    return 0;
}