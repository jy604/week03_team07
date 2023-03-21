import sys
sys.stdin=open("week03\input.txt", "rt")
input = sys.stdin.readline
sys.setrecursionlimit(10000)
from collections import deque

def bfs(v):
    global cnt
    q = deque([v])  # pop메서드의 시간복잡도가 낮은 덱 내장 메서드를 이용한다
    visited[v] = True  # 해당 V 값을 방문처리
    while q:  # q가 빌때까지 돈다.
        v = q.popleft()  # 큐에 있는 첫번째 값 꺼낸다.
        cnt += 1
        for i in range(1, n + 1):  # 1부터 N까지 돈다
            if not visited[i] and graph[v][i]:  # 만약 해당 i값을 방문하지 않았고 V와 연결이 되어 있다면
                q.append(i)  # 그 i 값을 추가
                visited[i] = True  # i 값을 방문처리


n = int(input())
m = int(input())

graph = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited = [False] * (n + 1)  

cnt = -1

bfs(1)
print(cnt)