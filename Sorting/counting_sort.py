""" https://www.hackerrank.com/challenges/countingsort2/problem """

def countingSort(arr):
    m = max(arr)
    freq = [0]*(m+1)
    for a in arr:
        freq[a] += 1
    sorted_arr = []
    for i in range(m+1):
        if freq[i] != 0:
            for _ in range(freq[i]):
                sorted_arr.append(i)
    return sorted_arr


n = int(input())
arr = list(map(int, input().split()))
result = countingSort(arr)
for a in result:
    print(a, end=' ')