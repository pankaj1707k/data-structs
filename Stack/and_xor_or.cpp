/*
    Given an array of N distinct elements. Let M1 and M2 be the smallest ans next smallest element 
    in the interval [L,R] where 1 <= L < R <= N.
    S = ((M1 AND M2) XOR (M1 OR M2)) AND (M1 XOR M2)
    AND, OR, XOR are bitwise operators.
    Find the maximum possible value of S.
*/

#include <bits/stdc++.h>

using namespace std;


int andXorOr(vector<int> a) {
    stack<int> stk;
    int s, n1 = a[0], n2 = a[1], max = n1 ^ n2;
    for (int i = 0; i < a.size(); i++) {
        while (!stk.empty()) {
            n1 = a[i];
            n2 = stk.top();
            s = n1 ^ n2;
            max = (max > s) ? max : s;
            if (n1 < n2)
                stk.pop();
            else
                break;
        }
        stk.push(n1);
    }

    return max;
}


int main() {
    int n;
    cin >> n;
    vector<int> arr;

    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        arr.push_back(temp);
    }

    int result = andXorOr(arr);
    
    cout << result << endl;

    return 0;
}