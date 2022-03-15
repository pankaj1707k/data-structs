""" https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/ """


def min_remove_to_make_valid(s: str) -> str:
    s = list(s)
    count = 0

    # Traverse forward
    for i, c in enumerate(s):
        if c.isalpha():
            continue
        if c == "(":
            count += 1
        else:
            if count == 0:
                s[i] = "*"
            else:
                count -= 1

    count = 0
    # Traverse backward
    for i in range(len(s) - 1, -1, -1):
        if s[i].isalpha():
            continue
        if s[i] == ")":
            count += 1
        else:
            if count == 0:
                s[i] = "*"
            else:
                count -= 1

    s = [c for c in s if c != "*"]
    return "".join(s)
