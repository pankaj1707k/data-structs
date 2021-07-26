/*
    A and B are playing a game. In this game, both of them are initially provided with a list of n numbers. (Both have the same list but their own copy).

    Now, they both have a different strategy to play the game. A picks the element from start of his list. B picks from the end of his list.

    You need to generate the result in form of an output list.

    Method to be followed at each step to build the output list is:
        If the number picked by A is bigger than B then this step's output is 1. B removes the number that was picked from their list.
        If the number picked by A is smaller than B then this step's output is 2. A removes the number that was picked from their list.
        If both have the same number then this step's output is 0. Both A and B remove the number that was picked from their list.
        This game ends when at least one of them has no more elements to be picked i.e. when the list gets empty.

    Output the built output list (space-separated elements).
*/

#include <bits/stdc++.h>

using namespace std;


vector<int> fun_game(vector<int> v) {
    stack<int> A, B;
    vector<int> result;
    int n = v.size();

    for (int i = 0; i < n; i++) {
        B.push(v[i]);
        A.push(v[n-i-1]);
    }

    while (!A.empty() && !B.empty()) {
        if (A.top() > B.top()) {
            result.push_back(1);
            B.pop();
        } else if (A.top() < B.top()) {
            result.push_back(2);
            A.pop();
        } else {
            result.push_back(0);
            A.pop();
            B.pop();
        }
    }

    return result;
}


int main() {
    int n;
    cin >> n;

    vector<int> a;
    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        a.push_back(temp);
    }

    vector<int> result = fun_game(a);

    for (int i = 0; i < result.size(); i++) {
        cout << result[i] << " ";
    }
    cout << endl;

    return 0;
}