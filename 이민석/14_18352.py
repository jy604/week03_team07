import sys
sys.stdin=open("week03\input.txt", "rt")
input = sys.stdin.readline
from collections import deque

n,m,k,x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)  
dist = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)



def bfs(v):
    ans = []
    q = deque([v])
    visited[v] = True
    dist[v] = 0
    while q:
        now = q.popleft()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                dist[i] = dist[now] + 1
                if dist[i] == k:
                    ans.append(i)
    if len(ans) == 0:
        print(-1)
    else:
        ans.sort()
        for i in ans:
            print(i, end='\n')

bfs(x)




    
