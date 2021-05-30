/*
    Skyline Real Estate Developers is planning to demolish a number of old, unoccupied buildings and construct a shopping mall in their place. 
    Your task is to find the largest solid area in which the mall can be constructed.

    There are a number of buildings in a certain two dimensional landscape. Each building has a height, given by,
    h[i] where i is from 1 thru n. If you join k adjacent buildings, they will form a solid rectangle of 
    area: k * min(h[i], h[i+1], h[i+2],..., h[i+k-1]).

    The following solution uses stack data structure.
*/

#include <bits/stdc++.h>

#define max(x,y) ((x>y) ? x : y)

using namespace std;

string ltrim(const string &);
string rtrim(const string &);
vector<string> split(const string &);

/*
 * The function is expected to return a LONG_INTEGER.
 * The function accepts INTEGER_ARRAY h as parameter.
 */

long largestRectangle(vector<int> h) {
    vector<int> s;
    s.clear();
    h.push_back(0);

    long sum = 0;
    int i = 0;
    while(i < h.size())
    {
        if(s.empty() || h[i] > h[s.back()])
        {
            s.push_back(i);
            i++;
        }
        else
        {
            int t = s.back();
            s.pop_back();

            sum = max(sum, h[t] * (s.empty() ? i : i - s.back() - 1));
        }
    }

    return sum;
}

int main()
{
    string n_temp;
    getline(cin, n_temp);

    int n = stoi(ltrim(rtrim(n_temp)));

    string h_temp_temp;
    getline(cin, h_temp_temp);

    vector<string> h_temp = split(rtrim(h_temp_temp));

    vector<int> h(n);

    for (int i = 0; i < n; i++) {
        int h_item = stoi(h_temp[i]);

        h[i] = h_item;
    }

    long result = largestRectangle(h);

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
