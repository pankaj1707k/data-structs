""" https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/ """


def get_smallest_string(n: int, k: int) -> str:
    values = {v: chr(ord("a") + v - 1) for v in range(1, 27)}
    result = []
    for i in range(n, 0, -1):
        val = 26 if k - (i - 1) >= 26 else k - (i - 1)
        result.append(values[val])
        k -= val
    result.reverse()
    return "".join(result)


print(get_smallest_string(99217, 131316))
