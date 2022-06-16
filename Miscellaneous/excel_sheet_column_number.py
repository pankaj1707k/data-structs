""" https://leetcode.com/problems/excel-sheet-column-number/ """


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        for i, c in enumerate(columnTitle[::-1]):
            num += (ord(c) - ord("A") + 1) * (26 ** i)
        return num
