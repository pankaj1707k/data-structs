""" https://leetcode.com/problems/champagne-tower/ """


def champagne_tower(poured: int, query_row: int, query_glass: int) -> float:
    if poured < 2:
        if query_row == 0 and query_glass == 0:
            return poured
        return 0

    glasses = [[0] * 100 for _ in range(100)]
    glasses[0][0] = poured

    for i in range(1, query_row + 1):
        for j in range(i + 1):
            if j == 0:
                if glasses[i - 1][j] - 1 > 0:
                    glasses[i][j] = (glasses[i - 1][j] - 1) / 2
            elif j == i:
                if glasses[i - 1][j - 1] - 1 > 0:
                    glasses[i][j] = (glasses[i - 1][j - 1] - 1) / 2
            else:
                if glasses[i - 1][j] - 1 > 0:
                    glasses[i][j] += (glasses[i - 1][j] - 1) / 2
                if glasses[i - 1][j - 1] - 1 > 0:
                    glasses[i][j] += (glasses[i - 1][j - 1] - 1) / 2

    if glasses[query_row][query_glass] < 0:
        return 0
    if glasses[query_row][query_glass] < 1:
        return glasses[query_row][query_glass]
    return 1
