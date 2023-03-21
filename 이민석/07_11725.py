import sys
sys.stdin=open("week03\input.txt", "rt")
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())

tree = [[] for i in range(n+1)]

for i in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

visited = [0]*(n+1)


def dfs(v):
    for i in tree[v]:
        if visited[i] == 0:
            visited[i] = v
            dfs(i)

dfs(1)

for x in range(2, n+1):
    print(visited[x])