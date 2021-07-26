#include <bits/stdc++.h>
using namespace std;


class node {
    public:
        long val;
        node* left;
        node* right;

        node(long val) {
            this->val = val;
            this->left = nullptr;
            this->right = nullptr;
        }
};


node* insert(node* root, long val) {
    if (root == nullptr) {
        root = new node(val);
        return root;
    }

    if (val < root->val)
        root->left = insert(root->left, val);
    else
        root->right = insert(root->right, val);
    
    return root;
}


bool search(node* root, long val) {
    if (root == nullptr)
        return false;
    if (val == root->val)
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

    while (t--) {
        node* root = nullptr;
        cin >> n >> m;
        long val;

        while (n--) {
            cin >> val;
            root = insert(root, val);
        }

        while (m--) {
            cin >> val;
            if (search(root, val))
                cout << "YES" << endl;
            else {
                cout << "NO" << endl;
                root = insert(root, val);
            }
        }
    }

    return 0;
}