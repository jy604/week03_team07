# # 미로 탐색
# # bfs
import sys
from collections import deque
input = sys.stdin.readline

# 노드, 간선 개수
n, m = map(int, input().split())
# 그래프 선언
graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))
# 방향 선언
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()

        # 이동한 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 공간에 벗어난 경우
            if nx < 0 or ny < 0 or nx >= n or ny >= m :
                continue # 무시
            # 이동할 수 없는 칸 (0)일 경우
            if graph[nx][ny] == 0:
                continue # 무시
            # 방문한 경우
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 # 최단 거리 기록
                q.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n - 1][m - 1]


print(bfs(0,0))