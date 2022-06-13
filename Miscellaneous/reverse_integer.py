""" https://leetcode.com/problems/reverse-integer/ """


class Solution:
    def count_digits(self, x: int) -> int:
        count = 0
        while x:
            count += 1
            x //= 10
        return count

    def reverse(self, x: int) -> int:
        UPPER_BOUND = (1 << 31) - 1
        MAX_COUNT = self.count_digits(UPPER_BOUND)
        sign = -1 if x < 0 else 1
        x = abs(x)
        count = self.count_digits(x)

        # Check if reversed number will go out of bounds
        if count == MAX_COUNT:
            for i in range(1, MAX_COUNT):
                right_digit_x = (x % (10 ** i)) // (10 ** (i - 1))
                left_digit_bound = (UPPER_BOUND // (10 ** (MAX_COUNT - i))) % 10
                if right_digit_x > left_digit_bound:
                    return 0
                if right_digit_x < left_digit_bound:
                    break

        # Reverse number
        reverse = 0
        while x:
            digit = x % 10
            reverse = reverse + (digit * (10 ** (count - 1)))
            x //= 10
            count -= 1

        return reverse * sign

    def reverse(self, x: int) -> int:
        INT_MAX = (1 << 31) - 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        reverse = 0
        while x:
            digit = x % 10
            x //= 10
            # Check for overflow
            if (
                (sign == 1)
                and (reverse > INT_MAX // 10)
                or (reverse == INT_MAX // 10 and digit > 7)
            ):
                return 0
            # Check for underflow
            if (
                (sign == -1)
                and (reverse > INT_MAX // 10)
                or (reverse == INT_MAX // 10 and digit > 8)
            ):
                return 0
            reverse = reverse * 10 + digit
        return reverse * sign
