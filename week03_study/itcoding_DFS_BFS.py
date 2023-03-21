from collections import deque
# 노드, 간선 개수, 정점 번호
n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    # 결론부터 말하면 엣지(정점)들간에 관계(간선)를 배열로 표현하는 중
    # 여기서 포인트는 1과 2가 연결 되어있으면 edges[1]에는 2가 edges[2]에는 1이 들어간다는 것.
    graph[a].append(b)
    graph[b].append(a)
    # print(graph)


dfs_visited = [0] * (n + 1) # dfs 방문 처리
bfs_visited = [0] * (n + 1) # bfs 방문 처리
# print(bfs_visited)
# print(graph)

# #n+1로 안 만들고 평소처럼 n으로 만들었을 때 벌어지는 일들.
# (별거없긴한데.. edges에서 값을 빼올 때 항상 -1을 해줘야한다는 걸 생각해야함.)
# edges= [[] for _ in range(n)]
# for i in range(m):
#   a, b = map(int, sys.stdin.readline().split())
#   edges[a-1].append(b)
#   edges[b-1].append(a)
# print(edges)


def dfs(v):
    dfs_visited[v] = True # 방문 처리
    print(v, end=' ')
    for i in graph[v]:
        if not dfs_visited[i]:
        # if d_visited[i] == False:
            dfs(i)


def bfs(v):
    bfs_visited[v] = 1
    q = deque([v])
    # 같은 표현
    # q = deque()
    # q.append(v)
    while q:
        v = q.popleft()
        print(v, end=' ')

        for i in range(1, n+1):
            if not bfs_visited[i]:
                q.append(i)
                bfs_visited[i] = 1



dfs(v)
print()
bfs(v)
