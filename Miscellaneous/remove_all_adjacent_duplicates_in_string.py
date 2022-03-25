""" https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/ """


def remove_duplicates(s: str) -> str:
    result = [""]
    for i in range(len(s)):
        if result[-1] == s[i]:
            result.pop()
        else:
            result.append(s[i])
    return "".join(result)
