/*
    Brute-force approach

    There are a number of plants in a garden. Each of the plants has been treated with some amount of pesticide. 
    After each day, if any plant has more pesticide than the plant on its left, being weaker than the left one, it dies.
    You are given the initial values of the pesticide in each of the plants. Determine the number of days after which no plant dies, 
    i.e. the time after which there is no plant with more pesticide content than the plant to its left.
*/

#include <bits/stdc++.h>

using namespace std;


int poisonousPlants(vector<int> p) {
    int day_count = 0;
    bool d = false;
    while (true) {
        d = false;

        for (int i = p.size()-1; i > 0; i--) {
            if (p[i] > p[i-1]) {
                p.erase(p.begin()+i);
                d = true;
            }
        }

        if (d)
            day_count++;
        else
            break;
    }

    return day_count;
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