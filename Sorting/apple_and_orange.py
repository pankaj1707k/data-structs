""" https://www.hackerrank.com/challenges/apple-and-orange/problem """


def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples = [ x+a for x in apples ]
    oranges = [ x+b for x in oranges ]
    
    apple_count = 0
    orange_count = 0

    for x in apples:
        if x >= s and x <= t:
            apple_count += 1
    
    for x in oranges:
        if x >= s and x <= t:
            orange_count += 1
    
    print(apple_count)
    print(orange_count)


s, t = list(map(int, input().rstrip().split()))
a, b = list(map(int, input().rstrip().split()))
m, n = list(map(int, input().rstrip().split()))
apples = list(map(int, input().rstrip().split()))
oranges = list(map(int, input().rstrip().split()))
countApplesAndOranges(s, t, a, b, apples, oranges)