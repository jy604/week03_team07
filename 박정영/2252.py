# 줄세우기
# 위상정렬
import sys
from collections import deque
input = sys.stdin.readline

# 노드, 간선
n, m = map(int, input().split())
# 그래프
graph = [[] for i in range(n + 1)]
# 진입 차수 초기화
indegree = [0] * (n + 1)
# 간선 정보 입력
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1


def topology_sort():
    result = []
    q = deque()

    # 진입 차수 0 노드 큐에 삽입
    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        # 진입 차수 빼기
        for i in graph[now]:
            indegree[i] -= 1
            # 빼서 진입 차수 0된 노드 큐에 삽입
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')


topology_sort()