# 장난감 조립 ㅗㅗㅗㅗㅗㅗㅗ
# 위상정렬
# result = [[0] for _ in range(n + 1)]
# [0] [0] [0] [0] [0] [0] [0] [0]
# result = [[0] * (n + 1) for _ in range(n + 1)]
# [0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0]
# [0, 0, 0, 0, 0, 0, 0, 0]
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
m = int(input())
graph = [[] for i in range(n + 1)]







# 진입 차수 초기화
indegree = [0] * (n + 1)

# 부품 수 세는 리스트
result = [[0] * (n + 1) for _ in range(n + 1)]
# 간선 정보 입력
for i in range(m):
    # y에서 x / k는 필요한 부품 수
    x, y, k = map(int, input().split())
    graph[y].append((x, k))
    indegree[x] += 1

q = deque()

# 진입 차수가 0인 노드 큐에 삽입
for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    # 현 제품의 다음 단계 번호, 현 제품이 얼마나 필요한지
    for next, next_result in graph[now]:
        # 만약 현 제품이 기본 부품이면
        if result[now].count(0) == n + 1:
            result[next][now] += next_result
        # 현 제품이 중간 부품이면
        else:
            for i in range(1, n + 1):
                result[next][i] += result[now][i] * next_result
        # 차수 - 1
        indegree[next] -= 1
        if indegree[next] == 0:
            # 차수 0이면 큐에 넣음
            q.append(next)
for x in enumerate(result[n]):
    if x[1] > 0:
        print(*x)
# print(result)