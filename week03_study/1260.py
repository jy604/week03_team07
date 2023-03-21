# 인접 리스트로 구현한 dfs와 bfs
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
# 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다.
# 문제에서 요구한 사항이기 때문에 그래프를 정렬하고 시작해야함함for g in graph:
    g.sort()

dfs_visited = [0] * (n + 1)
bfs_visited = [0] * (n + 1)


def dfs(v):
    dfs_visited[v] = True  # 방문 처리
    print(v, end=' ')
    for i in graph[v]:
        if not dfs_visited[i]:
            dfs(i)


def bfs(v):
    bfs_visited[v] = 1
    q = deque([v])
    while q:
        v = q.popleft()
        print(v, end=' ')

        for i in graph[v]: # 인접 리스트인지 인접행렬인지에 따라 다름
            if not bfs_visited[i]:
                q.append(i)
                # i 빼먹지 않기
                bfs_visited[i] = 1


dfs(v)
print()
bfs(v)
