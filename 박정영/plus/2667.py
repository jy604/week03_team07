# 단지번호 붙이기

import sys
from collections import deque


def bfs(g, x, y):
    q = deque()
    q.append((x, y))
    cnt = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n  or ny >= n:
                continue
            if g[nx][ny] == 1:
                g[nx][ny] = 0 # 다시 방문 못하게 0으로 바꿈
                # g[nx][ny] = g[x][y] + 1
                q.append((nx, ny))
                cnt += 1

    return cnt


n = int(input())
g = []
for _ in range(n):
    g.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

result = []
for i in range(n):
    for j in range(n):
        if g[i][j] == 1:
            result.append(g, i, j)

result.sort()
print(len(result))


