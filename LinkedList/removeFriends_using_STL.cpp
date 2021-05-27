/*
    After getting her PhD, Christie has become a celebrity at her university, 
    and her facebook profile is full of friend requests. Being the nice girl she is, 
    Christie has accepted all the requests.

    Now Kuldeep is jealous of all the attention she is getting from other guys, 
    so he asks her to delete some of the guys from her friend list.

    To avoid a 'scene', Christie decides to remove some friends from her friend list, 
    since she knows the popularity of each of the friend she has, 
    she uses the following algorithm to delete a friend.

    Algorithm to delete friend:
        deleteFriend = false
        for i=1 to friend.length-1
            if (friend[i].popularity < friend[i+1].popularity)
                delete i th friend
                deleteFriend = true
                break
        if deleteFriend == false
            delete the last friend

    INPUT:
    First line: T --> number of test cases
    For each test case
        First line: N K --> number of total friends and number of friends to remove
        Second line: N space-separated numbers representing the popularity of N friends
    
    OUTPUT:
    For each test case: print N-K space-separated numbers as the popularities of friends remaining
    after deleting K friends as per the algorithm

    CONSTRAINTS:
    1 <= T <= 1000
    1 <= N <= 100000
    0 <= K < N
    0 <= popularity_of_friend <= 100
*/

#include <bits/stdc++.h>

using namespace std;

int main() {

    int t;  // number of test cases
    cin >> t;

    while (t--) {
        int n, k, p;
        cin >> n >> k;
        list<int> lst;
        list<int>::iterator itr;

        for (int i=0; i<n; i++) {
            cin >> p;
            lst.push_back(p);
        }

        for (itr = lst.begin(); itr != lst.end(); ) {
            if (k==0)
                break;
            int start = *(lst.begin());
            int curr_val = *itr;
            itr++;
            int next_val = *itr;
            if (curr_val >= next_val)
                continue;
            else {
                itr--;
                lst.erase(itr);
                if (*itr != start)
                    itr--;
                else
                    itr = lst.begin();
                k--;
            }
        }

        if (k!=0) {
            for (int i=0; i<k; i++)
                lst.pop_back();
        }

        for (itr = lst.begin(); itr != lst.end(); itr++)
            cout << *itr << " ";
        cout << endl;
    }

    return 0;

}