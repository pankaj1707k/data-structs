/*
    Find the sum of values of nodes of a BST for given level(s).
    BST is given in preorder form.

    Level number starts from 1. Root node is at level 1.
    All nodes have distinct values.
*/

#include <bits/stdc++.h>

using namespace std;


class node {
    public:
        int data;
        node* left;
        node* right;

        // constructor
        node(int node_data) {
            this->data = node_data;
            this->left = this->right = nullptr;
        }
};


int levelSum(node* root, int level) {
    if (root == nullptr)
        return 0;
    
    queue<node*> q;
    q.push(root);

    int l = 1, sum = 0, flag = 0;
    while (!q.empty()) {
        int n = q.size();
        while (n--) {
            node* temp = q.front();
            q.pop();
            if (l == level) {
                flag = 1;
                sum += temp->data;
            } else {
                if (temp->left)
                    q.push(temp->left);
                
                if (temp->right)
                    q.push(temp->right);
            }
        }
        l++;
        if (flag) break;
    }

    return sum;
}


node* constructBST(vector<int> const& preOrder, int& index, int min, int max) {
    // base case 1
    if (index >= preOrder.size())
        return nullptr;
    
    int curr = preOrder[index];
    
    // base case 2
    if (curr < min || curr > max)   // value out of range
        return nullptr;

    node* root = new node(curr);
    index++;

    // construct left subtree
    root->left = constructBST(preOrder, index, min, curr-1);

    // construct right subtree
    root->right = constructBST(preOrder, index, curr+1, max);

    return root;
}


int main() {
    int n, k;
    cin >> n;
    vector<int> preOrder;
    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        preOrder.push_back(temp);
    }

    int index = 0;
    node* root = constructBST(preOrder, index, INT_MIN, INT_MAX);

    cin >> k;
    int sum = 0;
    for (int i = 0; i < k; i++) {
        int lvl;
        cin >> lvl;
        sum += levelSum(root, lvl);
    }

    cout << sum << endl;

    return 0;
}