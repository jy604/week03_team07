# 트리의 부모 찾기
# 그 노드를 탐색하기 전에 ans에 노드 번호를 저장
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline
n = int(input())
g = [[] for _ in range(n+1)]
for i in range(n-1):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

visited = [0] * (n + 1)
ans = [0] * (n + 1)


def dfs(v):
    visited[v] = 1
    for i in g[v]:
        if not visited[i]:
            ans[i] = v
            dfs(i)


dfs(1)

for i in range(2, n+1):
    print(ans[i])