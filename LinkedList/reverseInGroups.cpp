/* 
    Given a linked list reverse every k nodes.

    INPUT:
    First line of input takes two space-separated numbers:
        1. number of nodes in the linked list (n)
        2. max number of nodes taken per group for reversal (k)
    The next n lines take one integer each for data part of each node.

    OUTPUT:
    Linked list after reversing in groups of k nodes.

    Linked list is implemented using struct definition.
*/

#include <iostream>

using namespace std;

// Linked list node
struct llnode {
    int data;
    struct llnode* next;
};

typedef struct llnode node;


node* insert(node* head, int node_data) {
    node* temp = (node*)malloc(sizeof(node));
    temp->data = node_data;
    temp->next = nullptr;

    if (head == nullptr) {  // linked list is empty
        head = temp;
    }
    else {
        node* ptr = head;
        while (ptr->next != nullptr)  // reach the last node
            ptr = ptr->next;
        ptr->next = temp;
    }
    
    return head;
}


node* reverse_group(node* head, int k) {
    
    // base case
    if (head == nullptr)   // sublist contains only null
        return nullptr;
    
    // reverse a sublist of size k
    node* pre = nullptr;   // pointer to previous node
    node* cur = head;      // pointer to current node
    node* nxt = nullptr;   // pointer to next node
    int i = 0;
    while (cur!=nullptr && i<k) {   // reverse maximum k nodes
        nxt = cur->next;
        cur->next = pre;
        pre = cur;
        cur = nxt;
        i++;
    }

    // recursive case
    if (nxt!=nullptr) {
        head->next = reverse_group(nxt, k);
    }

    return pre;   // new head for the re-ordered list
}


void print_list(node* head) {
    node* ptr = head;
    while (ptr->next != nullptr) {
        cout << ptr->data << " -> ";
        ptr = ptr->next;
    }
    cout << ptr->data << " -> NULL" << endl;
}


int main() {
    int n, k;
    cin >> n >> k;
    node* head = nullptr;

    int data;
    for (int i=0; i<n; i++) {
        cin >> data;
        head = insert(head, data);
    }

    head = reverse_group(head, k);

    print_list(head);

    return 0;
}