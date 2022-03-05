""" https://leetcode.com/problems/generate-parentheses/ """

from typing import *


def generate_parentheses(n: int) -> List[str]:
    ans = []

    def generate(s: str) -> None:
        if len(s) == 2 * n:
            ans.append(s)
            return
        count_open = s.count("(")
        count_close = s.count(")")
        if count_open < n:
            generate(s + "(")
        if count_close < count_open:
            generate(s + ")")

    generate("")
    return ans
