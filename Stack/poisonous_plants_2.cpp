/*
    Optimal approach using stack

    There are a number of plants in a garden. Each of the plants has been treated with some amount of pesticide. 
    After each day, if any plant has more pesticide than the plant on its left, being weaker than the left one, it dies.
    You are given the initial values of the pesticide in each of the plants. Determine the number of days after which no plant dies, 
    i.e. the time after which there is no plant with more pesticide content than the plant to its left.
*/

#include <bits/stdc++.h>

using namespace std;


int poisonousPlants(vector<int> p) {
    stack<vector<int>> stk;
    int max_days = 0;
    int days;
    for (int i = 0; i < p.size(); i++) {
        days = 0;
        while (!stk.empty() && (stk.top())[0] >= p[i]) {
            days = days > (stk.top())[1] ? days : (stk.top())[1];
            stk.pop();
        }

        if (!stk.empty())
            days++;
        else
            days = 0;
        
        max_days = max_days > days ? max_days : days;
        vector<int> temp = {p[i], days};
        stk.push(temp);
    }

    return max_days;
}


int main() {
    int n;
    cin >> n;

    vector<int> p;
    for (int i = 0; i < n; i++) {
        int val;
        cin >> val;
        p.push_back(val);
    }

    int result = poisonousPlants(p);    // number of days after which plants stop dying

    cout << result << endl;

    return 0;
}