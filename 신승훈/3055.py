import sys
from collections import deque

input = sys.stdin.readline

# R행 C열
# '.' -> 비어있음 ,  '*' -> 물,  'X' -> 돌,  'D' -> 비버의 굴, 'S' -> 고슴도치의 위치

# 매 분 고슴도치(S)는 현재 있는 칸과 인접한 네 칸중 하나로 이동할 수 있다 
# 물(*)도 매 분마다 비어있는 칸으로 확장한다.
# 물(*)이 있는 칸과 인접해 있는 비어있는 칸(.)은 물이 차게 된다.
# 물(*)과 고슴도치(S)는 돌(X)을 통과할 수 없다. 
# 고슴도치(S)는 물(*)로 이동할 수 없고, 물(*)도 비버의 굴(D)로 이동할 수 없다
# 고슴도치 (S)가 안전하게 비버의 굴(D)로 이동하기 위해 필요한 최소 시간을 구하는 프로그램

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def escape(a, b):
    q = deque()
    visited = [[0]*c for _ in range(r)]
    q.append((a, b)) # 고슴도치의 위치
    visited[a][b] = 1 # 고슴도치의 위치를 덱에 넣고 1로 방문처리
    for i in range(r):
        for j in range(c):
            if graph[i][j] == "*":
                visited[i][j] = -1
                q.append((i, j))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx in range(r) and ny in range(c):
                if visited[x][y] > 0 and graph[nx][ny] =="D":
                    return visited[x][y]
            
                if graph[nx][ny] == ".":
                    # 고슴도치일 경우 방문을 확인
                    if visited[x][y] > 0 and not visited[nx][ny]:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx, ny))
                    elif visited[nx][ny] >= 0 and visited[x][y] == -1:
                        visited[nx][ny] = -1
                        q.append((nx, ny))
    return "KAKTUS"
    #                 
r, c = map(int, input().split())
graph = []
for _ in range(r):
    graph.append(list(map(str, input())))

for i in range(r):
    for j in range(c):
        if graph[i][j] == 'S':
            print(escape(i, j))
            break
    
    
