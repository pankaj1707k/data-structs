/*
    You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. 
    You can change the height of a stack by removing and discarding its topmost cylinder any number of times.
    Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. 
    This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they are all the same height, then return the height.
*/

/* This recursive solution results in excessive slow execution for very large inputs */

#include <bits/stdc++.h>

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

int totalStackHeight(vector<int> h) {
    int sum = 0;
    for (int i = 0; i < h.size(); i++)
        sum += h[i];
    return sum;
}

/*
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY h1
 *  2. INTEGER_ARRAY h2
 *  3. INTEGER_ARRAY h3
 */

int equalStacks(vector<int> h1, vector<int> h2, vector<int> h3) {
    if (h1.empty() || h2.empty() || h3.empty())
        return 0;
    
    int th1 = totalStackHeight(h1);
    int th2 = totalStackHeight(h2);
    int th3 = totalStackHeight(h3);
    if (th1==th2 && th2==th3 && th3==th1)
        return th1;
    
    vector<int> v = {th1, th2, th3};
    int max_height = *max_element(v.begin(), v.end());
    if (max_height == th1)
        h1.erase(h1.begin());
    if (max_height == th2)
        h2.erase(h2.begin());
    if (max_height == th3)
        h3.erase(h3.begin());
    
    return equalStacks(h1, h2, h3);
}

int main()
{
    string first_multiple_input_temp;
    getline(cin, first_multiple_input_temp);

    vector<string> first_multiple_input = split(rtrim(first_multiple_input_temp));

    int n1 = stoi(first_multiple_input[0]);

    int n2 = stoi(first_multiple_input[1]);

    int n3 = stoi(first_multiple_input[2]);

    string h1_temp_temp;
    getline(cin, h1_temp_temp);

    vector<string> h1_temp = split(rtrim(h1_temp_temp));

    vector<int> h1(n1);

    for (int i = 0; i < n1; i++) {
        int h1_item = stoi(h1_temp[i]);

        h1[i] = h1_item;
    }

    string h2_temp_temp;
    getline(cin, h2_temp_temp);

    vector<string> h2_temp = split(rtrim(h2_temp_temp));

    vector<int> h2(n2);

    for (int i = 0; i < n2; i++) {
        int h2_item = stoi(h2_temp[i]);

        h2[i] = h2_item;
    }

    string h3_temp_temp;
    getline(cin, h3_temp_temp);

    vector<string> h3_temp = split(rtrim(h3_temp_temp));

    vector<int> h3(n3);

    for (int i = 0; i < n3; i++) {
        int h3_item = stoi(h3_temp[i]);

        h3[i] = h3_item;
    }

    int result = equalStacks(h1, h2, h3);

    cout << result << endl;

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

vector<string> split(const string &str) {
    vector<string> tokens;

    string::size_type start = 0;
    string::size_type end = 0;

    while ((end = str.find(" ", start)) != string::npos) {
        tokens.push_back(str.substr(start, end - start));

        start = end + 1;
    }

    tokens.push_back(str.substr(start));

    return tokens;
}
