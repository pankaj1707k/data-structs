""" https://www.hackerrank.com/challenges/bigger-is-greater/problem """


def biggerIsGreater(w):
    a = list(w)
    n = len(a)

    i = n-1
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i <= 0:
        return "no answer"
    
    j = n-1
    while a[j] <= a[i-1]:
        j -= 1
    a[j], a[i-1] = a[i-1], a[j]

    a[i:] = a[n-1:i-1:-1]
    return "".join(a)


if __name__=='__main__':
    t = int(input().strip())

    result = []
    
    for _ in range(t):
        w = input().strip()
        result.append(biggerIsGreater(w))
    
    for r in result:
        print(r)