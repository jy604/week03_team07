# 최소 비용 구하기
# 다익스트라

import sys
input = sys.stdin.readline
from heapq import heappop, heappush
INF = int(1e9)


def dijkstra(start, end):
    q = []
    # 시작 노드에서 시작 노드로 가는 거리는 0, 큐에 push
    heappush(q, (0, start)) # 위치 잘 확인
    distance[start] = 0 # 시작 지점 0으로 초기화
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heappop(q)

        # 현재 노드가 이미 방문한 적 있는 경우라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now]:
            # 비용 계산 : 현재 노드의 누적 거리 + 다음 노드까지의 거리
            cost = dist + i[1] # (b, c)이므로 next[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            # cost가 distance에 저장된 값보다 작으면 갱신함
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))

    return distance[end]


# 노드
n = int(input())
# 간선
m = int(input())

graph = [[] for i in range(n + 1)]
# 최단 거리 테이블 초기화
distance = [INF] * (n + 1)
# 출발, 도착, 비용
for i in range(m):
    a, b, c = map(int, input().split())
    # a에서 b까지 가는 비용 c
    graph[a].append((b, c))

start, end = map(int, input().split())


print(dijkstra(start, end))