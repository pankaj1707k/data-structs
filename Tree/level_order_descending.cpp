/*
    Given a binary tree in level order form, print the level order traversal in descending order.
    The node values of each level is to be printed on a new line.
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


void sort(vector<int>& v) {
    int n = v.size();
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= n-i-1; j++) {
            if (v[j] < v[j+1])
                swap(v[j], v[j+1]);
        }
    }
}


void printLevelOrderDesc(node* root) {
    if (root == nullptr)
        return;
    
    queue<node*> q;
    q.push(root);

    vector<int> v;
    while (!q.empty()) {
        int n = q.size();
        while (n--) {
            node* temp = q.front();
            q.pop();
            v.push_back(temp->data);
            if (temp->left)
                q.push(temp->left);
            if (temp->right)
                q.push(temp->right);
        }
        if (v.size() > 1)
            sort(v);
        for (int i = 0; i < v.size(); i++)
            cout << v[i] << " ";
        cout << endl;
        v.clear();
    }
}


node* constructBinaryTree(vector<int> const& levelOrder, int i) {
    if (i >= levelOrder.size())
        return nullptr;
    
    node* root = new node(levelOrder[i]);

    root->left = constructBinaryTree(levelOrder, 2*i + 1);
    root->right = constructBinaryTree(levelOrder, 2*i + 2);

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

    node* root = constructBinaryTree(levelOrder, 0);

    printLevelOrderDesc(root);

    return 0;
}