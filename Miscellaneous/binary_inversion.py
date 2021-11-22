""" https://www.codechef.com/START17C/problems/BININV """

def numberOfInversions(s: str, l: int) -> int:
    ans = 0
    num_ones = 0
    for i in range(l):
        if s[i] == '1':
            num_ones += 1
        else:
            ans += num_ones
    return ans

t = int(input().strip())
result = []
for _ in range(t):
    n, m = list(map(int, input().rstrip().split()))
    arr = [input().strip() for i in range(n)]
    arr.sort(key=lambda s: s.count('1'))
    ans_str = "".join(arr)
    result.append(numberOfInversions(ans_str, n*m))

for r in result:
    print(r)