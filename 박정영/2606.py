# 바이러스
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
n = int(input()) # 노드 수
m = int(input()) # 간선 수
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (n + 1)


def dfs(v):
    global cnt
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
            # print(visited[i])
#
# for i in range(1, n+1):
#     if visited[i] == 0:
#         cnt += 1
#         dfs(i)
dfs(1)
print(sum(visited) - 1) # 맨 앞 빈 노드 뺴기