import sys
sys.stdin=open("week03\input.txt", "rt")
input = sys.stdin.readline
from collections import deque

r,c = map(int, input().split())
graph = []
for i in range(r):
    graph.append(list(input().rstrip()))

q1 = deque([])
q2 = deque([])


for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            q1.append((i, j))
        elif graph[i][j] == '*':
            q2.append((i, j))


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs():
    ans = 0
    while q1:
        # 물의 이동
        for _ in range(len(q2)):
            x, y = q2.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= r or ny >= c:
                    continue
                if graph[nx][ny] == '.':
                    graph[nx][ny] = '*'
                    q2.append((nx, ny))
        # 고슴도치 이동
        for _ in range(len(q1)):
            x, y = q1.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or ny < 0 or nx >= r or ny >= c:
                        continue
                if graph[nx][ny] in ['.', 'D']:
                    if graph[nx][ny] == 'D':
                        return ans+1
                    graph[nx][ny] = 'S'
                    q1.append((nx, ny))
        ans += 1
    
    return "KATUS"

print(bfs())
                
