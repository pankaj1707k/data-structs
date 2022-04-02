""" https://leetcode.com/problems/valid-palindrome-ii/ """


def valid_palindrome(s: str) -> bool:
    def solve(i: int, j: int, count: int) -> int:
        if count > 1:
            return False
        if i > j:
            return True
        if s[i] == s[j]:
            return solve(i + 1, j - 1, count)
        return solve(i + 1, j, count + 1) or solve(i, j - 1, count + 1)

    return solve(0, len(s) - 1, 0)


# Better time and space complexity
def valid_palindrome_2(s: str) -> bool:
    def check(i, j) -> bool:
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    i = 0
    j = len(s) - 1
    while i < j:
        if s[i] != s[j]:
            return check(i + 1, j) or check(i, j - 1)
        i += 1
        j -= 1
    return True
