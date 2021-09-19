""" https://www.hackerrank.com/challenges/between-two-sets/problem """


def getTotalX(a, b):
    lower_bound = max(a)
    upper_bound = min(b)
    count = 0

    for num in range(lower_bound, upper_bound+1):
        for x in a:
            if num % x != 0:
                break
        else:
            for y in b:
                if y % num != 0:
                    break
            else:
                count += 1
    
    return count


n, m = list(map(int, input().rstrip().split()))
a = list(map(int, input().rstrip().split()))
b = list(map(int, input().rstrip().split()))
print(getTotalX(a, b))