import sys
sys.stdin=open("week03\input.txt", "rt")
input = sys.stdin.readline
from collections import deque
import heapq

INF=int(1e9)

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
cost_lst = [INF] * (n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

start, end = map(int, input().split())
# print(graph)

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    cost_lst[start] = 0
    while q:
        min_cost, now = heapq.heappop(q)
        if cost_lst[now] < min_cost:
            continue
        for i in graph[now]:
            cost = min_cost + i[1]
            if cost < cost_lst[i[0]]:
                cost_lst[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(start)

print(cost_lst[end])
