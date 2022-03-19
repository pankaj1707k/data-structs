""" https://leetcode.com/problems/powx-n/ """


def pow_func(x: float, n: int) -> float:
    if n == 0:
        return 1.0
    if n > 0:
        if n % 2 == 0:
            return pow_func(x, n // 2) ** 2
        return x * pow_func(x, n // 2) ** 2
    else:
        if n % 2 == 0:
            return pow_func(1 / x, -n // 2) ** 2
        return (1 / x) * pow_func(1 / x, -n // 2) ** 2
