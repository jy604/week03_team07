import sys
sys.stdin=open("week03\input.txt", "rt")
input = sys.stdin.readline
sys.setrecursionlimit(10000)

def dfs(v):
    visited[v] = True  
    for i in range(1, n + 1):
        if not visited[i] and graph[v][i]:  
            dfs(i) 

n, m = map(int, input().split())

graph = [[False] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited = [False] * (n + 1)  

cnt = 0

for j in range(1, n+1):
    print(visited)
    if not visited[j]:
        dfs(j)
        cnt += 1

print(cnt)