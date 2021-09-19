""" https://www.hackerrank.com/challenges/queens-attack-2/problem """


def queensAttack(n, k, r_q, c_q, obstacles):
    numCells = 0

    # Use dictionary instead of list of obstacles for faster member-checking
    obs = dict()
    for ob in obstacles:
        obs[tuple(ob)] = 0
    obstacles = obs

    # Up
    i, j = r_q+1, c_q
    while (i <= n) and ((i,j) not in obstacles):
        numCells += 1
        i += 1
    
    # Down
    i, j = r_q-1, c_q
    while (i > 0) and ((i,j) not in obstacles):
        numCells += 1
        i -= 1
    
    # Left
    i, j = r_q, c_q-1
    while (j > 0) and ((i,j) not in obstacles):
        numCells += 1
        j -= 1
    
    # Right
    i, j = r_q, c_q+1
    while (j <= n) and ((i,j) not in obstacles):
        numCells += 1
        j += 1
    
    # Left-Up
    i, j = r_q+1, c_q-1
    while (i <= n) and (j > 0) and ((i,j) not in obstacles):
        numCells += 1
        i += 1
        j -= 1

    # Right-Up
    i, j = r_q+1, c_q+1
    while (i <= n) and (j <= n) and ((i,j) not in obstacles):
        numCells += 1
        i += 1
        j += 1
    
    # Right-Down
    i, j = r_q-1, c_q+1
    while (i > 0) and (j <= n) and ((i,j) not in obstacles):
        numCells += 1
        i -= 1
        j += 1
    
    # Left-Down
    i, j = r_q-1, c_q-1
    while (i > 0) and (j > 0) and ((i,j) not in obstacles):
        numCells += 1
        i -= 1
        j -= 1
    
    return numCells


if __name__=='__main__':
    n, k = list(map(int, input().rstrip().split()))
    r_q, c_q = list(map(int, input().rstrip().split()))
    obstacles = []
    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))
    
    result = queensAttack(n, k, r_q, c_q, obstacles)
    
    print(result)