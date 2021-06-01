/*
    You are a waiter at a party. There is a pile of numbered plates. Create an empty 'answers' array.
    At each iteration, i, remove each plate from the top of the stack in order. Determine if the number 
    on the plate is evenly divisible by the i_th prime number. If it is, stack it in pile B_i. Otherwise, 
    stack it in A_i. Store the values in B_i from top to bottom in answers. In the next iteration, do the 
    same with values in A_i. Once the required number of iterations is complete, store remaining values 
    in A_i in answers, again from top to bottom. Return the answers array.
*/

#include <bits/stdc++.h>

using namespace std;


vector<int> waiter(vector<int> numbers, int q) {
    vector<int> primes;
    // generate the required number of prime numbers
    int x = 2;
    for (int i = 0; i < q; i++) {
        bool p_num;
        while (true) {
            p_num = true;
            for (int j = 2; j <= (int)sqrt(x); j++) {
                if (x % j == 0) {
                    p_num = false;
                    break;
                }
            }

            if (p_num) {
                primes.push_back(x);
                x++;
                break;
            } else
                x++;
        }
    }

    // core function
    stack<int> a, b, a_new;
    vector<int> answers;

    for (int i = 0; i < numbers.size(); i++)
        a.push(numbers[i]);
    
    for (int i = 0; i < q; i++) {
        int p = primes[i];
        
        while (!a.empty()) {
            if (a.top() % p == 0)
                b.push(a.top());
            else
                a_new.push(a.top());
            a.pop();
        }

        while (!b.empty()) {
            answers.push_back(b.top());
            b.pop();
        }

        a = a_new;

        while (!a_new.empty())
            a_new.pop();
    }

    while (!a.empty()) {
        answers.push_back(a.top());
        a.pop();
    }

    return answers;
}


int main() {
    int n, q;
    cin >> n >> q;
    
    vector<int> nums;
    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        nums.push_back(temp);
    }

    vector<int> results = waiter(nums, q);

    for (int i = 0; i < results.size(); i++) {
        cout << results[i] << endl;
    }

    return 0;
}