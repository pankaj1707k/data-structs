/*
    Given a node of BST return its predecessor.
    The predecessor of a node is the maximum value in its left subtree.
    If such a node is not present, give zero as output.

    The BST is given in preorder form.
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


int findPredecessor(node* root, int value) {
    if (root == nullptr)
        return 0;

    while (root->data != value) {
        if (value < root->data)
            root = root->left;
        else
            root = root->right;
    }

    if (root->left) {
        root = root->left;
        while (root->right)
            root = root->right;
        return root->data;
    }

    return 0;
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
    int n;
    cin >> n;
    vector<int> preOrder;
    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        preOrder.push_back(temp);
    }

    int index = 0;
    node* root = constructBST(preOrder, index, INT_MIN, INT_MAX);

    int k;
    cin >> k;
    cout << findPredecessor(root, k) << endl;

    return 0;
}