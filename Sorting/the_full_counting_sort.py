""" https://www.hackerrank.com/challenges/countingsort4/problem """

# parameter: 2D_STRING_ARRAY
def countSort(arr):
    n = len(arr)
    lst = ['']*n
    for i in range(n):
        if i < n//2:
            lst[int(arr[i][0])] += '- '
        else:
            lst[int(arr[i][0])] += arr[i][1] + ' '
    
    for i in range(n):
        print(lst[i], end='')
    print()


n = int(input())
arr = []
for _ in range(n):
    arr.append(input().rstrip().split())

countSort(arr)