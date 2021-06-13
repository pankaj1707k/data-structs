/*
    Given a node of BST return its predecessor.
    The predecessor of a node is the maximum value in its left subtree.
    If such a node is not present, give zero as output.

    The BST is given in level order form.
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


node* lvlOrder(node* root, int data) {
    if (root == nullptr) {
        root = new node(data);
        return root;
    }

    if (data < root->data)
        root->left = lvlOrder(root->left, data);
    else
        root->right = lvlOrder(root->right, data);

    return root;
}


node* constructBST(vector<int> const& levelOrder) {
    if (levelOrder.size() == 0)
        return nullptr;
    
    node* root = nullptr;
    for (int i = 0; i < levelOrder.size(); i++)
        root = lvlOrder(root, levelOrder[i]);
    
    return root;
}


int main() {
    int n;
    cin >> n;
    vector<int> levelOrder;
    for (int i = 0; i < n; i++) {
        int temp;
        cin >> temp;
        levelOrder.push_back(temp);
    }

    node* root = constructBST(levelOrder);

    int k;
    cin >> k;
    cout << findPredecessor(root, k) << endl;

    return 0;
}