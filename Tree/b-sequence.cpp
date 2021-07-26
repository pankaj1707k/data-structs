#include <bits/stdc++.h>
using namespace std;


class BSTnode {
    public:
        int data;
        BSTnode* left;
        BSTnode* right;
        int count;

        // Constructor
        BSTnode(int node_data) {
            this->data = node_data;
            this->left = nullptr;
            this->right = nullptr;
            this->count = 1;
        }
};


BSTnode* insert(BSTnode* root, int data) {
    if (root == nullptr)
        root = new BSTnode(data);
    if (data < root->data)
        root->left = insert(root->left, data);
    else
        root->right = insert(root->right, data);
    return root;
}


BSTnode* constructBST(vector<int>& inOrder, int start, int end) {
    if (start > end)
        return nullptr;
    
    int mid = (start + end) / 2;
    BSTnode* root = new BSTnode(inOrder[mid]);
    root->left = constructBST(inOrder, start, mid-1);
    root->right = constructBST(inOrder, mid+1, end);
    return root;
}


BSTnode* findNode(BSTnode* root, int& key) {
    if (root == nullptr)
        return nullptr;
    if (key == root->data)
        return root;
    if (key < root->data)
        return findNode(root->left, key);
    return findNode(root->right, key);
}


int getMax(BSTnode* root) {
    while (root->right)
        root = root->right;
    return root->data;
}


void increasingSequence(BSTnode* root) {
    if (root == nullptr) return;
    increasingSequence(root->left);
    cout << root->data << " ";
    increasingSequence(root->right);
}


void decreasingSequence(BSTnode* root) {
    if (root == nullptr) return;
    decreasingSequence(root->right);
    if (root->count == 2)
        cout << root->data << " ";
    decreasingSequence(root->left);
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;
    vector<int> s, temp;
    for (int i = 0; i < n; i++) {
        int inp;
        cin >> inp;
        if (inp > s.back())
            s.push_back(inp);
        else
            temp.push_back(inp);
    }

    BSTnode* root = constructBST(s, 0, s.size()-1);

    for (int i = 0; i < temp.size(); i++)
        findNode(root, temp[i])->count++;
    
    int q;
    cin >> q;
    int max = s.back();
    while (q--) {
        int val;
        cin >> val;
        BSTnode* temp = findNode(root, val);
        if (val == max || (temp && temp->count >= 2))
            cout << n << endl;
        else {
            if (temp)
                temp->count++;
            else {
                root = insert(root, val);
            }
            max = (val > max) ? val : max;
            n++;
            cout << n << endl;
        }
    }

    increasingSequence(root);
    decreasingSequence(root);
    cout << endl;

    return 0;
}