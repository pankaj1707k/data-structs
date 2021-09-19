""" https://www.hackerrank.com/challenges/lilys-homework/problem """


def lilysHomework(arr):
    n = len(arr)
    arr_copy = list(arr)
    m = {}
    for i in range(n):
        m[arr[i]] = i
    
    s = sorted(arr)
    swaps_inc = 0
    for i in range(n):
        if arr[i] != s[i]:
            swaps_inc += 1
            swap_pos = m[s[i]]
            m[arr[i]] = swap_pos
            arr[swap_pos], arr[i] = arr[i], s[i]
    
    arr_copy.reverse()
    arr = arr_copy
    swaps_dec = 0
    m = {}
    for i in range(n):
        m[arr[i]] = i
    
    for i in range(n):
        if arr[i] != s[i]:
            swaps_dec += 1
            swap_pos = m[s[i]]
            m[arr[i]] = swap_pos
            arr[swap_pos], arr[i] = arr[i], s[i]
    
    if swaps_inc < swaps_dec:
        return swaps_inc
    else:
        return swaps_dec


n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
result = lilysHomework(arr)
print(result)