#include <bits/stdc++.h>
using namespace std;


class Node {
    private:
        int* keys;  // array of keys
        int m;      // minimum degree
        Node** children;    // array of child pointers
        int n;      // number of keys in the node
        bool leafNode;      // true if it is a leaf node, false otherwise
    
    public:
        // Constructor
        Node(int min_deg, bool lNode) {
            this->m = min_deg;
            this->leafNode = lNode;
            this->keys = new int[2*m-1];
            this->children = new Node*[2*m];    // number of children is one more than number of keys
            this->n = 0;
        }

        bool search(int k) {
            int i = 0;
            while (i < n && k > keys[i])    // move at the appropriate index in keys where the key k is likely to be found
                i++;
            
            if (keys[i] == k)     // key found
                return true;
            
            if (leafNode)     // key not found and this was a leaf node, i.e., key doesn't exist
                return false;
            
            return children[i]->search(k);    // key not found and it was not a leaf node, so search in the appropriate child node
        }

        void splitChild(int i, Node* y) {
            Node* temp = new Node(y->m, y->leafNode);   // create a new child node
            temp->n = m-1;  // this node will have m-1 keys

            for (int j = 0; j < m-1; j++)   // copy last m-1 keys of y to new child
                temp->keys[j] = y->keys[j+m];
            
            if (!y->leafNode) {
                for (int j = 0; j < m; j++)     // copy the equivalent number of children to the new node
                    temp->children[j] = y->children[j+m];
            }

            y->n = m-1;     // y will be left with m-1 keys

            // since this node will have one more child, shift the other children to create room of the new child
            for (int j = n; j >= i+1; j--)
                children[j+1] = children[j];
            
            children[i+1] = temp;   // link the new child with this node

            // shift the keys of this node to accommodate the middle key from y
            for (int j = n-1; j >= i; j--)
                keys[j+1] = keys[j];
            
            keys[i] = y->keys[m-1];     // copy middle key of y to this node
            n++;    // number of keys in this node increases by one
        }

        // this method is called only if the node has room to accommodate a new key
        void insertInNode(int k) {
            int i = n-1;    // start from last index of keys[]

            if (leafNode) {
                while (i >= 0 && keys[i] > k) {     // find appropriate index
                    keys[i+1] = keys[i];    // shift elements to right
                    i--;
                }

                keys[i+1] = k;      // insert key
                n++;    // increment number of keys
            } else {    // not a leaf node
                while (i >= 0 && keys[i] > k) i--;    // find index of child node in which key is to be inserted

                if (children[i+1]->n == 2*m-1) {    // child is full
                    splitChild(i+1, children[i+1]);
                    if (keys[i+1] < k) i++;    // after splitting, check in which part the key will be inserted
                }

                children[i+1]->insertInNode(k);     // recursively call the method to insert the key in the child
            }
        }
    
    friend class BTree;
};


class BTree {
    private:
        Node* root;
        int m;
    
    public:
        // Constructor
        BTree(int min_degree) {
            this->m = min_degree;
            this->root = nullptr;
        }

        bool search(int k) {
            return (root == nullptr) ? false : root->search(k);
        }

        void insert(int k) {
            // if tree is empty
            if (root == nullptr) {
                root = new Node(m, true);
                root->keys[0] = k;
                root->n = 1;
            } else {
                if (root->n == 2*m-1) {     // root is full, tree height will increase
                    Node* newRoot = new Node(m, false);     // create new root
                    newRoot->children[0] = root;    // make old root as the child of new root
                    newRoot->splitChild(0, root);   // split this child
                    int i = 0;
                    if (k > newRoot->keys[0])   i++;    // find appropriate child in which the key will be inserted
                    newRoot->children[i]->insertInNode(k);  // insert the key in appropriate child
                    root = newRoot;
                } else
                    root->insertInNode(k);
            }
        }
};


bool isPrime(int n) {
    if (n == 1) return false;
    for (int i = 2; i <= sqrt((float) n); i++) {
        if (n % i == 0)
            return false;
    }
    return true;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int m, n_insert, n_search;  // minimum degree, number of elements to insert, search
    cin >> m;
    BTree T(m);     // initialize b tree of minimum degree m
    
    cin >> n_insert;
    for (int i = 0; i < n_insert; i++) {
        int key;
        cin >> key;
        T.insert(key);
    }

    cin >> n_search;
    int sum = 0;
    for (int i = 0; i < n_search; i++) {
        int key;
        cin >> key;
        if (isPrime(key) && T.search(key))
            sum += key;
    }

    cout << sum << endl;

    return 0;
}