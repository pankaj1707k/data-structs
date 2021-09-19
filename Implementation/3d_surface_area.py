""" https://www.hackerrank.com/challenges/3d-surface-area/problem """


def leftSA(i, j, A):
    if j == 0:
        return A[i][j]
    if A[i][j-1] >= A[i][j]:
        return 0
    return A[i][j] - A[i][j-1]


def rightSA(i, j, A):
    if j == len(A[0])-1:
        return A[i][j]
    if A[i][j+1] >= A[i][j]:
        return 0
    return A[i][j] - A[i][j+1]


def upSA(i, j, A):
    if i == 0:
        return A[i][j]
    if A[i-1][j] >= A[i][j]:
        return 0
    return A[i][j] - A[i-1][j]


def downSA(i, j, A):
    if i == len(A)-1:
        return A[i][j]
    if A[i+1][j] >= A[i][j]:
        return 0
    return A[i][j] - A[i+1][j]


def surfaceArea(A):
    h = len(A)
    w = len(A[0])
    p = 2*h*w
    for i in range(h):
        for j in range(w):
            p += leftSA(i,j,A)
            p += rightSA(i,j,A)
            p += upSA(i,j,A)
            p += downSA(i,j,A)
    
    return p


h, w = list(map(int, input().rstrip().split()))
A = []
for _ in range(h):
    A.append(list(map(int, input().rstrip().split())))

price = surfaceArea(A)
print(price)