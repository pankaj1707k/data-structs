""" https://www.hackerrank.com/challenges/missing-numbers/problem """

def missingNumbers(arr, brr):
    freq_b = [0]*10007
    freq_a = [0]*10007
    for b in brr:
        freq_b[b] += 1
    
    for a in arr:
        freq_a[a] += 1
    
    missing = []
    for i in range(10007):
        if freq_a[i] != freq_b[i]:
            missing.append(i)
    
    return missing


if __name__=='__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    m = int(input().strip())
    brr = list(map(int, input().rstrip().split()))
    result = missingNumbers(arr, brr)
    for r in sorted(result):
        print(r, end=' ')