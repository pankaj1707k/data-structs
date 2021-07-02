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
                while (i >= 0 && keys[i] > k)   i--;    // find index of child node in which key is to be inserted

                if (children[i+1]->n == 2*m-1) {    // child is full
                    splitChild(i+1, children[i+1]);
                    if (keys[i+1] < k)  i++;    // after splitting, check in which part the key will be inserted
                }

                children[i+1]->insertInNode(k);     // recursively call the method to insert the key in the child
            }
        }

        int findKey(int k) {
            int pos = 0;
            while (pos < n && keys[pos] < k)
                pos++;
            return pos;
        }

        int getPredecessor(int pos) {
            Node* curr = children[pos];
            while (!curr->leafNode)     // move to the right-most child until a leaf node is reached
                curr = curr->children[curr->n];
            return curr->keys[curr->n-1];
        }

        int getSuccessor(int pos) {
            Node* curr = children[pos+1];
            while (!curr->leafNode)     // move to the left-most child until a leaf node is reached
                curr = curr->children[0];
            return curr->keys[0];
        }

        void fill(int pos) {
            if (pos != 0 && children[pos-1]->n >= m)    // left sibling has at least m keys
                borrowFromPrevChild(pos);
            else if (pos != n && children[pos+1]->n >= m)   // right sibling has at least m keys
                borrowFromNextChild(pos);
            else {
                if (pos == n)   // if last child, merge with previous sibling
                    merge(pos-1);
                else    // merge with its next sibling
                    merge(pos);
            }
        }

        void borrowFromPrevChild(int pos) {
            Node* child = children[pos];
            Node* sibling = children[pos-1];

            // shift all keys of child one step ahead
            for (int i = child->n-1; i >= 0; i--)
                child->keys[i+1] = child->keys[i];
            
            // if child is not a leaf node, shift its children one step ahead
            if (!child->leafNode) {
                for (int i = child->n; i >= 0; i--)
                    child->children[i+1] = child->children[i];
            }

            child->keys[0] = keys[pos-1];   // copy the key from parent to child

            // move sibling's last child to make it child's first child
            if (!child->leafNode)
                child->children[0] = sibling->children[sibling->n];
            
            // move the last key of sibling to parent
            keys[pos-1] = sibling->keys[sibling->n-1];

            child->n++; // number of keys in child increases by one
            sibling->n--;   // number of keys in its sibling decreases by one
        }

        void borrowFromNextChild(int pos) {
            Node* child = children[pos];
            Node* sibling = children[pos+1];

            // copy keys[pos] as last key of child
            child->keys[child->n] = keys[pos];

            // move sibling's first child to make it child's last child
            if (!child->leafNode)
                child->children[child->n+1] = sibling->children[0];
            
            // move first key of sibling to parent
            keys[pos] = sibling->keys[0];

            // shift the keys of sibling one step behind
            for (int i = 0; i < sibling->n-1; i++)
                sibling->keys[i] = sibling->keys[i+1];
            
            // if sibling is not leaf, shift its children one step behind
            if (!sibling->leafNode) {
                for (int i = 0; i < sibling->n; i++)
                    sibling->children[i] = sibling->children[i+1];
            }

            child->n++;
            sibling->n--;
        }

        void merge(int pos) {
            Node* child = children[pos];
            Node* sibling = children[pos+1];

            child->keys[m-1] = keys[pos];   // copy key from parent and insert it at m-1 position in child's keys

            // copy the keys from sibling to child
            for (int i = 0; i < sibling->n; i++)
                child->keys[i+m] = sibling->keys[i];
            
            // copy the child pointers of sibling
            if (!child->leafNode) {
                for (int i = 0; i <= sibling->n; i++)
                    child->children[i+m] = sibling->children[i];
            }

            // fill the gap created by copying key from parent to child
            for (int i = pos+1; i < n; i++)
                keys[i-1] = keys[i];
            
            // also shift the child pointers one step towards left
            for (int i = pos+2; i <= n; i++)
                children[i-1] = children[i];

            // update number of keys for child and parent
            child->n += 1 + sibling->n;
            n--;

            delete sibling;
        }

        void removeFromLeaf(int pos) {
            for (int i = pos; i < n-1; i++) // shift all elements after index pos one step back
                keys[i] = keys[i+1];
            n--;    // reduce number of keys
        }

        void removeFromNonLeaf(int pos) {
            int k = keys[pos];

            // if the child just preceding the key has at least m keys then,
            // get the predecessor of the key from this child, replace the key in the current node with this predecessor
            // and delete the predecessor from the child recursively
            if (children[pos]->n >= m) {
                int predecessor = getPredecessor(pos);
                keys[pos] = predecessor;
                children[pos]->remove(predecessor);
            } else if (children[pos+1]->n >= m) {
                // if the child preceding the key has less than m keys then check for the child just ahead of the key
                // if it has at least m keys, then get the successor of the key from this child,
                // replace the key with this successor, and
                // recursively delete the successor from the child
                int successor = getSuccessor(pos);
                keys[pos] = successor;
                children[pos+1]->remove(successor);
            } else {
                // if both preceding and succeeding children have less than m keys, then
                // merge the key and the succeeding child with the preceding child, and
                // remove noe remove the key recursively
                merge(pos);
                children[pos]->remove(k);
            }
        }

        void remove(int k) {
            int pos = findKey(k);   // find the position of the key

            // key is present in current node
            if (pos < n && keys[pos] == k) {
                if (leafNode)
                    removeFromLeaf(pos);
                else
                    removeFromNonLeaf(pos);
            } else {    // key is not present in current node
                if (leafNode) return;   // key does not exist
                bool keyInLastNode = ((pos == n) ? true : false);   // indicates whether the key is present in the subtree rooted with the last child of this node
                
                // if the child in which the key is expected to be present has less than m keys, fill the child
                // because, upon removal of a key, it will have less than m-1 keys which violates the criteria for B tree
                if (children[pos]->n < m)
                    fill(pos);
                
                // if the last child has been merged then, recur on either the (pos-1)th child or pos-th child
                if (keyInLastNode && pos > n)
                    children[pos-1]->remove(k);
                else
                    children[pos]->remove(k);
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
                if (root->n < 2*m-1)    // root is not full
                    root->insertInNode(k);
                else {     // root is full, tree height will increase
                    Node* newRoot = new Node(m, false);     // create new root
                    newRoot->children[0] = root;    // make old root as the child of new root
                    newRoot->splitChild(0, root);   // split this child
                    int i = 0;
                    if (k > newRoot->keys[0])   i++;    // find appropriate child in which the key will be inserted
                    newRoot->children[i]->insertInNode(k);  // insert the key in appropriate child
                    root = newRoot;
                }
            }
        }

        void remove(int k) {
            if (root == nullptr) return;
            root->remove(k);

            if (root->n == 0) {
                Node* temp = root;
                if (root->leafNode) root = nullptr;
                else root = root->children[0];  // root will have only one child in this case
                delete temp;
            }
        }
};


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr);

    int m, n_insert, n_delete, n_search;  // minimum degree, number of elements to insert, delete, search
    cin >> m;
    BTree T(m);     // initialize b tree of minimum degree m
    
    cin >> n_insert;
    for (int i = 0; i < n_insert; i++) {
        int key;
        cin >> key;
        T.insert(key);
    }

    cin >> n_delete;
    for (int i = 0; i < n_delete; i++) {
        int key;
        cin >> key;
        T.remove(key);
    }

    cin >> n_search;
    int h = 0;
    for (int i = 0; i < n_search; i++) {
        int key;
        cin >> key;
        if (T.search(key)) h++;
    }

    float hit_ratio = ((float) h) / n_search;

    cout << fixed << setprecision(2) << hit_ratio << endl;

    return 0;
}