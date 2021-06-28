/*
    Construct a BST from the given list of numbers. After the construction of BST, you are asked to delete some numbers from the BST.
    You have to delete only one entry for one time and not all its duplicate entries. Finally, calculate and print the weighted sum of duplicate entries in the BST.
    Weighted sum of duplicates of a BST is equal to the sum of keys of duplicate nodes multiplied by their respective counts.

    INPUT:
        First line: number of elements in BST
        Second line: list of space-separated elements
        Third line: number of elements to delete
        Fourth line: list of space-separated elements to delete
    
    OUTPUT:
        Single integer representing weighted sum of duplicates.
*/

#include <bits/stdc++.h>
using namespace std;


class node {
    public:
        int val;
        node* left;
        node* right;
        int count;

        node(int val) {
            this->val = val;
            this->left = nullptr;
            this->right = nullptr;
            this->count = 1;
        }
};


node* insert(node* root, int val) {
    if (root == nullptr) {
        root = new node(val);
        return root;
    }

    if (val == root->val) {
        root->count++;
        return root;
    }

    if (val < root->val)
        root->left = insert(root->left, val);
    else
        root->right = insert(root->right, val);
    
    return root;
}


void del_val(node* root, int val) {
    while (root != nullptr) {
        if (val == root->val) {
            root->count--;
            break;
        } else if (val < root->val)
            root = root->left;
        else
            root = root->right;
    }

    return;
}


int weighted_sum(node* root) {
    if (root == nullptr)
        return 0;
    return ((root->count > 1) ? (root->count): 0)*(root->val) + weighted_sum(root->left) + weighted_sum(root->right);
}


int main() {
    int n, d;
    node* root = nullptr;

    cin >> n;
    int val;
    
    while (n--) {
        cin >> val;
        root = insert(root, val);
    }

    cin >> d;

    while (d--) {
        cin >> val;
        del_val(root, val);
    }

    cout << weighted_sum(root) << endl;

    return 0;
}