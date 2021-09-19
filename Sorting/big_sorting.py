""" https://www.hackerrank.com/challenges/big-sorting/problem """

def bigSorting(unsorted):
    n = len(unsorted)
    unsorted.sort(key = int)
    return unsorted


n = int(input().strip())

unsorted = []

for _ in range(n):
    unsorted_item = input()
    unsorted.append(unsorted_item)

result = bigSorting(unsorted)

for i in range(n):
    print(unsorted[i])