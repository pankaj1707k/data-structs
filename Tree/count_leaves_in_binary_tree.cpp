/*
    Given a binary tree, count the leaves in it.
    Binary tree is given in level order form.
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


int countLeaves(node* root) {
    if (root == nullptr)
        return 0;
    
    if (!root->left && !root->right)
        return 1;
    
    return countLeaves(root->left) + countLeaves(root->right);
}


node* constructBinaryTree(vector<int> const& levelOrder, int i) {
    if (i >= levelOrder.size() || levelOrder[i] == 'N')
        return nullptr;
    
    node* root = new node(levelOrder[i]);

    root->left = constructBinaryTree(levelOrder, 2*i + 1);
    root->right = constructBinaryTree(levelOrder, 2*i + 2);

    return root;
}


int main() {

    vector<int> levelOrder;
    string input, temp;
    getline(cin, input);
    int i = 0;
    while (i < input.length()) {
        temp = "";
        while (input[i] != ' ' && input[i] != '\n') {
            temp += input[i];
            i++;
        }
        if (temp[0] != 'N')
            levelOrder.push_back(stoi(temp));
        else
            levelOrder.push_back('N');
        i++;
    }

    node* root = constructBinaryTree(levelOrder, 0);
    
    cout << countLeaves(root) << endl;

    return 0;
}