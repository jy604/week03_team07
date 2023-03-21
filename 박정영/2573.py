# 빙산
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0] * m for i in range(n)] # 방문 체크
count = [[0] * m for _ in range(n)]
result = []

# 빙산 넣기
ice = []
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            ice.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
year = 0

def bfs(a, b):
    q = deque()
    q.append((a,b))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] != 0 and visited == 0:
                visited[nx][ny] = 1
                q.append((nx, ny))
            elif graph[nx][ny] == 0:
