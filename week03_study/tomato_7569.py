import sys
from collections import deque
input = sys.stdin.readline
# 가로, 세로, 높이
m, n, h = map(int, input().split())
# 행, 열, 높이
# tomato = [[[list(map(int, input().split()))] for _ in range(n)] for _ in range(h)]
tomato = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
# print(tomato)
# 상 하 좌 우 앞 뒤
dx = [0, 0, 0, 0, -1, 1]
dy = [0, 0, -1, 1, 0, 0]
dz = [-1, 1, 0, 0, 0, 0]
# tomato = [[[map(int, input().split())] for _ in range(n)] for _ in range(h)]
# for i in tomato:
#     for j in i:
#         for k in j:
#             # print(k, end= ' ')
#         print()
#     print()

# 0이 없으면 result = 0
# 0이 있을떄, bfs() 후에 또 0이 없으면 result = max_value / else: 0이 하나라도 있으면 -1
# for i in range(h):
#     for j in range(n):
#         for k in range(m):
#             if tomato[i][j][k] != 0:
#                 result = 0
#             else:
#                 bfs()

# 층 행 열
def bfs():
    global h, n, m
    cnt = 0
    max_value = 0
    q = deque()
    # 초기 익은 토마토 넣기
    for i in range(h):
        for j in range(n):
            for k in range(m):
                if tomato[i][j][k] == 1:
                    q.append((i, j, k))
                    #
    while q:
        z, x, y = q.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]

            if 0 <= nx < n and 0 <= ny < m and 0 <= nz < h and tomato[nz][nx][ny] == 0:
                tomato[nz][nx][ny] = tomato[z][x][y] + 1 # 날짜
                q.append((nz, nx, ny)) # 익은 토마토 인덱스
    #             max_value = max(max_value, tomato[nz][nx][ny])
    #
    # return max_value-1


bfs()
ans = 0
# print(tomato)

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                print(-1)
                exit(0)
            if tomato[i][j][k] > ans:
                ans = tomato[i][j][k]

print(ans - 1)

