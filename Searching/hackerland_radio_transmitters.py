""" https://www.hackerrank.com/challenges/hackerland-radio-transmitters/problem """

def hackerlandRadioTransmitters(x, k):
    x.sort()
    transmitterCount = 0
    n = len(x)
    i = 0
    while (i < n):
        transmitterCount += 1
        nextLocation = x[i] + k
        while i < n and x[i] <= nextLocation:
            i += 1
        i -= 1
        nextLocation = x[i] + k
        while i < n and x[i] <= nextLocation:
            i += 1
    
    return transmitterCount


if __name__=='__main__':
    n, k = list(map(int, input().rstrip().split()))
    x = list(map(int, input().rstrip().split()))
    result = hackerlandRadioTransmitters(x, k)
    print(result)