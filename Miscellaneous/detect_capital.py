""" https://leetcode.com/problems/detect-capital/ """


def detectCapital(word: str) -> bool:
    if word.isupper():
        return True
    if word[0].isupper() and word[1:].islower():
        return True
    if word.islower():
        return True
    return False
