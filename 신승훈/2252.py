import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
indegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1
    
result = []
q = deque()

for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)
        
while q:
    current = q.popleft()
    result.append(current)
    
    for v in graph[current]:
        indegree[v] -= 1
        if indegree[v] == 0:
            q.append(v)

for res in result:
    print(res, end=' ')

