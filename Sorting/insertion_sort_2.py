""" https://www.hackerrank.com/challenges/insertionsort2/problem """

def insertionSort2(n, arr):
    for i in range(1,n):
        temp = arr[i]
        j = i-1
        while j >= 0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = temp
        for x in arr:
            print(x, end=' ')
        print()


n = int(input())
arr = list(map(int, input().split()))
insertionSort2(n, arr)