/*
    A magician is standing at the door of his classroom. There are currently N students in the class, i_th student got A[i] candies.
    There are still M more students to come. At every instant, a student enters the class and wishes to be seated with a student who has exactly the same number of candies.
    For each student, the magician shouts "YES" if such a student is found, "NO" otherwise.

    INPUT:
        Firs line contains an integer T. T test cases follow.
        First line of each test case contains two space-separated integers N and M.
        Second line contains N+M space separated integers, the candies of the students.
    
    OUTPUT:
        For each test case, output in M new lines, magician's answers to the M students.
        Print "YES" or "NO" (without quotes) pertaining to the magician's answers.
    
    CONSTRAINTS:
        1 <= T <= 10
        1 <= N,M <= 10^5
        0 <= A[i] <= 10^12
    
    The following solution uses a self-balancing BST (AVL tree).
*/

#include <bits/stdc++.h>
#define max(x, y) ((x > y) ? x : y)
using namespace std;


class node {
    public:
        long val;
        node* left;
        node* right;
        int ht;

        node(long val) {
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


node* insert(node* root, long val) {
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


bool search(node* root, long val) {
    if (root == nullptr)
        return false;
    if (root->val == val)
        return true;
    if (val < root->val)
        return search(root->left, val);
    return search(root->right, val);
}


int main() {

    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int t, n, m;
    cin >> t;
    node* root = nullptr;
    while (t--) {
        cin >> n >> m;
        long value;
        while (n--) {
            cin >> value;
            root = insert(root, value);
        }

        while (m--) {
            cin >> value;
            if (search(root, value))
                cout << "YES" << endl;
            else {
                cout << "NO" << endl;
                root = insert(root, value);
            }
        }

        delete root;
        root = nullptr;
    }

    return 0;
}