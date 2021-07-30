""" https://www.hackerrank.com/challenges/insertionsort1/problem """


def insertionSort1(n, arr):
    temp = arr[n-1]
    for i in range(n-2,-1,-1):
        if arr[i] > temp:
            arr[i+1] = arr[i]
            for x in arr:
                print(x, end=' ')
        else:
            arr[i+1] = temp            
            for x in arr:
                print(x, end=' ')
            break;
        print()
    else:
        arr[0] = temp
        for x in arr:
            print(x, end=' ')


n = int(input())
arr = list(map(int, input().split()))
insertionSort1(n, arr)