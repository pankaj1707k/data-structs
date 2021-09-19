""" https://leetcode.com/problems/counting-bits/ """


def countBits(n):
    arr = [0] * (n + 1)
    for i in range(1, n + 1):
        arr[i] = arr[i >> 1] + i % 2
    return arr


if __name__ == "__main__":
    n = int(input().strip())
    result = countBits(n)
    print(result)
