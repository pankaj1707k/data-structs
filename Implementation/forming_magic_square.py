""" https://www.hackerrank.com/challenges/magic-square-forming/problem """

def formingMagicSquare(s):
    magicSquares = [
        [
            [2,9,4],
            [7,5,3],
            [6,1,8]
        ],
        [
            [4,9,2],
            [3,5,7],
            [8,1,6]
        ],
        [
            [6,1,8],
            [7,5,3],
            [2,9,4]
        ],
        [
            [8,1,6],
            [3,5,7],
            [4,9,2]
        ],
        [
            [4,3,8],
            [9,5,1],
            [2,7,6]
        ],
        [
            [8,3,4],
            [1,5,9],
            [6,7,2]
        ],
        [
            [2,7,6],
            [9,5,1],
            [4,3,8]
        ],
        [
            [6,7,2],
            [1,5,9],
            [8,3,4]
        ]
    ]

    costs = [0]*8
    for sq in range(8):
        for i in range(3):
            for j in range(3):
                costs[sq] += abs(s[i][j] - magicSquares[sq][i][j])
    
    return min(costs)


s = []
for _ in range(3):
    s.append(list(map(int, input().rstrip().split())))

result = formingMagicSquare(s)
print(result)