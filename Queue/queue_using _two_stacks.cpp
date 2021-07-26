/*
    Implement a queue using two stacks. Then, process the following 3 types of queries:
    1. 1 x : enqueue x at the rear
    2. 2 : dequeue from the front
    3. 3 : print the the element at the front

    Input format:
        First line takes number of queries (q).
        Each line (i) of the q subsequent lines takes a query of any of the 3 types.
     Ouput format:
        For each query of type 3, print the element at the front of the queue.
    It is guaranteed that a valid answer always exists for query of type 3.
*/

#include <bits/stdc++.h>

using namespace std;


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int q;  // number of queries
    cin >> q;
    int q_type;
    long num;
    stack<long> s1, s2;     // top of s2 is front of queue
    
    for (int i = 0; i < q; i++) {
        cin >> q_type;
        if (q_type == 1) {
            cin >> num;
            s1.push(num);
        } else if (q_type == 2) {
            if (s2.empty()) {
                while (!s1.empty()) {
                    s2.push(s1.top());
                    s1.pop();
                }
            }
            s2.pop();
        } else {
            if (s2.empty()) {
                while (!s1.empty()) {
                    s2.push(s1.top());
                    s1.pop();
                }
            }
            cout << s2.top() << "\n";
        }
    }

    return 0;
}