""" https://www.hackerrank.com/challenges/closest-numbers/problem """

def closestNumbers(arr):
    arr.sort()
    pairs = []
    diffs = {}  # key -> difference; value -> array of pairs (tuples are used for pairs)
    for i in range(1, len(arr)):
        diff = arr[i] - arr[i-1]
        if diff in diffs:
            diffs[diff].append((arr[i-1], arr[i]))
        else:
            diffs[diff] = [(arr[i-1], arr[i])]
    
    m = min(diffs.keys())
    for pair in diffs[m]:
        pairs.extend([pair[0], pair[1]])
    return pairs


n = int(input())
arr = list(map(int, input().split()))
result = closestNumbers(arr)
for r in result:
    print(r, end=' ')
print()