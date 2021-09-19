""" https://www.hackerrank.com/challenges/sherlock-and-array/problem """

def balancedSums(arr):
    n = len(arr)
    preSum = [0]*(n+1)
    for i in range(1,n+1):
        preSum[i] = preSum[i-1] + arr[i-1]
    
    for i in range(1,n+1):
        leftSum = preSum[i-1]
        rightSum = preSum[n] - preSum[i]
        if leftSum == rightSum:
            return "YES"
    
    return "NO"


if __name__=='__main__':
    t = int(input().strip())
    results = []
    for _ in range(t):
        n = int(input().strip())
        arr = list(map(int, input().rstrip().split()))
        results.append(balancedSums(arr))
    
    for r in results:
        print(r)