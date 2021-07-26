#include <bits/stdc++.h>
#define max(x, y) ((x > y) ? x : y)
using namespace std;


class node {
    public:
        int val;
        node* left;
        node* right;
        int ht;

        node(int val) {
            this->val = val;
            this->left = nullptr;
            this->right = nullptr;
            this->ht = 0;
        }
};


int height(node* root) {
    if (root == nullptr)
        return -1;
    return root->ht;
}


int setHeight(node* root) {
    if (root == nullptr)
        return -1;
    return 1 + max(height(root->left), height(root->right));
}


node* leftRotate(node* root) {
    node* newRoot = root->right;
    root->right = newRoot->left;
    newRoot->left = root;
    root->ht = setHeight(root);
    newRoot->ht = setHeight(newRoot);
    return newRoot;
}


node* rightRotate(node* root) {
    node* newRoot = root->left;
    root->left = newRoot->right;
    newRoot->right = root;
    root->ht = setHeight(root);
    newRoot->ht = setHeight(newRoot);
    return newRoot;
}


node* insert(node* root, int val) {
    if (root == nullptr) {
        root = new node(val);
        return root;
    }

    if (val < root->val)
        root->left = insert(root->left, val);
    else
        root->right = insert(root->right, val);
    
    int balance = height(root->left) - height(root->right);

    if (balance > 1) {
        if (val < root->left->val)
            return rightRotate(root);
        else {
            root->left = leftRotate(root->left);
            return rightRotate(root);
        }
    }

    if (balance < -1) {
        if (val > root->right->val)
            return leftRotate(root);
        else {
            root->right = rightRotate(root->right);
            return leftRotate(root);
        }
    }

    else
        root->ht = setHeight(root);
    
    return root;
}


void preOrder(node* root) {
    if (root == nullptr)
        return;
    
    int balance = height(root->left) - height(root->right);
    cout << root->val << "(" << balance << ")" << " ";

    preOrder(root->left);
    preOrder(root->right);
}


int main() {
    node* root = nullptr;
    root = insert(root, 2);
    root = insert(root, 3);
    root = insert(root, 4);
    root = insert(root, 5);
    root = insert(root, 6);
    // root = insert(root, 25);

    preOrder(root);
    cout << endl;

    return 0;
}