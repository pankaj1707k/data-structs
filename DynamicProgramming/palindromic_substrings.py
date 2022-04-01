""" https://leetcode.com/problems/palindromic-substrings/ """


def count_substrings(s: str) -> int:
    dp = [None for _ in range(len(s))]
    result = 0

    for j in range(len(s)):
        for i in range(j + 1):
            if i == j:
                dp[i] = True
            elif i + 1 == j:
                dp[i] = s[i] == s[j]
            else:
                dp[i] = (s[i] == s[j]) and dp[i + 1]

            result += int(dp[i])

    return result
