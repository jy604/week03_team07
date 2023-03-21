# 미로 만들기
# 미로 탐색 + 다익스트라 힙
import sys
from heapq import heappop, heappush
input = sys.stdin.readline
n = int(input())
# n*n 배열 선언
graph =[list(map(int, input().rstrip())) for i in range(n)]
visited = [[0] * n for _ in range(n)]


def dijkstra(x, y):
    # 상 하 좌 우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    heap = []
    heappush(heap, (0, x, y))

    while heap:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        cnt, end_x, end_y = heappop(heap)
        if end_x == n - 1 and end_y == n - 1: # 맨 끝 도달
            return cnt
        # 위치확인
        for i in range(4):
            next_x = end_x + dx[i]
            next_y = end_y + dy[i]

            if 0 <= next_x < n and 0 <= next_y < n and visited[next_x][next_y] == 0:
                # 검은 방
                if graph[next_x][next_y] == 0:
                    heappush(heap, (cnt+1, next_x, next_y))
                else:
                    heappush(heap, (cnt, next_x, next_y))
                visited[next_x][next_y] = 1



print(dijkstra(0,0))
for i in graph:
    print(*i)