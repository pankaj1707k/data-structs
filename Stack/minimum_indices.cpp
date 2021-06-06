/*
    You are given an array A with N integers and Q queries. In each query, you are given an integer i.
    The task is to find the minimum index greater than i such that:
        1. Sum of digits if A_i is greater than the sum of digits of A_j
        2. A_i < A_j
    If there is no answer, print -1.

    INPUT:
        First line: 2 integers N and Q
        Second line: N integers
        Next Q lines contain 1 query each (a positive integer)
*/

#include <bits/stdc++.h>

using namespace std;


int sum_of_digits(int num) {
    int sum = 0;
    while (num != 0) {
        sum += num % 10;
        num /= 10;
    }

    return sum;
}


int main() {
    int n, q;
    cin >> n >> q;

    vector<int> A, digit_sums;
    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        A.push_back(temp);
        digit_sums.push_back(sum_of_digits(temp));
    }

    vector<int> Q;
    for (int k = 0; k < q; k++) {
        int i;
        cin >> i;
        i--;
        bool found = false;
        int j = i + 1;
        while (j < n) {
            if (A[i] < A[j] && digit_sums[i] > digit_sums[j]) {
                found = true;
                break;
            }
            j++;
        }

        if (found)
            Q.push_back(j+1);
        else
            Q.push_back(-1);
    }

    for (int i = 0; i < q; i++)
        cout << Q[i] << endl;

    return 0;
}