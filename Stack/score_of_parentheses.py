""" https://leetcode.com/problems/score-of-parentheses/ """


def score_of_parentheses(s: str) -> int:
    score = balance = 0
    for i, p in enumerate(s):
        if p == "(":
            balance += 1
        else:
            balance -= 1
            if s[i - 1] == "(":
                score += 1 << balance

    return score
