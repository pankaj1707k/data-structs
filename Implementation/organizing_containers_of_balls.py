""" https://www.hackerrank.com/challenges/organizing-containers-of-balls/problem """


def organizingContainers(containers):
    n = len(containers)
    totalBallsByType = [0]*n
    totalBallsByContainer = [0]*n
    for i in range(n):
        for j in range(n):
            totalBallsByType[j] += containers[i][j]
            totalBallsByContainer[i] += containers[i][j]
    
    totalBallsByType.sort()
    totalBallsByContainer.sort()
    if totalBallsByContainer == totalBallsByType:
        return "Possible"
    return "Impossible"


q = int(input().strip())
results = []
for _ in range(q):
    n = int(input().strip())
    containers = []
    for __ in range(n):
        containers.append(list(map(int, input().rstrip().split())))
    results.append(organizingContainers(containers))

for r in results:
    print(r)