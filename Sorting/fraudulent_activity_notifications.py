""" https://www.hackerrank.com/challenges/fraudulent-activity-notifications/problem """


def getTwiceMedian(freq, d):
    m = []
    c = 0
    m1, m2 = d//2, d//2 + 1
    for i in range(201):
        c += freq[i]
        if m==[] and m1<=c:
            m.append(i)
        if m2<=c:
            m.append(i)
            break
    
    if d%2 == 0:
        return sum(m)
    else:
        return m[-1]


def activityNotifications(exp, d):
    n = len(exp)
    ans = 0
    freq = [0]*201
    for i in range(d):
        freq[exp[i]] += 1
    
    for i in range(d,n):
        limit = getTwiceMedian(freq, d)
        if exp[i] >= limit:
            ans += 1
        freq[exp[i]] += 1
        freq[exp[i-d]] -= 1

    return ans 


n, d = list(map(int, input().split()))
expenditure = list(map(int, input().split()))
result = activityNotifications(expenditure, d)
print(result)