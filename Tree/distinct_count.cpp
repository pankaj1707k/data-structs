/*
    Given an array A of N integers, classify it as being Good Bad or Average. 
    It is called Good, if it contains exactly X distinct integers, Bad if it contains less than X distinct integers and Average if it contains more than X distinct integers.

    INPUT:
        First line consists of a single integer T denoting the number of test cases.
        First line of each test case consists of two space separated integers denoting N and X.
        Second line of each test case consists of N space separated integers denoting the array elements.
    
    OUTPUT:
        Print the required answer for each test case on a new line.

    CONSTRAINTS:
        1 <= T <= 50
        1 <= X,N <= 13000
        1 <= A[i] <= 10^9
*/

#include <bits/stdc++.h>
using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int t, n, x;
    cin >> t;
    set<int> s;

    while (t--) {
        cin >> n >> x;
        for (int i = 0; i < n; i++) {
            int temp;
            cin >> temp;
            s.insert(temp);
        }

        int l = s.size();
        if (l == x)
            cout << "Good" << endl;
        else if (l < x)
            cout << "Bad" << endl;
        else
            cout << "Average" << endl;
        
        s.clear();
    }

    return 0;
}