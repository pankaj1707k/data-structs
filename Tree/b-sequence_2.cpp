/*
    Any sequence of size n is called a b-sequence if:
    1.  A_1 < A_2 < ... < A_k > A_k+1 > ... > A_n, i.e., the sequence is initially strictly increasing, reaches a maximum value and then is strictly decreasing.
    2.  All elements in the sequence comes atmost twice (once in increasing part and second in decreasing part), except the maximum element which comes exactly once.
    3.  All elements in the decreasing part must have come once in the increasing part.

    You are given a b-sequence S, and Q operations. For each operation, you are given a value val. You have to insert val in S if and only if after insertion, S still remains a b-sequence.
    After each operation, print the size of S and after all operations print the sequence S.

    INPUT:
        First line consists of an integer N, denoting size of S.
        Second line consists of N space separated integers, denoting elements of S.
        Next line consists of an integer Q, denoting number of operations.
        Each of the following Q lines consists of an integer val.
    
    OUTPUT:
        After each operation, print the size of S in a new line.
        After all operations, print the sequence S.

    CONSTRAINTS:
        1 <= N <= 10^5
        1 <= S_i <= 10^9
        1 <= Q <= 10^5
        1 <= val <= 10^9
*/

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