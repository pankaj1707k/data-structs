#include <bits/stdc++.h>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    map<int,int> m;
    int max = INT_MIN;
    for (int i = 0; i < n; i++) {
        int inp;
        cin >> inp;
        max = (inp > max) ? inp : max;
        if (m.find(inp) != m.end())
            m[inp]++;
        else
            m.insert(make_pair(inp,1));
    }

    int q;
    cin >> q;
    for (int i = 0; i < q; i++) {
        int val;
        cin >> val;
        if (val == max || m[val] >= 2)
            cout << n << endl;
        else {
            if (m.find(val) != m.end())
                m[val]++;
            else
                m.insert(make_pair(val,1));
            max = (val > max) ? val : max;
            n++;
            cout << n << endl;
        }
    }

    for (auto itr = m.begin(); itr != m.end(); itr++)
        cout << itr->first << " ";
    
    for (auto itr = m.rbegin(); itr != m.rend(); itr++) {
        if (itr->second == 2)
            cout << itr->first << " ";
    }
    cout << endl;

    return 0;
}