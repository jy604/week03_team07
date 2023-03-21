# 특정 거리의 도시 찾기
# 모든 도로의 거리가 1이기 때문에 bfs로 해결 가능
import sys
from collections import deque
input = sys.stdin.readline

# n : 노드 / m 간선 / k 간선 거리 / x 시작 노드
n, m, k, x = map(int, input().split())

graph = [[] for i in range(n + 1)]

# 모든 간선 간 정보 입력
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0


q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시 확인
    for next_node in graph[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            # 최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

# 최단 거리가 k인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
    if distance[i] == k:
        print(i)
        check = True

# 만약 최단 거리가 k인 도시가 없다면, -1 출력
if check == False:
    print(-1)
