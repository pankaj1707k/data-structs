""" https://leetcode.com/problems/min-cost-climbing-stairs/ """


def minCostClimbingStairs(C):
    f = []
    f.append(0)
    f.append(0)
    for i in range(2, 1 + len(C)):
        val = min(f[i - 1] + C[i - 1], f[i - 2] + C[i - 2])
        f.append(val)

    return f[-1]


if __name__ == "__main__":
    cost = list(map(int, input().rstrip().split()))
    result = minCostClimbingStairs(cost)
    print(result)
