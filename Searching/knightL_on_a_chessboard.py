""" https://www.hackerrank.com/challenges/knightl-on-chessboard/problem """


def neighbor_cells(i, j, x, y, n):
    return filter(
        lambda a: a[0] >= 0 and a[1] >= 0 and a[0] < n and a[1] < n,
        [
            [x + i, y + j],
            [x - i, y + j],
            [x + i, y - j],
            [x - i, y - j],
            [x + j, y + i],
            [x - j, y + i],
            [x + j, y - i],
            [x - j, y - i],
        ],
    )


def move(i, j, n, memo):
    if memo[i][j] is not None:
        return memo[i][j]
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = [[0, 0, 0]]  # q[i] = [x,y,depth]
    while len(q) > 0:
        x, y, l = q.pop()
        if x == n - 1 and y == n - 1:
            memo[i][j] = l
            memo[j][i] = l
            return l
        neighbors = [
            [x_i, y_i]
            for x_i, y_i in neighbor_cells(i, j, x, y, n)
            if visited[y_i][x_i] == False
        ]
        for x_i, y_i in neighbors:
            visited[y_i][x_i] = True
            q.insert(0, [x_i, y_i, l + 1])

    memo[i][j] = -1
    memo[j][i] = -1
    return -1


def knightlOnAChessboard(n):
    moveNumbers = []
    memo = [[None for _ in range(n + 1)] for _ in range(n + 1)]
    for i in range(1, n):
        row = []
        for j in range(1, n):
            row.append(move(i, j, n, memo))
        moveNumbers.append(row)

    return moveNumbers


if __name__ == "__main__":
    n = int(input().strip())
    result = knightlOnAChessboard(n)
    for i in result:
        for j in result[i]:
            print(j, end=" ")
        print()
