/* 
    Given a singly linked list of N integers, perform the following operation:
    Select all the subparts of the list that contain only even integers.
    For example, if the list is {1,2,8,9,12,16} then the selected subparts will be
    {2,8} and {12,16}. Reverse the selected subparts: {8,2} and {16,12}.
    Print the full list upon reversal of appropriate subparts.

    INPUT:
    First line: N -> length of list
    Second line: N space-separated integers

    OUTPUT:
    N space-separated integers (elements of the modified linked list).
*/

#include <iostream>
using namespace std;

class node {
    public:
        int data;
        node* next;

        node(int node_data) {
            this->data = node_data;
            this->next = nullptr;
        }
};


node* insert_node(node* head, int node_data) {
    node* new_node = new node(node_data);
    
    if (head == nullptr) {
        head = new_node;
    } else {
        node* ptr = head;
        while (ptr->next != nullptr) {
            ptr = ptr->next;
        }
        ptr->next = new_node;
    }

    return head;
}


void print_llist(node* head) {
    node* ptr = head;
    while (ptr->next != nullptr) {
        cout << ptr->data << " ";
        ptr = ptr->next;
    }
    cout << ptr->data << endl;
}


node* reverse_even_sublists(node* head) {
    // base case
    if (head->next == nullptr) {
        return head;
    }

    node* pre = nullptr;
    node* cur = head;
    node* nxt = head->next;

    // reversing the sublist of even integers, exclusing the last node
    while (cur != nullptr && cur->data % 2 == 0 && nxt != nullptr && nxt->data % 2 == 0) {
        cur->next = pre;
        pre = cur;
        cur = nxt;
        nxt = nxt->next;
    }

    // changing next pointer of the last node of sublist
    if (cur != nullptr && cur->data % 2 == 0 && pre != nullptr && pre->data % 2 == 0) {
        cur->next = pre;
    }

    // recursive case: merge the reversed sublist with the remaining list forward (may be even or odd)
    if (nxt != nullptr) {
        head->next = reverse_even_sublists(nxt);
    }

    return cur;
}


int main() {
    int n, num;
    cin >> n;
    node* head = nullptr;
    
    for (int i=0; i < n; i++) {
        cin >> num;
        head = insert_node(head, num);
    }

    head = reverse_even_sublists(head);

    print_llist(head);

    return 0;
}