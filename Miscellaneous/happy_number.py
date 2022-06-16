""" https://leetcode.com/problems/happy-number/ """


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            n = self.digit_sq_sum(n)
        return True

    def digit_sq_sum(self, n: int) -> int:
        result = 0
        while n:
            result += (n % 10) ** 2
            n //= 10
        return result
