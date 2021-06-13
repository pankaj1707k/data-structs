/*
    After getting her PhD, Christie has become a celebrity at her university, 
    and her facebook profile is full of friend requests. Being the nice girl she is, 
    Christie has accepted all the requests.

    Now Kuldeep is jealous of all the attention she is getting from other guys, 
    so he asks her to delete some of the guys from her friend list.

    To avoid a 'scene', Christie decides to remove some friends from her friend list, 
    since she knows the popularity of each of the friend she has, 
    she uses the following algorithm to delete a friend.

    Algorithm to delete friend:
        deleteFriend = false
        for i=1 to friend.length-1
            if (friend[i].popularity < friend[i+1].popularity)
                delete i th friend
                deleteFriend = true
                break
        if deleteFriend == false
            delete the last friend

    INPUT:
    First line: T --> number of test cases
    For each test case
        First line: N K --> number of total friends and number of friends to remove
        Second line: N space-separated numbers representing the popularity of N friends
    
    OUTPUT:
    For each test case: print N-K space-separated numbers as the popularities of friends remaining
    after deleting K friends as per the algorithm

    CONSTRAINTS:
    1 <= T <= 1000
    1 <= N <= 100000
    0 <= K < N
    0 <= popularity_of_friend <= 100
*/

#include <bits/stdc++.h>

using namespace std;


class linkedListNode {
    public:
        int data;
        linkedListNode* next;

        linkedListNode(int node_data) {
            this->data = node_data;
            this->next = nullptr;
        }
};


// class linkedList {
//     public:
//         linkedListNode* head;
//         linkedListNode* tail;

//         linkedList() {
//             this->head = nullptr;
//             this->tail = nullptr;
//         }

//         void insert_node(int node_data) {
//             linkedListNode* node = new linkedListNode(node_data);

//             if (this->head == nullptr) {
//                 this->head = node;
//             } else {
//                 this->tail->next = node;
//             }

//             this->tail = node;
//         }

//         void print_llist() {
//             linkedListNode* ptr = this->head;
//             while (ptr->next != nullptr) {
//                 cout << ptr->data << " ";
//                 ptr = ptr->next;
//             }
//             cout << ptr->data << endl;
//         }
// };


linkedListNode* insert_node(linkedListNode* head, int node_data) {
    linkedListNode* node = new linkedListNode(node_data);

    if (head == nullptr) {
        head = node;
    } else {
        linkedListNode* ptr = head;
        while (ptr->next != nullptr) {
            ptr = ptr->next;
        }
        ptr->next = node;
    }

    return head;
}

void print_llist(linkedListNode* head) {
    linkedListNode* ptr = head;
    while (ptr->next != nullptr) {
        cout << ptr->data << " ";
        ptr = ptr->next;
    }
    cout << ptr->data << endl;
}


// linkedListNode* deleteFriend(linkedListNode* head) {
//     if (head->data < head->next->data) {
//         linkedListNode* temp = head;
//         head = head->next;
//         delete temp;
//     } else {
//         linkedListNode* ptr = head->next;
//         linkedListNode* pre = head;
//         bool deleted = false;
//         while (ptr->next != nullptr) {
//             if (ptr->data < ptr->next->data) {
//                 pre->next = ptr->next;
//                 delete ptr;
//                 ptr = pre->next;
//                 deleted = true;
//                 break;
//             } else {
//                 pre = ptr;
//                 ptr = ptr->next;
//             }
//         }
//         if (deleted == false) {
//             pre->next = ptr->next;
//             delete ptr;
//         }
//     }

//     return head;
// }


linkedListNode* removeFriends(linkedListNode* head, int k) {
    if (head->next==nullptr || k<=0)
        return head;
    linkedListNode* nxt = removeFriends(head->next, k-1);
    if (head->data < nxt->data) {
        head = nxt;
    }

    return head;
}


int main() {
    int T;  // number of test cases
    cin >> T;
    linkedListNode* llist_heads[T] = {nullptr};

    for (int i = 0; i < T; i++) {
        int N, K, pop_num;  // number of friends, friends to delete and popularity number
        cin >> N >> K;

        for (int j = 0; j < N; j++) {
            cin >> pop_num;
            insert_node(llist_heads[i], pop_num);
        }

        // Now make a function call to delete the said number of friends as per given algorithm
        llist_heads[i] = removeFriends(llist_heads[i], K);
    }

    for (int i = 0; i < T; i++) {
        print_llist(llist_heads[i]);
    }

    return 0;
}