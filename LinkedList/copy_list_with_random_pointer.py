""" https://leetcode.com/problems/copy-list-with-random-pointer/ """

from typing import *


class Node:
    def __init__(
        self, val: int = 0, next: "Node" = None, random: "Node" = None
    ) -> None:
        self.val = val
        self.next = next
        self.random = random


# Time: O(n^2), Space: O(n)
def copy_random_list(head: Optional[Node]) -> Optional[Node]:
    if head == None:
        return None
    random_hash = {}
    i = 0
    node = head
    while node:
        if node.random == None:
            random_hash[i] = None
            node = node.next
            i += 1
            continue
        temp = head
        j = 0
        while temp:
            if temp == node.random:
                random_hash[i] = j
                break
            temp = temp.next
            j += 1
        node = node.next
        i += 1

    new_head = Node(head.val)
    new_node = None
    new_prev = new_head
    old_node = head.next
    while old_node:
        new_node = Node(old_node.val)
        new_prev.next = new_node
        new_prev = new_node
        old_node = old_node.next

    i = 0
    node = new_head
    while node:
        if random_hash[i] == None:
            node.random = None
            node = node.next
            i += 1
            continue
        j = 0
        temp = new_head
        while temp:
            if random_hash[i] == j:
                node.random = temp
                break
            temp = temp.next
            j += 1
        node = node.next
        i += 1

    return new_head


# Time: O(n), Space: O(n)
def copy_random_list_2(head: Optional[Node]) -> Optional[Node]:
    node_hash = {}
    new_list = Node(0)
    old_node = head
    new_node = new_list
    while old_node:
        new_node.next = Node(old_node.val)
        new_node = new_node.next
        node_hash[old_node] = new_node
        old_node = old_node.next

    old_node = head
    new_node = new_list.next
    while old_node:
        new_node.random = node_hash[old_node.random] if old_node.random else None
        new_node = new_node.next
        old_node = old_node.next

    return new_list.next
