""" https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/ """


class Solution:
    # O(n*k) time; O(n*k) space
    def hasAllCodes(self, s: str, k: int) -> bool:
        req = 1 << k  # 2^k binary codes are required
        seen = set()  # set of binary codes already seen
        for i in range(k, len(s) + 1):  # O(n) time
            sub = s[i - k : i]  # O(k) time
            if sub not in seen:  # O(1) time
                seen.add(sub)
                req -= 1
                if req == 0:
                    return True
        return False
