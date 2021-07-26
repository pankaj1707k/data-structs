/*
    Humpy likes to jump from one building to another. 
    But he only jumps to next higher building and stops when no higher building is available. 
    Stamina required for a journey is xor of all the heights on which humpy jumps until he stops.

    If heights are [1 2 4], and he starts from 1, goes to 2 stamina required is 1 XOR 2 = 3, then from 2 to 4. 
    Stamina for the entire journey is 1 XOR 2 XOR 4 = 7. Find the maximum stamina required if can start his journey from any building.
*/

#include <bits/stdc++.h>

using namespace std;


int max_stamina(vector<int> h) {
    int n = h.size();
    int max_s = 0;
    vector<int> nxt(n, 0);
    stack<int> s;
    s.push(0);
    for (int i = 1; i < n; i++) {
        while (!s.empty() && h[i] > h[s.top()]) {
            nxt[s.top()] = i;
            s.pop();
        }
        s.push(i);
    }

    while (!s.empty()) {
        nxt[s.top()] = -1;
        s.pop();
    }

    vector<int> stamina(n,0);
    for (int i = n-1; i >= 0; i--) {
        if (nxt[i] == -1) {
            stamina[i] = h[i];
        } else {
            stamina[i] = h[i] ^ stamina[nxt[i]];
        }
        max_s = (max_s > stamina[i]) ? max_s : stamina[i];
    }

    return max_s;
}


int main() {
    int n;
    cin >> n;

    vector<int> heights;
    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        heights.push_back(temp);
    }

    int result = max_stamina(heights);
    cout << result << endl;

    return 0;
}