/*
    Delete all duplicate entries in a linked list.

    INPUT:
    First line of input takes in a positive integer (n -> number of test cases).
    Next n lines contain variable number of space-separated integers.
    Each such line represents a linked list and the integer (-1) is reserved to
    mark the end of each line (-1 is not included in the linked list).

    OUTPUT:
    n lines each containing space-separated integers.
    Each line represents the corresponding linked list from input line
    after deleting all duplicate nodes.

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


// check whether num exists in arr[], return true if found
bool found(int arr[], int num, int length) {
    for (int i=0; i < length; i++) {
        if (arr[i] == num)
            return true;
    }
    return false;
}


node* delete_duplicate(node* head, int length) {
    int arr[length] = {-1}, i = 0;   // -1 cannot be present in the linked list
    node* pre = nullptr;    // pointer to previous node
    node* cur = head;       // pointer to current node

    while (cur != nullptr) {
        if ( !found(arr, cur->data, length) ) {   // encountered the first instance of the node
            arr[i] = cur->data;
            i++;
        } else {    // encountered a duplicate entry for the node
            pre->next = cur->next;
            delete cur;
            cur = pre->next;
            continue;
        }

    // Following 2 lines are executed if current node is not a duplicate of any node covered so far
        pre = cur;
        cur = cur->next;
    }

    return head;
}


node* insert(node* head, int node_data) {
    node* temp = (node*)malloc(sizeof(node));
    temp->data = node_data;
    temp->next = nullptr;

    if (head == nullptr) {  // linked list is empty
        head = temp;
    }
    else {
        node* ptr = head;
        while (ptr->next != nullptr)    // reach the last node
            ptr = ptr->next;
        ptr->next = temp;
    }
    
    return head;
}


void print_list(node* head) {
    node* ptr = head;
    while (ptr->next != nullptr) {
        cout << ptr->data << " ";
        ptr = ptr->next;
    }
    cout << ptr->data << endl;
}


int main() {
    int n;
    cin >> n;
    node* heads[n] = {nullptr};     // Contains pointers to the head of n linked lists from input
    for (int i=0; i<n; i++) {
        int num = 0, count = 0;
        cin >> num;
        while (num != -1) {
            heads[i] = insert(heads[i], num);
            count++;
            cin >> num;
        }

        heads[i] = delete_duplicate(heads[i], count);
    }

    for (int i=0; i<n; i++) {
        print_list(heads[i]);
    }

    return 0;
}