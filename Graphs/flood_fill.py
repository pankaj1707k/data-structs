""" https://leetcode.com/problems/flood-fill/ """

from typing import *

def floodFill(image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
    m = len(image)
    n = len(image[0])
    init_color = image[sr][sc]

    def dfs(i:int, j:int):
        if i < 0 or i >= m or j < 0 or j >= n:  return
        if image[i][j] != init_color:   return
        image[i][j] = newColor
        dfs(i-1,j)
        dfs(i,j-1)
        dfs(i+1,j)
        dfs(i,j+1)

    if init_color != newColor:
        dfs(sr,sc)
    
    return image


tests = [
    [[[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2],
    [[[0,0,0],[0,0,0]], 0, 0, 2]
]
for t in tests:
    print(floodFill(t[0], t[1], t[2], t[3]))