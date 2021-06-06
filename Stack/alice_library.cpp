/*
    Alice is rearranging her library. She takes the innermost shelf and reverses the order of books. 
    She breaks the walls of the shelf. In the end, there will be only books and no shelf walls. Print the order of books.
    Opening and closing walls of shelves are shown by '/' and '\' respectively whereas books are represented by lower case alphabets.

    INPUT: string s displaying her library (example: '/u/love\i\')
    OUTPUT: string displaying her library after  rearrangement (without '/' and '\')
*/

#include <bits/stdc++.h>

using namespace std;


string reverse(string s) {
    char temp;
    int n = s.length();
    for (int i = 0; i < n/2; i++) {
        temp = s[i];
        s[i] = s[n-i-1];
        s[n-i-1] = temp;
    }

    return s;
}


string rearrange(string s) {
    stack<string> stk;

    string temp;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] != '\\') {
            temp = "";
            temp += s[i];
            stk.push(temp);
        } else {
            while ((stk.top())[0] != '/') {
                temp += stk.top();
                stk.pop();
            }
            stk.pop();
            if (!stk.empty()) {
                stk.push(reverse(temp));
            } else {
                s = temp;
            }
        }
        temp = "";
    }

    return s;
}


int main() {
    string s;
    cin >> s;

    s = rearrange(s);

    cout << s << endl;

    return 0;
}