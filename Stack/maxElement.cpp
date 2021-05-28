/*
    Given an empty sequence and N queries, each one of the following types:
        1 x -push element x to the stack
        2   -pop element from the stack
        3   -print the maximum element in the stack
    
    The getMax function has the following parameter:
        string operations[N]: operations/queries as strings
    The function return:
        int[]: the answers to each of the type 3 query
*/

#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);

/*
    The function is expected to return an INTEGER_ARRAY.
    The function accepts STRING_ARRAY operations as parameter.
*/

vector<int> getMax(vector<string> operations) {
    vector<int> maxElements;
    vector<int> stk;
    int len = operations.size();
    for (int i = 0; i < len; i++) {
        string query = operations[i];
        if (query[0] == '1') {
            stk.push_back(stoi(query.substr(2, query.length()-2)));
        } else if (query[0] == '2') {
            stk.pop_back();
        } else {
            int max = stk[0];
            for (int j = 0; j < stk.size(); j++) {
                if (stk[j] > max)
                    max = stk[j];
            }
            // this approach of finding the max element is slower
            // for greater speed, use: max = *max_element(stk.begin(), stk.end());
            // *max_element() comes from the <algorithm> header
            maxElements.push_back(max);
        }
    }

    return maxElements;
}

int main()
{
    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    vector<string> ops(n);

    for (int i = 0; i < n; i++) {
        string ops_item;
        getline(cin, ops_item);

        ops[i] = ops_item;
    }

    vector<int> res = getMax(ops);

    for (size_t i = 0; i < res.size(); i++) {
        cout << res[i];

        if (i != res.size() - 1) {
            cout << endl;
        }
    }

    cout << endl;

    return 0;
}

string ltrim(const string &str) {
    string s(str);

    s.erase(
        s.begin(),
        find_if(s.begin(), s.end(), not1(ptr_fun<int, int>(isspace)))
    );

    return s;
}

string rtrim(const string &str) {
    string s(str);

    s.erase(
        find_if(s.rbegin(), s.rend(), not1(ptr_fun<int, int>(isspace))).base(),
        s.end()
    );

    return s;
}
