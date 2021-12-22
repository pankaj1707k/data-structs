""" https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/t1-1-6064aa64/ """

import sys
from queue import Queue
from collections import defaultdict

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline

n = int(input())
a = tuple(input().split())
level = defaultdict(int)

a_sorted = tuple(sorted(a))
q = Queue()
q.put(a)
while not q.empty():
    curr_perm = q.get()
    if curr_perm == a_sorted:
        break
    flag = False
    for k in range(1, n):
        new_perm = curr_perm[k::-1] + curr_perm[k + 1 :]
        if not level[new_perm]:
            q.put(new_perm)
            level[new_perm] = level[curr_perm] + 1
        if new_perm == a_sorted:
            flag = True
            break
    if flag:
        break

print(level[a_sorted])
