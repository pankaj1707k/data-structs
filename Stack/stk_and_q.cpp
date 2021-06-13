/*
    You are given a stack of N integers such that the first element represents the top of the stack and the last element represents the bottom of the stack. 
    You need to pop at least one element from the stack. At any one moment, you can convert stack into a queue. 
    The bottom of the stack represents the front of the queue. You cannot convert the queue back into a stack. 
    Your task is to remove exactly K elements such that the sum of the K removed elements is maximised.

    Print the maximum possible sum.
*/

#include <bits/stdc++.h>

using namespace std;


long max_sum(vector<long> v, int k) {
    long max = 0;
    int n = v.size();

    long sum = 0;
    for (int i = 0; i < k; i++)
        sum += v[i];
    
    max = sum;

    for (int i = k-1, j = n-1; i > 0; i--, j--) {
        sum += v[j] - v[i];
        max = (sum > max) ? sum : max;
    }

    return max;
}


int main() {
    int n, k;
    cin >> n >> k;

    vector<long> v;
    for (int i = 0; i < n; i++) {
        long temp;
        cin >> temp;
        v.push_back(temp);
    }

    long result = max_sum(v, k);
    cout << result << endl;

    return 0;
}