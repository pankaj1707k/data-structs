""" https://www.hackerearth.com/practice/algorithms/graphs/breadth-first-search/practice-problems/algorithm/dhoom-4/ """

import sys
from queue import Queue

sys.stdin = open("../../input.txt", "r")
input = sys.stdin.readline
MOD = 100000

source, target = map(int, input().split())
n = int(input())
keys = list(map(int, input().split()))
level = [0] * (MOD + 1)

q = Queue()
q.put(source)
curr_product = source
while not q.empty():
    curr_product = q.get()
    flag = False
    for key in keys:
        new_product = (curr_product * key) % MOD
        if not level[new_product]:
            q.put(new_product)
            level[new_product] = level[curr_product] + 1
        if new_product == target:
            flag = True
            break
    if flag:
        break

print(level[target] if level[target] else -1)
