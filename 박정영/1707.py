# bfs
import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    # visited[v] = 1
    q = deque([start]) # 시작 정점 값을 큐에 담음
    visited[start] = 1# 시작 그룹

    while q:
        x = q.popleft() # 맨 앞의 원소를 뺴냄

        for i in g[x]:
            if not visited[i]:
                q.append(i)
                # visited[i] = 1
                visited[i] = -1 * visited[x] # 다른 그룹 지정 ??
                # print(visited[x])
            elif visited[i] == visited[x]: # 만약 정점을 이미 방문했는데 같은 그룹이면
                return False
    return True


T = int(input()) # test case
for _ in range(T):
    v, e = map(int, input().split()) # w정점, 간선
    g = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)

    for _ in range(e):
        u, v = map(int, input().split())
        g[u].append(v)
        g[v].append(u)

    for i in range(1, v+1):
        if not visited[i]:
            result = bfs(i)
        if not result:
            break

    print('YES' if result else 'NO')