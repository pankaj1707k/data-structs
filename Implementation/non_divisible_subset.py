""" https://www.hackerrank.com/challenges/non-divisible-subset/problem """


def nonDivisibleSubset(k, s):
    d = [0]*k
    for a in s:
        d[a%k] += 1
    
    maxSize = 0
    endPoint = k//2+1 if k%2!=0 else k//2
    for i in range(1,endPoint):
        maxSize += max([d[i], d[k-i]])
    
    if d[0]:
        maxSize += 1
    if k%2 == 0 and d[k/2]:
        maxSize += 1
    
    return maxSize


if __name__=='__main__':
    n, k = list(map(int, input().rstrip().split()))
    s = list(map(int, input().rstrip().split()))
    maxSize = nonDivisibleSubset(k, s)
    print(maxSize)