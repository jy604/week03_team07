# 고슴도치 탈출
import sys
from collections import deque
input = sys.stdin.readline
r, c = map(int, input().split())

graph = [list(input().strip()) for _ in range(r)]
distance = [[0] * c for _ in range(r)]
queue = deque()

# 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(Dx, Dy):
    while queue:
        x, y = queue.popleft()
        if graph[Dx][Dy] == 'S':
            return distance[Dx][Dy]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < r and 0 <= ny < c:
                if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and graph[x][y] == 'S':
                    graph[nx][ny] = 'S'
                    distance[nx][ny] = distance[x][y] + 1
                    queue.append((nx, ny))
                elif (graph[nx][ny] == '.' or graph[nx][ny] == 'S') and graph[x][y] =='*':
                    graph[nx][ny] = '*'
                    queue.append((nx, ny))
    return "KAKTUS"


for x in range(r):
    for y in range(c):
        if graph[x][y] == 'S':
            queue.append((x, y))
        elif graph[x][y] == 'D':
            Dx, Dy = x, y

for x in range(r):
    for y in range(c):
        if graph[x][y] == '*':
            queue.append((x, y))

print(bfs(Dx,Dy))
