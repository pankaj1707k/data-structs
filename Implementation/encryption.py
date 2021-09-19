""" https://www.hackerrank.com/challenges/encryption/problem """

from math import *


def encryption(s):
    L = len(s)
    lowerBound = floor(sqrt(L))
    upperBound = ceil(sqrt(L))
    rows = lowerBound
    columns = upperBound
    while (rows*columns < L):
        rows += 1
    
    arr = []
    i = 0
    for i in range(rows):
        row = []
        for j in range(columns):
            if i < L:
                row.append(s[i])
            else:
                row.append('')
            i += 1
        arr.append(row)
    
    encrypted = ""
    for j in range(columns):
        for i in range(rows):
            encrypted += arr[i][j]
        encrypted += " "
    
    return encrypted


s = input().strip()
print(encryption(s))