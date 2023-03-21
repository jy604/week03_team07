import sys
sys.stdin=open("week03\input.txt", "rt")
input = sys.stdin.readline
from collections import deque

m,n,h = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
q = deque([])

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                q.append((i, j, k))

# print(q)

# print(tomato[1][1][2])


dx = [1,-1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

def bfs():
    while q:
        z,y,x = q.popleft()
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            if nx < 0 or ny < 0 or nz < 0 or nx >= m or ny >= n or nz >= h:
                continue
            if tomato[nz][ny][nx] == -1:
                continue
            if tomato[nz][ny][nx] == 0:
                tomato[nz][ny][nx] = tomato[z][y][x] + 1
                q.append((nz,ny,nx))
bfs()
# print(tomato)

ans = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            if  tomato[i][j][k] == 0:
                print(-1)
                exit(0)
            if tomato[i][j][k] > ans:
                ans = tomato[i][j][k]

print(ans-1)
            