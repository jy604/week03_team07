import sys
sys.stdin=open("week03\input.txt", "rt")
input = sys.stdin.readline
from collections import deque
import heapq

INF=int(1e9)

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int,input().rstrip())))

dist = [[INF]*n for _ in range(n)]
dist[0][0] = 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]



def maze(x,y,cnt):
    q = deque()
    q.append((x,y,cnt))
    ans = INF
    while q:
        x, y, cnt = q.popleft()
        if x == n-1 and y == n-1 and ans > cnt:
            ans = cnt
        if dist[x][y] < cnt:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 0 and dist[nx][ny] > (cnt+1):
                dist[nx][ny] = cnt + 1
                q.append((nx,ny,cnt+1))
            if graph[nx][ny] == 1 and dist[nx][ny] > cnt:
                dist[nx][ny] = cnt
                q.append((nx,ny,cnt))
    return ans

print(maze(0,0,0))