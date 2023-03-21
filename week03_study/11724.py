# 연결 요소의 개수 = dfs를 실행한 횟수
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)] # 노드 담는 리스트
for i in range(m):
    u, v = map(int, input().split())
    # 무방향이기때문에 서로 가르키는 것을 나타냄
    graph[u].append(v)
    graph[v].append(u)

visited = [0] * (n + 1)
cnt = 0


def dfs(v):
    # if visited[v] == 1:
    #     return

    visited[v] = 1
    # print(v, end= ' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


for i in range(1, n+1):
    if visited[i] == 0:
        cnt += 1
        dfs(i) # v가 아니라 i로 돌려야함
# for i in visited:
#     print(i, end=' ')
print(cnt)