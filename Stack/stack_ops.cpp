/*
    You are given a stack of N integers. 
    In one operation, you can either pop an element from the stack or push any popped element into the stack. 
    You need to maximize the top element of the stack after performing exactly K operations. 
    If the stack becomes empty after performing K operations and there is no other way for the stack to be non-empty, print -1.

    Note: The maximum element at the top of the stack after k operations need not be the maximum element of the complete stack.
    While taking input for elements of the stack, the first element represents the top and last element represents the bottom of the stack.
    Print the maximum element at the top after k operations. 

    Data types used are:
        long --> size of stack
        long long --> each element of stack
        long --> number of operations
*/

#include <bits/stdc++.h>
#define ll long long
using namespace std;


int main() {
    long n, k;
    cin >> n >> k;
    ll max;
    ll temp;
    cin >> temp;
    max = temp;
    for (long i = 1; i < n; i++) {
        cin >> temp;
        if (i <= k-2 && temp > max)
            max = temp;
    }

    cout << max << endl;

    return 0;
}